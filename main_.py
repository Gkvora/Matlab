import streamlit as st
import pandas as pd
import warnings
import os
import sys_disc_
from io import BytesIO

## python -m streamlit run "G:/Gautam/Streamlit/main.py"

warnings.filterwarnings('ignore')
def create_excel_file(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    writer.close()  # Close the Excel writer object
    output.seek(0)
    return output.getvalue()
filepath = st.file_uploader('Browse')
name = None
if filepath is None:
    st.text("Upload Excel")
else:
    name = filepath.name
    print(name)
    
#path = st.text_input("Give filepath:")
if name is not None:
    df = sys_disc_.call(filepath)
    st.dataframe(df)
    excel_data = create_excel_file(df)
    st.download_button(label='Download Excel File', data=excel_data, file_name='data.xlsx', mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    

# python -m streamlit run "G:/Gautam/Streamlit/price/main_.py"