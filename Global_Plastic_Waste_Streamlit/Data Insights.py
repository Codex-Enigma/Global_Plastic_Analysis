from numpy import fix
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

global_plastic = pd.read_csv('Plastic Waste Around the World.csv')

def plot_top_sources(global_plastic):
    Top_source = global_plastic['Main_Sources'].value_counts()
    fig, ax = plt.subplots(figsize=(8, 8))
    sns.barplot(x=Top_source.values, y=Top_source.index, palette='viridis', ax=ax)
    ax.set_xlabel("Count")
    ax.set_ylabel("Main Sources")
    ax.set_title("Top Sources of Plastic Waste")
    plt.tight_layout()
    return  st.pyplot(fig)

def plot_top_plastic_waste_Countries(global_plastic):
    Top_Plastic_Waste_Countries = global_plastic.nlargest(10,'Total_Plastic_Waste_MT')
    fig = plt.figure(figsize=(8,6))
    sns.barplot(y=Top_Plastic_Waste_Countries['Country'], x = Top_Plastic_Waste_Countries['Total_Plastic_Waste_MT'],hue= Top_Plastic_Waste_Countries['Country'], palette='Reds')
    plt.title("Top 10 Plastic Waste Producing Countries")
    plt.xlabel("Total Plastic Waste (MT)")
    plt.ylabel("Country")
    return  st.pyplot(fig)

def plot_pie_chart(global_plastic):
    high_risk = global_plastic[global_plastic['Coastal_Waste_Risk']=='High']['Coastal_Waste_Risk'].count()
    low_risk = global_plastic[global_plastic['Coastal_Waste_Risk']=='Low']['Coastal_Waste_Risk'].count()
    medium_risk = global_plastic[global_plastic['Coastal_Waste_Risk']=='Medium']['Coastal_Waste_Risk'].count()
    very_high_risk = global_plastic[global_plastic['Coastal_Waste_Risk']=='Very_High']['Coastal_Waste_Risk'].count()

    fig = plt.figure(figsize=(10,6))
    index_values = [high_risk, low_risk, medium_risk, very_high_risk]
    index_labels = ['High Risk', 'Low Risk', 'Medium Risk', 'Very High Risk']
    plt.pie(index_values, labels = index_labels, autopct='%2.2f%%')
    plt.title('Coastal Risk Distribution', fontsize=20)
    return st.pyplot(fig)

def plot_top_Countries_Highest_Recycling_Rate(global_plastic):
    Top_recycling_Countires = global_plastic.nlargest(10,'Recycling_Rate')
    fig = plt.figure(figsize=(8,8))
    sns.barplot(y = Top_recycling_Countires['Country'],x = Top_recycling_Countires['Recycling_Rate'], hue = Top_recycling_Countires['Country'], palette='Greens')
    plt.title("Top 10 Countries with Highest Recycling Rates")
    plt.xlabel('Recycling Rate(%)')
    plt.ylabel('Country')
    return st.pyplot(fig)

def Scatter_Plot(global_plastic):
    fig =  plt.figure(figsize=(8,6))
    sns.scatterplot(x=global_plastic['Per_Capita_Waste_KG'], y = global_plastic['Total_Plastic_Waste_MT'] ,hue=global_plastic["Coastal_Waste_Risk"], palette="coolwarm")
    plt.title("Per Capita Waste vs Total Plastic Waste")
    plt.xlabel("Per Capita Waste (KG)")
    plt.ylabel("Total Plastic Waste (MT)")
    return st.pyplot(fig)


def box_plot(global_plastic):
    col = ['Total_Plastic_Waste_MT', 'Recycling_Rate', 'Per_Capita_Waste_KG']
    colors = ['royalblue', 'crimson', 'seagreen']

    selected_column = st.selectbox("Choose a distribution to display:", col)
    fig, ax = plt.subplots(figsize=(12, 6)) 
    sns.boxplot(y=global_plastic[selected_column], ax=ax, color=colors[col.index(selected_column)], showfliers=True)
    
    ax.set_title(f'Distribution of {selected_column}', fontsize=16)
    ax.set_xlabel("")  
    ax.set_ylabel("Value", fontsize=14)
    ax.tick_params(axis='y', labelsize=12)
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    return st.pyplot(fig)

def Correlation_Matrix(global_plastic):
    correlation_matrix = global_plastic.select_dtypes(include=['number']).corr()
    fig = plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
    plt.title("Correlation Matrix")
    return st.pyplot(fig)


