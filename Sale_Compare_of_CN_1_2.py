import pandas as pd
import numpy as np
import datetime
import streamlit as st
from PIL import Image
import seaborn as sn
import matplotlib.pyplot as plt
import plotly.express as px
import re
import base64
from io import BytesIO
import warnings
warnings.filterwarnings('ignore')

# python -m streamlit run "G:/Gautam/Streamlit/Sale_Compare_of_CN_1_2.py"

### for data load
@st.cache_data 
def load_data():
    path = r"G:\Gautam\reporttt\CN -127 Report.xlsx"
    return pd.read_excel(path)
df = load_data()

print(df.columns)

df['MONTH'] = df['TRANS_DATE'].dt.strftime('%B')

df['COLOR'] = df['COLOR'].apply(lambda x: re.sub(r'[+-]', '', x))
df['PURITY'] = df['PURITY'].apply(lambda x: re.sub(r'[+-]', '', x))
df = df[~df['PURITY'].isin(['I1', 'I2', 'I3'])]
df['COLOR_1'] = np.where(df['COLOR'].isin(['D','E','F','G','H','I','J','K','L','M','N']),df['COLOR'],"FANCY")

# df['DEPTH_RANGE123'] = np.where( df['SHAPE']=='CE' & df['DEPTH_PER']>=57 & df['DEPTH_PER'] <=62,"57 - 62",
#                     np.where( df['SHAPE']=='CE' & df['DEPTH_PER']>=62.1 & df['DEPTH_PER'] <=63.9,"62.1 - 63.9",
#                     np.where( df['SHAPE']=='CE' & df['DEPTH_PER']>=64 & df['DEPTH_PER'] <=67.9,"64 - 67.9",
#                     np.where( df['SHAPE']=='CE' & df['DEPTH_PER']>=68 & df['DEPTH_PER'] <=68.9,"68 - 68.9",
#                     np.where( df['SHAPE']=='CE' & df['DEPTH_PER']>=69 & df['DEPTH_PER'] <=69.9,"69 - 69.9",
#                     np.where( df['SHAPE']=='CE' & df['DEPTH_PER']>=70 & df['DEPTH_PER'] <=99.99,"70 - 99.99","NO"))))))

# df['DEPTH_RANGE_1'] = np.where(df['SHAPE']=='CE' & df['DEPTH_PER'].between(57,62),"57.0 - 62.0",
#                       np.where(df['SHAPE']=='CE' & df['DEPTH_PER'].between(62.1,63.9),"62.1 - 63.9",
#                       np.where(df['SHAPE']=='CE' & df['DEPTH_PER'].between(57,62),"57.0 - 62.0",
#                       np.where(df['SHAPE']=='CE' & df['DEPTH_PER'].between(57,62),"57.0 - 62.0",
#                       np.where(df['SHAPE']=='CE' & df['DEPTH_PER'].between(57,62),"57.0 - 62.0",
#                       np.where(df['SHAPE']=='CE' & df['DEPTH_PER'].between(57,62),"57.0 - 62.0"))))))
                     
User = st.sidebar.text_input("User")
pass_ = st.sidebar.text_input("Password",type="password")
bott = st.sidebar.checkbox("Login")

### for Logo
    # img = Image.open(r"G:\Gautam\Streamlit\logo.png")
    # col1, col2 = st.columns([1,10])

    # with col1:
    #     st.write(' ')
    # with col2:
    #     st.image(img,width= 100)
#with col3:
#    st.write(' ')
#*****
def image_to_base64(img):
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

# Load and convert the image to base64
img = Image.open(r"G:\Gautam\Streamlit\logo.png")
img_base64 = image_to_base64(img)

# Center the logo using Markdown
st.markdown(f'<div style="text-align: center; padding-top: 20px;"><img src="data:image/png;base64,{img_base64}" width="100"></div>', unsafe_allow_html=True)
#********

######################################################################################
# df['TRANS_DATE'] = pd.to_datetime(df['TRANS_DATE'])

# # Extract different date and time formats
# df['Full Month Name'] = df['TRANS_DATE'].dt.strftime('%B')
# df['Abbreviated Month Name'] = df['TRANS_DATE'].dt.strftime('%b')
# df['Full Weekday Name'] = df['TRANS_DATE'].dt.strftime('%A')
# df['Abbreviated Weekday Name'] = df['TRANS_DATE'].dt.strftime('%a')
# df['Full Date'] = df['TRANS_DATE'].dt.strftime('%Y-%m-%d')
# df['Full Date and Time'] = df['TRANS_DATE'].dt.strftime('%Y-%m-%d %H:%M:%S')
# df['Locale Date'] = df['TRANS_DATE'].dt.strftime('%x')
# df['Locale Time'] = df['TRANS_DATE'].dt.strftime('%X')
############################################################################################

### for Greeting
now = datetime.datetime.now()
hour = now.hour

if hour<12:
    greeting = "GOOD MORNING"
elif hour<17:
    greeting = "GOOD AFTERNOON"
