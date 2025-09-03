import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from numerize.numerize import numerize
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
 
# Perform user authentication

 
# Check if the user is authenticated
if not st.session_state.get("authentication_status"):
    st.info('Please log in to access the application from the MainPage.')
else:
   def main():
    
    # Access data from session state
    data = st.session_state.get("data_key3", None)
    # Check if the user is authenticated
    if data is None:
     st.info('Please Kindly Access the DataPage to Configure your DataSet.')
     
    else: 
      
      table_feature = data.columns.tolist()
      
    


      if data is not None:
 
            with st.container():
                     
                     data_df= data
                     data_df.columns.tolist()

                     cpp1, cpp2 = st.columns(2)
                     with cpp1:
                        st.title('Univariate Analysis')
                     with cpp2:
                           #selected_uni_feature = st.selectbox('Select Feature', data_df)
                           selected_feature=st.selectbox('Select a Feature', options=table_feature, key='selected_model')

                     co1, co2 = st.columns(2)
                                    
                     with co1:
                           fig = px.histogram(data, x=selected_feature, color=selected_feature, barmode="group", height=400, width=500)
                           fig.update_yaxes(title_text=None)
                           st.plotly_chart(fig)
   
                     with co2:
                           fig = px.box(data, x=selected_feature, height=400, width=500)
                           st.plotly_chart(fig)
            with st.container():
                     data_df2= data
                     data_df2.columns.tolist()
                     

                     qpp1, qpp2 = st.columns(2)
                     with qpp1:
                         st.title('Response Rate: For  Selected Features')   
                     with qpp2:
                           #selected_uni_feature = st.selectbox('Select Feature', data_df)
                           selected_featureq=st.selectbox('Select a Feature', options=table_feature, key='selected_model2')       

                     cn1, cn2 = st.columns(2)
                     
                     with cn1:
                           fig = px.histogram(data_df2, x=selected_featureq, height=400, width=500)
                           fig.update_yaxes(title_text=None)
                           st.plotly_chart(fig)
   
                     with cn2:
                           senior_citizen_pie = px.pie(data_df2, names=selected_featureq, color=selected_featureq)
                           st.plotly_chart(senior_citizen_pie, use_container_width=True)
                        
            with st.container():
                     data_df3 = data
                     data_df3.columns.tolist()

                     cppo1, cppo2, cppo3 = st.columns(3)
                     with cppo1:
                        st.title('Bivariate Analysis')
                     with cppo2:
                        selected_feature1 = st.selectbox('Select Feature X', options=table_feature, key='selected_modeli')
                     with cppo3:
                        selected_feature2 = st.selectbox('Select Feature Hue', options=table_feature, key='selected_modela')

                     c1, c2 = st.columns(2)

                     with c1:
                        fig1, ax1 = plt.subplots()
                        sns.histplot(data_df3, x=selected_feature1, hue=selected_feature2, multiple="stack", ax=ax1)
                        st.pyplot(fig1)

                     with c2:
                        fig2, ax2 = plt.subplots()
                        sns.scatterplot(data=data_df3, x=selected_feature1, y=selected_feature2, hue=selected_feature2, ax=ax2)
                        ax2.set_title(f"Scatter plot: {selected_feature1} vs {selected_feature2}")
                        st.pyplot(fig2)

                                           
            with st.container():
                        df1 = data
                        numeric_columns = df1.select_dtypes(include=np.number).columns.tolist()

                        
                        
                           
                           
                           
                     
                        qppo1, qppo2, qppo3, qppo4, qppo5, qppo6 = st.columns(6)
                        with qppo1:
                           st.header('Multivariate')
                        with qppo2:
                           pass
                        with qppo3:
                           pass 
                        if len(numeric_columns) < 3:
                           st.warning("You need at least 3 numerical features to plot a 3D scatter plot.")
                        else:  
                         with qppo4:
                           z_variable = st.selectbox("Par1:", numeric_columns, key="z_axis")  
                         with qppo5:
                           x_variable = st.selectbox("Par2:", numeric_columns, key="x_axis")
                         with qppo6:
                           y_variable = st.selectbox("Par3:", numeric_columns, key="y_axis")   
                     
                     
                        ca1, ca2 = st.columns(2)
                        correlation_matrix = df1.corr(numeric_only=True)
                     
                        with ca1:  
                        
                         plt.figure(figsize=(10, 8))
                         sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
                         plt.title("Correlation Matrix")
                         st.pyplot(plt)
                           
   
                        with ca2:
               
                                 # Create 3D scatterplot
                           fig = plt.figure(figsize=(10, 8))
                           ax = fig.add_subplot(111, projection='3d')
                           ax.scatter(df1[x_variable], df1[y_variable], df1[z_variable])
                           ax.set_xlabel(x_variable)
                           ax.set_ylabel(y_variable)
                           ax.set_zlabel(z_variable)
                           plt.title("Correlation Matrix")
                        
                           st.pyplot(fig)
                           
   if __name__ == '__main__':
              main()