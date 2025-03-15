import streamlit as st
import pandas as pd
from EDA import *
from storytelling_script import storytelling_app
from map import interactive_map

global_plastic = pd.read_csv('Plastic Waste Around the World.csv')       


st.sidebar.title("🌍 Plastic Waste Storytelling App")
menu = st.sidebar.radio("Select Page", ["Data Insights", "Storytelling", "Interactive Map"])

def set_background():
    st.markdown(
        """
        <style>
        body {
            background-color: #f5f5f5; /* Light gray */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

set_background()

if menu == "Data Insights":
    st.title("📊 Plastic Waste Analysis")

    tab1, tab2, tab3, tab4 = st.tabs([
        "🌍 Top Sources & Waste Countries", 
        "🌊 Coastal Risk & Recycling Rates", 
        "📈 Scatter & Box Plot", 
        "🔬 Correlation Matrix"
    ])

    with tab1:
        st.subheader("🔍 Top Sources of Plastic Waste")
        plot_top_sources(global_plastic)  # Chart remains visible
        with st.expander("📢 Key Insights"):
            st.markdown("""
            - 🏭 **Consumer packaging** is the largest contributor (**131 cases**), highlighting the impact of **single-use plastics**.  
            - 📦 **Industrial packaging (14 cases)** follows, but consumer waste dominates plastic pollution.  
            - ❌ **Reducing single-use plastics** can significantly cut overall waste.
            """)

        st.subheader("🌍 Top 10 Plastic Waste Producing Countries")
        plot_top_plastic_waste_Countries(global_plastic)  # Chart remains visible
        with st.expander("📊 Key Insights"):
            st.markdown("""
            - 🇨🇳 **China (59 MT)**, 🇺🇸 **U.S. (42 MT)**, and 🇮🇳 **India (26 MT)** lead in **plastic waste production**.  
            - 📉 **Waste generation drops significantly after the top three**, with Germany, Brazil, and Indonesia at around **6 MT**.  
            - 🌍 **Industrialized nations** remain key contributors, emphasizing the need for **stricter waste policies**.
            """)

    with tab2:
        st.subheader("🌊 Coastal Risk Distribution")
        plot_pie_chart(global_plastic)  # Chart remains visible
        with st.expander("🚨 Key Insights"):
            st.markdown("""
            - ⚠️ **High-risk areas (44.85%)** dominate, indicating major **environmental threats**.  
            - 🌎 **Low-risk regions (32.73%)** still face plastic waste concerns.  
            - 🆘 **Very high-risk areas (2.42%)** require **urgent intervention**.
            """)

        st.subheader("♻️ Top 10 Countries with Highest Recycling Rates")
        plot_top_Countries_Highest_Recycling_Rate(global_plastic)  # Chart remains visible
        with st.expander("🔄 Key Insights"):
            st.markdown("""
            - 🏆 **Japan leads with an 84.8% recycling rate**, followed by 🇸🇬 **Singapore (59.8%)** and 🇰🇷 **South Korea (59.1%)**.  
            - 🇩🇪 **European countries** dominate, with Germany and the Netherlands recycling **over 55%**.  
            - ❌ Despite being a top waste producer, **the U.S. is absent from the top recyclers**, indicating **inefficiencies**.
            """)

    with tab3:
        st.subheader("💡 Per Capita Waste vs Total Plastic Waste")
        Scatter_Plot(global_plastic)  # Chart remains visible
        with st.expander("📍 Key Insights"):
            st.markdown("""
            - 📌 **Most countries cluster in the lower-left**, showing **low total and per capita waste**.  
            - 🚀 **A few extreme values highlight major disparities** in plastic waste generation.  
            - 🌊 Different **coastal risk categories** appear even at lower waste levels, showing vulnerability is **not solely dependent** on plastic waste amounts.
            """)

        st.subheader("📊 Box Plot Analysis")
        box_plot(global_plastic)  # Chart remains visible
        with st.expander("📦 Key Insights"):
            st.markdown("""
            - ❗ **Multiple outliers confirm that a few countries dominate** global plastic waste production.  
            - 🔍 The **IQR suggests** most countries generate **relatively low plastic waste**.  
            - 🔄 **Recycling rates vary widely**, with significant differences between countries.
            """)

    with tab4:
        st.subheader("🔬 Correlation Matrix")
        Correlation_Matrix(global_plastic)  # Chart remains visible
        with st.expander("📈 Key Insights"):
            st.markdown("""
            - ⚖️ **Total Plastic Waste (MT) vs. Per Capita Waste (KG)**: Weak **negative correlation (-0.05)** → High total waste **does not always mean** high per capita waste.  
            - ♻️ **Recycling Rate vs. Per Capita Waste (KG)**: Weak **positive correlation (0.30)** → Countries with **higher per capita waste** may have **slightly better recycling practices**.  
            - 🔄 **Total Plastic Waste (MT) vs. Recycling Rate**: Weak **positive correlation (0.21)** → High waste generation **does not always mean better recycling efforts**.
            """)

elif menu == "Storytelling":
    storytelling_app()

elif menu == "Interactive Map":
    interactive_map()