else:
    greeting = "GOOD EVENING"

st.write(f"{greeting}!")

def pass_word():
    if bott == True:
        if User == "GK.ai":
            if pass_ == "GK@786":
                
                # ---- MAINPAGE ----
                st.title(":bar_chart: Dashboard")
                st.markdown("##")

                #st.header("Please filter here: ")
                custom_css = """
                                <style>
                                    /* Decrease the size of the header */
                                    .stHeader {
                                        font-size: 18px; /* Adjust the font size as needed */
                                        font-weight: bold; /* Optional: make the header bold */
                                    }
                                </style>
                            """

                # Apply custom CSS
                st.markdown(custom_css, unsafe_allow_html=True)
                st.markdown('<h1 class="stHeader">Please filter here:</h1>', unsafe_allow_html=True)
                slc1, slc2, slc3 = st.columns(3)

                Month = slc1.multiselect(label="Select Month",options=df['MONTH'].unique())
                Shape = slc2.multiselect(label="Select Shape",options=df['SHAPE'].unique())
                CNO = slc3.multiselect(label="Select Company",options=df['COMP_NO'].unique())
                
                #Shade = st.multiselect(label="Select Month",options=df['SHADE'].unique())

                custom_css = """
                            <style>
                                .custom-line {
                                    border: 0;
                                    height: 2px; /* Adjust the thickness of the line */
                                    background: #FFFFFF; /* Adjust the color of the line to white */
                                }
                            </style>
                        """

                # Apply custom CSS
                st.markdown(custom_css, unsafe_allow_html=True)

                # Add a styled horizontal line
                st.markdown('<hr class="custom-line">', unsafe_allow_html=True)

                #Button = st.button('View Report')
                
                #if Button:

                    ### Create Query
                df_selection = df.query('SHAPE == @Shape & MONTH == @Month & COMP_NO == @CNO')

                if df_selection.empty:
                    st.warning("No data available base on this filter")
                    st.stop()    
                with st.spinner():

                    col_1,col_2,col_3 = st.columns(3)
                    
                    total_sales = "$ "+str(round(df_selection['NET_VALUE'].sum()/1000000,2))
                    total_CRT = round(df_selection['WGT'].sum(),2)
                    total_PCS = df_selection['PACKET_NO'].count()

                    with col_1:
                        st.metric("Total Sales (M)",value=total_sales)
                    with col_2:
                        st.metric("Total CRT",value=total_CRT)
                    with col_3:
                        st.metric("Total PCS",value=total_PCS)

                    st.write(df_selection)
                    
                    sales_by_col = df_selection.groupby(by=["COLOR_1","COMP_NO"])[["PACKET_NO"]].count().reset_index()

                    #fig_product_col = st.bar_chart(sales_by_col,x="COLOR_1",y="PACKET_NO",color="COMP_NO") 

                    fig_product_col = px.bar(
                        sales_by_col,                           
                        x= "COLOR_1",
                        y= "PACKET_NO",color="COMP_NO",text="PACKET_NO",barmode='group'
                    )
                    
                    fig_product_col.update_traces(
                        texttemplate='%{text}',
                        textposition='outside',
                        textfont_size=12,  # Optional: adjust the font size for better visibility
                        #marker=dict(color='rgba(255,165, 0, 0.6)')  # Optional: adjust color for better contrast
                    )

                    # Adjust layout if necessary
                    fig_product_col.update_layout(
                        xaxis_title='Color',
                        yaxis_title='Stones',
                        title='Sale by Color'
                    )
                    
                    sales_by_clarity = df_selection.groupby(by=["PURITY","COMP_NO"])[["PACKET_NO"]].count().reset_index()
                    #st.write(sales_by_clarity)
        
                    fig_product_clar = px.bar(
                        sales_by_clarity,
                        y= sales_by_clarity["PACKET_NO"],
                        x= sales_by_clarity["PURITY"],text="PACKET_NO",color="COMP_NO",barmode='group'
                    )    

                    fig_product_clar.update_traces(
                        texttemplate='%{text}',
                        textposition='outside',
                        textfont_size=12,  # Optional: adjust the font size for better visibility
                        #marker=dict(color='rgba(55, 83, 109, 0.6)')  # Optional: adjust color for better contrast
                    )

                    # Adjust layout if necessary
                    fig_product_clar.update_layout(
                        xaxis_title='Clarity',
                        yaxis_title='Stones',
                        title='Sale by Clarity'
                    )    

                    left_column, right_column = st.columns(2)
                    left_column.plotly_chart(fig_product_col, use_container_width=True)
                    right_column.plotly_chart(fig_product_clar, use_container_width=True)
                    
                    # st.subheader("Sales by Color")
                    # st.plotly_chart(fig_product_col, use_container_width=True)
    
                    # st.subheader("Sales by Clarity")
                    # st.plotly_chart(fig_product_clar, use_container_width=True)
                        
            else:
                st.write("Password is wrong")
        else:
            st.write("User is not valid")

pass_word()













