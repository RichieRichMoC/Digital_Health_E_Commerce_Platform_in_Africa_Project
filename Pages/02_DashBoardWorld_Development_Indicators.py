import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

# ---------------- Page Config ----------------
st.set_page_config(
    page_title='02_World_Development_Indicators',
    page_icon='📈',
    layout='wide'
)

# ---------------- Load Config ----------------
with open('./config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

# ---------------- Auth Check ----------------
if not st.session_state.get("authentication_status"):
    st.info('Please log in to access the application from the MainPage.')
else:
    def main():
        # Access dataset from session state
        data = st.session_state.get("data_key4", None)

        if data is None:
            st.info('Please Kindly Access the DataPage to Configure your DataSet.')
        else:
            st.title("📊 World Development Indicators - Performance Analysis")

            # =====================================================
            # 🔹 Reshape Data (Wide → Long)
            # =====================================================
            df_long = pd.melt(
                data,
                id_vars=["Country Name", "Country Code", "Series Name", "Series Code"],
                value_vars=[col for col in data.columns if "YR" in col],
                var_name="Year",
                value_name="Value"
            )
            df_long["Year"] = df_long["Year"].str.extract(r"(\d{4})").astype(int)

            # =====================================================
            # 📈 Line Trend Over Years
            # =====================================================
            st.subheader("📈 Performance Trend Over Years")
            selected_series = st.selectbox("Select Indicator (Series)", df_long["Series Name"].unique())

            fig = px.line(
                df_long[df_long["Series Name"] == selected_series],
                x="Year", y="Value", color="Country Name", markers=True,
                title=f"Performance Trend of {selected_series}"
            )
            st.plotly_chart(fig, use_container_width=True)

            # =====================================================
            # 🌍 Country Comparison (Bar Chart)
            # =====================================================
            st.subheader("🌍 Country Comparison by Year")
            selected_year = st.selectbox("Select Year", sorted(df_long["Year"].unique()))
            fig = px.bar(
                df_long[(df_long["Series Name"] == selected_series) & (df_long["Year"] == selected_year)],
                x="Country Name", y="Value", color="Country Name",
                title=f"{selected_series} in {selected_year}"
            )
            st.plotly_chart(fig, use_container_width=True)

            # =====================================================
            # 📊 Histogram of Values
            # =====================================================
            st.subheader("📊 Distribution of Values (Histogram)")
            fig = px.histogram(
                df_long[df_long["Series Name"] == selected_series],
                x="Value", color="Country Name", nbins=20,
                title=f"Distribution of {selected_series} Values"
            )
            st.plotly_chart(fig, use_container_width=True)

            # =====================================================
            # 🔗 Correlation Across Years
            # =====================================================
            st.subheader("🔗 Correlation Between Years")
            pivot_df = df_long.pivot_table(
                index=["Country Name", "Series Name"], columns="Year", values="Value"
            )
            corr_matrix = pivot_df.corr()

            plt.figure(figsize=(10, 6))
            sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
            plt.title("Correlation Between Years")
            st.pyplot(plt)

           

    if __name__ == '__main__':
        main()
