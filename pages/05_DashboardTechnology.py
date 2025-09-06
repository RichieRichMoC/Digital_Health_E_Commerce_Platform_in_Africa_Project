import streamlit as st
import pandas as pd
import plotly.express as px
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

st.set_page_config(
    page_title='Dashboard',
    page_icon='📈',
    layout='wide'
)

# Load configuration from YAML file
with open('./config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# Initialize Streamlit Authenticator with configuration settings
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

# Check if the user is authenticated
if not st.session_state.get("authentication_status"):
    st.info('Please log in to access the application from the MainPage.')
else:
    def main():
        # Access data from session state
        data = st.session_state.get("data_key4", None)

        if data is None:
            st.info('Please Kindly Access the DataPage to Configure your DataSet.')
        else:
            # Ensure Year is string for plotting
            if "Year" in data.columns:
                data["Year_str"] = data["Year"].astype(str)

            # ============================
            # Country + Series Filter
            # ============================
            st.title("Country Technology Usage Over Time")

            col1, col2 = st.columns([2, 2])
            with col1:
                selected_country = st.selectbox(
                    "Select Country",
                    options=data["Country Name"].unique(),
                    key="country_perf"
                )
            with col2:
                country_data = data[data["Country Name"] == selected_country]
                if not country_data.empty:
                    selected_series = st.selectbox(
                        "Select Series",
                        options=country_data["Series Name"].unique(),
                        key="series_filter"
                    )
                else:
                    selected_series = None

            if selected_series:
                series_data = country_data[country_data["Series Name"] == selected_series]

                if not series_data.empty:
                    st.subheader(f"Performance of {selected_country} ({selected_series})")

                    # Create three side-by-side columns
                    col_a, col_b, col_c = st.columns(3)

                    # --- Bar Chart ---
                    with col_a:
                        fig_bar = px.bar(
                            series_data,
                            x="Year_str",
                            y="OBS_VALUE",
                            title=f"Yearly OBS_VALUE"
                        )
                        st.plotly_chart(fig_bar, use_container_width=True)

                    # --- Pie Chart ---
                    with col_b:
                        fig_pie = px.pie(
                            series_data,
                            names="Year_str",
                            values="OBS_VALUE",
                            title=f"OBS_VALUE Share by Year"
                        )
                        st.plotly_chart(fig_pie, use_container_width=True)

                    # --- Line Chart ---
                    with col_c:
                        fig_line = px.line(
                            series_data,
                            x="Year_str",
                            y="OBS_VALUE",
                            markers=True,
                            title=f"OBS_VALUE Trend Over Years"
                        )
                        st.plotly_chart(fig_line, use_container_width=True)

                else:
                    st.warning(f"No data available for {selected_country} in {selected_series}")

    if __name__ == '__main__':
        main()
