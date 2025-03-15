import geopandas as gpd
import folium
from streamlit_folium import folium_static
import streamlit as st
from EDA import global_plastic
import pandas as pd

# Fixing incorrect geometries for small islands
def fix_geometries(gdf):
    gdf = gdf[gdf.geometry.notnull()]
    gdf = gdf[gdf.geometry.is_valid]
    gdf = gdf[gdf.geometry.area > 0.0]  # Removing empty polygons
    return gdf

@st.cache_data
def load_map():
    world = gpd.read_file("data/ne_10m_admin_0_countries.shp") 
    world = world.rename(columns={'SOVEREIGNT': 'Country'})
    name_mapping = {
        "United States of America": "United States",
        "Republic of the Congo": "Republic of Congo",
        "United Republic of Tanzania": "Tanzania",
        "Federated States of Micronesia": "Micronesia",
        "New Caledonia": "New Caledonia",
        "Cabo Verde": "Cape Verde",
        "Democratic Republic of the Congo": "Democratic Republic of Congo",
        "Czechia": "Czech Republic",
        "São Tomé and Principe": "Sao Tome and Principe",
        "eSwatini": "Eswatini",
        "Netherlands Antilles": "Netherlands"
    }

    world['Country'] = world['Country'].replace(name_mapping)
    world.fillna("No Data", inplace=True)

    merged = world.merge(global_plastic, on="Country", how="left")
    merged = fix_geometries(merged)
    numeric_cols = ['Total_Plastic_Waste_MT', 'Recycling_Rate']
    for col in numeric_cols:
        merged[col] = pd.to_numeric(merged[col], errors='coerce')
    merged = merged[merged['Total_Plastic_Waste_MT'].notna()]

    # Preserving categorical columns
    merged['Coastal_Waste_Risk'] = merged['Coastal_Waste_Risk'].fillna("No Data")

    # Dropping Invalid Coordinates
    merged = merged[~merged['Country'].isin(["Antarctica", "No Data"])]
    return merged


def interactive_map():
    st.title("🗺️ Interactive Plastic Waste Map")
    world = load_map()

    tab1, tab2, tab3, tab4 = st.tabs(["Main Sources Map", "Top Countries", "Coastal Waste Risk Map", "Recycling Rate Map"])

    with tab1:
        st.subheader("Main Sources Map")
        sources_options = ['All'] + [s for s in world['Main_Sources'].unique() if s not in ['No Data', '0']]
        selected_source = st.sidebar.selectbox("Filter by Main Sources", sources_options, index=0)
        m3 = folium.Map(location=[20, 0], zoom_start=2, tiles='CartoDB Positron')
        if selected_source == 'All':
            filtered_world = world[~world['Main_Sources'].isin(['No Data', '0'])]
        else:
            filtered_world = world[world['Main_Sources'] == selected_source]

        for _, row in filtered_world.iterrows():
            if pd.notna(row['Main_Sources']):
                folium.CircleMarker(
                    location=[row['geometry'].centroid.y, row['geometry'].centroid.x],
                    radius=6,
                    tooltip=f"{row['Country']}: {row['Main_Sources']}",
                    color='blue',
                    fill=True,
                    fill_color='blue',
                    fill_opacity=0.7
                ).add_to(m3)
        folium_static(m3)
            
    with tab2:
        st.subheader("Total Plastic Waste Map (Top 10 Countries)")
        m = folium.Map(location=[20, 0], zoom_start=2, tiles='CartoDB Positron')
        top_10 = world.drop_duplicates(subset='Country').nlargest(10, 'Total_Plastic_Waste_MT')

        for _, row in top_10.iterrows():
            folium.CircleMarker(
                location=[row['geometry'].centroid.y, row['geometry'].centroid.x],
                radius=8,
                tooltip=f"{row['Country']}: {row['Total_Plastic_Waste_MT']} MT",
                color='red',
                fill=True,
                fill_color='red',
                fill_opacity=0.7
            ).add_to(m)
        folium_static(m)
        

    with tab3:
        st.subheader("Coastal Waste Risk Map")
        risk_options = ['All', 'Low', 'Medium', 'High', 'Very_High']
        selected_risk = st.sidebar.selectbox("Filter by Coastal Waste Risk", risk_options, index=0)
        risk_colors = {'Low': 'green', 'Medium': 'orange', 'High': 'red', 'Very_High': 'darkred'}

        m2 = folium.Map(location=[20, 0], zoom_start=2, tiles='CartoDB Positron')
        filtered_world = world.copy()

        # Apply Coastal Waste Risk Filter
        if selected_risk != 'All':
            filtered_world = filtered_world[filtered_world['Coastal_Waste_Risk'] == selected_risk]
        else:
            filtered_world = filtered_world[filtered_world['Coastal_Waste_Risk'].isin(risk_colors.keys())]

        filtered_world = filtered_world.drop_duplicates(subset='Country')
        filtered_world = filtered_world[filtered_world['geometry'].notna()]

        for _, row in filtered_world.iterrows():
            if pd.notna(row['Coastal_Waste_Risk']):
                folium.CircleMarker(
                    location=[row['geometry'].centroid.y, row['geometry'].centroid.x],
                    radius=6 if row['Coastal_Waste_Risk'] != 'Very_High' else 10,
                    tooltip=f"{row['Country']}: {row['Coastal_Waste_Risk']}",
                    color=risk_colors.get(row['Coastal_Waste_Risk'], 'gray'),
                    fill=True,
                    fill_color=risk_colors.get(row['Coastal_Waste_Risk'], 'gray'),
                    fill_opacity=0.7
                ).add_to(m2)

        folium_static(m2)

        
    with tab4:
        st.subheader("Recycling Rate Map")
        filter_rate = st.sidebar.slider("Filter by Recycling Rate (%)", 0, 85, (0, 85))
        filtered_world = world[(world['Recycling_Rate'] >= filter_rate[0]) & (world['Recycling_Rate'] <= filter_rate[1])]
        if filter_rate[1] == 85 & filter_rate[0]==85:
                filtered_world = world[world['Recycling_Rate'] == world['Recycling_Rate'].max()]
        m1 = folium.Map(location=[20, 0], zoom_start=2, tiles='CartoDB Positron')
        for _, row in filtered_world.iterrows():
                if pd.notna(row['Recycling_Rate']):
                    color = 'green' if row['Recycling_Rate'] > 50 else 'orange' if row['Recycling_Rate'] > 20 else 'red'
                    folium.CircleMarker(
                        location=[row['geometry'].centroid.y, row['geometry'].centroid.x],
                        radius=4,
                        tooltip=f"{row['Country']}: {row['Recycling_Rate']}%",
                        color=color,
                        fill=True,
                        fill_color=color,
                        fill_opacity=0.7
                    ).add_to(m1)
        folium_static(m1)

