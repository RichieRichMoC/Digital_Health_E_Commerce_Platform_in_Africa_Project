import streamlit as st
import numpy as np
import pandas as pd
import apy  # import your dataset loaders from app.py

# Define constants for session keys
DATA_KEY1 = "data_key1"   # Health, Nutrition & Population
DATA_KEY2 = "data_key2"   # Population Estimates
DATA_KEY3 = "data_key3"   # Statistical Performance Indicators
DATA_KEY4 = "data_key4"   # World Development Indicators

# Page config
st.set_page_config(
    page_title='View Data',
    page_icon='📊',
    layout='wide'
)

# Cached loader for all 4 datasets
@st.cache_resource
def load_all_data():
    try:
        df1 = apy.load_data()    # Health, Nutrition & Population
        df2 = apy.load_data2()   # Population Estimates
        df3 = apy.load_data3()   # Statistical Performance Indicators
        df4 = apy.load_data4()   # World Development Indicators
        return df1, df2, df3, df4
    except FileNotFoundError as e:
        st.error(f"Error loading dataset: {e}")
        return None, None, None, None

# Function to select features by type
def select_features(feature_type, data_df):
    if feature_type == 'Numerical Features':
        return data_df.select_dtypes(include=np.number)
    elif feature_type == 'Categorical Features':
        return data_df.select_dtypes(include='object')
    else:
        return data_df

# Function to display each dataset separately
def show_dataset(title, df, key_prefix):
    st.subheader(title)

    if df is None:
        st.error("Dataset could not be loaded.")
        return

    feature_type = st.selectbox(
        f"Select features for {title}",
        options=['All Features', 'Numerical Features', 'Categorical Features'],
        key=f"{key_prefix}_features"
    )

    if feature_type == 'All Features':
        st.write(df)
    else:
        st.write(select_features(feature_type, df))


# Authentication check
if not st.session_state.get("authentication_status"):
    st.info('Please log in to access the application from the Home page.')
else:
    st.title('Datasets Overview')

    # Load all datasets
    df1, df2, df3, df4 = load_all_data()

    # Store datasets into session_state with static keys
    if df1 is not None:
        st.session_state[DATA_KEY1] = df1
    if df2 is not None:
        st.session_state[DATA_KEY2] = df2
    if df3 is not None:
        st.session_state[DATA_KEY3] = df3
    if df4 is not None:
        st.session_state[DATA_KEY4] = df4

    # Show all datasets with feature selection
    show_dataset("World Development Indicators", df4, "df4")
    st.divider()
    show_dataset("Health, Nutrition & Population", df1, "df1")
    st.divider()
    show_dataset("Population Estimates", df2, "df2")
    st.divider()
    show_dataset("Statistical Performance Indicators", df3, "df3")
