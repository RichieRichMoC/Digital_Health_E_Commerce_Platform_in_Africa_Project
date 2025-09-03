import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

# Streamlit page setup
st.set_page_config(
    page_title='Digital_Health_E_Commerce_Platform_in_Africa_Project',
    page_icon='🏘️',
    layout='wide'
)

# Load config.yaml file
with open('./config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# Initialize the authenticator
authenticator = stauth.Authenticate(
    credentials=config['credentials'],
    cookie_name=config['cookie']['name'],
    key=config['cookie']['key'],
    expiry_days=config['cookie']['expiry_days']
)

# Show login widget in sidebar
authenticator.login(location='sidebar')

# Check authentication status
if st.session_state.get("authentication_status"):
    # ✅ LOGGED IN
    authenticator.logout("Logout", "sidebar")
    st.sidebar.success(f"Welcome {st.session_state['name']} 👋")

    # MAIN CONTENT
    st.markdown("<h2 style='color:#0066ff;'>Welcome to the Digital_Health_E_Commerce_Platform_in_Africa_Project Data Analysis </h2>", unsafe_allow_html=True)
    image_path = './Images/welcomepage.jpeg'
    st.image(image_path, use_container_width=True, output_format="auto")

    

    col1, col2 = st.columns(2)

    with col1:
        st.header("App Information 💬")
        st.write("Experience the future of telecommunications with our cutting-edge Customer Churn Prediction App! ...")

        st.header("Dataset Information")
        st.write("- REGION: The location of each customer")
        st.write("- TENURE: Number of months the customer has stayed with the company")
        st.write("- MONTANT: Top-up amount")
        st.write("- FREQUENCE_RECH: Frequency of recharges by the customer")
        st.write("- DATA_VOLUME: Volume of data consumed by the customer")
        st.write("- CHURN: Whether the customer churned or not")

    with col2:
        st.header("How to Use the App")
        st.write("* Go to the 'Predictions' page.")
        st.write("* Enter the customer's information.")
        st.write("* Click 'Predict'.")

        st.header("Source Code")
        st.markdown("[GitHub Repository](https://github.com/Elphoxa/ChurnGuard-Project.git)")

        st.header("Social Handles")
        st.write("- [GitHub](https://github.com/Elphoxa)")
        st.write("- [LinkedIn](https://www.linkedin.com/in/efosa-omosigho)")

elif st.session_state.get("authentication_status") is False:
    st.error("🚫 Username/Password is incorrect")
    st.code("Username: beatit\nPassword: abc123")

elif st.session_state.get("authentication_status") is None:
    st.warning("Please enter your username and password.")
