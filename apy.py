import streamlit as st
import pandas as pd

# Function to load and cache the dataset
@st.cache(allow_output_mutation=True)
def load_data():
    # Load the dataset from the Dataset folder
    df = pd.read_csv("./dataset/P_Data_Extract_From_Health_Nutrition_and_Population_StatisticsProcessed.csv") 
    return df
def load_data2():
    # Load the dataset from the Dataset folder
    df2 = pd.read_csv("./dataset/P_Data_Extract_From_Population_estimates_and_projectionsProcessed.csv") 
    return df2
def load_data3():
    # Load the dataset from the Dataset folder
    df3 = pd.read_csv("./dataset/P_Data_Extract_From_Statistical_Performance_IndicatorsProcessed.csv") 
    return df3
def load_data4():
    # Load the dataset from the Dataset folder
    df4 = pd.read_csv("./dataset/P_Data_Extract_From_World_Development_IndicatorsProcessed.csv") 
    return df4
def main():
    # Load the dataset
    df = load_data()
   

    # Display the first few rows of the dataset
    st.write(df.head())

if __name__ == '__main__':
    main()