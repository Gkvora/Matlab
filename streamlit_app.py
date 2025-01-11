# description
    # this code is created to generate regulor reports in short time withot involment of data directoly
    # this code will generate reports easily for all type of user (with codding knowlage or without)

# database
    # in this web application we used mongodg database
    # this database has all data preprepared for this application

# framwork
    # we used streamlit framework to build this web application

# manualy run script
    # python -m streamlit run "//Sfs.net/BIA/BIA_FT/shani/project/web site/code/testing_version_4.py" --server.port 8501

#=========================== all required librarys that used in this web application ===========================

# a= datetime.datetime.now()
# b= str(a.hour)
# c = a.strftime("%A")

# if b<str(13):
#     Stock1 = Query(2,date.today(),date.today(),'1')
#     if c == "Monday":
#         Stock2 = Query(2,date.today()-timedelta(days=2),date.today()-timedelta(days=2),'2')
#     else:
#         Stock2 = Query(2,date.today()-timedelta(days=1),date.today()-timedelta(days=1),'2')
    
#     Stock = pd.concat([Stock1,Stock2])

# else:
#     Stock = Query(2,date.today(),date.today(),"1,2")

import streamlit as st # type: ignore
from PIL import Image # type: ignore
import datetime
import calendar
from datetime import datetime, timedelta,date
import pandas as pd # type: ignore
import polars as pl # type: ignore
import numpy as np # type: ignore
import math
import plotly.express as px # type: ignore
import logging
from streamlit import runtime # type: ignore
from streamlit.runtime.scriptrunner import get_script_run_ctx # type: ignore
import time
import subprocess
import pymongo # type: ignore
import pyodbc
import os
from io import BytesIO
from rembg import remove # type: ignore
import cv2
import base64
from streamlit_extras.metric_cards import style_metric_cards # type: ignore
from millify import millify # type: ignore
from streamlit_js_eval import streamlit_js_eval # type: ignore

import sys
sys.path.insert(0, r"\\Sfs.net\\BIA\\BIA_FT\\shani\\project\\web site\\Cut_Redefined\\assests\\code")
import code_a # type: ignore
sys.path.insert(0,r"\\Sfs.net\\BIA\\BIA_FT\\shani\\project\\web site\\pricing\\assests\\code")
import sys_disc # type: ignore
sys.path.insert(0, r"\\sfs.net\\bia\\BIA_FT\\shani\\project\\web site\\Light\\assests\\code")
import proportion_ov_copy2,proportion_ps_copy,proportion_ov4_copy2 # type: ignore
import proportion_ov_middle2,proportion_ov4_middle2,proportion_ps_middle # type: ignore

# =========================== connect mongo database ===========================
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client.finestar
monthly_collection_1 = db["cno 1"]
monthly_collection_2 = db["cno 2"]
monthly_collection_7 = db["cno 7"]
monthly_collection_9 = db["cno 9"]
monthly_collection_rap = db["Rap data"]

db_report_log = db["streamlit log"]

# =========================== setup streamlit page ===========================
def set_page_config():
    """Sets the page configuration."""
    st.set_page_config(
        page_title = "Finestar",
        page_icon= Image.open("//sfs.net/bia/BIA_AI/web site/logo.png"),
        layout="wide")

set_page_config()


placeholder = st.empty()

# =========================== change background color of the page ===========================
st.markdown("""
<style>
body {
    background-color: #BED8DD;
}
</style>
""", unsafe_allow_html=True)

# =========================== User login ===========================

actual_email = {"admin": "admin","AI-Report":"AI#pass"}
team_email = {"admin": "admin","AI-Report":"AI#pass"}
light_email = {"admin": "admin","ammar": "ammar"}
# power_bi = {"admin": "admin","parthiv": "parthiv"}

st.sidebar.markdown("#### Enter your credentials")

report = st.sidebar.selectbox("Select Report", tuple(["Dashboard","Cut Redefine","Pricing","Light"]))
email = st.sidebar.text_input("User")
password = st.sidebar.text_input("Password", type="password")
submit = st.sidebar.checkbox("Stay Login")

# =========================== log session ===========================
def create_db_log(selected_report_type,selected_start_date,selected_end_date,selected_shape,selected_color,selected_purity,selected_fls,selected_band, selected_chart_comp, selected_chart_comp2, selected_mode, selected_type, selected_lab,stone_location,mfg_location,stage,sub_report_type,Month,params,shape_for_sub_report,shape_for_sub_report_1,status,range_for_sub_report,file_path,image_names,local_ip):
    """
    Creates a log entry in the database.

    Args:
        selected_report_type (str): Selected Report Name.
        selected_start_date (Date): USer Selected Start Date.
        selected_end_date (Date): User Selected end Date.
        selected_shape (list): User Selected Shapes.
        selected_color (list): User Selected Colors.
        selected_purity (list): User Selected Puritys.
        selected_fls (list): User Selected LFS's.
        selected_band (list): User Selected Bands.
        selected_chart_comp (int): User Selected first  Chart Component.
        selected_chart_comp2 (int): User Selected Second  Chart Component.
        selected_mode (str): User Selected Mode daily,weekly, monthly,quaterly,yearly.
        selected_type (str): User Selected type total value,total crt, # of stones.
        selected_lab (list): User Selected  Lab.
        stone_location (list): USer Selected Stone Location.
        mfg_location (list): User Selected MFG Location.
        stage (list): User Selected  Stage.
        sub_report_type (str): User Selected Subreports.
        Month (list): User Selected Months.
        params (list): USer Selected Parametar.
        shape_for_sub_report (str): User Selected Filter for sub report.
        shape_for_sub_report_1 (str): User Selected Shape to compare shape with other shape in sub report.
        status (str): user selected status from sale , new arrival, and stock.
        range_for_sub_report (list): User Selected range for sub report.
        file_path (str): image file path.
        image_names (str): USer entered image name.
        local_ip (str): USer ip address.
    """
    temp_log_for_db = {
        "Date": str(datetime.now()),
        "Report_Type":str(report),
        "login":str(email),
        "sub_report":str(selected_report_type),
        "start_date": str(selected_start_date),
        "end_date": str(selected_end_date),
        "shape":str(selected_shape),
        "color":str(selected_color),
        "purity":str(selected_purity),
        "fls":str(selected_fls),
        "size":str(selected_band),
        "lab":str(selected_lab),
        "local_ip": str(local_ip),
        "mod": str(selected_mode),
        "type": str(selected_type),
        "first_comp": str(selected_chart_comp),
        "second_comp": str(selected_chart_comp2),
        "stone_location": str(stone_location),
        "mfg_location": str(mfg_location),
        "stage": str(stage),
        "sub_report_type": str(sub_report_type),
        "Month": str(Month),
        "params": str(params),
        "shape_for_sub_report": str(shape_for_sub_report),
        "shape_for_sub_report_1": str(shape_for_sub_report_1),
        "status": str(status),
        "range_for_sub_report": str(range_for_sub_report),
        "file_path": str(file_path),
        "image_names": str(image_names)
        }
    db_report_log.insert_one(temp_log_for_db)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('//Sfs.net/BIA/BIA_FT/shani/project/web site/log/'+str(time.strftime('%Y%m%d'))+'.log')
file_handler.setLevel(logging.INFO)

# =========================== find remote IP Address ===========================
def get_remote_ip() -> str:
    """
    Return  user ip address.

    Returns:
        str: IP  address of the user.

    """

    try:
        ctx = get_script_run_ctx()
        if ctx is None:
            return None
        session_info = runtime.get_instance().get_client(ctx.session_id)
        if session_info is None:
            return None
    except Exception as e:
        return None
    return session_info.request.remote_ip

returned_value = subprocess.check_output("ipconfig")
if get_remote_ip() == "::1":
    try:
        local_ip = str(str(str(str(returned_value).split(":")[9]).replace("   ","|")).split("|")[0])[1:-4]
    except:
        local_ip = str(str(str(str(returned_value).split(":")[3]).replace("   ","|")).split("|")[0])[1:-4]
else:
    local_ip = get_remote_ip()

if submit:

    # =========================== Report Selection Dashboard ===========================
    if  report=="Dashboard" and actual_email[email] == password:

        placeholder.empty()
        # SET COLUMAN
        sct1, sct2 = st.columns([9,1])

        # SET IMAGE
        image = Image.open("//Sfs.net/BIA/BIA_FT/shani/project/web site/image/logo.png")
        sct2.image(image, width=150)

        # TITLE
        sct1.title('DAILY REPORT')

        ## GREETING
        now = datetime.now()
        hour = now.hour
        if hour < 12:
            greeting = "Good morning"
        elif hour < 17:
            greeting = "Good afternoon"
        else:
            greeting = "Good evening"
        st.write("{}!".format(greeting))

        # =========================== Quotes for user ===========================
        @st.cache_data(show_spinner="Fetching data ......")
        def get_data():
            """
            read  data from excel file

            Returns:
                DataFrame: date,quotes data.
            """
            url2 = "//sfs.net/bia/BIA_AI/web site/Quotes.xlsx"
            return pd.read_excel(url2)
        
        Quotes= get_data()
        # date1 = '2024-03-10'
        date1 = date.today()
        date1 = pd.to_datetime(date1)
        date1 = date1.strftime('%Y-%m-%d')
        Quotes['Date'] = pd.to_datetime(Quotes['Date'])
        Quotes['Date'] = Quotes['Date'].dt.strftime('%Y-%m-%d')

        qq = Quotes[Quotes['Date'] == date1]

        qq = qq.reset_index()
        qq = qq.iloc[0]['Quote']
        qq1 = qq
        
        # =========================== Quote stream ===========================
        def stream_data(stream_str):
            for word in stream_str.split(" "):
                yield word + " "
                time.sleep(0.05)
        
        st.write_stream(stream_data(qq1))

        formatter = logging.Formatter(f'%(asctime)s - %(levelname)s - %(message)s - Local IP: {local_ip}')

        # =========================== some predifine variables ===========================
        total_report_type = ["Sale Dashboard", "Full Stock Report", "Quick Sale Report", "Sale/New Arrival Report", "Trend Report in %", "InFlow OutFlow Report", "Change in Price (Disc%/PPC)", "Shape wise Report", "Zone Wise Sale Report", "Sale Percentage Report", "Sale Proportion Report", "Heat Map of PPC Report", "Sale Comparison Report", "Tradescreen","Cno1 and Cno.2 Stock summary"]
        # total_report_type = ["Sale Dashboard", "Full Stock Report", "Quick Sale Report", "Sale/New Arrival Report", "Trend Report in %", "InFlow OutFlow Report", "Change in Price (Disc%/PPC)", "Shape wise Report", "Zone Wise Sale Report", "Sale Percentage Report", "Sale Proportion Report", "Import Report", "Heat Map of PPC Report", "Sale Comparison Report", "Tradescreen","Cno1 and Cno.2 Stock summary"]

        total_month = ['Dec','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov']

        total_year = ["2024","2023","2022"]

        total_first_comp = [1,2,7,9,"Rap Net","Manufacturing",None]
        total_second_comp = [2,1,7,9,"Rap Net","Manufacturing",None]
        total_first_comp_for_stock = [1,2,7,9,"Manufacturing",None]
        total_second_comp_for_stock = [2,1,7,9,"Manufacturing",None]
        total_comp_without_none = [1,2,7,9,"Rap Net","Manufacturing"]
        zone_wise_comp_without_none = [1,"Rap Net"]

        total_status = ["All", "Sale","New Arrival", "Stock"]
        final_status = ["Sale","New Arrival", "Stock"]

        total_params = ['Shape','Range',"Color","Purity","FLS","Polish","cut","symm"]

        total_parameters = ["Depth","Table","Ratio","Range"]

        total_mode = ["Daily", "Weekly", "Month", "Quarter", "Yearly"]
        total_data_type = ['No of Stone', 'Total Crt', 'Total Value']

        total_shape = ["All", "RD", "EM", "OV", "OVM", "RA", "PS", "CU", "CE", "CEB", "CM", "PC", "HT", "MQ", "AS", "BG", "TP", "Other"]
        final_shape = ["RD", "EM", "OV", "OVM", "RA", "PS", "CU", "CE", "CEB", "CM", "PC", "HT", "MQ", "AS", "BG", "TP", "Other"]
        
        final_first_shape = ["RD", "EM", "OV", "OVM", "RA", "PS", "CU", "CE", "CEB", "CM", "PC", "HT", "MQ", "AS", "BG", "TP", "Other",None]
        final_second_shape = ["EM", "RD", "OV", "OVM", "RA", "PS", "CU", "CE", "CEB", "CM", "PC", "HT", "MQ", "AS", "BG", "TP", "Other",None]

        total_lab = ["All", "GIA", "OTHER"]
        final_lab = ["GIA", "OTHER"]

        total_range = ["All", "1.00-1.19", "1.20-1.49", "1.50-1.99", "2.00-2.99", "3.00-3.99", "4.00-4.99", "5.00-9.99", "10+", "Doss"]
        final_range = ["1.00-1.19", "1.20-1.49", "1.50-1.99", "2.00-2.99", "3.00-3.99", "4.00-4.99", "5.00-9.99", "10+", "Doss"]

        total_color = ["All", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "FANCY"]
        final_color = ["D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "FANCY"]

        total_purity = ["All", "IF", "FL", "VVS1", "VVS2", "VS1", "VS2", "SI1", "SI2", "SI3-"]
        final_purity = ["IF", "FL", "VVS1", "VVS2", "VS1", "VS2", "SI1", "SI2", "SI3-"]

        total_fls = ["All", "NON", "FNT", "VSL", "SLT", "MED", "STG", "VST", "Other"]
        final_fls = ["NON", "FNT", "VSL", "SLT", "MED", "STG", "VST", "Other"]

        total_cut = ["All", "EX", "GD", "VG", "FR", "PR", "NON"]
        final_cut = ["EX", "GD", "VG", "FR", "PR", "NON"]

        total_symm = ["All", "EX", "GD", "VG", "FR", "PR"]
        final_symm = ["EX", "GD", "VG", "FR", "PR"]

        total_polish = ["All", "EX", "GD", "VG", "FR", "PR"]
        final_polish = ["EX", "GD", "VG", "FR", "PR"]

        quick_sale_selection = ["Shape","Range","Color","Purity"]

        select_full_stock_stage = ['All','STOCK', 'LAB', 'WITHOUT PRICE', 'UPCOMING', 'MANUFACTURING']

        data_uploaded_months_list = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

        # ======================== some Functions that will helps to generate reports ========================
        def log(selected_report_type,selected_start_date,selected_end_date,selected_shape,selected_color,selected_purity,selected_fls,selected_band,*args):
            """
            create  a log line for the report

            Args:
                selected_report_type (str): Selected Report Name.
                selected_start_date (Date): USer Selected Start Date.
                selected_end_date (Date): User Selected end Date.
                selected_shape (list): User Selected Shapes.
                selected_color (list): User Selected Colors.
                selected_purity (list): User Selected Puritys.
                selected_fls (list): User Selected LFS's.
                selected_band (list): User Selected Bands.
            """
            for fh in logger.handlers:
                logger.removeHandler(fh)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
            if len(args)==3:
                logger.info(f'IN-OT {selected_report_type} generated, Date: {selected_start_date} to {selected_end_date}, Shape:{selected_shape}, Color:{selected_color}, Purity:{selected_purity}, Fls:{selected_fls}, Size:{selected_band}, {args[0], args[1], args[3]} Filter generated')
            elif len(args)==1:
                logger.info(f'IN-OT {selected_report_type} generated, Date: {selected_start_date} to {selected_end_date}, Shape:{selected_shape}, Color:{selected_color}, Purity:{selected_purity}, Fls:{selected_fls}, Size:{selected_band}, {args[0]} Filter generated')
            else:
                logger.info(f'IN-OT {selected_report_type} generated, Date: {selected_start_date} to {selected_end_date}, Shape:{selected_shape}, Color:{selected_color}, Purity:{selected_purity}, Fls:{selected_fls}, Size:{selected_band}, {args[0], args[1]} Filter generated')

        @st.cache_data(show_spinner="Fetching data ......")
        def get_months(selected_from_year,selected_from_data_range,selected_data_range,selected_year):
            """
            month list from user selected data.
            Args:
                selected_from_year (str): user selected from year.
                selected_from_data_range (str): user selected  from data range.
                selected_data_range (str): user selected  data range.
                selected_year (str): user selecetd  year.

            Returns:
                list: Month List from user selected range.
            """
            months = []
            num = int(datetime.strptime(selected_from_data_range, '%b').month)
            if selected_from_year != selected_year:
                num_1 = 12 + int(datetime.strptime(selected_data_range, '%b').month)
            else:
                num_1 = int(datetime.strptime(selected_data_range, '%b').month)
            while num<=num_1:
                if num > 12:
                    temp_num = num
                    months.append(calendar.month_abbr[temp_num])
                else:
                    months.append(calendar.month_abbr[num])
                num+=1
            del num,num_1,selected_from_year,selected_from_data_range,selected_data_range,selected_year
            return months
        
        # @st.cache_data
        def get_cno_data(d_base,s_date,e_date):
            """search data from database using  date range.

            Args:
                d_base (collection): data base collection
                s_date (date): start date.
                e_date (date): end date.

            Returns:
                DataFram: data from database in range of start date and end date.
            """
            res = d_base.find({'Date': {'$gte': str(s_date),'$lte': str(e_date)}})
            temp_new_d= pd.DataFrame(res)
            # temp_df = temp_new_d.to_pandas()
            return temp_new_d
        
        new_d = ""
        new_data_fram_type = False
        month_list_for_inflow_outflow = []
        
        @st.cache_data(show_spinner="Fetching data ......")
        def filter_data(selected_start_date, selected_end_date, selected_comps):
            """call get_cno_data function and  filter data using selected start date and end date add cno filter for db collection.

            Args:
                selected_start_date (dare): user selcted satrt date.
                selected_end_date (date): user selected end date.
                selected_comps (list): user selected companys.

            Returns:
                DataFram: fina data frame with concated data of all selected companys.
            """
            # IF CODE BLOCK FOR START DATE AND END DATE IS SELECTED OR NOT 
            if selected_start_date and selected_end_date:
                new_df = pd.DataFrame()
                for i in selected_comps:
                    temp_new_df = pd.DataFrame()
                    if i == 1:
                        temp_new_df = get_cno_data(monthly_collection_1,selected_start_date,selected_end_date)
                        # res= monthly_collection_1.find({'Date': {'$gte': str(selected_start_date),'$lte': str(selected_end_date)}})
                    elif i == 2:
                        temp_new_df = get_cno_data(monthly_collection_2,selected_start_date,selected_end_date)
                        # res= monthly_collection_2.find({'Date': {'$gte': str(selected_start_date),'$lte': str(selected_end_date)}})
                    elif i == 7:
                        temp_new_df = get_cno_data(monthly_collection_7,selected_start_date,selected_end_date)
                        # res= monthly_collection_7.find({'Date': {'$gte': str(selected_start_date),'$lte': str(selected_end_date)}})
                    elif i == 9:
                        temp_new_df = get_cno_data(monthly_collection_9,selected_start_date,selected_end_date)
                        # res= monthly_collection_9.find({'Date': {'$gte': str(selected_start_date),'$lte': str(selected_end_date)}})
                    elif i == "Rap Net":
                        temp_new_df = get_cno_data(monthly_collection_rap,selected_start_date,selected_end_date)
                        # res= monthly_collection_rap.find({'Date': {'$gte': str(selected_start_date),'$lte': str(selected_end_date)}})
                    else:
                        df_1 = get_cno_data(monthly_collection_1,selected_start_date,selected_end_date)
                        df_2 = get_cno_data(monthly_collection_2,selected_start_date,selected_end_date)
                        df_7 = get_cno_data(monthly_collection_7,selected_start_date,selected_end_date)
                        df_9 = get_cno_data(monthly_collection_9,selected_start_date,selected_end_date)
                        temp_new_df = pd.concat([df_1,df_2,df_7,df_9])
                        del df_1,df_2,df_7,df_9
                    # temp_new_d= pl.DataFrame(res)
                    # temp_new_df = temp_new_d.to_pandas()
                    
                    new_df = pd.concat([new_df,temp_new_df])
                new_df['COMP_NO'] = new_df.apply(lambda x: "Rap Net" if x['COMP_NO'] == 11 else x['COMP_NO'], axis=1)

                try:
                    new_df.drop(columns=['_id'],inplace=True)
                except:
                    pass

            del selected_start_date, selected_end_date, temp_new_df
            return new_df

        @st.cache_data(show_spinner="Fetching data ......")
        def filter_data_with_user_selected(df2, selected_lab, selected_shape, selected_band, selected_color, selected_purity, selected_fls,selected_polish,selected_cut,selected_symm):
            """filter data with user selected data filter values.

            Args:
                df2 (dataFram): datafram to perform filters.
                selected_lab (list): user selected  lab values.
                selected_shape (list): user selected  shape values.
                selected_band (list): user selected bands.
                selected_color (list): user selected colors.
                selected_purity (list): user selected purity.
                selected_fls (list): user selected fls.
                selected_polish (list): user selected polish.
                selected_cut (list): user selected cut.
                selected_symm (list): user selected symm.

            Returns:
                DataFram: with filtered data.
            """
            with st.spinner('Preparing Data for more oprations...'):
                # FILTER DATA BY USER SELECTED        
                df2['LAB'] = df2.apply(lambda x: "GIA" if x['X_LAB'] == "GIA" else "OTHER", axis=1)
                df2['CUT_ACTUAL'] = df2.apply(lambda x: "EX" if x['CUT_ACTUAL'] == "-" else "EX" if x["CUT_ACTUAL"] == None else x['CUT_ACTUAL'], axis=1)
                df2 = df2[df2['LAB'].isin(selected_lab)]
                df2 = df2[df2['SHAPE1'].isin(selected_shape)]
                df2 = df2[df2['Band'].isin(selected_band)]
                df2 = df2[df2['COLOR_A'].isin(selected_color)]
                df2 = df2[df2['PURITY_A'].isin(selected_purity)]
                df2 = df2[df2['POLISH'].isin(selected_polish)]
                df2 = df2[df2['FLS'].isin(selected_fls)]
                df2 = df2[df2['CUT_ACTUAL'].isin(selected_cut)]
                df2 = df2[df2['SYMM'].isin(selected_symm)]
                
                return df2

                # del selected_lab, selected_shape, selected_band, selected_color, selected_purity, selected_fls,selected_polish,selected_cut,selected_symm

        @st.cache_data(show_spinner="Fetching data ......")
        def get_sorted_data_frane(selected_mode, df2, for_selected_type, for_aggfunc,selected_from_year,selected_from_data_range,selected_data_range,selected_year):
            """return pivot table by selected mode,comp,type and selected type.

            Args:
                selected_mode (str): user selected  mode.
                df2 (DataFram):  datafram to perform filters.
                for_selected_type (str): user selected type # of stones, total value and total crt.
                for_aggfunc (str): aggfunc type sum aor count.
                selected_from_year (str): user selected  from year.
                selected_from_data_range (str): user selected   from data range.
                selected_data_range (str): user selected   data range.
                selected_year (str): user selected   year.

            Returns:
                DataFram: final Pivot Table
            """
            with st.spinner('Preparing by Mode...'):
                df2['LAB1']=df2['X_LAB'].apply(lambda x: 1 if x=="GIA" else 2)
                df3 = df2.loc[(df2['TYPE'].isin(["SALE","NEW ARRIVAL"]))]
                # df_new = df2.loc[df2['TYPE'] == "NEW ARRIVAL"]
                # df3 = pd.concat([df_sale,df_new])
                # del df_sale,df_new

                df4 = df2.loc[df2['TYPE'] == "STOCK"]
                df3.sort_values(by=['PACKET_NO', 'LAB1'])
                df3 = df3.drop_duplicates(subset=['PACKET_NO', 'TYPE'])
                df4 = df4.drop_duplicates(subset=['PACKET_NO', selected_mode, 'TYPE'])
                df2 = pd.concat([df3,df4])
                df2.drop(['LAB1'], axis=1)
                del df3,df4

                if selected_mode == "Date":
                    
                    # SORT DATA BY DATE
                    df2.sort_values(by=[selected_mode])
                    
                    # CREATE PIVOT TABLE OF df2
                    df2 = pd.pivot_table(data=df2, index=[selected_mode],
                            columns=['COMP_NO', 'TYPE'],
                            values=for_selected_type,
                            aggfunc={for_selected_type: for_aggfunc},
                            fill_value=0,
                            margins=False).reset_index()
                elif selected_mode == "Week":

                    # SORT DATA BY DATE
                    s = {'Jan-1':0, 'Jan-2':1, 'Jan-3':2,'Jan-4':3,'Jan-5':4,
                        'Feb-1':5,'Feb-2':6,'Feb-3':7,'Feb-4':8,'Feb-5':9,
                        'Mar-1':10,'Mar-2':11,'Mar-3':12,'Mar-4':13,'Mar-5':14,
                        'Apr-1':15,'Apr-2':16,'Apr-3':17,'Apr-4':18,'Apr-5':19,
                        'May-1':20,'May-2':21,'May-3':22,'May-4':23,'May-5':24,
                        'Jun-1':25,'Jun-2':26,'Jun-3':27,'Jun-4':28,'Jun-5':29,
                        'Jul-1':30,'Jul-2':31,'Jul-3':32,'Jul-4':33,'Jul-5':34,
                        'Aug-1':35,'Aug-2':36,'Aug-3':37,'Aug-4':38,'Aug-5':39,
                        'Sep-1':40,'Sep-2':41,'Sep-3':42,'Sep-4':43,'Sep-5':44,
                        'Oct-1':45,'Oct-2':46,'Oct-3':47,'Oct-4':48,'Oct-5':49,
                        'Nov-1':50,'Nov-2':51,'Nov-3':52,'Nov-4':53,'Nov-5':54,
                        'Dec-1':55,'Dec-2':56,'Dec-3':57,'Dec-4':58,'Dec-5':59,}
                    
                    df2['Week'] = df2.apply(lambda x: 'Jan-1' if x['Week'] == 'Jan-01' else 'Jan-2' if x['Week'] == 'Jan-02' else 'Jan-3' if x['Week'] == 'Jan-03' else 'Jan-4' if x['Week'] == 'Jan-04' else 'Jan-5' if x['Week'] == 'Jan-05' else 'Feb-1' if x['Week'] == 'Feb-01' else 'Dec-5' if x['Week'] == 'Dec-05' else x['Week'], axis=1)
                    months = get_months(selected_from_year,selected_from_data_range,selected_data_range,selected_year)
                    
                    df2['is_week']=df2.apply(lambda x: True if str(x['Week']).split('-')[0] in months else False, axis=1)
                    df2 = df2.loc[(df2['is_week'] == True)]

                    # CREATE PIVOT TABLE OF df2
                    df2 = pd.pivot_table(data=df2.sort_values(by=[selected_mode], key=lambda x: x.map(s)).reset_index(), index=[selected_mode],
                            columns=['COMP_NO', 'TYPE'],
                            values=for_selected_type,
                            aggfunc={for_selected_type: for_aggfunc},
                            fill_value=0,
                            margins=False).reset_index()
                    
                    df2 = df2.sort_values(by=[selected_mode], key=lambda x: x.map(s)).reset_index()
                elif selected_mode == "Month":
                    # SORT DATA BY DATE
                    s = {'Jan - %s' % (selected_year[2:]):0,'Feb - %s' % (selected_year[2:]):1,'Mar - %s' % (selected_year[2:]):2,'Apr - %s' % (selected_year[2:]):3,'May - %s' % (selected_year[2:]):4,'Jun - %s' % (selected_year[2:]):5,'Jul - %s' % (selected_year[2:]):6,'Aug - %s' % (selected_year[2:]):7,'Sep - %s' % (selected_year[2:]):8,'Oct - %s' % (selected_year[2:]):9,'Nov - %s' % (selected_year[2:]):10,'Dec - %s' % (selected_year[2:]):11}
                    # CREATE PIVOT TABLE OF df2
                    df2 = pd.pivot_table(data=df2, index=[selected_mode],
                            columns=['COMP_NO', 'TYPE'],
                            values=for_selected_type,
                            aggfunc={for_selected_type: for_aggfunc},
                            fill_value=0,
                            margins=False).reset_index()
                    df2 = df2.sort_values(by=[selected_mode], key=lambda x: x.map(s)).reset_index()
                else:
                    # CREATE PIVOT TABLE OF df2
                    df2 = pd.pivot_table(data=df2, index=[selected_mode],
                            columns=['COMP_NO', 'TYPE'],
                            values=for_selected_type,
                            aggfunc={for_selected_type: for_aggfunc},
                            fill_value=0,
                            margins=False).reset_index()
                del selected_mode, for_selected_type, for_aggfunc
                return df2

        @st.cache_data(show_spinner="Fetching data ......")
        def get_selected_data(selected_fun_end_date, selected_fun_start_date,selected_comp_list,with_sun):
            """return filtered data.

            Args:
                selected_end_date (Date): End Date.
                selected_start_date (Date): Start Date.
                selected_comp_list (list): USer Selected Company list.
                with_sun (str): with ot without sunday.

            Returns:
                DataFrma: Filter Performed Data.
            """
            # GET FILTERED DATA
            df2 = filter_data(selected_fun_start_date, selected_fun_end_date, selected_comp_list)
            try:
                df2['Day'] = df2.apply(lambda x: datetime.strptime(str(x['Date']), "%d-%m-%Y").date().strftime('%a'), axis=1)
            except:
                df2['Day'] = df2.apply(lambda x: datetime.strptime(str(x['Date']), "%Y-%m-%d").date().strftime('%a'), axis=1)
            del selected_fun_start_date, selected_fun_end_date

            if with_sun=="sun":
                return df2
            else:
                return df2[df2['Day']!='Sun']

        @st.cache_data(show_spinner="Fetching data ......")
        def get_full_stock_data():
            """this function is created to  get full stock data from database.
                then perform some basic  data cleaning and return the data.
            Returns:
                DataFram: Full Stock Data.
            """
            con1 = pyodbc.connect(
                Driver="{ODBC Driver 18 for SQL Server}",
                Server="192.168.70.146\\FSD",
                Database="SALE_DISC",
                UID="analysis",
                port="1433",
                PWD="ai@2021",
                Encrypt='no',
                autocommit=True)

            full_stock = pd.read_sql("EXEC dbo.SP_GET_FULL_STOCK",con1)
            
            full_stock = full_stock.loc[(full_stock['STAGE'].isin(['STOCK', 'LAB', 'WITHOUT PRICE', 'UPCOMING', 'FACTORY',None]))]
            
            full_stock["STAGE"] = full_stock.apply(lambda x: "FACTORY" if x["STAGE"]==None else x["STAGE"], axis=1)
            
            full_stock['MFG_LOCATION'] = full_stock.apply(lambda x: "SURAT" if x['MFG_LOCATION']=="PURCHASE" else x['MFG_LOCATION'], axis=1)
            select_full_stock_location = full_stock['MFG_LOCATION'].unique()

            select_full_stock_stone_location = full_stock['STONE_LOCATION'].unique()
            
            
            full_stock['count']=1
            diameter = full_stock[["LENGTH", "WIDTH"]]
            full_stock["Length"] = diameter.apply(max, axis=1)
            full_stock["Width"] = diameter.apply(min, axis=1)

            # add new col for ratio this will cover ratio of width and length
            full_stock['Ratio'] = full_stock.apply(lambda x: round(x['Width'] / x['Length'], 2) if x['SHAPE'] == 'HT' and x['Length'] != 0 else round(x['Length'] / x['Width'], 2) if x['Length'] != 0 else 0, axis=1)

            full_stock['RANGE'] = full_stock.apply(lambda x: 'Doss' if x['WGT'] < 1 else '1.00-1.19' if x['WGT'] < 1.2 else '1.20-1.49' if x['WGT'] < 1.5 else '1.50-1.99' if x['WGT'] < 2 else '2.00-2.99' if x['WGT'] < 3 else '3.00-3.99' if x['WGT'] < 4 else '4.00-4.99' if x['WGT'] < 5 else '5.00-9.99' if x['WGT'] < 10 else '10+', axis=1)
            full_stock['Band'] = full_stock['WGT'].apply(lambda x: '0.01-0.23' if x <= 0.22 else
                                                    '0.23-0.29' if x <= 0.29 else
                                                    '0.30-0.34' if x <= 0.34 else
                                                    '0.35-0.39' if x <= 0.39 else
                                                    '0.40-0.49' if x <= 0.49 else
                                                    '0.50-0.59' if x <= 0.59 else
                                                    '0.60-0.69' if x <= 0.69 else
                                                    '0.70-0.79' if x <= 0.79 else
                                                    '0.80-0.89' if x <= 0.89 else
                                                    '0.90-0.94' if x <= 0.94 else
                                                    '0.95-0.99' if x <= 0.99 else
                                                    '1.00-1.09' if x <= 1.09 else
                                                    '1.10-1.17' if x <= 1.17 else
                                                    '1.18-1.29' if x <= 1.29 else
                                                    '1.30-1.39' if x <= 1.39 else
                                                    '1.40-1.49' if x <= 1.49 else
                                                    '1.50-1.69' if x <= 1.69 else
                                                    '1.70-1.99' if x <= 1.99 else
                                                    '2.00-2.49' if x <= 2.49 else
                                                    '2.50-2.99' if x <= 2.99 else
                                                    '3.00-3.99' if x <= 3.99 else
                                                    '4.00-4.99' if x <= 4.99 else
                                                    '5.00-5.99' if x <= 5.99 else
                                                    '6+')
            
            full_stock['SHAPE'] = full_stock.apply(lambda x: 'CM' if x['SHAPE'] == 'CM' and pd.isna(x['Ratio']) else 'CE' if x['SHAPE'] == 'CM' and x['Ratio'] >= 1.24 else x['SHAPE'], axis=1)
            full_stock['SHAPE'] = full_stock.apply(lambda x: 'CE' if x['SHAPE'] == 'CE' and pd.isna(x['Ratio']) else 'CM' if x['SHAPE'] == 'CE' and x['Ratio'] <= 1.23 else x['SHAPE'], axis=1)

            full_stock['SHAPE1'] = full_stock.apply(lambda x: 'RD' if x['SHAPE'] == 'RD' else 'EM' if x['SHAPE'] == 'EM' else 'AS' if x['SHAPE'] in ['AS', 'SE'] else 'BG' if x['SHAPE'] in ['BG', 'BT'] else 'CM' if x['SHAPE'] == 'CM' else 'HT' if x['SHAPE'] == 'HT' else 'MQ' if x['SHAPE'] == 'MQ' else 'OV' if x['SHAPE'] == 'OV' else 'PC' if x['SHAPE'] == 'PC' else 'PS' if x['SHAPE'] == 'PS' else 'RA' if x['SHAPE'] in ['RA', 'RN'] else 'CU' if x['SHAPE'] in ['CS', 'CU'] else 'CE' if x['SHAPE'] == 'CE' else 'CB' if x['SHAPE'] == 'CB' else 'Other', axis=1)
            full_stock['Shape Type'] = full_stock.apply(lambda x: "ROUND" if x['SHAPE1'] == "RD" else "FANCY", axis=1)
            
            full_stock['COLOR'] = full_stock['COLOR'].str.replace('+', '', regex=False)
            full_stock['COLOR'] = full_stock['COLOR'].str.replace('-', '', regex=False)

            full_stock['Col_Group']  = full_stock.apply(lambda x: "DEF" if x["COLOR"] in ["D","E","F"] else "GHI" if x["COLOR"] in ["G","H","I"] else "JKL" if x["COLOR"] in ['J','K','L'] else "M-/FANCY",axis=1)

            # edit purity some data has extra contant like + or -
            full_stock['PURITY'] = full_stock['PURITY'].str.replace("+", "", regex=False)
            full_stock['PURITY'] = full_stock['PURITY'].str.replace("-", "", regex=False)

            full_stock["clarity_Group"] = full_stock['PURITY'].str.replace("1", "", regex=False)
            full_stock["clarity_Group"] = full_stock['clarity_Group'].str.replace("2", "", regex=False)
            full_stock["clarity_Group"] = full_stock['clarity_Group'].str.replace("3", "", regex=False)
            full_stock["clarity_Group"] = full_stock.apply(lambda x: "FL-IF" if x['clarity_Group'] in ["FL","IF"] else x['clarity_Group'], axis=1)

            full_stock['COLOR_A'] = full_stock.apply(lambda x: "FANCY" if x['COLOR'] not in ['', 'D','E','F','G','H','I','J','K','L','M','N'] else x['COLOR'], axis=1)

            full_stock['LAB1'] = full_stock.apply(lambda x: 1 if x['LAB'] == 'GIA' else 2, axis=1)
                                    
            full_stock = full_stock.sort_values(["VPACKET_NO","LAB1"])
            full_stock = full_stock.drop_duplicates("VPACKET_NO")
            
            return full_stock,select_full_stock_location,select_full_stock_stone_location

        def full_stock_rapaport_formate(stock_data,full_stock_type_wise,for_selected_type,colors):
            """this function is created  to convert the data in rapaport formate HTML Table

                Args: 
                stock_data (dataframe): dataframe of stock data
                full_stock_type_wise (dataframe): dataframe of stock data type wise
                for_selected_type (str): selected type of stock
                colors (list): list of colors
            """

            # range_seq = ["1.00-1.19", "1.20-1.49", "1.50-1.99", "2.00-2.99", "3.00-3.99", "4.00-4.99", "5.00-9.99", "10+", "Doss"]
            # range_seq = ["0.01 - 0.03","0.04 - 0.07", "0.08 - 0.14", "0.15 - 0.17", "0.18 - 0.22", "0.23 - 0.29", "0.30 - 0.39", "0.40 - 0.49", "0.50 - 0.69", "0.70 - 0.89", "0.90 - 0.99", "1.00 - 1.49", "1.50 - 1.99", "2.00 - 2.99", "3.00 - 3.99", "4.00 - 4.99", "5.00 - 99.99"]
            range_seq = ["6+","5.00-5.99","4.00-4.99","3.00-3.99", "2.50-2.99", "2.00-2.49", "1.70-1.99", "1.50-1.69","1.40-1.49","1.30-1.39","1.18-1.29","1.10-1.17","1.00-1.09","0.95-0.99","0.90-0.94","0.80-0.89","0.70-0.79","0.60-0.69","0.50-0.59","0.40-0.49","0.35-0.39","0.30-0.34","0.23-0.29","0.01-0.22"]
            color_seq = []
            purity_seq = []
            if colors != "Col_Group":
                color_seq = ["D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "FANCY"]
                purity_seq = ['FL','IF','VVS1','VVS2','VS1','VS2','SI1','SI2','I1','I2','I3']
            else:
                color_seq = ["DEF", "GHI", "JKL", "M-/FANCY"]
                purity_seq = ['FL-IF','VVS','VS','SI','I']
            
            table_head = """<tr><th class="table_head">COLOR</th><th class="table_head">CLARITY</th><th class="table_head">6+</th><th class="table_head">5.00-5.99</th><th class="table_head">4.00-4.99</th><th class="table_head">3.00-3.99</th><th class="table_head">2.50-2.99</th><th class="table_head">2.00-2.49</th><th class="table_head">1.70-1.99</th><th class="table_head">1.50-1.69</th><th class="table_head">1.40-1.49</th><th class="table_head">1.30-1.39</th><th class="table_head">1.18-1.29</th><th class="table_head">1.10-1.17</th><th class="table_head">1.00-1.09</th><th class="table_head">0.95-0.99</th><th class="table_head">0.90-0.94</th><th class="table_head">0.80-0.89</th><th class="table_head">0.70-0.79</th><th class="table_head">0.60-0.69</th><th class="table_head">0.50-0.59</th><th class="table_head">0.40-0.49</th><th class="table_head">0.35-0.39</th><th class="table_head">0.30-0.34</th><th class="table_head">0.23-0.29</th><th class="table_head">0.01-0.22</th><th class="table_head">TOTAL</th></tr>"""
            table_rows = []
            range_head_str = ['<th class="table_header" colspan="2">Total</th>']
            final_total = 0
            for size_t in range_seq:
                if size_t in full_stock_type_wise['Band'].unique():
                    t = full_stock_type_wise.loc[(full_stock_type_wise['Band']==str(size_t))]
                    total = 0
                    if for_selected_type == "count":
                        total = sum(t[for_selected_type])
                    else:
                        total = round(sum(t[for_selected_type]),2)
                    final_total+=total
                    if total>0 and (for_selected_type == "count" or for_selected_type == "WGT"):
                        range_head_str.append('<td class="table_header">%s</td>' % total)
                    elif total>0 and for_selected_type != "count":
                        range_head_str.append('<td class="table_header">%s</td>' % '{:,.0f}'.format(total))
                    else:
                        range_head_str.append('<td class="table_header"></td>')
                else:
                    range_head_str.append('<td class="table_header"></td>')
            if for_selected_type == "count" or for_selected_type == "WGT":
                if for_selected_type != "count":
                    range_head_str.append('<td class="table_header">%s</td>' % round(final_total,2))
                else:
                    range_head_str.append('<td class="table_header">%s</td>' % final_total)
            else:
                range_head_str.append('<td class="table_header">%s</td>' % '{:,.0f}'.format(final_total))
            range_head_str = "<tr>%s</tr>" % ''.join(range_head_str)
            col_data = []
            is_first = True
            t_data = []
            for color_t in color_seq:
                col_data = ['<td class="table_header" rowspan="%s">%s</td>' % (len(purity_seq),''.join(str(color_t)))]
                row_data = []
                count = 0
                for purity_t in purity_seq:
                    row_data.append('<td class="table_header">%s</td>' % ''.join(str(purity_t)))
                    final_total = 0
                    for size_t in range_seq:
                        if size_t in full_stock_type_wise['Band'].unique():
                            # t = full_stock_type_wise.loc[(full_stock_type_wise['Band']==str(size_t))]
                            temp_d = stock_data.loc[((stock_data['Band']==str(size_t)) & (stock_data[colors]==str(color_t)))]
                            try:
                                if for_selected_type == "count":
                                    total = temp_d[str(purity_t)].iloc[0]
                                else:
                                    total = round(temp_d[str(purity_t)].iloc[0],2)
                                final_total+=total
                            except:
                                total = 0
                                final_total+=0
                            if total>0 and (for_selected_type == "count" or for_selected_type == "WGT"):
                                row_data.append('<td class="table_data_style">%s</td>' % total)
                            elif total>0 and for_selected_type != "count":
                                row_data.append('<td class="table_data_style">%s</td>' % '{:,.0f}'.format(total))
                            else:
                                row_data.append('<td class="table_data_style"></td>')
                        else:
                            row_data.append('<td class="table_data_style"></td>')
                    if final_total>0 and (for_selected_type == "count" or for_selected_type == "WGT"):
                        if for_selected_type != "count":
                            row_data.append('<td class="table_header">%s</td>' % round(final_total,2))
                        else:
                            row_data.append('<td class="table_header">%s</td>' % final_total)
                    elif final_total>0 and for_selected_type != "count":
                        row_data.append('<td class="table_header">%s</td>' % '{:,.0f}'.format(final_total))
                    else:
                        row_data.append('<td class="table_header"></td>')

                    count += 1
                    if is_first==True:
                        t_data.append("<tr>%s%s</tr>" % (''.join(col_data),''.join(row_data)))
                        is_first=False
                    else:
                        t_data.append("<tr>%s</tr>" % ''.join(row_data))
                    row_data = []
                    if len(purity_seq)==count:
                        is_first=True
            
            table_rows = str(''.join(table_head) + range_head_str + ''.join(t_data))
            st.markdown("""
                        <style>
                            .table_1 {
                                width:100%; 
                                }
                            .table_header{
                                text-align: center;
                                font-weight: bold;
                                font-size: 14px;
                                padding: 1px;
                                margin: 1px 1px 1px 1px;
                            }
                            .table_head{
                                text-align: center;
                                font-weight: bold;
                                font-size: 16px;
                                padding: 1px;
                                background-color: #287E8F;
                                margin: 1px 1px 1px 1px;
                                color: #FFFFFF;
                            }
                            .table_data_style{
                                text-align: center;
                                font-size: 14px;
                                padding: 1px;
                                margin: 1px 1px 1px 1px;
                            }
                            td, th{
                                width: 2%;
                            }
                            tr{
                                height: 12px;
                            }
                            tr:nth-child(even) {background-color: #f2f2f2;}
                        </style>
                        """, unsafe_allow_html=True)
            table_html_string = """
                        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                        <table id="data-table" class="table-borderless table-responsive card-1 p-4">%s</table>""" % ''.join(str(table_rows))
            st.markdown(((''.join(table_html_string).replace("'","")).replace("[","")).replace("]",""), unsafe_allow_html=True)

        def full_stock_report(fs,full_stock_report_data,for_selected_type,for_aggfunc,report_is_detailed):
            """this function created to create pivot table of fullstock data for rapaport formate data input.

            Args:
                fs (DataFram): Full stock data.
                full_stock_report_data (list): full stock stage.
                for_selected_type (str): data column one from # of stones, total crt, or total value.
                for_aggfunc (str): aggfunc type sum or count.
                report_is_detailed (str): if report is detailed or not. (group or detail)
            """
            if for_selected_type=="Net Value":
                for_selected_type = "NET_VALUE"
            
            col_type = "COLOR_A"
            clar_type = "PURITY"
            if report_is_detailed=="Group":
                col_type = "Col_Group"
                clar_type = "clarity_Group"
            else:
                col_type = "COLOR_A"
                clar_type = "PURITY"

            fs.groupby([clar_type, 'Band', col_type])[[str(for_selected_type)]].sum()
            
            df4 = pd.pivot_table(data=fs, index=['Band',col_type],
                                    columns=[clar_type],
                                    values=for_selected_type,
                                    aggfunc={for_selected_type: for_aggfunc},
                                    fill_value=0,
                                    margins=False).reset_index()
            # df4=df4[['Band','COLOR_A','FL','IF','VVS1','VVS2','VS1','VS2','SI1','SI2','I1','I2','I3']]
            # st.markdown("<h3 style='text-align: center;font-weight: bold;'>%s</h3>" % shape_1, unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: center;font-weight: bold;'>%s</h5>" % ",".join(full_stock_report_data), unsafe_allow_html=True)
            full_stock_rapaport_formate(df4,fs,for_selected_type,col_type)


        def pass_class():
            """this function is main function for dashboard report.
                this function will use some pre created function which listed below.
                1. get_months()
                2. get_cno_data()
                3. filter_data()
                4. filter_data_with_user_selected()
                5. get_sorted_data_frane()
                6. get_selected_data()
                7. get_full_stock_data()
                8. full_stock_rapaport_formate()
                9. full_stock_report()
                
            Returns:
                Report: selection wise report.
            """
            # ======================== from date and to date selection ========================
            
            col1,col2 = st.sidebar.columns([1,1])
           
            # SELECT YEAR FROM
            with col1:
                selected_from_year = st.selectbox("Select from Year", tuple(total_year))
            with col2:
                selected_from_data_range = st.selectbox("Select from Month", tuple(total_month))

            st.sidebar.write("TO")
            col1,col2 = st.sidebar.columns([1,1])
            
            # SELECT YEAR TO
            with col1:
                selected_year = st.selectbox("Select to Year", tuple(total_year))
            with col2:
                selected_data_range = st.selectbox("Select to Month", tuple(total_month))

            st.sidebar.write("COMPANYS")

            selected_companys_to_load_data = st.sidebar.multiselect("Select Companys:", [1,2,7,9,"Rap Net","Manufacturing"], [1,2])
            submit_load_data = st.sidebar.checkbox("Load Data")
            
            if (str(selected_year) != "2024" and str(selected_from_year) != "2024" and selected_data_range not in data_uploaded_months_list) or (str(selected_year) in total_year and str(selected_from_year) in total_year and selected_data_range in data_uploaded_months_list):
            # try:
                if submit_load_data:
                    # st.toast("Data Loading.......")
                    col1,col2,col3 = st.columns([5,1,1])
                    with col2:
                        if st.button("Clear Cache Data"):
                            st.cache_data.clear()
                            st.toast("Cleared Cach Data!")
                            # streamlit_js_eval(js_expressions="parent.window.location.reload()")
                    with col3:
                        if st.button("Reload page"):
                            streamlit_js_eval(js_expressions="parent.window.location.reload()")
                            st.toast("Reloaded Page!")
                            
                    total_first_comp = []
                    total_second_comp = []
                    total_second_comp_for_stock = []
                    total_first_comp_for_stock = []
                    total_comp_without_none = []
                    zone_wise_comp_without_none = []
                    for i in selected_companys_to_load_data:
                        total_first_comp.append(i)
                        total_second_comp.append(i)
                        total_first_comp_for_stock.append(i)
                        total_second_comp_for_stock.append(i)
                        total_comp_without_none.append(i)
                        if i in [1,"Rap Net"]:
                            zone_wise_comp_without_none.append(1)
                    total_first_comp.append(None)
                    total_second_comp.append(None)
                    total_first_comp_for_stock.append(None)
                    total_second_comp_for_stock.append(None)

                    selected_end_date = ""
                    selected_start_date=datetime.strptime(str(str(selected_from_year) + '-' + str(datetime.strptime(selected_from_data_range, '%b').month) + '-01'), "%Y-%m-%d").date()
                    if selected_data_range in ['Jan','Mar','May','Jul','Aug','Oct','Dec']:
                        selected_end_date=datetime.strptime(str(str(selected_year) + '-' + str(datetime.strptime(selected_data_range, '%b').month) + '-31'), "%Y-%m-%d").date()
                    elif selected_data_range in ['Apr','Jun','Sep','Nov']:
                        selected_end_date=datetime.strptime(str(str(selected_year) + '-' + str(datetime.strptime(selected_data_range, '%b').month) + '-30'), "%Y-%m-%d").date()
                    else:
                        selected_end_date=datetime.strptime(str(str(selected_year) + '-' + str(datetime.strptime(selected_data_range, '%b').month) + '-28'), "%Y-%m-%d").date()

                    # ======================== loading data ========================
                    df3 = get_selected_data(selected_end_date, selected_start_date,selected_companys_to_load_data,"without")
                    df3['count']=1
                    
                    # ======================== some filter input functions and some data filter function ========================
                    def get_table_of_data(df2,selected_mode,selected_companys):
                        """this function is created to create  table of data with sale% of each company
                            Args:
                                df2 (dataframe): dataframe of data
                                selected_mode (str): mode of data
                                selected_companys (list): list of companys to load data
                        """

                        comp_list = []
                        for i in selected_companys:
                            if i in [1,2,7,9]:
                                comp_list.append(i)
                        with st.spinner('Preparing Data Table...'):
                            # MAIN TITLE FOR DATA TABLE 
                            st.markdown("<h3 style='text-align: center;'>%s Brief Import Export Report</h3>" % (selected_mode), unsafe_allow_html=True)
                            # TEMP VARIABLES FOR LIST
                            comp_head = []
                            sale_proportion_head_string = []

                            # CREATE COMP HEAD BASED IN SELECTED COMP
                            # for com in [1,2,7,9]:
                            for com in comp_list:
                                comp_head.append('<th colspan="3" class="table_head" style="background-color:#287E8F;color:#FFFFFF;">%s</th>' % com)
                                sale_proportion_head_string.append('<th class="table_head" style="background-color:#287E8F;color:#FFFFFF;">%s</th>' % com)

                            # CREATE HEAD BASED ON NEW, STOCK, AND SALE
                            new_stock_sale_head_string = []
                            # for n in range(0, len([1,2,7,9])):
                            for n in range(0, len(comp_list)):
                                new_stock_sale_head_string.append('<th class="table_head" style="background-color:#287E8F;color:#FFFFFF;">New</th>')
                                new_stock_sale_head_string.append('<th class="table_head" style="background-color:#287E8F;color:#FFFFFF;">Stock</th>')
                                new_stock_sale_head_string.append('<th class="table_head" style="background-color:#287E8F;color:#FFFFFF;">Sale</th>') 

                            # CREATE HEAD BASED ON SELECTED TYPE
                            count_ctr_values_head_string = []
                            for n in range(0, len(comp_list)*3):
                            # for n in range(0, len([1,2,7,9])*3):
                                count_ctr_values_head_string.append('<th class="table_head" style="background-color:#287E8F;color:#FFFFFF;">%s</th>' % for_head_print_type)

                            # CREATE HEAD FOR TOTAL OF SALE, NEW, AND STOCK
                            data_total_of_all_type_string = []
                            comp_proposition_string = []
                            # for comp in [1,2,7,9]:
                            for comp in comp_list:
                                temp_total_string = []
                                try:
                                    proportion = round(df2[comp]['SALE'].sum()/(df2[comp]['STOCK'].sum()+df2[comp]['NEW ARRIVAL'].sum())*100, 2)
                                    comp_proposition_string.append('<th class="text-end" style="text-align: right;">%s</th>' % (0.0 if math.isnan(proportion) else proportion))
                                    # pass
                                except:
                                    comp_proposition_string.append('<th class="text-end" style="text-align: right;">%s</th>' % ('0.0'))
                                    # continue

                                for s_type in ['NEW ARRIVAL', 'STOCK', 'SALE']:
                                    try:
                                        if for_head_print_type == 'Total Crt':
                                            temp_total_string.append('<th class="text-end" style="text-align: right;">%s</th>' % round(df2[comp][s_type].sum(), 2))
                                        elif for_head_print_type == 'Total Value':
                                            temp_total_string.append('<th class="text-end" style="text-align: right;">%s</th>' % "${:,}".format(round(df2[comp][s_type].sum())))
                                        else:
                                            temp_total_string.append('<th class="text-end" style="text-align: right;">%s</th>' % df2[comp][s_type].sum())
                                        pass
                                    except:
                                        if for_head_print_type == 'Total Value':
                                            temp_total_string.append('<th class="text-end" style="text-align: right;">0.0</th>')
                                        else:
                                            temp_total_string.append('<th class="text-end" style="text-align: right;">0</th>')
                                        continue
                                data_total_of_all_type_string.append(''.join(temp_total_string))

                            if selected_mode == "Daily":
                                final_total_data_string = '<tr style="background-color:#287E8F;color:#FFFFFF;"><th class="table_head" colspan="2">TOTAL</th>%s%s</tr>' % (''.join(comp_proposition_string), ''.join(data_total_of_all_type_string))
                            else:
                                final_total_data_string = '<tr style="background-color:#287E8F;color:#FFFFFF;"><th class="table_head" colspan="1">TOTAL</th>%s%s</tr>' % (''.join(comp_proposition_string), ''.join(data_total_of_all_type_string))
                            # CREATE DATA ROW OF TABLE
                            data_row_string = []
                            for index in df2.index:

                                # TEMP VARIABLE FOR TD STRING LIST
                                comp_count_crt_values_string = []
                                comp_sale_proposition_string = []

                                # LOOP FOR SELECTED COMP
                                # for comp in [1,2,7,9]:
                                for comp in comp_list:
                                    # TEMP VARIABLE FOR ROW STRING
                                    temp_row_string = []
                                    # FOR LOOP FOR NEW, STOCK, AND SALE THIS WILL HELPS TO PRINT DATA BY THIS THREE COL
                                    for s_type in ['NEW ARRIVAL', 'STOCK', 'SALE']:
                                        # TRY BLOCK FOR PRINT DATA BY SELECTED TYPE 
                                        try:
                                            # CONDITIONAL BLOCK FOR EACH TYPE FOR FORMAT DATA AND ROUND IT
                                            if for_head_print_type == 'Total Crt':
                                                temp_row_string.append('<td class="text-end" style="text-align: right;">%s</td>' % round(df2[comp][s_type][index], 2))
                                            elif for_head_print_type == 'Total Value':
                                                temp_row_string.append('<td class="text-end" style="text-align: right;">%s</td>' %  "${:,}".format(round(df2[comp][s_type][index])))
                                            else:
                                                temp_row_string.append('<td class="text-end" style="text-align: right;">%s</td>' % df2[comp][s_type][index])
                                            pass
                                        except:
                                            if for_head_print_type == 'Total Value':
                                                temp_row_string.append('<td class="text-end" style="text-align: right;">0.0</td>')
                                            else:
                                                temp_row_string.append('<td class="text-end" style="text-align: right;">0</td>')
                                            continue
                                    # JOIN TEMP ROW STRING FOR SINGLE ROW WHICH START FROM COMP 1 TO LAST 
                                    comp_count_crt_values_string.append(''.join(temp_row_string))
                                    # TRY BLOCK FOR COUNT SALE PROPOTION BY. IF THER IS ANY ERROR OF SOME VALUES CAN BE NAN THAT TIME THIS WILL HELP
                                    try:
                                        sale_proportion = round(df2[comp]['SALE'][index]/(df2[comp]['STOCK'][index]+df2[comp]['NEW ARRIVAL'][index])*100, 2)
                                        comp_sale_proposition_string.append('<td class="text-end" style="text-align: right;">%s</td>' % (0.0 if math.isnan(sale_proportion) else sale_proportion))
                                        pass
                                    except:
                                        comp_sale_proposition_string.append('<td class="text-end" style="text-align: right;">%s</td>' % ('0.0'))
                                        continue
                                if selected_mode == "Daily":
                                    
                                    # ADD COLOR WHERE DAY IS SUNDAY
                                    if datetime.strptime(df2["Date"][index], '%Y-%m-%d').strftime("%A") == 'Sunday':
                                        # JOIN FINAL LISTS FOR SINGLE ROW WITH ROW COLOR
                                        data_row_string.append('<tr style="background-color:#FFCC99;color:#000000;"><td>%s</td><td>%s</td>%s%s</tr>' % (str(df2["Date"][index]), str(datetime.strptime(df2["Date"][index], '%Y-%m-%d').strftime("%A")), ''.join(comp_sale_proposition_string), ''.join(comp_count_crt_values_string)))
                                    else:
                                        # JOIN FINAL LISTS FOR SINGLE ROW 
                                        data_row_string.append('<tr style="color:#000000;"><td>%s</td><td>%s</td>%s%s</tr>' % (str(df2["Date"][index]), str(datetime.strptime(df2["Date"][index], '%Y-%m-%d').strftime("%A")), ''.join(comp_sale_proposition_string), ''.join(comp_count_crt_values_string)))
                                elif selected_mode == "Weekly":
                                    # JOIN FINAL LISTS FOR SINGLE ROW 
                                    data_row_string.append('<tr style="color:#000000;"><td colspan="2" style="text-align: center;">%s</td>%s%s</tr>' % (str(df2["Week"][index]), ''.join(comp_sale_proposition_string), ''.join(comp_count_crt_values_string)))
                                elif selected_mode == "Month":
                                    # JOIN FINAL LISTS FOR SINGLE ROW 
                                    data_row_string.append('<tr style="color:#000000;"><td colspan="2" style="text-align: center;">%s</td>%s%s</tr>' % (str(df2["Month"][index]), ''.join(comp_sale_proposition_string), ''.join(comp_count_crt_values_string)))
                                else:
                                    # JOIN FINAL LISTS FOR SINGLE ROW 
                                    data_row_string.append('<tr style="color:#000000;"><td colspan="2" style="text-align: center;">%s</td>%s%s</tr>' % (str(df2["Quarter"][index]), ''.join(comp_sale_proposition_string), ''.join(comp_count_crt_values_string)))
                            # STYLE FOR TABLE 
                            st.markdown("""
                                <style>
                                    .table_1 {
                                        width:100%; 
                                        }
                                    .table_head{
                                        text-align: center;
                                        font-weight: bold;
                                        font-size: 15px;
                                        padding: 2px;
                                    }
                                </style>
                                """, unsafe_allow_html=True)
                            
                            table_heading_html_string = ""
                            if selected_mode == "Daily":
                                # TABLE CODE JOINED SAPRATED STRINGS 
                                table_heading_html_string = """
                                        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                                        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                                        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                                        <table class="table_1 table-borderless table-responsive card-1 p-4">
                                            <tr style="background-color:#287E8F;color:#FFFFFF;">
                                                <th class="table_head">DATE</th>
                                                <th class="table_head" rowspan="3">Day</th>
                                                <th class="table_head" rowspan="2" colspan="%s">SALE %s</th>
                                                %s
                                            </tr>
                                            <tr style="background-color:#287E8F;color:#FFFFFF;">
                                                <th class="table_head" rowspan="2">Type</th>
                                                %s
                                            </tr>
                                            <tr>
                                                %s
                                                %s
                                            </tr>
                                            %s
                                            %s
                                        </table>
                                        """ % (str(len(comp_list)), '%', ''.join(comp_head), ''.join(new_stock_sale_head_string), ''.join(sale_proportion_head_string), ''.join(count_ctr_values_head_string), final_total_data_string, ''.join(data_row_string))
                                        # """ % (str(len([1,2,7,9])), '%', ''.join(comp_head), ''.join(new_stock_sale_head_string), ''.join(sale_proportion_head_string), ''.join(count_ctr_values_head_string), final_total_data_string, ''.join(data_row_string))
                            else:
                                # TABLE CODE JOINED SAPRATED STRINGS 
                                table_heading_html_string = """
                                        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                                        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                                        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                                        <table class="table_1 table-borderless table-responsive card-1 p-4">
                                            <tr style="background-color:#287E8F;color:#FFFFFF;">
                                                <th class="table_head" rowspan="4">%s</th>
                                                <th class="table_head" rowspan="3">Type</th>
                                                <th class="table_head" rowspan="2" colspan="%s">SALE %s</th>
                                                %s
                                            </tr>
                                            <tr style="background-color:#287E8F;color:#FFFFFF;">
                                                %s
                                            </tr>
                                            <tr>
                                                %s
                                                %s
                                            </tr>
                                            %s
                                            %s
                                        </table>
                                        """ % (selected_mode, str(len(comp_list)), '%', ''.join(comp_head), ''.join(new_stock_sale_head_string), ''.join(sale_proportion_head_string), ''.join(count_ctr_values_head_string), final_total_data_string, ''.join(data_row_string))
                                        # """ % (selected_mode, str(len([1,2,7,9])), '%', ''.join(comp_head), ''.join(new_stock_sale_head_string), ''.join(sale_proportion_head_string), ''.join(count_ctr_values_head_string), final_total_data_string, ''.join(data_row_string))
                            # EXECUTE HTML CODE 
                            st.markdown(table_heading_html_string, unsafe_allow_html=True)
                    
                    def get_demand_supply_chart(selected_mode,df3,selected_chart_comp,selected_type):
                        """this function is create to create demand and supply report from user given data and selected filter or paramers.
                        Args:
                            selected_mode (str): User Selected mode of report data daily,weekly,monthly, quaterly, or yearly.
                            df3 (DataFram): data with all filters which have to perform in this datafram.
                            selected_chart_comp (int): user selected comp.
                            selected_type (str): user selected  type # of Stones, total crt or total Value.

                        Returns:
                            write data frame in streamlit app web view.
                        """
                        with st.spinner('Preparing...'):
                            # EXECUTE HTML CODE 
                            st.markdown("<h3 style='text-align: center;'>Sale/New Arrival Report (Company-%s)</h3>" % selected_chart_comp, unsafe_allow_html=True)
                            if selected_chart_comp == "Manufacturing":
                                cno_1 = pd.concat([df3[1], df3[selected_mode]], axis=1)
                                cno_2 = pd.concat([df3[2], df3[selected_mode]], axis=1)
                                cno_7 = pd.concat([df3[7], df3[selected_mode]], axis=1)
                                cno_9 = pd.concat([df3[9], df3[selected_mode]], axis=1)
                                df2 = pd.DataFrame(pd.concat([cno_1, cno_2, cno_7, cno_9]))
                                df2 = df2.groupby([str(selected_mode)])[["NEW ARRIVAL","SALE","STOCK"]].sum().reset_index()
                            else:
                                df2 = pd.concat([df3[selected_chart_comp], df3[selected_mode]], axis=1)

                            # df2 = pd.concat([df3[selected_chart_comp], df3[selected_mode]], axis=1)
                            fig = px.line(df2, x=selected_mode, y=["SALE", 'NEW ARRIVAL'], markers=True)

                            newnames = {'SALE': "Sale", 'NEW ARRIVAL': "New Arrival"}
                            fig.for_each_trace(lambda t: t.update(name = newnames[t.name],
                                                            legendgroup = newnames[t.name],
                                                            hovertemplate = t.hovertemplate.replace(t.name, newnames[t.name])
                                                            )
                                        )
                            fig.update_layout(
                                legend_title="TYPE"
                            )
                            
                            # del newnames,df2,selected_mode,selected_chart_comp,df3
                            st.plotly_chart(fig, theme=None, use_container_width=True)

                            if selected_type=="No of Stone":
                                st.markdown("<h3 style='text-align: center;'># of Stone</h3>", unsafe_allow_html=True)
                            elif selected_type=="Total Value":
                                st.markdown("<h3 style='text-align: center;'>NET VALUE</h3>", unsafe_allow_html=True)
                            else:
                                st.markdown("<h3 style='text-align: center;'>Total Crt.</h3>", unsafe_allow_html=True)
                            if selected_chart_comp not in ['Rap Net','Global']:
                                df2=df2[[str(selected_mode),"STOCK","NEW ARRIVAL","SALE"]]
                            else:
                                df2=df2[[str(selected_mode),"NEW ARRIVAL","SALE"]]
                            return st.write(df2)

                    def get_trend_chart(selected_mode,df3,selected_chart_comp,selected_type):
                        """this function is created to cteate trend report with user selected  comp and type of data.

                        Args:
                            selected_mode (str): User Selected mode of report data daily,weekly,monthly, quaterly, or yearly.
                            df3 (DataFram): data with all filters which have to perform in this datafram.
                            selected_chart_comp (int): user selected comp.
                            selected_type (str): user selected  type # of Stones, total crt or total Value.

                        Returns:
                            write data frame in streamlit app web view.
                        """
                        with st.spinner('Preparing...'):
                            # EXECUTE HTML CODE 
                            st.markdown("<h3 style='text-align: center;'>Trend Report in % (Company-" + str(selected_chart_comp) + ")</h3>", unsafe_allow_html=True)
                            # df2 = pd.concat([df3[selected_chart_comp], df3[selected_mode]], axis=1)
                            if selected_chart_comp == "Manufacturing":
                                cno_1 = pd.concat([df3[1], df3[selected_mode]], axis=1)
                                cno_2 = pd.concat([df3[2], df3[selected_mode]], axis=1)
                                cno_7 = pd.concat([df3[7], df3[selected_mode]], axis=1)
                                cno_9 = pd.concat([df3[9], df3[selected_mode]], axis=1)
                                df2 = pd.DataFrame(pd.concat([cno_1, cno_2, cno_7, cno_9]))
                                df2 = df2.groupby([str(selected_mode)])[["NEW ARRIVAL","SALE","STOCK"]].sum().reset_index()
                            else:
                                df2 = pd.concat([df3[selected_chart_comp], df3[selected_mode]], axis=1)
                            if selected_chart_comp not in ['Rap Net','Global']:
                                df2['proportion'] = df2.apply(lambda x: round((x['SALE']/(x['SALE']+x['STOCK']))*100, 2) if x['SALE'] != 0 and x['STOCK'] else round(0, 2) , axis=1)
                            else:
                                df2['proportion'] = df2.apply(lambda x: round((x['SALE']/x['NEW ARRIVAL'])*100, 2) if x['SALE'] != 0 and x['NEW ARRIVAL'] else round(0, 2) , axis=1)
                            fig = px.line(df2, x=selected_mode, y="proportion", markers=True, text="proportion")
                            fig.update_traces(textposition="bottom right")
                            
                            st.plotly_chart(fig, theme=None, use_container_width=True)

                            if selected_type=="No of Stone":
                                st.markdown("<h3 style='text-align: center;'># of Stone</h3>", unsafe_allow_html=True)
                            elif selected_type=="Total Value":
                                st.markdown("<h3 style='text-align: center;'>NET VALUE</h3>", unsafe_allow_html=True)
                            else:
                                st.markdown("<h3 style='text-align: center;'>Total Crt.</h3>", unsafe_allow_html=True)

                            if selected_chart_comp not in ['Rap Net','Global']:
                                df2=df2[[str(selected_mode),"STOCK","NEW ARRIVAL","SALE","proportion"]]
                            else:
                                df2=df2[[str(selected_mode),"NEW ARRIVAL","SALE","proportion"]]
                            
                            df2["proportion"] = df2.apply(lambda x: f"{x['proportion']}%", axis=1)

                            return st.write(df2)

                    def get_heat_map(df5, selected_band,selected_chart_comp):
                        """this function is created to create heatmap report with user selected  band and company.

                        Args:
                            df3 (DataFram): data with all filters which have to perform in this datafram.
                            selected_band (list): user selected  band.
                            selected_chart_comp (int): user selected comp.
                        """
                        with st.spinner('Preparing...'):
                            # EXECUTE HTML CODE 
                            st.markdown("<h3 style='text-align: center;'>Company - " + str(selected_chart_comp) + "</h3>", unsafe_allow_html=True)
                            # "10+","5.00-9.99","4.00-4.99","3.00-3.99","2.00-2.99","1.50-1.99","1.20-1.49","1.00-1.19","Doss"
                            # "1.00-1.19", "1.20-1.49", "1.50-1.99", "2.00-2.99", "3.00-3.99", "4.00-4.99", "5.00-9.99", "10+", "Doss"
                            df5 = df5.loc[(df5["TYPE"]=="SALE")]
                            df3=df5.loc[(df5['Band'].isin(selected_band))]
                            df3.groupby(['COLOR_A', 'PURITY_A'])[['NET_RATE']].mean()
                            # df3.groupby(['COLOR_A', 'PURITY_A'])[['Net Value','WGT']].sum()
                            # df3['Result']=round((df3['Net Value']/df3['WGT']),2)
                            df3['Result']=round(df3["NET_RATE"],2)
                            df3['PURITY']=df3['PURITY_A']
                            df3['COLOR']=df3['COLOR_A']

                            s = {'D':0,'E':1,'F':2,'G':3,'H':4,'I':5,'J':6,'K':7,'L':8,'M':9,'N':10,'FANCY':11}
                            df3 = df3.sort_values(by=['COLOR'], key=lambda x: x.map(s)).reset_index()

                            # CREATE PIVOT TABLE OF df2
                            df2 = pd.pivot_table(data=df3, index=['COLOR'],
                                    columns=['PURITY'],
                                    aggfunc={'Result': 'mean'},
                                    fill_value=0,
                                    margins=False, sort=False)
                            
                            df = pd.DataFrame(df2['Result'])
                            
                            sort_head = ['FL','IF','VVS1','VVS2','VS1','VS2','SI1','SI2','SI3-']
                            head_list=list(df.columns)
                            list_of_head_index = []
                            
                            for i in head_list:
                                list_of_head_index.append(sort_head.index(str(i)))
                            
                            list_of_head_index.sort()
                            
                            df_sorted = [sort_head[i] for i in list_of_head_index]
                            df=df[df_sorted]
                            
                            for head in head_list:
                                df[str(head)] = df[str(head)].round(0)
                            fig = px.imshow(df,text_auto=True,aspect="auto")
                            fig.update_xaxes(side="top")
                            st.plotly_chart(fig, use_container_width=True)
                            
                            st.markdown("<h3 style='text-align: center;'>Company - " + str(selected_chart_comp) + "(# of Stones)</h3>", unsafe_allow_html=True)

                            df3=df5.loc[(df5['Band'].isin(selected_band))]
                            df3.groupby(['COLOR_A', 'PURITY_A'])[['PACKET_NO']].count()
                            # df3.groupby(['COLOR_A', 'PURITY_A'])[['Net Value','WGT']].sum()
                            # df3['Result']=round((df3['Net Value']/df3['WGT']),2)
                            df3['Result']=df3["PACKET_NO"]
                            df3['PURITY']=df3['PURITY_A']
                            df3['COLOR']=df3['COLOR_A']

                            s = {'D':0,'E':1,'F':2,'G':3,'H':4,'I':5,'J':6,'K':7,'L':8,'M':9,'N':10,'FANCY':11}
                            df3 = df3.sort_values(by=['COLOR'], key=lambda x: x.map(s)).reset_index()

                            # CREATE PIVOT TABLE OF df2
                            df2 = pd.pivot_table(data=df3, index=['COLOR'],
                                    columns=['PURITY'],
                                    aggfunc={'Result': 'count'},
                                    fill_value=0,
                                    margins=False, sort=False)
                            
                            df = pd.DataFrame(df2['Result'])
                            
                            sort_head = ['FL','IF','VVS1','VVS2','VS1','VS2','SI1','SI2','SI3-']
                            head_list=list(df.columns)
                            list_of_head_index = []
                            
                            for i in head_list:
                                list_of_head_index.append(sort_head.index(str(i)))
                            
                            list_of_head_index.sort()
                            
                            df_sorted = [sort_head[i] for i in list_of_head_index]
                            df=df[df_sorted]
                            
                            for head in head_list:
                                df[str(head)] = df[str(head)].round(0)
                            fig = px.imshow(df,text_auto=True,aspect="auto")
                            fig.update_xaxes(side="top")
                            st.plotly_chart(fig, use_container_width=True)

                            del fig,df_sorted,list_of_head_index,head_list,sort_head,df,df2,df3,s

                    def get_pie_chart(for_selected_type,df3,for_aggfunc,selected_chart_comp):
                        """This function is create to create zone wise pie chart from user selected  type of data.
                        
                        Args:
                            for_selected_type (str): user selected  type # of Stones, total crt or total Value.
                            df3 (DataFram): data with all filters which have to perform in this datafram.
                            for_aggfunc (str): aggfunc type sum or count.
                            selected_chart_comp (int): user selected comp.
                        Return:
                            this function datafram  df3 and selected chart company name.

                        """

                        # EXECUTE HTML CODE 
                        st.markdown("<h3 style='text-align: center;'>Zone wise Sale</h3>", unsafe_allow_html=True)
                        df3['SHAPE']=df3['SHAPE1']
                        new_d = pd.read_excel(r"\\sfs.net\bia\BIA_FT\shani\project\web site\country_to_zone.xlsx")

                        df3 = pd.merge(df3[['COMP_NO','TYPE','SALE_COUNTRY',for_selected_type,]], new_d[['SALE_COUNTRY','ZONE']],on='SALE_COUNTRY', how='left')
                        df3['ZONE'] = df3.apply(lambda x: "Other" if pd.isna(x['ZONE']) else x['ZONE'], axis=1)

                        if for_selected_type == "WGT":
                            df3.groupby(['COMP_NO', 'ZONE', 'TYPE'])[[str(for_selected_type)]].count()
                        else:
                            df3.groupby(['COMP_NO', 'ZONE', 'TYPE'])[[str(for_selected_type)]].sum()
                        
                        df4 = pd.pivot_table(data=df3, index=['ZONE'],
                                    columns=['COMP_NO', 'TYPE'],
                                    values=for_selected_type,
                                    aggfunc={for_selected_type: for_aggfunc},
                                    fill_value=0,
                                    margins=False).reset_index()
                        
                        if selected_chart_comp == "Manufacturing":
                            cno_1 = pd.concat([df4[1], df4['ZONE']], axis=1)
                            cno_2 = pd.concat([df4[2], df4['ZONE']], axis=1)
                            cno_7 = pd.concat([df4[7], df4['ZONE']], axis=1)
                            cno_9 = pd.concat([df4[9], df4['ZONE']], axis=1)
                            df2 = pd.DataFrame(pd.concat([cno_1, cno_2, cno_7, cno_9]))
                            # df2 = df2.groupby([str('ZONE')])[["NEW ARRIVAL","SALE","STOCK"]].sum().reset_index()
                        else:
                            df2 = pd.concat([df4[selected_chart_comp], df4['ZONE']], axis=1)
                        df2 = df2[df2["SALE"]!=0.00]
                        df2["ZONE"] = df2.apply(lambda x: "OTHER" if x["ZONE"]=="Other" else x["ZONE"], axis=1)

                        total = sum(df2["SALE"])
                        if for_selected_type == "count":
                            for_selected_type = "No of Stones"
                        table_head = "<tr><th class='table_header'>ZONE</th><th class='table_header'>%s</th><th class='table_header'>Percent</th></tr>" % for_selected_type
                        table_data = []
                        zone_list = ["U.S.A/CANADA","INDIA","HONGKONG/CHINA","SOUTHEAST ASIA","ISRAEL","EUROPE","OTHER"]
                        
                        for i in zone_list:
                            if i in df2['ZONE'].unique():
                                j = df2.loc[(df2["ZONE"].isin([i]))]
                                table_row = ['<td class="table_head">%s</td>' % i]
                                if for_selected_type == "Net Value":
                                    table_row.append('<td class="table_data_style">%s</td>' % '{:,.0f}'.format(sum(j["SALE"])))
                                else:
                                    table_row.append('<td class="table_data_style">%s</td>' % sum(j["SALE"]))
                                table_row.append('<td class="table_data_style">%s%s</td>' % (round(sum(j["SALE"])/total*100,1),str('%')))
                                table_data.append('<tr>%s</tr>' % ''.join(table_row))
                        
                        st.markdown("""
                                    <style>
                                        .table_1 {
                                            width:100%; 
                                            }
                                        .table_header{
                                            text-align: center;
                                            font-weight: bold;
                                            font-size: 18px;
                                            padding: 1px;
                                            margin: 1px 1px 1px 1px;
                                        }
                                        .table_head{
                                            text-align: center;
                                            font-weight: bold;
                                            font-size: 16px;
                                            padding: 1px;
                                            margin: 1px 1px 1px 1px;
                                        }
                                        .table_data_style{
                                            text-align: center;
                                            font-size: 14px;
                                            padding: 1px;
                                            margin: 1px 1px 1px 1px;
                                        }
                                        td, th{
                                            width: 2%;
                                        }
                                        tr{
                                            height: 12px;
                                        }
                                        tr:nth-child(even) {background-color: #f2f2f2;}
                                    </style>
                                    """, unsafe_allow_html=True)
                        
                        final_table_tag_str = "%s%s" % (table_head,table_data)
                        table_html_string = """
                                    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                                    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                                    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                                    <table class="table-borderless table-responsive card-1 p-4">%s</table>""" % final_table_tag_str
                        
                        zone_dict = {"U.S.A/CANADA":1,"INDIA":2,"HONGKONG/CHINA":3,"SOUTHEAST ASIA":4,"ISRAEL":5,"EUROPE":6,"OTHER":7}
                        df2.sort_values(by=["ZONE"], key=lambda x: x.map(zone_dict)).reset_index()
                        fig=px.pie(df2, values="SALE", names="ZONE", color="ZONE", hole=.4)
                        del df2,df4,df3,new_d,for_selected_type,for_aggfunc,selected_chart_comp
                        st.plotly_chart(fig, theme=None, use_container_width=True)
                        return st.markdown((((''.join(table_html_string).replace("'","")).replace("[","")).replace("]","")).replace("</tr>,","</tr>"), unsafe_allow_html=True)

                    def get_buble_chart(selected_mode,df3,selected_status):
                        """this function is created to ctreat  the bubble chart of ppc.

                        Args:
                            selected_mode (str): User Selected mode of report data daily,weekly,monthly, quaterly, or yearly.
                            df3 (DataFram): data with all filters which have to perform in this datafram.
                            selected_status (str): selected status sale, new arrival, or stock.

                        Returns:
                            plotly chart: returns the bubble chart of ppc.

                        """
                        # EXECUTE HTML CODE 
                        st.markdown("<h3 style='text-align: center;'>Bubble Chart</h3>", unsafe_allow_html=True)
                        df3=df3.loc[(df3['TYPE'].isin(selected_status))]
                        df3['Count'] = df3.apply(lambda x: 1 if x['PACKET_NO'] not in ['na', 'none', 0, "", " "] else 0, axis=1)
                        df3 = df3.groupby([selected_mode, 'COMP_NO'])[['Count', 'Net Value', 'WGT']].sum().reset_index()
                        df3['ppc']=round(df3['Net Value']/df3['WGT'],2)
                        df3['COMP_NO']= df3['COMP_NO'].apply(str)
                        # filter
                        if selected_mode == 'Week':
                            s = {'Jan-1':0, 'Jan-2':1, 'Jan-3':2,'Jan-4':3,'Jan-5':4,
                                'Feb-1':5,'Feb-2':6,'Feb-3':7,'Feb-4':8,'Feb-5':9,
                                'Mar-1':10,'Mar-2':11,'Mar-3':12,'Mar-4':13,'Mar-5':14,
                                'Apr-1':15,'Apr-2':16,'Apr-3':17,'Apr-4':18,'Apr-5':19,
                                'May-1':20,'May-2':21,'May-3':22,'May-4':23,'May-5':24,
                                'Jun-1':25,'Jun-2':26,'Jun-3':27,'Jun-4':28,'Jun-5':29,
                                'Jul-1':30,'Jul-2':31,'Jul-3':32,'Jul-4':33,'Jul-5':34,
                                'Aug-1':35,'Aug-2':36,'Aug-3':37,'Aug-4':38,'Aug-5':39,
                                'Sep-1':40,'Sep-2':41,'Sep-3':42,'Sep-4':43,'Sep-5':44,
                                'Oct-1':45,'Oct-2':46,'Oct-3':47,'Oct-4':48,'Oct-5':49,
                                'Nov-1':50,'Nov-2':51,'Nov-3':52,'Nov-4':53,'Nov-5':54,
                                'Dec-1':55,'Dec-2':56,'Dec-3':57,'Dec-4':58,'Dec-5':59,}
                        elif selected_mode == 'Month':
                            s = {'Jan-%s' % (selected_year[2:]):0,'Feb - %s' % (selected_year[2:]):1,'Mar - %s' % (selected_year[2:]):2,'Apr - %s' % (selected_year[2:]):3,'May - %s' % (selected_year[2:]):4,'Jun - %s' % (selected_year[2:]):5,'Jul - %s' % (selected_year[2:]):6,'Aug - %s' % (selected_year[2:]):7,'Sep - %s' % (selected_year[2:]):8,'Oct - %s' % (selected_year[2:]):9,'Nov - %s' % (selected_year[2:]):10,'Dec - %s' % (selected_year[2:]):11}
                        
                        if selected_mode in ['Week','Month']:
                            df3_1 = df3[df3['COMP_NO'] == '1'].reset_index()
                            df3_1 = df3_1.sort_values(by=[selected_mode], key=lambda x: x.map(s)).reset_index()
                            df3_2 = df3[df3['COMP_NO'] == '2'].reset_index()
                            df3_2 = df3_2.sort_values(by=[selected_mode], key=lambda x: x.map(s)).reset_index()
                            df3_7 = df3[df3['COMP_NO'] == '7'].reset_index()
                            df3_7 = df3_7.sort_values(by=[selected_mode], key=lambda x: x.map(s)).reset_index()
                            df3_9 = df3[df3['COMP_NO'] == '9'].reset_index()
                            df3_9 = df3_9.sort_values(by=[selected_mode], key=lambda x: x.map(s)).reset_index()
                        else:
                            df3_1 = df3[df3['COMP_NO'] == '1'].reset_index()
                            df3_2 = df3[df3['COMP_NO'] == '2'].reset_index()
                            df3_7 = df3[df3['COMP_NO'] == '7'].reset_index()
                            df3_9 = df3[df3['COMP_NO'] == '9'].reset_index()
                        df3_1['seq'] = df3_1.index
                        df3_2['seq'] = df3_2.index
                        df3_7['seq'] = df3_7.index
                        df3_9['seq'] = df3_9.index
                        df3 = pd.concat([df3_1, df3_2, df3_7, df3_9])

                        fig = px.scatter(
                            df3,
                            x="seq",
                            y="ppc",
                            size="Count",
                            color="COMP_NO",
                            hover_name=selected_mode,
                            log_x=True,
                            size_max=20,
                        )
                        del df3,df3_1,df3_2,df3_7,df3_9,selected_mode
                        return st.plotly_chart(fig, theme=None, use_container_width=True)

                    @st.cache_data(show_spinner="Fetching data ......")
                    def filter_data_user_selected(df2, type, selected_lab, *args):
                        """this function  filters data based on user selected filters.

                        Args:
                            df2 (DataFram): data frame to perform filter.
                            type (str): selection one of 'SHAPE1','Band','COLOR_A','PURITY_A','POLISH','FLS','CUT_ACTUAL','SYMM'.
                            selected_lab (str): user selected lab.

                        Returns:
                            DataFram: Filtered data.
                        """
                        # FILTER DATA BY USER SELECTED
                        df2['LAB'] = df2.apply(lambda x: "GIA" if x['X_LAB'] == "GIA" else "OTHER", axis=1)
                        df2 = df2[df2['LAB'].isin(selected_lab)]

                        tag_list = ['SHAPE1','Band','COLOR_A','PURITY_A','POLISH','FLS','CUT_ACTUAL','SYMM']
                        tag_list.remove(str(type))
                        for i in range(0,len(tag_list)):
                            df2 = df2[df2[tag_list[i]].isin(args[i])]
                        del tag_list,selected_lab
                        return df2

                    def get_shape_wise_Comparison_chart(for_selected_type,df3,for_aggfunc,selected_chart_comp,selected_chart_comp2,type):
                        """this  function  returns type wise comparison chart.
                        in this function we used predifine function listed below.
                            1.filter_data_user_selected

                        Args:
                            for_selected_type (str): selected 
                            df3 (DataFram): datafram  to perform filter.
                            for_aggfunc (str): sggfunc  to perform aggfunc sum or count.
                            selected_chart_comp (int): selected first company.
                            selected_chart_comp2 (int): selected second company.
                            type (str): selection one of 'SHAPE1','Band','COLOR_A','PURITY_A','POLISH','FLS','CUT_ACTUAL','SYMM'.
                        """
                        if selected_chart_comp == selected_chart_comp2:
                            st.warning("Please Selecte Different Comapany.")
                        elif selected_chart_comp == None:
                            df3=df3[df3['COMP_NO']==selected_chart_comp2]
                        elif selected_chart_comp2 == None:
                            df3=df3[df3['COMP_NO']==selected_chart_comp]
                        elif selected_chart_comp == "Manufacturing":
                            df1 = df3.loc[(df3['COMP_NO'].isin([1,2,7,9]))]
                            df1['COMP_NO']="Manufacturing"
                            df2=df3[df3['COMP_NO']==selected_chart_comp2]
                            df3=pd.concat([df1, df2])
                        elif selected_chart_comp2 == "Manufacturing":
                            df2 = df3.loc[(df3['COMP_NO'].isin([1,2,7,9]))]
                            df2['COMP_NO']="Manufacturing"
                            df1=df3[df3['COMP_NO']==selected_chart_comp]
                            df3=pd.concat([df1, df2])
                        else:
                            df1=df3[df3['COMP_NO']==selected_chart_comp]
                            df2=df3[df3['COMP_NO']==selected_chart_comp2]
                            df3=pd.concat([df1, df2])

                        head_str = str("<h3 style='text-align: center;'>" + str(type) + " Wise Sale% Comparison</h3>")
                        
                        # EXECUTE HTML CODE 
                        st.markdown(head_str, unsafe_allow_html=True)
                        
                        if str(type) == 'Shape':
                            type="SHAPE1"
                            df3 = filter_data_user_selected(df3, type, selected_lab, selected_band, selected_color, selected_purity, selected_polish,selected_fls,selected_cut,selected_symm)
                            s = {"RD":0,"EM":1,"OV":2,"RA":3,"PS":4,"CU":5,"CE":6,"CM":7,"PC":8,"HT":9,"MQ":10,"AS":11,"BG":12,"TP":13,"Other":14}
                            df3 = df3.sort_values(by=['SHAPE1'], key=lambda x: x.map(s)).reset_index()
                        elif str(type) == "Range":
                            type="Band"
                            df3 = filter_data_user_selected(df3, type, selected_lab, selected_shape, selected_color, selected_purity, selected_polish,selected_fls,selected_cut,selected_symm)
                            s = {"10+":7,"5.00-9.99":6,"4.00-4.99":5,"3.00-3.99":4,"2.00-2.99":3,"1.50-1.99":2,"1.20-1.49":1,"1.00-1.19":0,"Doss":8}
                            df3 = df3.sort_values(by=['Band'], key=lambda x: x.map(s)).reset_index()
                        elif str(type) == "Polish":
                            type = "POLISH"
                            df3 = filter_data_user_selected(df3, type, selected_lab, selected_shape, selected_band, selected_color, selected_purity,selected_fls,selected_cut,selected_symm)
                            s = {"EX":0,"VG":1,"GD":2,"FR":3,"PR":4}
                            df3 = df3.sort_values(by=['POLISH'], key=lambda x: x.map(s)).reset_index()
                        elif str(type) == "Color":
                            type="COLOR_A"
                            df3 = filter_data_user_selected(df3, type, selected_lab, selected_shape, selected_band, selected_purity, selected_polish,selected_fls,selected_cut,selected_symm)
                            s = {"D":0,"E":1,"F":2,"G":3,"H":4,"I":5,"J":6,"K":7,"L":8,"M":9,"N":10,"FANCY":11}
                            df3 = df3.sort_values(by=['COLOR_A'], key=lambda x: x.map(s)).reset_index()
                        elif str(type) == "Purity":
                            type="PURITY_A"
                            df3 = filter_data_user_selected(df3, type, selected_lab, selected_shape, selected_band, selected_color, selected_polish,selected_fls,selected_cut,selected_symm)
                            s = {"FL":0,"IF":1,"VVS1":2,"VVS2":3,"VS1":4,"VS2":5,"VS3-":6}
                            df3 = df3.sort_values(by=['PURITY_A'], key=lambda x: x.map(s)).reset_index()
                        elif str(type)=="cut":
                            type="CUT_ACTUAL"
                            df3 = filter_data_user_selected(df3, type, selected_lab, selected_shape, selected_band, selected_color, selected_purity,selected_polish,selected_fls,selected_symm)
                            s = {"EX":0,"VG":1,"GD":2,"FR":3,"PR":4}
                            df3 = df3.sort_values(by=['CUT_ACTUAL'], key=lambda x: x.map(s)).reset_index()
                        elif str(type)=="symm":
                            type="SYMM"
                            df3 = filter_data_user_selected(df3, type, selected_lab, selected_shape, selected_band, selected_color, selected_purity,selected_polish,selected_fls,selected_cut)
                            s = {"EX":0,"VG":1,"GD":2,"FR":3,"PR":4}
                            df3 = df3.sort_values(by=['SYMM'], key=lambda x: x.map(s)).reset_index()
                        elif str(type) == "FLS":
                            type="FLS"
                            df3 = filter_data_user_selected(df3, type, selected_lab, selected_shape, selected_band, selected_color, selected_purity,selected_polish,selected_cut,selected_symm)
                            s = {"NON":0,"FNT":1,"VSL":2,"SLT":3,"NED":4,"STG":5,"VST":6}
                            df3 = df3.sort_values(by=['FLS'], key=lambda x: x.map(s)).reset_index()
                        else:
                            type=type
                        
                        if for_selected_type == "WGT":
                            df3.groupby(['COMP_NO', str(type), 'TYPE'])[[str(for_selected_type)]].count()
                        else:
                            df3.groupby(['COMP_NO', str(type), 'TYPE'])[[str(for_selected_type)]].sum()
                        df2=df3[df3['TYPE']=="SALE"]
                        df = df2[df2['COMP_NO']==selected_chart_comp]
                        
                        total_df = df[str(for_selected_type)].sum()
                        df['result'] = (df[str(for_selected_type)]/total_df)*100

                        df1 = df2[df2['COMP_NO']==selected_chart_comp2]
                        total_df = df1[str(for_selected_type)].sum()

                        df1['result'] = (df1[str(for_selected_type)]/total_df)*100
                        df2= pd.concat([df,df1])

                        fig = px.histogram(df2, 
                                           x=str(type),
                                           y='result', 
                                           color='COMP_NO', 
                                           histfunc='sum', 
                                           barmode='group',
                                           height=400,
                                           hover_data=df2.columns)
                        fig.update_traces(hovertemplate='%{x} - %{y:.2f}%')
                        fig.update_layout(
                            yaxis=dict(
                            title='Sale%',
                            titlefont_size=16,
                            tickfont_size=14,
                        ),
                        xaxis=dict(
                            title=str(type),
                            titlefont_size=16,
                            tickfont_size=14,
                        ),)
                        
                        st.plotly_chart(fig, theme=None, use_container_width=True)
                        df2['Sale%']=df2['result']
                        
                        df3 = pd.pivot_table(data=df2, index=[str(type)],
                                columns=['COMP_NO'],
                                aggfunc={for_selected_type: 'sum'},
                                fill_value=0,
                                margins=False, sort=False)
                        try:
                            df3['Diff']=df3[for_selected_type][selected_chart_comp]-df3[for_selected_type][selected_chart_comp2]
                        except:
                            pass

                        df4=pd.DataFrame()
                        a = list(df3.columns)
                        for i in a:
                            if selected_chart_comp in i:
                                df4[str(selected_chart_comp)] = df3[i]
                                df4[str(selected_chart_comp)] = df4[str(selected_chart_comp)].apply(lambda x: float("{:.2f}".format(x)))
                            if selected_chart_comp2 in i:
                                df4[str(selected_chart_comp2)] = df3[i]
                                df4[str(selected_chart_comp2)] = df4[str(selected_chart_comp2)].apply(lambda x: float("{:.2f}".format(x)))
                        if selected_chart_comp == None or selected_chart_comp2 == None:
                            pass
                        else:
                            df4['Diff'] = df3[df3.columns[2]]
                            df4["Diff"] = df4["Diff"].apply(lambda x: float("{:.2f}".format(x)))
                        if for_selected_type == "count":
                            head_str = str("<h3 style='text-align: center;'>No of Stones.</h3>")
                        elif for_selected_type == "WGT":
                            head_str = str("<h3 style='text-align: center;'>Total CRT.</h3>")
                        else:
                            head_str = str("<h3 style='text-align: center;'>Total Net Value.</h3>")
                        # EXECUTE HTML CODE 
                        st.markdown(head_str, unsafe_allow_html=True)
                        del df1,df2,df,total_df,for_selected_type,type,head_str,df3,for_aggfunc,selected_chart_comp,selected_chart_comp2

                    def get_shape_wise_proportion_chart(for_selected_type,df3,for_aggfunc,selected_chart_comp,selected_chart_comp2,type,selected_type):
                        """this function is created to create  a bar chart of shape wise proportion of two companies.

                        Args:
                            for_selected_type (str): selected 
                            df3 (DataFram): datafram  to perform filter.
                            for_aggfunc (str): sggfunc  to perform aggfunc sum or count.
                            selected_chart_comp (int): selected first company.
                            selected_chart_comp2 (int): selected second company.
                            type (str): selection one of 'SHAPE1','Band','COLOR_A','PURITY_A','POLISH','FLS','CUT_ACTUAL','SYMM'.
                            selected_type (str): user selected  type # of stones,total value, or total crt.
                        """
                        if selected_chart_comp == selected_chart_comp2:
                            st.warning("Please Selecte Different Comapany.")
                        elif selected_chart_comp == None:
                            df3=df3[df3['COMP_NO']==selected_chart_comp2]
                        elif selected_chart_comp2 == None:
                            df3=df3[df3['COMP_NO']==selected_chart_comp]
                        elif selected_chart_comp == "Manufacturing":
                            cno_1 = df3[df3['COMP_NO']==1]
                            cno_2 = df3[df3['COMP_NO']==2]
                            cno_7 = df3[df3['COMP_NO']==7]
                            cno_9 = df3[df3['COMP_NO']==9]
                            df1 = pd.DataFrame(pd.concat([cno_1, cno_2, cno_7, cno_9]))
                            df1['COMP_NO']="Manufacturing"
                            df2=df3[df3['COMP_NO']==selected_chart_comp2]
                            df3=pd.concat([df1, df2])
                        elif selected_chart_comp2 == "Manufacturing":
                            cno_1 = df3[df3['COMP_NO']==1]
                            cno_2 = df3[df3['COMP_NO']==2]
                            cno_7 = df3[df3['COMP_NO']==7]
                            cno_9 = df3[df3['COMP_NO']==9]
                            df2 = pd.DataFrame(pd.concat([cno_1, cno_2, cno_7, cno_9]))
                            df2['COMP_NO']="Manufacturing"
                            df1=df3[df3['COMP_NO']==selected_chart_comp]
                            df3=pd.concat([df1, df2])
                        else:
                            df1=df3[df3['COMP_NO']==selected_chart_comp]
                            df2=df3[df3['COMP_NO']==selected_chart_comp2]
                            df3=pd.concat([df1, df2])
                        
                        df3['LAB1'] = df3.apply(lambda x: 1 if x['X_LAB'] == 'GIA' else 2, axis=1)
                        df3.sort_values(by=['PACKET_NO', 'LAB1'])
                        df3 = df3.drop_duplicates(subset=['PACKET_NO', 'Flow_type'])

                        s=""
                        # EXECUTE HTML CODE 
                        st.markdown("<h3 style='text-align: center;'>" + str(type) + " Wise Sale Proportion Comparison.</h3>", unsafe_allow_html=True)
                        if str(type) == 'Shape':
                            type="SHAPE1"
                            df3 = filter_data_user_selected(df3, type, selected_lab, selected_band, selected_color, selected_purity, selected_polish,selected_fls,selected_cut,selected_symm)
                            s = {"RD":0,"EM":1,"OV":2,"RA":3,"PS":4,"CU":5,"CE":6,"CM":7,"PC":8,"HT":9,"MQ":10,"AS":11,"BG":12,"TP":13,"Other":14}
                        elif str(type) == "Range":
                            type="Band"
                            df3 = filter_data_user_selected(df3, type, selected_lab, selected_shape, selected_color, selected_purity, selected_polish,selected_fls,selected_cut,selected_symm)
                            s = {"10+":7,"5.00-9.99":6,"4.00-4.99":5,"3.00-3.99":4,"2.00-2.99":3,"1.50-1.99":2,"1.20-1.49":1,"1.00-1.19":0,"Doss":8}
                        elif str(type) == "Polish":
                            type = "POLISH"
                            df3 = filter_data_user_selected(df3, type, selected_lab, selected_shape, selected_band, selected_color, selected_purity,selected_fls,selected_cut,selected_symm)
                            s = {"EX":0,"VG":1,"GD":2,"FR":3,"PR":4}
                        elif str(type) == "Color":
                            type="COLOR_A"
                            df3 = filter_data_user_selected(df3, type, selected_lab, selected_shape, selected_band, selected_purity, selected_polish,selected_fls,selected_cut,selected_symm)
                            s = {"D":0,"E":1,"F":2,"G":3,"H":4,"I":5,"J":6,"K":7,"L":8,"M":9,"N":10,"FANCY":11}
                        elif str(type) == "Purity":
                            type="PURITY_A"
                            df3 = filter_data_user_selected(df3, type, selected_lab, selected_shape, selected_band, selected_color, selected_polish,selected_fls,selected_cut,selected_symm)
                            s = {"FL":0,"IF":1,"VVS1":2,"VVS2":3,"VS1":4,"VS2":5,"VS3-":6}
                        elif str(type)=="cut":
                            type="CUT_ACTUAL"
                            df3 = filter_data_user_selected(df3, type, selected_lab, selected_shape, selected_band, selected_color, selected_purity,selected_polish,selected_fls,selected_symm)
                            s = {"EX":0,"VG":1,"GD":2,"FR":3,"PR":4}
                        elif str(type)=="symm":
                            type="SYMM"
                            df3 = filter_data_user_selected(df3, type, selected_lab, selected_shape, selected_band, selected_color, selected_purity,selected_polish,selected_fls,selected_cut)
                            s = {"EX":0,"VG":1,"GD":2,"FR":3,"PR":4}
                        elif str(type) == "FLS":
                            type="FLS"
                            df3 = filter_data_user_selected(df3, type, selected_lab, selected_shape, selected_band, selected_color, selected_purity,selected_polish,selected_cut,selected_symm)
                            s = {"NON":0,"FNT":1,"VSL":2,"SLT":3,"NED":4,"STG":5,"VST":6}
                        else:
                            type=type
                        
                        if for_selected_type == "WGT":
                            df3.groupby(['COMP_NO', str(type), 'TYPE'])[[str(for_selected_type)]].count()
                        else:
                            df3.groupby(['COMP_NO', str(type), 'TYPE'])[[str(for_selected_type)]].sum()
                        
                        df4 = pd.pivot_table(data=df3, index=[str(type)],
                                    columns=['COMP_NO', 'TYPE'],
                                    values=for_selected_type,
                                    aggfunc={for_selected_type: for_aggfunc},
                                    fill_value=0,
                                    margins=False).reset_index()
                        
                        if selected_chart_comp == None:
                            df2 = pd.concat([df4[selected_chart_comp2], df4[str(type)]], axis=1)
                            df2['COMP_NO']=selected_chart_comp2
                        elif selected_chart_comp2 == None:
                            df2 = pd.concat([df4[selected_chart_comp], df4[str(type)]], axis=1)
                            df2['COMP_NO']=selected_chart_comp
                        else:
                            df2 = pd.concat([df4[selected_chart_comp], df4[str(type)]], axis=1)
                            df2['COMP_NO']=selected_chart_comp
                            df1 = pd.concat([df4[selected_chart_comp2], df4[str(type)]], axis=1)
                            df1['COMP_NO']=selected_chart_comp2
                            df2=pd.concat([df2, df1])
                        df2 = df2.sort_values(by=[str(type)], key=lambda x: x.map(s)).reset_index()
                        
                        df1=df2[df2['COMP_NO']==selected_chart_comp]
                        if selected_chart_comp not in ['Rap Net','Global']:
                            df1['proportion'] = df1.apply(lambda x: round((x['SALE']/(x['NEW ARRIVAL']+x['STOCK']))*100, 2) if x['SALE'] != 0 and x['NEW ARRIVAL'] and x['STOCK'] else round(0, 2) , axis=1)
                        else:
                            df1['proportion'] = df1.apply(lambda x: round((x['SALE']/x['NEW ARRIVAL'])*100, 2) if x['SALE'] != 0 and x['NEW ARRIVAL'] else round(0, 2) , axis=1)
                        
                        df4=df2[df2['COMP_NO']==selected_chart_comp2]
                        if selected_chart_comp2 not in ['Rap Net','Global']:
                            df4['proportion'] = df4.apply(lambda x: round((x['SALE']/(x['NEW ARRIVAL']+x['STOCK']))*100, 2) if x['SALE'] != 0 and x['NEW ARRIVAL'] and x['STOCK'] else round(0, 2) , axis=1)
                        else:
                            df4['proportion'] = df4.apply(lambda x: round((x['SALE']/x['NEW ARRIVAL'])*100, 2) if x['SALE'] != 0 and x['NEW ARRIVAL'] else round(0, 2) , axis=1)

                        df2=pd.concat([df1, df4])

                        fig = px.histogram(df2, x=str(type),y='proportion', color='COMP_NO', barmode='group',histfunc='sum',height=400)
                        fig.update_layout(
                            yaxis=dict(
                            title='Proportion',
                            titlefont_size=16,
                            tickfont_size=14,
                        ),
                        xaxis=dict(
                            title=str(type),
                            titlefont_size=16,
                            tickfont_size=14,
                        ),)
                        st.plotly_chart(fig, theme=None, use_container_width=True)
                        
                        df2["NEW ARRIVAL"] = df2["NEW ARRIVAL"].apply(lambda x: float("{:.2f}".format(x)))
                        df2["STOCK"] = df2["STOCK"].apply(lambda x: float("{:.2f}".format(x)))
                        if selected_chart_comp not in ['Rap Net','Global']:
                            df2=df2[["COMP_NO",str(type),"NEW ARRIVAL","STOCK","SALE","proportion"]]
                            df2["SALE"] = df2["SALE"].apply(lambda x: float("{:.2f}".format(x)))
                        else:
                            df2=df2[["COMP_NO",str(type),"NEW ARRIVAL","SALE","proportion"]]

                        if selected_type=="No of Stone":
                            st.markdown("<h3 style='text-align: center;'># of Stone</h3>", unsafe_allow_html=True)
                        elif selected_type=="Total Value":
                            st.markdown("<h3 style='text-align: center;'>NET VALUE</h3>", unsafe_allow_html=True)
                        else:
                            st.markdown("<h3 style='text-align: center;'>Total Crt.</h3>", unsafe_allow_html=True)
                        
                        if selected_chart_comp == None or selected_chart_comp2 == None:
                            df2.pop("COMP_NO")
                            st.write(df2)
                        else:
                            col1,col2 = st.columns(2)
                            col1.markdown("<h3 style='text-align: center;'>Company - %s</h3>" % selected_chart_comp, unsafe_allow_html=True)
                            df1 = df2[df2["COMP_NO"]==selected_chart_comp]                            
                            df1.pop("COMP_NO")
                            df1 = df1.reset_index()
                            df1.pop("index")
                            col1.write(df1)

                            col2.markdown("<h3 style='text-align: center;'>Company - %s</h3>" % selected_chart_comp2, unsafe_allow_html=True)
                            df2 = df2[df2["COMP_NO"]==selected_chart_comp2]
                            df2.pop("COMP_NO")
                            df2 = df2.reset_index()
                            df2.pop("index")
                            col2.write(df2)
                            
                        del df4,df3,for_selected_type,type,s,for_aggfunc,selected_chart_comp,selected_chart_comp2
                        # return st.plotly_chart(fig, theme=None, use_container_width=True)

                    def get_inflow_outflow(temp_data,selected_chart_comp,for_selected_type,selected_type, selected_perms, *args):
                        """This function create a bar chart to show the inflow and outflow of the selected type of stone in the selected

                        Args:
                            temp_data (DataFram): data for report
                            selected_chart_comp (int): to filter data by this comp
                            for_selected_type (str): report type
                            selected_type (str): to show data by (for x axis)
                            selected_perms (str): for y axis
                        """
                        selected_shape1 = ""
                        if len(args):
                            selected_shape1 = str(args[0])
                        # SORT DATA BY DATE
                        start_date=datetime.strptime(str(str(selected_from_year) + '-' + str(datetime.strptime(selected_from_data_range, '%b').month) + '-01'), "%Y-%m-%d").date()

                        if selected_type=="No of Stone":
                            st.markdown("<h3 style='text-align: center;'>Company %s (# of Stones)</h3>" % selected_chart_comp, unsafe_allow_html=True)
                        elif selected_type=="Total Value":
                            st.markdown("<h3 style='text-align: center;'>Company %s (Total Net Value)</h3>" % selected_chart_comp, unsafe_allow_html=True)
                        else:
                            st.markdown("<h3 style='text-align: center;'>Company %s (Total Crt.)</h3>" % selected_chart_comp, unsafe_allow_html=True)
                        
                        data_stock = temp_data[temp_data['Date'] == min(temp_data['Date'])]
                        # data_stock = temp_data[temp_data['Date'] == str(datetime.strptime(str(start_date), "%Y-%m-%d").date())]
                        
                        stock_df2 = data_stock[data_stock['COMP_NO']==selected_chart_comp]
                        final_stock = stock_df2[stock_df2['TYPE']=="STOCK"]
                        if selected_chart_comp == "Manufacturing":
                            df2 = temp_data.loc[(temp_data['COMP_NO'].isin([1,2,7,9]))]
                            df2['COMP_NO']="Manufacturing"
                        else:
                            df2 = temp_data[temp_data['COMP_NO']==selected_chart_comp]
                        if selected_chart_comp not in ['Rap Net','Global']:
                            inflow=pd.concat([df2[df2['TYPE']=="NEW ARRIVAL"],final_stock])
                        else:
                            inflow=df2[df2['TYPE']!="SALE"]

                        inflow['Flow_type'] = "InFlow"

                        inflow['LAB1'] = inflow.apply(lambda x: 1 if x['LAB'] == 'GIA' else 2, axis=1)
                                    
                        inflow = inflow.sort_values(["PACKET_NO","LAB1"])
                        inflow = inflow.drop_duplicates("PACKET_NO")

                        inflow.drop(['LAB1'], axis=1)

                        df2 = df2[df2['TYPE']=="SALE"]
                        df2['Flow_type']="OutFlow"

                        df2['LAB1'] = df2.apply(lambda x: 1 if x['LAB'] == 'GIA' else 2, axis=1)
                                    
                        df2 = df2.sort_values(["PACKET_NO","LAB1"])
                        df2 = df2.drop_duplicates("PACKET_NO")

                        df2.drop(['LAB1'], axis=1)
                        df3 = pd.concat([df2,inflow])

                        # CREATE PIVOT TABLE OF df2
                        if for_selected_type == "PACKET_NO":
                            df3['count']=1
                            for_selected_type = "count"
                        else:
                            pass

                        if selected_perms == "Range":
                            selected_perms = "Band"
                            s = {"10+":7,"5.00-9.99":6,"4.00-4.99":5,"3.00-3.99":4,"2.00-2.99":3,"1.50-1.99":2,"1.20-1.49":1,"1.00-1.19":0,"Doss":8}
                            df3 = df3.sort_values(by=['Band'], key=lambda x: x.map(s)).reset_index()
                            inflow_outflow_table(df3,selected_perms,for_selected_type,selected_type)
                        elif selected_perms == "Ratio":
                            if selected_shape1 in ["EM", "OV", "RA", "PS", "CU", "CE", "CM", "PC", "HT", "MQ", "AS", "BG", "TP", "Other"]:
                                if selected_shape1 in ["EM", "OV", "RA", "PS", "CU", "CE", "CM", "PC", "AS", "TP", "Other"]:
                                    df3 = df3[df3['Ratio'] >= 1.20]
                                    df3 = df3[df3['Ratio'] <= 1.70]
                                elif selected_shape1 == "HT":
                                    df3 = df3[df3['Ratio'] >= 0.75]
                                    df3 = df3[df3['Ratio'] <= 1.00]
                                elif selected_shape1 == "MQ":
                                    df3 = df3[df3['Ratio'] >= 1.80]
                                    df3 = df3[df3['Ratio'] <= 2.50]
                                elif selected_shape1 == "BG":
                                    df3 = df3[df3['Ratio'] >= 1.50]
                                    df3 = df3[df3['Ratio'] <= 2.99]
                                elif selected_shape1 in ["SQ-EM","SQ-CM","SQ-PC"]:
                                    df3 = df3[df3['Ratio'] <= 1.10]

                                df3['Ratio']=round(df3['Ratio'],2)
                                inflow_outflow_table(df3,selected_perms,for_selected_type,selected_type)
                            else:
                                st.warning("Please Select Shape One Of This EM, OV, RA, PS, CU, CE, CM, PC, HT, MQ, AS, BG, TP, Other")
                        elif selected_perms == "SHAPE1":
                            s = {"RD":0, "EM":1, "OV":2, "RA":3, "PS":4, "CU":5, "CE":6, "CM":7, "PC":8, "HT":9, "MQ":10, "AS":11, "BG":12, "TP":13, "Other":14}
                            df3 = df3.sort_values(by=['SHAPE1'], key=lambda x: x.map(s)).reset_index()
                            inflow_outflow_table(df3,selected_perms,for_selected_type,selected_type)
                        elif selected_perms == "TABLE_PER":
                            if selected_shape1 == "PC":
                                df3 = df3[df3['TABLE_PER'] >= 64.00]
                                df3 = df3[df3['TABLE_PER'] <= 84.00]
                            else:
                                df3 = df3[df3['TABLE_PER'] >= 49.00]
                                df3 = df3[df3['TABLE_PER'] <= 87.00]
                            inflow_outflow_table(df3,selected_perms,for_selected_type,selected_type)
                        elif selected_perms == "Depth":
                            df3 = df3[df3['Depth'] > 40]
                            df3['Depth']  = round(df3['Depth'], 2)
                            inflow_outflow_table(df3,selected_perms,for_selected_type,selected_type)
                        else:
                            pass
                        del df3,selected_perms,selected_shape1,for_selected_type,df2,inflow,final_stock,stock_df2,data_stock,start_date

                    @st.cache_data(show_spinner="Fetching data ......")
                    def inflow_outflow_table(df3,selected_perms,for_selected_type,selected_type):
                        """create inflow outflow data table at bottom of report

                        Args:
                            df3 (DataFram): to show data
                            selected_perms (str): parms for y axis
                            for_selected_type (str): report type
                            selected_type (str): data type

                        Returns:
                            st.write: write data table
                        """
                        if selected_perms == "Band":
                            selected_perms = "Range"
                            df3['Range']=df3['Band']
                        if selected_perms in ['Range','SHAPE1']:
                            df4 = pd.pivot_table(data=df3, index=[selected_perms],
                                    columns=['Flow_type'],
                                    values=for_selected_type,
                                    aggfunc=np.sum,sort=False)
                        else:
                            df4 = pd.pivot_table(data=df3, index=[selected_perms],
                                    columns=['Flow_type'],
                                    values=for_selected_type,
                                    aggfunc=np.sum)

                        df2 = df4.apply(lambda c: c / c.sum(), axis=0).round(4) * 100
                        color_list = {'InFlow': "green","OutFlow": "red"}
                        fig = px.line(df2, x=df2.index, y=["InFlow", 'OutFlow'], markers=True, color_discrete_map=color_list)

                        if selected_perms == "TABLE_PER":
                            selected_perms="Table"
                        elif selected_perms == "Band":
                            selected_perms = "Range"
                        elif selected_perms == "SHAPE1":
                            selected_perms = "Shape"
                        else:
                            pass
                        fig.update_layout(
                            legend=dict(title='<b> Trend </b>',
                                x=0,
                                y=10,
                                traceorder="normal",
                                font=dict(
                                    family="sans-serif",
                                    size=12,
                                    color="black"
                                ),
                            ),
                            yaxis=dict(
                            title="Percentage",
                            titlefont_size=16,
                            tickfont_size=14,
                        ),
                        xaxis=dict(
                            title=str(selected_perms),
                            titlefont_size=16,
                            tickfont_size=14,
                        ),)
                        st.plotly_chart(fig,theme=None, use_container_width=True)

                        if selected_chart_comp not in ['Rap Net','Global']:
                            df4['proportion'] = df4.apply(lambda x: round((x['OutFlow']/x['InFlow'])*100, 2) if x['OutFlow'] != 0 and x['InFlow'] else round(0, 2) , axis=1)
                        else:
                            df4['proportion'] = df4.apply(lambda x: round((x['OutFlow']/x['InFlow'])*100, 2) if x['OutFlow'] != 0 and x['InFlow'] else round(0, 2) , axis=1)
                        # def color_survived(val):
                        #         color = "#FFFFFF"
                        #         try:
                        #             if [val].index(None):
                        #                 pass
                        #         except:
                        #             if val>60:
                        #                 color="#FCBCBE"
                        #         return f'background-color: {color}'
                        if selected_type=="No of Stone":
                            st.markdown("<h3 style='text-align: center;'># of Stone</h3>", unsafe_allow_html=True)
                        elif selected_type=="Total Value":
                            st.markdown("<h3 style='text-align: center;'>NET VALUE</h3>", unsafe_allow_html=True)
                        else:
                            st.markdown("<h3 style='text-align: center;'>Total Crt.</h3>", unsafe_allow_html=True)
                        # if len(df2)>0:
                        # return st.dataframe(df4.style.applymap(color_survived, subset="proportion"))
                        return st.write(df4.T)
                        # else:
                        #     return st.error("Data Filter is Missing.....")

                    def footer_part(updated_date,selected_lab, selected_shape, selected_band, selected_color, selected_purity, selected_fls,selected_report_type):
                        st.markdown("### This Report Generated With Data Filter")
                        # if email == "admin":
                        #     if selected_report_type == "Sale/New Arrival Report":
                        #         st.markdown(str("###### :point_right: Data"))
                        #         st.markdown(str(" - Value is one of you selected (# of Stones, Total Crt, and Total Value)"))
                        #         st.markdown(str(" - Date is one of you selected (Dailty, Monthly, quaterly, and yearly)"))
                        #         st.markdown(str(" - Demand is Sale and Supply is New"))
                        #         st.markdown(str(" - Data is sortlised with company you given into selection"))
                        #     elif selected_report_type == "Trend Report in %":
                        #         st.markdown(str("###### :point_right: Data"))
                        #         st.markdown(str(" - Proportion is Sale / (new arrival + stock)"))
                        #         st.markdown(str(" - Date is one of you selected (Dailty, Monthly, quaterly, and yearly)"))
                        #         st.markdown(str(" - Data is sortlised with company you given into selection"))
                        #     elif selected_report_type == "Heat Map":
                        #         st.markdown(str("###### :point_right: Data"))
                        #         st.markdown(str(" - Data is sortlised with company you given into selection"))
                        #         st.markdown(str(" - PPC is Net value/WGT"))
                        #         st.markdown(str(" - X axis is Purity and Y axis is Color."))
                        #         st.markdown(str(" - Light Color Show PPC is low."))
                        #     elif selected_report_type == "Bubble Chart":
                        #         st.markdown(str("###### :point_right: Data"))
                        #         st.markdown(str(" - Date is one of you selected (Dailty, Monthly, Quaterly, and yearly)"))
                        #         st.markdown(str(" - PPC is Net value/WGT"))
                        #         st.markdown(str(" - X axis is Sequence and Y axis is PPC."))
                        #         st.markdown(str(" - Size of Bubble is Depend on # of Stone."))
                        #         st.markdown(str(" - hight of Bubble is Depend on ppc."))
                        #         st.markdown(str(" - Color of Bubble is Depend on Company."))
                        #     elif selected_report_type == "Zone Wise Sale":
                        #         st.markdown(str("###### :point_right: Data"))
                        #         st.markdown(str(" - Data is sortlised with company you given into selection"))
                        #         st.markdown(str(" - Value is one of you selected (# of Stones, Total Crt, and Total Value)"))
                        #     elif selected_report_type == "Sale%":
                        #         st.markdown(str("###### :point_right: Data"))
                        #         st.markdown(str(" - Comare two company's Sale%."))
                        #         st.markdown(str(" - Select Two different Company to compar eachother sale%"))
                        #         st.markdown(str(" - Value is one of you selected (# of Stones, Total Crt, and Total Value)"))
                        #         st.markdown(str(" - parameter is X-Axis (Shape, Range, FLS, Polish, Color, Purity, Cut, and Symm)"))
                        #         st.markdown(str(" - Sale% (Value/total Value)"))
                        #     elif selected_report_type == "Sale Proportion":
                        #         st.markdown(str("###### :point_right: Data"))
                        #         st.markdown(str(" - Comare two company's Sale%."))
                        #         st.markdown(str(" - Select Two different Company to compar eachother sale%"))
                        #         st.markdown(str(" - Value is one of you selected (# of Stones, Total Crt, and Total Value)"))
                        #         st.markdown(str(" - parameter is X-Axis (Shape, Range, FLS, Polish, Color, Purity, Cut, and Symm)"))
                        #         st.markdown(str(" - Proportion is Sale / (New Arrival + Stock)"))
                        #     elif selected_report_type == "Report":
                        #         st.markdown(str("###### :point_right: Data"))
                        #         st.markdown(str(" - Select date mode (daily,monthly,weekly, or Quaterly)"))
                        #         st.markdown(str(" - Value is one of you selected (# of Stones, Total Crt, and Total Value)"))
                        #         st.markdown(str(" - Sale% (Sale / (New Arrival + Stock))"))
                        #         st.markdown(str(" - it shows all data as selected mode."))
                        #     elif selected_report_type == "InFlow/OutFlow":
                        #         st.markdown(str("##### :point_right: Data"))
                        #         st.markdown(str(" - Comparison of two company's InFlow and OutFlow."))
                        #         st.markdown(str(" - Select Two Differemt Company."))
                        #         st.markdown(str(" - Percentagee is value / sum(value)*100"))
                        #         st.markdown(str(" - parameter is X-Axis (Shape)"))
                        #     elif selected_report_type == "Parameter wise InFlow-OutFlow":
                        #         st.markdown(str("##### :point_right: Data"))
                        #         st.markdown(str(" - Comparison of two company's InFlow and OutFlow."))
                        #         st.markdown(str(" - Select Two Differemt Company."))
                        #         st.markdown(str(" - Percentagee is value / sum(value)*100"))
                        #         st.markdown(str(" - parameter is X-Axis (depth,Table,Ratio,Range)"))
                        #         st.markdown(str(' - Filter by shape ("RD", "EM", "OV", "RA", "PS", "CU", "CE", "CM", "PC", "HT", "MQ", "AS", "BG", "TP", "Other", "SQ-EM","SQ-CM","SQ-PC")'))
                        #     else:
                        #         st.markdown(str("##### :point_right: Data"))
                        #         st.markdown(str(" - Data is sortlised with company you given into selection"))
                        #         st.markdown(str("##### :point_right: Total Revenue, Total Sold CRT., and Total Sold Pieces."))
                        #         st.markdown (str(" - Selected Options wise."))
                        #         st.markdown(str("##### :point_right: Sold Proportion (New Arrival)"))
                        #         st.markdown (str(" - sale which sold from new arrival/total new arival (CRT)"))
                        #         st.markdown(str("##### :point_right: Sold Proportion (Stock)"))
                        #         st.markdown (str(" - sale which sold from Stock/total Stock (CRT)"))
                        #         st.markdown(str("##### :point_right: Sold Proportion"))
                        #         st.markdown (str(" - total sale/total new arrival + nstock (CRT)"))
                        #         st.markdown(str("##### :point_right: Sale Cycle Time"))
                        #         st.markdown (str(" - Average Sale Day to Sale 70%"))
                        #         st.markdown(str("##### :point_right: Round%"))
                        #         st.markdown (str(" - shape Type% From Total Sold Stones"))                
                        if selected_shape:
                            st.markdown(str("###### :point_right: Shape: %s" % ", ".join(selected_shape)))
                        if selected_band:
                            st.markdown(str("###### :point_right: Range: %s" % ", ".join(selected_band)))
                        if selected_color:
                            st.markdown(str("###### :point_right: Color: %s" % ", ".join(selected_color)))
                        if selected_purity:
                            st.markdown(str("###### :point_right: Purity: %s" % ", ".join(selected_purity)))
                        if selected_lab:
                            st.markdown(str("###### :point_right: Lab: %s" % ", ".join(selected_lab)))
                        if selected_fls:
                            st.markdown(str("###### :point_right: FLS: %s" % ", ".join(selected_fls)))
                        if updated_date:
                            col1, col2 = st.columns(2)
                            col1.markdown(str('<div style="text-align: left; font-weight: bold;">Report Generated At: ' + str(datetime.today()) + '</div>'), unsafe_allow_html=True)
                            col2.markdown(str('<div style="text-align: right; font-weight: bold;">Last Updated: ' + str(updated_date[0]) + '</div>'), unsafe_allow_html=True)
                        
                    @st.cache_data(show_spinner="Fetching data ......")
                    def get_shape_chart(temp_data1,selected_chart_comp,selected_mode,selected_status,selected_shape1):
                        """ Get shape chart data
                            Args:
                                temp_data1 (list): list of data
                                selected_chart_comp (list): list of company
                                selected_mode (list): list of mode
                                selected_status (list): list of status
                                selected_shape1 (list): list of shape
                        """
                        # EXECUTE HTML CODE 
                        st.markdown("<h3 style='text-align: center;'>" + str(selected_shape1) + "</h3>", unsafe_allow_html=True)

                        if selected_chart_comp == "Manufacturing":
                            temp_data1 = temp_data1.loc[(temp_data1['COMP_NO'].isin([1,2,7,9]))]

                            temp_data1['COMP_NO']="Manufacturing"
                        else:
                            temp_data1 = temp_data1[temp_data1['COMP_NO']==selected_chart_comp]
                        
                        # temp_data=temp_data[temp_data['COMP_NO'] == selected_chart_comp]
                        temp_data1=temp_data1[temp_data1['SHAPE1'] == str(selected_shape1)]
                        df3=temp_data1[temp_data1['TYPE'].isin(selected_status)]

                        # df3['LAB1']=df3.apply(lambda x: 1 if x['X_LAB']=="GIA" else 2)
                        # df3.sort_values(by=['PACKET_NO', 'LAB1'])
                        df2 = df3.drop_duplicates(subset=['PACKET_NO', selected_mode, 'TYPE'])
                        
                        if selected_mode == "Week":
                            # SORT DATA BY DATE
                            s = {'Jan-1':0, 'Jan-2':1, 'Jan-3':2,'Jan-4':3,'Jan-5':4,
                                'Feb-1':5,'Feb-2':6,'Feb-3':7,'Feb-4':8,'Feb-5':9,
                                'Mar-1':10,'Mar-2':11,'Mar-3':12,'Mar-4':13,'Mar-5':14,
                                'Apr-1':15,'Apr-2':16,'Apr-3':17,'Apr-4':18,'Apr-5':19,
                                'May-1':20,'May-2':21,'May-3':22,'May-4':23,'May-5':24,
                                'Jun-1':25,'Jun-2':26,'Jun-3':27,'Jun-4':28,'Jun-5':29,
                                'Jul-1':30,'Jul-2':31,'Jul-3':32,'Jul-4':33,'Jul-5':34,
                                'Aug-1':35,'Aug-2':36,'Aug-3':37,'Aug-4':38,'Aug-5':39,
                                'Sep-1':40,'Sep-2':41,'Sep-3':42,'Sep-4':43,'Sep-5':44,
                                'Oct-1':45,'Oct-2':46,'Oct-3':47,'Oct-4':48,'Oct-5':49,
                                'Nov-1':50,'Nov-2':51,'Nov-3':52,'Nov-4':53,'Nov-5':54,
                                'Dec-1':55,'Dec-2':56,'Dec-3':57,'Dec-4':58,'Dec-5':59,}
                            
                            df2['Week'] = df2.apply(lambda x: 'Jan-1' if x['Week'] == 'Jan-01' else 'Jan-2' if x['Week'] == 'Jan-02' else 'Jan-3' if x['Week'] == 'Jan-03' else 'Jan-4' if x['Week'] == 'Jan-04' else 'Jan-5' if x['Week'] == 'Jan-05' else 'Feb-1' if x['Week'] == 'Feb-01' else 'Dec-5' if x['Week'] == 'Dec-05' else x['Week'], axis=1)
                            months = get_months(selected_from_year,selected_from_data_range,selected_data_range,selected_year)
                            
                            df2['is_week']=df2.apply(lambda x: True if str(x['Week']).split('-')[0] in months else False, axis=1)
                            df2 = df2.loc[(df2['is_week'] == True)]
                            
                            df2 = df2.sort_values(by=[selected_mode], key=lambda x: x.map(s)).reset_index()
                        elif selected_mode == "Month":
                            # SORT DATA BY DATE
                            s = {'Jan-%s' % (selected_year[2:]):0,'Feb - %s' % (selected_year[2:]):1,'Mar - %s' % (selected_year[2:]):2,'Apr - %s' % (selected_year[2:]):3,'May - %s' % (selected_year[2:]):4,'Jun - %s' % (selected_year[2:]):5,'Jul - %s' % (selected_year[2:]):6,'Aug - %s' % (selected_year[2:]):7,'Sep - %s' % (selected_year[2:]):8,'Oct - %s' % (selected_year[2:]):9,'Nov - %s' % (selected_year[2:]):10,'Dec - %s' % (selected_year[2:]):11}
                            df2 = df2.sort_values(by=[selected_mode], key=lambda x: x.map(s)).reset_index()
                        elif selected_mode == "Date":
                            df2.sort_values(by=[selected_mode])
                        
                        df2 = pd.pivot_table(data=df2, index=[selected_mode],
                                    columns=[],
                                    values=["WGT",'Net Value'],
                                    aggfunc={"WGT": 'sum','Net Value':'sum'},
                                    fill_value=0,
                                    margins=False,
                                    sort=False)

                        df2[selected_mode]=df2.index
                        df2['PPC']=round((df2['Net Value']/df2['WGT']),2)
                        fig = px.line(df2, x=selected_mode, y="PPC", markers=True)
                        fig.update_traces(textposition="bottom right")
                        #st.plotly_chart(fig)
                        st.plotly_chart(fig, theme=None, use_container_width=True)
                        df2=df2[["WGT","Net Value","PPC"]]
                        

                        st.markdown("<h3 style='text-align: center;'>PPC</h3>", unsafe_allow_html=True)
                        return st.write(df2)

                    def selected_parameter(type):
                        """ Select parameter to display
                            Args:
                                type (str): type of parameter to display
                            return :
                                selected_parameter (str): Uniformed selected parameter
                        """
                        
                        if str(type) == 'Shape':
                            return "SHAPE1"
                        elif str(type) == "Range":
                            return "Band"
                        elif str(type) == "Polish":
                            return "POLISH"
                        elif str(type) == "Color":
                            return "COLOR_A"
                        elif str(type) == "Purity":
                            return "PURITY_A"
                        elif str(type)=="cut":
                            return "CUT_ACTUAL"
                        elif str(type)=="symm":
                            return "SYMM"
                        elif str(type) == "FLS":
                            return "FLS"
                        else:
                            return type

                    @st.cache_data(show_spinner="Fetching data ......")
                    def get_sale_chart(temp_data,selected_chart_comp,selected_mode,selected_x,selected_color_1):
                        """ Get sale chart data
                            
                            Args:
                                temp_data (df): temporary data
                                selected_chart_comp (str): selected chart component
                                selected_mode (str): selected mode
                                selected_x (str): selected x-axis
                                selected_color_1 (str): selected color 1
                        """
                        
                        if selected_chart_comp == "Manufacturing":
                            temp_data1 = temp_data.loc[(temp_data['COMP_NO'].isin([1,2,7,9]))]

                            temp_data1['COMP_NO']="Manufacturing"
                        else:
                            temp_data1 = temp_data[temp_data['COMP_NO']==selected_chart_comp]
                        # temp_data=temp_data[temp_data['COMP_NO'] == selected_chart_comp]

                        df3=temp_data1[temp_data1['TYPE'].isin(['SALE'])]
                        df2 = df3.drop_duplicates(subset=['PACKET_NO', selected_mode])

                        if selected_mode == "Week":
                            # SORT DATA BY DATE
                            s = {'Jan-1':0, 'Jan-2':1, 'Jan-3':2,'Jan-4':3,'Jan-5':4,
                                'Feb-1':5,'Feb-2':6,'Feb-3':7,'Feb-4':8,'Feb-5':9,
                                'Mar-1':10,'Mar-2':11,'Mar-3':12,'Mar-4':13,'Mar-5':14,
                                'Apr-1':15,'Apr-2':16,'Apr-3':17,'Apr-4':18,'Apr-5':19,
                                'May-1':20,'May-2':21,'May-3':22,'May-4':23,'May-5':24,
                                'Jun-1':25,'Jun-2':26,'Jun-3':27,'Jun-4':28,'Jun-5':29,
                                'Jul-1':30,'Jul-2':31,'Jul-3':32,'Jul-4':33,'Jul-5':34,
                                'Aug-1':35,'Aug-2':36,'Aug-3':37,'Aug-4':38,'Aug-5':39,
                                'Sep-1':40,'Sep-2':41,'Sep-3':42,'Sep-4':43,'Sep-5':44,
                                'Oct-1':45,'Oct-2':46,'Oct-3':47,'Oct-4':48,'Oct-5':49,
                                'Nov-1':50,'Nov-2':51,'Nov-3':52,'Nov-4':53,'Nov-5':54,
                                'Dec-1':55,'Dec-2':56,'Dec-3':57,'Dec-4':58,'Dec-5':59,}
                            
                            df2['Week'] = df2.apply(lambda x: 'Jan-1' if x['Week'] == 'Jan-01' else 'Jan-2' if x['Week'] == 'Jan-02' else 'Jan-3' if x['Week'] == 'Jan-03' else 'Jan-4' if x['Week'] == 'Jan-04' else 'Jan-5' if x['Week'] == 'Jan-05' else 'Feb-1' if x['Week'] == 'Feb-01' else 'Dec-5' if x['Week'] == 'Dec-05' else x['Week'], axis=1)
                            months = get_months(selected_from_year,selected_from_data_range,selected_data_range,selected_year)
                            
                            df2['is_week']=df2.apply(lambda x: True if str(x['Week']).split('-')[0] in months else False, axis=1)
                            df2 = df2.loc[(df2['is_week'] == True)]
                            
                            df2 = df2.sort_values(by=[selected_mode], key=lambda x: x.map(s)).reset_index()
                        elif selected_mode == "Month":
                            # SORT DATA BY DATE
                            s = {'Jan-%s' % (selected_year[2:]):0,'Feb - %s' % (selected_year[2:]):1,'Mar - %s' % (selected_year[2:]):2,'Apr - %s' % (selected_year[2:]):3,'May - %s' % (selected_year[2:]):4,'Jun - %s' % (selected_year[2:]):5,'Jul - %s' % (selected_year[2:]):6,'Aug - %s' % (selected_year[2:]):7,'Sep - %s' % (selected_year[2:]):8,'Oct - %s' % (selected_year[2:]):9,'Nov - %s' % (selected_year[2:]):10,'Dec - %s' % (selected_year[2:]):11}
                            df2 = df2.sort_values(by=[selected_mode], key=lambda x: x.map(s)).reset_index()
                        elif selected_mode == "Date":
                            df2.sort_values(by=[selected_mode])
                        
                        fig = px.histogram(df2, x=str(selected_parameter(selected_x)),
                        y="WGT", color=str(selected_parameter(selected_color_1)),
                        barnorm='percent', text_auto='.0f',
                        title=str(selected_x + " & " + selected_color_1 + " Wise Sale Report" + " of Company-" + str(selected_chart_comp)))

                        # fig.update_traces(textposition="bottom right")
                        
                        st.plotly_chart(fig, theme=None, use_container_width=True)

                        st.markdown("<h3 style='text-align: center;'>PPC</h3>", unsafe_allow_html=True)

                        df2 = df2[[selected_mode,selected_parameter(selected_x),selected_parameter(selected_color_1),"WGT","Net Value"]]
                        return st.write(df2)

                    @st.cache_data(show_spinner="Fetching data ......")
                    def get_cumulative_chart(temp_data, selected_chart_comp):
                        """ This function is used to get cumulative chart of the data.

                            Args:
                                temp_data (df): This is the data which is used to plot the cumulative chart.
                                selected_chart_comp (str): This is the company name which is used to plot the cumulative chart
                            
                            Returns:
                                fig: This is the cumulative chart of the data.
                        """
                        
                        st.markdown("<h3>Quickness in sale (# of Stone) (Company - %s)</h3>" % selected_chart_comp, unsafe_allow_html=True)
                        temp_data1 = temp_data.loc[temp_data['COMP_NO']==selected_chart_comp]
                        temp_data1['Duration'] = np.where((temp_data1['TYPE'] == 'SALE') & ((temp_data1['COMP_NO'] == 1) & (((temp_data1['SALE_DAYS'] <= 2) & (temp_data1['WGT'] >= 4)) | (temp_data1['SALE_DAYS'] == 1))) | ((temp_data1['COMP_NO'] == 2) & ((temp_data1['SALE_DAYS'] <= 5) & (temp_data1['WGT'] >= 2)) | (temp_data1['SALE_DAYS'] <= 3)), 'Same Day',
                                np.where((temp_data1['TYPE'] == 'SALE') & (temp_data1['SALE_DAYS'] < 8), '1st Week',
                                        np.where((temp_data1['TYPE'] == 'SALE') & (temp_data1['SALE_DAYS'] < 16), '1st Fortnight',
                                                np.where((temp_data1['TYPE'] == 'SALE') & (temp_data1['SALE_DAYS'] < 31), '1st Month',
                                                        np.where((temp_data1['TYPE'] == 'SALE') & (temp_data1['SALE_DAYS'] < 61), '2nd Month',
                                                                np.where((temp_data1['TYPE'] == 'SALE') & (temp_data1['SALE_DAYS'] < 91), '1st Quater',
                                                                        np.where((temp_data1['TYPE'] == 'SALE') & (temp_data1['SALE_DAYS'] < 181), '2nd Quater',
                                                                                np.where((temp_data1['TYPE'] == 'SALE') & (temp_data1['SALE_DAYS'] < 366), '1st Year',
                                                                                        np.where((temp_data1['TYPE'] == 'SALE') & (temp_data1['SALE_DAYS'] > 365), 'More Than Year', '')))))))))
                        temp_data1 = temp_data1.loc[(temp_data1['TYPE']=="SALE")]
                        duration_list = temp_data1['Duration'].unique()
                        
                        def custom_sort_duration(dr_list):
                            """ This function is used to sort the duration list.
                                
                                Args:
                                    dr_list (list): This is the list of duration which is used to sort the duration list
                            """
                            
                            fix_duration_list = {"Same Day":1,"1st Week":2,"1st Fortnight":3,"1st Month":4,
                                            "2nd Month":5,"1st Quater":6,"2nd Quater":7,"1st Year":8,"More Than Year":9}
                            return fix_duration_list.get(dr_list,999)
                        
                        till_2month_duration_list = ["Same Day","1st Week","1st Fortnight","1st Month","2nd Month"]
                        duration_list = sorted(duration_list,key=custom_sort_duration)
                        duration_list = list(filter(None, duration_list))
                        # ["Same Day","1st Week","1st Fortnight","1st Month","2nd Month","1st Quater","2nd Quater","1st Year","More Than Year"]
                        
                        duration_head=[]
                        for dr in duration_list:
                            duration_head.append("<th class='table_head'>%s</th>" % dr)
                        duration_head = "<tr><th class='table_head'>Range</th><th class='table_head'>Total Stones</th>%s</tr>" % "".join(duration_head)

                        range_list = temp_data1['Band'].unique()

                        def custom_sort_range(rg_list):
                            """ This function is used to sort the range list.

                                Args:
                                    rg_list (list): This is the list of range which is used to sort the range list
                            """
                            
                            fix_range_list = {"1.00-1.19":1,"1.20-1.49":2,"1.50-1.99":3,"2.00-2.99":4,"3.00-3.99":5,"4.00-4.99":6,"5.00-9.99":7,"10+":8,"Doss":9}
                            return fix_range_list.get(rg_list,999)

                        range_list = sorted(range_list,key=custom_sort_range)
                        range_list = list(filter(None, range_list))

                        table_rows = []
                        # count_table_rows = []
                        for size_str in range_list:
                            data = temp_data1.loc[(temp_data1['Band']==str(size_str))]
                            total_stones = sum(data['count'])
                            size_row = "<td class='table_sub_head'>%s</td>" % str(size_str)
                            table_data = []
                            # count_table_data = []
                            temp_duration = []
                            for duration_time in duration_list:
                                temp_duration.append(duration_time)
                                t_data = data.loc[(data['Duration'].isin(temp_duration))]
                                count_t_data = data.loc[(data['Duration'].isin([duration_time]))]
                                per = round(sum(t_data['count'])/total_stones*100,0)
                                if duration_time in till_2month_duration_list and per>=60:
                                    # table_data.append("""<td class='table_data_style'><b>%s/<span style="color:rgb(99, 190, 123);">%s%s</span></b></td>""" % (sum(count_t_data['count']),round(per),str('%')))
                                    table_data.append("""<td class='table_data_style' style="background-color: #C6E0B4;"><b>%s/<span style="color:#548235;">%s%s</span></b></td>""" % (sum(count_t_data['count']),round(per),str('%')))
                                else:
                                    table_data.append("""<td class='table_data_style'><b>%s/<span style="color:rgb(99, 190, 123);">%s%s</span></b></td>""" % (sum(count_t_data['count']),round(per),str('%')))
                                # count_table_data.append("<td class='table_data_style'>%s</td>" % sum(count_t_data['count']))
                            table_rows.append("<tr>%s<td class='table_data_style'><b>%s</b></td>%s</tr>" % ("".join(size_row),total_stones,"".join(table_data)))
                            # count_table_rows.append("<tr>%s<td class='table_data_style'>%s</td>%s</tr>" % ("".join(size_row),total_stones,"".join(count_table_data)))
                        final_table_tag_str = "%s%s" % (duration_head,"".join(table_rows))
                        # count_final_table_tag_str = "%s%s" % (duration_head,"".join(count_table_rows))

                        st.markdown("""
                                    <style>
                                        .table_1 {
                                            width:100%; 
                                            }
                                        .table_header{
                                            text-align: center;
                                            font-weight: bold;
                                            color: #FFFFFF;
                                            font-size: 12px;
                                        }
                                        .table_head{
                                            text-align: center;
                                            font-weight: bold;
                                            font-size: 18px;
                                            background-color:#287E8F;
                                            color: #FFFFFF;
                                            padding: 1px;
                                            margin: 1px 1px 1px 1px;
                                        }
                                        .table_sub_head{
                                            text-align: center;
                                            font-weight: bold;
                                            font-size: 16px;
                                            padding: 1px;
                                            margin: 1px 1px 1px 1px;
                                        }
                                        .table_data_style{
                                            text-align: center;
                                            font-size: 16px;
                                            padding: 1px;
                                            margin: 1px 1px 1px 1px;
                                        }
                                        td, th{
                                            width: 2%;
                                        }
                                        tr{
                                            height: 12px;
                                        }
                                        tr:nth-child(even) {background-color: #f2f2f2;}
                                    </style>
                                    """, unsafe_allow_html=True)
                        # st.mardown("""
                        #         <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                        #             <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                        #             <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                        #     """, unsafe_allow_html=True)
                        
                        table_html_string = """
                                    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                                    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                                    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                                    <table class="table-borderless table-responsive card-1 p-4">%s</table>
                                    """ % (final_table_tag_str)
                        st.markdown((((''.join(table_html_string).replace("'","")).replace(",","")).replace("[","")).replace("]",""), unsafe_allow_html=True)
                        

                        # st.markdown("<h3 class='table_header'>quickness in sale (# of Stone) (Company - %s)</h3>" % selected_chart_comp, unsafe_allow_html=True)

                        # count_table_html_string = """<table class="table-borderless table-responsive card-1 p-4">%s</table> """ % count_final_table_tag_str
                        # st.markdown(count_table_html_string, unsafe_allow_html=True)
                    
                    # ======================== all report generation as user selection ========================
                    if len(df3)>=1:
                        
                        # st.toast('Data Loaded Successfully.')
                        expander = st.expander("Filter", expanded=True)
                        expander.header('Data Filters For Report', divider='gray')
                        col1, col2, col3 = expander.columns([1,1,1])
                        
                        # ======================== data filters for report ========================
                        
                        # SELECT LAB
                        selected_lab = col1.multiselect("Select LAB", total_lab, ["All"])
                        if 'All' in selected_lab:
                            selected_lab = final_lab
                    
                        # SELECT SHAPE
                        selected_shape = col2.multiselect("Select Shape", total_shape,["All"])
                        if "All" in selected_shape:
                            selected_shape = final_shape
                        
                        # SELECT BAND
                        selected_band = col3.multiselect("Select Range", total_range, ["All"])
                        if "All" in selected_band:
                            selected_band = final_range

                        col1, col2, col3 = expander.columns([1,1,1])
                        # SELECT COLOR
                        selected_color = col1.multiselect("Select Color", total_color, ["All"])
                        if "All" in selected_color:
                            selected_color = final_color

                        # SELECT PURITY
                        selected_purity = col2.multiselect("Select Purity", total_purity, ["All"])
                        if "All" in selected_purity:
                            selected_purity = final_purity
                        
                        # SELECT FLS
                        selected_fls = col3.multiselect("Select FLS", total_fls, ["All"])
                        if "All" in selected_fls:
                            selected_fls = final_fls
                        
                        col1, col2, col3 = expander.columns([1,1,1])
                    
                        # SELECT CUT
                        selected_cut = col1.multiselect("Select Cut", total_cut, ["All"])
                        if "All" in selected_cut:
                            selected_cut = final_cut
                        
                        # SELECT SYMM
                        selected_symm = col3.multiselect("Select Symm", total_symm, ["All"])
                        if "All" in selected_symm:
                            selected_symm = final_symm

                        # SELECT POLISH
                        selected_polish = col2.multiselect("Select Polish", total_polish, ["All"])
                        if "All" in selected_polish:
                            selected_polish = final_polish

                        expander1 = st.expander("Report Filter", expanded=True)
                        expander1.header('Report Selection', divider='gray')

                        selected_report_type = expander1.selectbox("Select Report Type", tuple(total_report_type))
                        
                        def report_mode(selected_mode):
                            """ uniform report modes
                                
                                Args:
                                    selected_mode (str): selected report mode
                            """
                            
                            if selected_mode == 'Daily':
                                del selected_mode
                                return 'Date'
                            elif selected_mode == 'Weekly':
                                del selected_mode
                                return 'Week'
                            elif selected_mode == 'Month':
                                del selected_mode
                                return 'Month'
                            elif selected_mode == 'Yearly':
                                del selected_mode
                                return 'YEAR'
                            else:
                                return "Quarter"

                        def heat_report_selection():
                            """ give options for heat report two cno and range in single line"""
                            
                            col1, col2, col3 = expander1.columns([1,1,1])
                            # SELECT COMP
                            selected_chart_comp = col1.selectbox("Select Company 1", tuple(total_first_comp))

                            selected_chart_comp2 = col2.selectbox("Select company 2", tuple(total_second_comp),total_second_comp[0])

                            selected_chart_band = col3.multiselect("Select Range", total_range, ["1.00-1.19","1.20-1.49"])

                            if selected_chart_band == "All":
                                selected_chart_band = final_range

                            return selected_chart_comp,selected_chart_comp2,selected_chart_band

                        def treand_report_selection():
                            """ give options for trend report two comp inlingle line and in second line give mode and type selection"""
                            
                            col1, col2 = expander1.columns([1,1])
                            
                            # SELECT COMP
                            selected_chart_comp = col1.selectbox("Select Company 1", tuple(total_first_comp))

                            # SELECT COMP
                            selected_chart_comp2 = col2.selectbox("Select Company 2", tuple(total_second_comp),total_second_comp[0])

                            col1, col2 = expander1.columns([1,1])

                            # SELECT MODE
                            selected_mode = col1.selectbox("Select Mode", tuple(total_mode))
                            
                            # SELECTED TYPE
                            selected_type = col2.selectbox("Select Type", tuple(total_data_type))
                            
                            return selected_chart_comp,selected_chart_comp2,selected_mode,selected_type

                        def report_selection_with_two_comp():
                            """ give options for report two comp in single line and in second line give type and parmeters selection"""
                            
                            col1, col2 = expander1.columns([1,1])
                            
                            # SELECT COMP
                            selected_chart_comp = col1.selectbox("Select Company 1", tuple(total_first_comp))

                            selected_chart_comp2 = col2.selectbox("Select Company 2", tuple(total_second_comp),total_second_comp[0])

                            col1, col2 = expander1.columns([1,1])
                                
                            # SELECTED TYPE
                            selected_type = col1.selectbox("Select Type", tuple(total_data_type))
                            
                            selected_perms = col2.selectbox("Select Parmeters", tuple(total_params))
                            
                            return selected_chart_comp,selected_chart_comp2,selected_type,selected_perms
                        
                        def report_without_comp():
                            """ give options for report mode and type selection"""
                            
                            col1, col2 = expander1.columns([1,1])
                            
                            # SELECT MODE
                            selected_mode = col1.selectbox("Select Mode", tuple(total_mode))
                            
                            # SELECTED TYPE
                            selected_type = col2.selectbox("Select Type", tuple(total_data_type))
                            
                            return selected_mode,selected_type

                        def print_type(selected_type):
                            """ uniform type data type to return pivot aggfunc

                                Args:
                                    selected_type (str): type of data to be selected from user input
                            """

                            for_head_print_type = selected_type
                            
                            if selected_type == "No of Stone":
                                for_head_print_type = 'COUNT'
                            else:
                                for_head_print_type = selected_type
                            
                            for_aggfunc = 'sum'
                            
                            if selected_type == 'No of Stone':
                                for_selected_type = 'count'
                                for_aggfunc = 'sum'
                            elif selected_type == 'Total Crt':
                                for_selected_type = 'WGT'
                                for_aggfunc = "sum"
                            else:
                                for_selected_type = 'Net Value'
                                for_aggfunc = "sum"
                            
                            return for_head_print_type,for_selected_type,for_aggfunc

                        def pie_report_selection():
                            """ give options for pie report selection"""
                            
                            col1,  col3 = expander1.columns([1,1])
                            
                            # SELECT COMP
                            selected_chart_comp = col1.selectbox("Select Company", tuple(zone_wise_comp_without_none))

                            # SELECT MODE
                            # selected_mode = col2.selectbox("SELECT MODE", ("Daily", "Weekly", "Month", "Quarter"))
                            
                            # SELECTED TYPE
                            selected_type = col3.selectbox("Select Type", tuple(total_data_type))
                            
                            return selected_chart_comp,selected_type

                        def sum_of_count_crt_net_value_stock(data,selected_chart_comp):
                            """sum of count, crt, and net value stock for stock report

                                Args:
                                    data (df): data to be processed
                                    selected_chart_comp (str): selected company for stock report
                            """
                            
                            st.markdown("<h3 style='text-align: center;'>Sale Dashboard (Company-" + str(selected_chart_comp) + ")</h3>", unsafe_allow_html=True)
                            if selected_chart_comp == "Manufacturing":
                                cno_1 = data[data['COMP_NO']==1]
                                cno_2 = data[data['COMP_NO']==2]
                                cno_7 = data[data['COMP_NO']==7]
                                cno_9 = data[data['COMP_NO']==9]
                                temp_data2 = pd.concat([cno_1, cno_2, cno_7, cno_9])
                                temp_data2['COMP_NO']="Manufacturing"
                            else:
                                temp_data2 = data[data['COMP_NO']==selected_chart_comp]
                            
                            temp_data2['']
                            temp_data1 = temp_data2[temp_data2['TYPE']=='STOCK']
                            
                            def findDay(date):
                                """return date.day"""
                                date = datetime.strptime(str(date), '%Y-%m-%d').date()
                                year, month, day = (int(i) for i in str(date).split('-'))    
                                dayNumber = calendar.weekday(year, month, day)
                                
                                # Modify days list to start with Sunday as 0
                                days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday","Sunday"]
                                return days[dayNumber]
                            
                            date_list_1 = temp_data1['Date'].unique()
                            date2=date_list_1[-1]
                            if findDay(date_list_1[-1])=="Sunday":
                                date2 = date_list_1[-1] - timedelta(days=1)
                            else:
                                date2 = date_list_1[-1]
                            temp_data1 = temp_data1[temp_data1['Date']==str(date2)]
                            temp_data = temp_data1.drop_duplicates(subset=['PACKET_NO'])

                            temp_data['Count'] = temp_data.apply(lambda x: 1 if x['PACKET_NO'] not in ['na', 'none', 0, "", " "] else 0, axis=1)
                            
                            count = temp_data['Count'].sum()
                            ctr = temp_data['WGT'].sum()
                            total = temp_data['Net Value'].sum()

                            round_data = temp_data[temp_data['Shape Type'].isin(['ROUND'])]
                            fancy_data = temp_data[temp_data['Shape Type'].isin(['FANCY'])]
                            
                            round_crt = round_data['WGT'].sum()
                            fancy_crt = fancy_data['WGT'].sum()

                            total_round = round_data['Net Value'].sum()
                            total_fancy = fancy_data['Net Value'].sum()

                            try:
                                round_pr = round(round_crt/ctr*100)
                                fancy_pr = round(fancy_crt/ctr*100)
                            except:
                                round_pr = 0
                                fancy_pr = 0

                            with st.container():
                                col1, col2, col3 = st.columns([1,1,1])
                                col1.markdown("<h5 style='text-align: center; background-color:#EBF1DE;box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);'>Total Stock Valuation</h5>", unsafe_allow_html=True)
                                col1.markdown("<h2 style='text-align: center; background-color:#EBF1DE; color: green; box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);'>%s%s</h2>" % (str('$'),round(total/1000000,2)), unsafe_allow_html=True)
                                col2.markdown("<h5 style='text-align: center; background-color:#EBF1DE; box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);'>Total Stock Crt.</h5>", unsafe_allow_html=True)
                                col2.markdown("<h2 style='text-align: center; background-color:#EBF1DE; box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19); color: green;'>%s</h2>" % (round(ctr,2)), unsafe_allow_html=True)
                                col3.markdown("<h5 style='text-align: center; background-color:#EBF1DE; box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);'>Total Avalilable Pieces</h5>", unsafe_allow_html=True)
                                col3.markdown("<h2 style='text-align: center; background-color:#EBF1DE; box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19); color: green;'>%s</h2>" % (count), unsafe_allow_html=True)
                            
                                st.markdown("<br/>", unsafe_allow_html=True)
                                col1, col2 = st.columns([1,1])
                                col1.markdown("<h5 style='text-align: center; background-color:#EBF1DE; box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);'>Round%</h5>", unsafe_allow_html=True)
                                col1.markdown("<h2 style='text-align: center; background-color:#EBF1DE; box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19); color: green;'>%s%s</h2>" % (round_pr,str('%')), unsafe_allow_html=True)
                                col2.markdown("<h5 style='text-align: center; background-color:#EBF1DE; box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);'>Fancy%</h5>", unsafe_allow_html=True)
                                col2.markdown("<h2 style='text-align: center; background-color:#EBF1DE; box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19); color: green;'>%s%s</h2>" % (fancy_pr,str('%')), unsafe_allow_html=True)

                                st.markdown("<br/>", unsafe_allow_html=True)
                                col1, col2 = st.columns([1,1])
                                col1.markdown("<h5 style='text-align: center; background-color:#EBF1DE;box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);'>Round Avg Price</h5>", unsafe_allow_html=True)
                                col1.markdown("<h2 style='text-align: center; background-color:#EBF1DE; color: green; box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);'>%s%s</h2>" % (str('$'),round(total_round/round_crt,2)), unsafe_allow_html=True)
                                col2.markdown("<h5 style='text-align: center; background-color:#EBF1DE; box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);'>Fancy Avg Price</h5>", unsafe_allow_html=True)
                                col2.markdown("<h2 style='text-align: center; background-color:#EBF1DE; box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19); color: green;'>%s%s</h2>" % (str('$'),round(total_fancy/fancy_crt,2)), unsafe_allow_html=True)

                        def sum_of_count_crt_net_value(data,selected_chart_comp,selected_lab, selected_shape, selected_band, selected_color, selected_purity, selected_fls,selected_polish,selected_cut,selected_symm):
                            """ create sale dashboard according to report filters and required data selection
                                
                                Args:
                                    data (df): data frame containing all the data
                                    selected_chart_comp (str): selected chart component
                                    selected_lab (str): selected lab
                                    selected_shape (str): selected shape
                                    selected_band (str): selected band
                                    selected_color (str): selected color
                                    selected_purity (str): selected purity
                                    selected_fls (str): selected fls
                                    selected_polish (str): selected polish
                                    selected_cut (str): selected cut
                                    selected_symm (str): selected symmetry  
                            """
                            
                            st.markdown("<h3 style='text-align: center;'>Sale Dashboard (Company-" + str(selected_chart_comp) + ")</h3>", unsafe_allow_html=True)
                            last = selected_end_date.strftime('%b')
                            last = str(str(last) + "-" + str(selected_end_date.strftime('%y')))
                            first = selected_start_date.strftime('%b')
                            first = str(str(first) + "-" + str(selected_start_date.strftime('%y')))                    

                            if selected_chart_comp == "Manufacturing":
                                temp_data2 = data.loc[(data['COMP_NO'].isin([1,2,7,9]))]
                                temp_data2['COMP_NO']="Manufacturing"
                            else:
                                temp_data2 = data[data['COMP_NO']==selected_chart_comp]
                            
                            
                            temp_data1 = temp_data2[temp_data2['TYPE']=='SALE']
                            
                            temp_data1['website_band'] = temp_data1['WGT'].apply(lambda x: '0.01-0.23' if x <= 0.22 else
                                                    '0.23-0.29' if x <= 0.29 else
                                                    '0.30-0.34' if x <= 0.34 else
                                                    '0.35-0.39' if x <= 0.39 else
                                                    '0.40-0.49' if x <= 0.49 else
                                                    '0.50-0.59' if x <= 0.59 else
                                                    '0.60-0.69' if x <= 0.69 else
                                                    '0.70-0.79' if x <= 0.79 else
                                                    '0.80-0.89' if x <= 0.89 else
                                                    '0.90-0.94' if x <= 0.94 else
                                                    '0.95-0.99' if x <= 0.99 else
                                                    '1.00-1.09' if x <= 1.09 else
                                                    '1.10-1.17' if x <= 1.17 else
                                                    '1.18-1.29' if x <= 1.29 else
                                                    '1.30-1.39' if x <= 1.39 else
                                                    '1.40-1.49' if x <= 1.49 else
                                                    '1.50-1.69' if x <= 1.69 else
                                                    '1.70-1.99' if x <= 1.99 else
                                                    '2.00-2.49' if x <= 2.49 else
                                                    '2.50-2.99' if x <= 2.99 else
                                                    '3.00-3.99' if x <= 3.99 else
                                                    '4.00-4.99' if x <= 4.99 else
                                                    '5.00-5.99' if x <= 5.99 else
                                                    '6+')
                            
                            temp_data1_trend_doss = temp_data1[temp_data1['Band']!='Doss']
                            temp_data1_trend_doss = temp_data1_trend_doss[temp_data1_trend_doss['SHAPE1']!='RD']
                            temp_data1_trend_doss = temp_data1_trend_doss[temp_data1_trend_doss['COLOR_A'].isin(["D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N"])]
                            if len(temp_data1_trend_doss)>0:
                                temp_data1_trend_doss = temp_data1_trend_doss.groupby(['website_band', 'SHAPE1', 'COLOR_A', 'PURITY_A', 'CUT_ACTUAL', 'POLISH', 'SYMM', 'FLS']).agg({
                                        'PACKET_NO': 'count',
                                        'SALE_DAYS': 'mean',
                                        'NET_RATE': 'mean',
                                        'Net Value': 'mean'
                                    }).rename(columns={
                                        'PACKET_NO': 'count',
                                        'SALE_DAYS': 'avg_days',
                                        'NET_RATE': 'PPC',
                                        'Net Value': 'NET_VALUE'
                                    }).reset_index()
                                
                                temp_data1_trend_doss = temp_data1_trend_doss.sort_values(by=["count", 'avg_days','NET_VALUE'], ascending=[False, True,False])
                                
                                temp_data1_trend_doss['avg_days'] = round(temp_data1_trend_doss['avg_days'])
                                temp_data1_trend_doss['PPC'] = round(temp_data1_trend_doss['PPC'],1)
                                temp_data1_trend_doss['NET_VALUE'] = round(temp_data1_trend_doss['NET_VALUE'],1)
                            
                            
                            temp_data1_trend = temp_data1[temp_data1['Band']!='Doss']
                            temp_data1_trend = temp_data1_trend[temp_data1_trend['SHAPE1']=='RD']
                            temp_data1_trend = temp_data1_trend[temp_data1_trend['COLOR_A'].isin(["D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N"])]
                            if len(temp_data1_trend)>0:
                                temp_data1_trend = temp_data1_trend.groupby(['website_band', 'SHAPE1', 'COLOR_A', 'PURITY_A', 'CUT_ACTUAL', 'POLISH', 'SYMM', 'FLS']).agg({
                                        'PACKET_NO': 'count',
                                        'SALE_DAYS': 'mean',
                                        'NET_RATE': 'mean',
                                        'Net Value': 'mean'
                                    }).rename(columns={
                                        'PACKET_NO': 'count',
                                        'SALE_DAYS': 'avg_days',
                                        'NET_RATE': 'PPC',
                                        'Net Value': 'NET_VALUE'
                                    }).reset_index()
                                
                                temp_data1_trend = temp_data1_trend.sort_values(by=["count", 'avg_days','NET_VALUE'], ascending=[False, True,False])
                                
                                temp_data1_trend['avg_days'] = round(temp_data1_trend['avg_days'])
                                temp_data1_trend['PPC'] = round(temp_data1_trend['PPC'],1)
                                temp_data1_trend['NET_VALUE'] = round(temp_data1_trend['NET_VALUE'],1)
                            
                            temp_first_sale = temp_data1[temp_data1['Month']==str(first)]
                            temp_first_sale = temp_first_sale.drop_duplicates(subset=['PACKET_NO'])
                            first_sale_crt = temp_first_sale['WGT'].sum()

                            temp_last_sale = temp_data1[temp_data1['Month']==str(last)]
                            temp_last_sale = temp_last_sale.drop_duplicates(subset=['PACKET_NO'])

                            temp_data1['LAB1'] = temp_data1.apply(lambda x: 1 if x['LAB'] == 'GIA' else 2, axis=1)
                                    
                            temp_data1 = temp_data1.sort_values(["PACKET_NO","LAB1","Date"], ascending=[True, True, False])
                            temp_data = temp_data1.drop_duplicates(subset=['PACKET_NO'])
                            
                            temp_data['Count'] = temp_data.apply(lambda x: 1 if x['PACKET_NO'] not in ['na', 'none', 0, "", " "] else 0, axis=1)
                            
                            count = temp_data['Count'].sum()
                            ctr = temp_data['WGT'].sum()
                            total = temp_data['Net Value'].sum()
                            
                            round_data = temp_data[temp_data['Shape Type'].isin(['ROUND'])]
                            fancy_data = temp_data[temp_data['Shape Type'].isin(['FANCY'])]
                            
                            round_sale = round_data['Count'].sum()
                            fancy_sale = fancy_data['Count'].sum()
                            round_crt = round_data['WGT'].sum()
                            fancy_crt = fancy_data['WGT'].sum()

                            total_round = round_data['Net Value'].sum()
                            total_fancy = fancy_data['Net Value'].sum()

                            new_sale = temp_data[temp_data['status']=="New-Sale"]
                            
                            sale_count = len(new_sale)
                            new = temp_data2[temp_data2['TYPE']=="NEW ARRIVAL"]
                            new_count = len(new)
                            
                            stock_sale = temp_data[temp_data['status']=="Stock-Sale"]
                            
                            sale_stock_count = len(stock_sale)
                            stock = temp_data2[temp_data2['Date']==str(selected_end_date)]
                            stock = stock[stock['TYPE']=="STOCK"]
                            
                            stock_count = len(stock)
                            total_stock = temp_data2[temp_data2['TYPE'].isin(["STOCK","NEW ARRIVAL"])]
                            
                            total_stock_count = len(total_stock)
                            
                            try:
                                round_pr = round(round_sale/count*100)
                                fancy_pr = round(fancy_sale/count*100)
                            except:
                                round_pr = 0
                                fancy_pr = 0
                            
                            try:
                                temp_data.to_clipboard()
                                # avg_day = round(temp_data['SALE_DAYS'].sum()/count * 0.7)
                                avg_day = round(temp_data['SALE_DAYS'].mean()*0.7)
                            except:
                                st.error("Data Missing in CNO - %s" % str(selected_chart_comp))
                            
                            pre_rd_ppc = 0
                            curr_rd_ppc = 0
                            pre_fa_ppc = 0
                            curr_fa_ppc = 0

                            round_data = temp_data[temp_data['Shape Type'].isin(['ROUND'])]
                            fancy_data = temp_data[temp_data['Shape Type'].isin(['FANCY'])]

                            
                            if selected_from_year==selected_year and selected_from_data_range==selected_data_range:
                                curr_rd_ppc = round(total_round/round_crt,0)
                                if len(fancy_data)>0:
                                    curr_fa_ppc = round(total_fancy/fancy_crt,0)
                            else:
                                pre_rd_data = round_data.loc[(round_data['Month']==str(str(selected_from_data_range) + "-" + str(selected_from_year[-2:])))]
                                pre_fa_data = fancy_data.loc[(fancy_data['Month']==str(str(selected_from_data_range) + "-" + str(selected_from_year[-2:])))]
                                if len(pre_rd_data)>0:
                                    pre_rd_ppc = round(sum(pre_rd_data['Net Value'])/sum(pre_rd_data['WGT']),0)
                                if len(pre_fa_data)>0:
                                    pre_fa_ppc = round(sum(pre_fa_data['Net Value'])/sum(pre_fa_data['WGT']),0)
                                curr_rd_data = round_data.loc[(round_data['Month']==str(str(selected_data_range) + "-" + str(selected_year[-2:])))]
                                curr_fa_data = fancy_data.loc[(fancy_data['Month']==str(str(selected_data_range) + "-" + str(selected_year[-2:])))]
                                if len(curr_rd_data)>0:
                                    curr_rd_ppc = round(sum(curr_rd_data['Net Value'])/sum(curr_rd_data['WGT']),0)
                                if len(curr_fa_data)>0:
                                    curr_fa_ppc = round(sum(curr_fa_data['Net Value'])/sum(curr_fa_data['WGT']),0)
                            
                            def get_mfg_data(db,year,month,a_1):
                                """ Get MFG data for a given year and month"""
                                if a_1 == 1:
                                    res = db.find({"TYPE":"SALE","Month": str(str(month) + "-" + str(str(year-1)[-2:])), "YEAR": str(year-1)})
                                    # res = db.find({"TYPE":{"$in":["SALE","NEW ARRIVAL"]},"Month": str(str(month) + "-" + str(str(year-1)[-2:])), "YEAR": str(year-1)})
                                else:
                                    # res = monthly_collection.find({"TYPE":"SALE","COMP_NO": comp_fun,"Month": str(str(curr_month_fun) + "-" + str(str(selected_year_fun)[-2:])), "YEAR": str(selected_year_fun)})
                                    # res = db.find({"TYPE":type_fun,"Month": str(str(month) + "-" + str(str(year)[-2:])), "YEAR": str(year)})
                                    res = db.find({"TYPE":"SALE","Month": str(str(month) + "-" + str(str(year)[-2:])), "YEAR": str(year)})
                                    # res = db.find({"TYPE":{"$in":["SALE","NEW ARRIVAL"]},"Month": str(str(month) + "-" + str(str(year)[-2:])), "YEAR": str(year)})
                                df_prev2= pl.DataFrame(res)
                                df_prev3 = df_prev2.to_pandas()
                                return df_prev3

                            def get_prev_growth_data(prev_month_fun,selected_year_fun,comp_fun):
                                """ Get previous month data for a given year and month"""
                                
                                selected_year_fun = int(selected_year_fun)
                                df_prev1=pd.DataFrame()
                                if comp_fun == "Manufacturing":
                                    df_1 = get_mfg_data(monthly_collection_1,selected_year_fun,prev_month_fun,1)
                                    df_2 = get_mfg_data(monthly_collection_2,selected_year_fun,prev_month_fun,1)
                                    df_7 = get_mfg_data(monthly_collection_7,selected_year_fun,prev_month_fun,1)
                                    df_9 = get_mfg_data(monthly_collection_9,selected_year_fun,prev_month_fun,1)
                                    df_prev1 = pd.concat([df_1,df_2,df_7,df_9])
                                    del df_1,df_2,df_7,df_9
                                    # res = monthly_collection.find({"TYPE":"SALE","COMP_NO": { "$in": [1, 2, 7, 9]},"Month": str(str(prev_month_fun) + "-" + str(str(selected_year_fun-1)[-2:])), "YEAR": str(selected_year_fun-1)})
                                elif comp_fun == 1:
                                    df_prev1 = get_mfg_data(monthly_collection_1,selected_year_fun,prev_month_fun,1)
                                elif comp_fun == 2:
                                    df_prev1 = get_mfg_data(monthly_collection_2,selected_year_fun,prev_month_fun,1)
                                elif comp_fun == 7:
                                    df_prev1 = get_mfg_data(monthly_collection_7,selected_year_fun,prev_month_fun,1)
                                elif comp_fun == 9:
                                    df_prev1 = get_mfg_data(monthly_collection_9,selected_year_fun,prev_month_fun,1)
                                        # res = monthly_collection.find({"TYPE":"SALE","COMP_NO": comp_fun,"Month": str(str(prev_month_fun) + "-" + str(str(selected_year_fun-1)[-2:])), "YEAR": str(selected_year_fun-1)})
                                else:
                                    df_prev1 = get_mfg_data(monthly_collection_rap,selected_year_fun,prev_month_fun,1)
                                    # res = monthly_collection_rap.find({"TYPE":"SALE","COMP_NO": 11,"Month": str(str(prev_month_fun) + "-" + str(str(selected_year_fun-1)[-2:])), "YEAR": str(selected_year_fun-1)})
                                # df_prev2= pl.DataFrame(res)
                                # df_prev1 = df_prev2.to_pandas()
                                df_prev1['LAB1'] = df_prev1.apply(lambda x: 1 if x['X_LAB'] == 'GIA' else 2, axis=1)
                                
                                df_prev1 = filter_data_with_user_selected(df_prev1, selected_lab, selected_shape, selected_band, selected_color, selected_purity, selected_fls, selected_polish,selected_cut,selected_symm)
                                df_prev1 = df_prev1.sort_values(["PACKET_NO","LAB1","Date"])
                                df_prev1 = df_prev1.drop_duplicates("PACKET_NO")
                                del prev_month_fun,selected_year_fun
                                return df_prev1

                            def get_growth_data(curr_month_fun,selected_year_fun,comp_fun):
                                """ Get current month data for a given year and month"""
                                
                                df_curr1=pd.DataFrame()

                                if comp_fun == "Manufacturing":
                                    df_1 = get_mfg_data(monthly_collection_1,selected_year_fun,curr_month_fun,0)
                                    df_2 = get_mfg_data(monthly_collection_2,selected_year_fun,curr_month_fun,0)
                                    df_7 = get_mfg_data(monthly_collection_7,selected_year_fun,curr_month_fun,0)
                                    df_9 = get_mfg_data(monthly_collection_9,selected_year_fun,curr_month_fun,0)
                                    df_curr1 = pd.concat([df_1,df_2,df_7,df_9])
                                    del df_1,df_2,df_7,df_9
                                    # res = monthly_collection.find({"TYPE":"SALE","COMP_NO": {"$in": [1,2,7,9]},"Month": str(str(curr_month_fun) + "-" + str(str(selected_year_fun)[-2:])), "YEAR": str(selected_year_fun)})
                                elif comp_fun == 1:
                                    df_curr1 = get_mfg_data(monthly_collection_1,selected_year_fun,curr_month_fun,0)
                                elif comp_fun == 2:
                                    df_curr1 = get_mfg_data(monthly_collection_2,selected_year_fun,curr_month_fun,0)
                                elif comp_fun == 7:
                                    df_curr1 = get_mfg_data(monthly_collection_7,selected_year_fun,curr_month_fun,0)
                                elif comp_fun == 9:
                                    df_curr1 = get_mfg_data(monthly_collection_9,selected_year_fun,curr_month_fun,0)
                                else:
                                    df_curr1 = get_mfg_data(monthly_collection_rap,selected_year_fun,curr_month_fun,0)
                                    # res = monthly_collection.find({"TYPE":"SALE","COMP_NO": comp_fun,"Month": str(str(curr_month_fun) + "-" + str(str(selected_year_fun)[-2:])), "YEAR": str(selected_year_fun)})
                                # df_curr1= pl.DataFrame(res)
                                # df_curr1 = df_curr1.to_pandas()
                                
                                df_curr1['LAB1'] = df_curr1.apply(lambda x: 1 if x['X_LAB'] == 'GIA' else 2, axis=1)
                                df_curr1 = filter_data_with_user_selected(df_curr1, selected_lab, selected_shape, selected_band, selected_color, selected_purity, selected_fls, selected_polish,selected_cut,selected_symm)
                                df_curr1 = df_curr1.sort_values(["PACKET_NO","LAB1","Date"])
                                df_curr1 = df_curr1.drop_duplicates("PACKET_NO")

                                del curr_month_fun,selected_year_fun
                                return df_curr1
                                
                            mon=  ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
                            monthly_growth = 0
                            selected_growth = 0
                            quaterly_growth = 0
                            if (selected_data_range in mon) and (selected_from_data_range==selected_data_range):
                                selected_growth = 0
                            else:
                                df = temp_data1

                                df['LAB1'] = df.apply(lambda x: 1 if x['X_LAB'] == 'GIA' else 2, axis=1)
                                df = df.sort_values(["PACKET_NO","LAB1","Date"])
                                df = df.drop_duplicates("PACKET_NO")

                                df_curr = df.loc[(df['Month']==str(str(selected_data_range) + "-" + str(str(selected_year)[-2:])))]
                                df_prev = df.loc[(df['Month']==str(str(selected_from_data_range) + "-" + str(str(selected_from_year)[-2:])))]
                                
                                selected_growth = (sum(df_curr['Net Value']) - sum(df_prev['Net Value']))/sum(df_prev['Net Value'])*100
                                del df_curr,df_prev

                            month = selected_data_range
                            def get_per_monthly_change(type):
                                """ Get the percentage change of the monthly data"""
                                if (selected_data_range in mon) and (month=='Jan'):
                                    prev_month = 'Dec'
                                    df_prev = get_prev_growth_data(prev_month,selected_year,selected_chart_comp)
                                    df_curr = get_growth_data(selected_data_range,selected_year,selected_chart_comp)

                                    if type == "Count":
                                        monthly_growth_1 = (len(df_curr["PACKET_NO"]) - len(df_prev["PACKET_NO"]))/len(df_prev["PACKET_NO"])*100
                                    else:
                                        monthly_growth_1 = (sum(df_curr[type])/1000000 - sum(df_prev[type])/1000000)/(sum(df_prev[type])/1000000)*100
                                    del df_curr,df_prev,prev_month
                                else:
                                    prev_month = mon[mon.index(selected_data_range)-1]
                                    df_prev = get_growth_data(prev_month,selected_from_year,selected_chart_comp)
                                    df_curr = get_growth_data(selected_data_range,selected_year,selected_chart_comp)
                                    
                                    if type == "Count":
                                        monthly_growth_1 = (len(df_curr["PACKET_NO"]) - len(df_prev["PACKET_NO"]))/len(df_prev["PACKET_NO"])*100
                                    else:
                                        monthly_growth_1 = (sum(df_curr[type]) - sum(df_prev[type]))/sum(df_prev[type])*100
                                    del df_curr,df_prev,prev_month
                                return monthly_growth_1
                            
                            monthly_growth = get_per_monthly_change('Net Value')

                            if (selected_data_range in mon) and (selected_data_range=='Jan'):
                                prev_year = int(selected_year)-1
                                prev_month = mon[len(mon)-2]
                                df_prev = get_growth_data(prev_month,prev_year,selected_chart_comp)
                                df_curr = get_growth_data(selected_data_range,selected_year,selected_chart_comp)
                                
                                quaterly_growth = (sum(df_curr['Net Value']) - sum(df_prev['Net Value']))/sum(df_prev['Net Value'])*100
                                del df_curr,df_prev,prev_month,prev_year
                            elif (selected_data_range in mon) and (selected_data_range=='Feb'):
                                prev_year = int(selected_year)-1
                                prev_month = mon[len(mon)-1]
                                df_curr = get_growth_data(selected_data_range,selected_year,selected_chart_comp)
                                df_prev = get_growth_data(prev_month,prev_year,selected_chart_comp)
                                
                                quaterly_growth = (sum(df_curr['Net Value']) - sum(df_prev['Net Value']))/sum(df_prev['Net Value'])*100
                                del df_curr,df_prev,prev_month,prev_year
                            else:
                                prev_month = mon[mon.index(selected_data_range)-2]
                                df_prev = get_growth_data(prev_month,selected_year,selected_chart_comp)
                                df_curr = get_growth_data(selected_data_range,selected_year,selected_chart_comp)

                                quaterly_growth = (sum(df_curr['Net Value']) - sum(df_prev['Net Value']))/sum(df_prev['Net Value'])*100
                                del df_curr,df_prev,prev_month

                            dash_2 = st.container()
                            with dash_2:
                                col1, col2, col3 = st.columns(3)
                                # style_metric_cards(border_left_color="#EBF1DE",box_shadow=True,border_radius_px=5,background_color="#EBF1DE")
                                style_metric_cards(border_left_color="#e4e7f5",box_shadow=True,border_radius_px=5,background_color="#e4e7f5")
                                col1.metric(label="Total Revenue", value= "$"+millify(total/1000000, precision=2) , delta=f"{get_per_monthly_change('Net Value'):.2f}%")
                                col2.metric(label="Total Sold Crt.", value = round(ctr,2) , delta=f"{get_per_monthly_change('WGT'):.2f}%")
                                col3.metric(label="Total Sold Pieces", value= count , delta=f"{get_per_monthly_change('Count'):.2f}%")
                                
                                if selected_chart_comp not in ['Global', "Rap Net"]:
                                    col1, col2, col3 = st.columns(3)
                                    col1.metric(label="Sold Proportion (New Arrival)", value= f"{(sale_count/new_count)*100:.1f}%")
                                    col2.metric(label="Sold Proportion (Stock)", value= f"{sale_stock_count/(stock_count + count)*100:.1f}%")
                                    col3.metric(label="Sold Proportion", value= f"{(count/total_stock_count)*100:.1f}%")                                    

                                    col1, col2, col3 = st.columns(3)
                                    col1.metric(label="Sales Cycle Time", value= f"{avg_day} Days")
                                    col2.metric(label="Round%", value= f"{round_pr:.0f}%")
                                    col3.metric(label="Fancy%", value= f"{fancy_pr:.0f}%")

                                    col1, col2, col3 = st.columns(3)
                                    col1.metric(label="Monthly Growth Rate", value= f"{monthly_growth:.0f}%")
                                    col2.metric(label="Quarterly Growth Rate", value= f"{quaterly_growth:.0f}%")
                                    col3.metric(label="Selected time period Growth Rate", value= f"{selected_growth:.0f}%")

                                    col1, col2, col3 = st.columns(3)
                                    if pre_rd_ppc<=0 and pre_fa_ppc<=0:
                                        col1.metric(label="Round Avg Price", value= "$"+str(round(curr_rd_ppc)))
                                        if len(fancy_data)>0:
                                            col2.metric(label="Fancy Avg Price", value= "$"+str(round(curr_fa_ppc)))
                                    else:    
                                        if (curr_rd_ppc>0) and (pre_rd_ppc>0):
                                            col1.metric(label="Round Avg Price (%s)" % selected_from_data_range, value= "$"+str(round(pre_rd_ppc)))
                                            col2.metric(label="Round Avg Price (%s)" % selected_data_range, value= "$"+str(round(curr_rd_ppc)))
                                            col3.metric(label="Round change in per.", value= f"{(curr_rd_ppc-pre_rd_ppc)/pre_rd_ppc*100:.0f}%")

                                        col1, col2, col3 = st.columns(3)
                                        if (curr_fa_ppc>0) and (pre_fa_ppc>0):
                                            col1.metric(label="Fancy Avg Price (%s)" % selected_from_data_range, value= "$"+str(round(pre_fa_ppc)))
                                            col2.metric(label="Fancy Avg Price (%s)" % selected_data_range, value= "$"+str(round(curr_fa_ppc)))
                                            col3.metric(label="Fancy change in per.", value= f"{(curr_fa_ppc-pre_fa_ppc)/pre_fa_ppc*100:.0f}%")
                                else:
                                    col1, col2, col3 = st.columns(3)
                                    col1.metric(label="Sales Cycle Time", value= f"{avg_day} Days")
                                    col2.metric(label="Round%", value= f"{round_pr:.0f}%")
                                    col3.metric(label="Fancy%", value= f"{fancy_pr:.0f}%")

                                    col1, col2, col3 = st.columns(3)
                                    col1.metric(label="Round Avg Price", value= "$"+str(round(total_round/round_crt,2)))
                                    col2.metric(label="Fancy Avg Price", value= "$"+str(round(total_fancy/fancy_crt,2)))
                                    col3.metric(label="Sold Proportion", value= f"{(count/total_stock_count)*100:.1f}%")
                            
                            if len(temp_data1_trend)>0:
                                st.markdown("<h3 style='text-align: center;'>Best Sale Category in Selected Time Period (Round)</h3>", unsafe_allow_html=True)
                                st.write(temp_data1_trend.head())
                                
                            if len(temp_data1_trend_doss)>0:
                                st.markdown("<h3 style='text-align: center;'>Best Sale Category in Selected Time Period (Fancy)</h3>", unsafe_allow_html=True)
                                st.write(temp_data1_trend_doss.head())
                            
                        def buble_report_without_comp():
                            """ Return input stream for mode (daily,weekly,month, and quarter)"""
                            col1, col2 = expander1.columns([1,1])
                            # SELECT MODE
                            selected_mode = col1.selectbox("Select Mode", tuple(total_mode))
                            
                            # SELECTED TYPE
                            selected_status = col2.multiselect("Select status", total_status, ["Sale"])
                            status_list = []
                            if "Sale" in selected_status:
                                status_list.append("SALE")
                            if "New Arrival" in selected_status:
                                status_list.append("NEW ARRIVAL")
                            if "Stock" in selected_status:
                                status_list.append("STOCK")
                            if "All" in selected_status:
                                status_list = final_status
                            return selected_mode,status_list

                        def inflow_outflow_report_selection(selected_chart, month_list_for_inflow_outflow):
                            """ Return input stream for two company and  value type (count, crt, and value) 

                                Args:
                                    selected_chart (str): selected chart type (inflow, outflow, and total)
                                    month_list_for_inflow_outflow (list): list of month for inflow and outflow
                                
                            """
                            # SELECT Chart Type
                            if selected_chart == "Parameter wise InFlow-OutFlow":
                                col1, col2, col3 = expander1.columns([1,1,1])
                                
                                # SELECT COMP
                                selected_chart_comp = col1.selectbox("Select Company 1", tuple(total_first_comp))

                                selected_chart_comp2 = col2.selectbox("Select Company 2", tuple(total_second_comp),total_second_comp[0])

                                select_inflow_outflow_month = col3.multiselect("Select Month", month_list_for_inflow_outflow, month_list_for_inflow_outflow)

                                col1, col2, col3 = expander1.columns([1,1,1])
                                    
                                # SELECTED TYPE
                                selected_type = col1.selectbox("Select Type", tuple(total_data_type))
                                
                                selected_perms = col2.selectbox("Select Params", tuple(total_parameters))
                                
                                # SELECT SHAPE
                                
                                selected_shape1 = col3.selectbox("Select Shape", tuple(final_shape))
                        
                                if selected_perms == "Table":
                                    selected_perms="TABLE_PER"
                                else:
                                    pass
                                return selected_chart_comp,selected_chart_comp2,selected_type,selected_perms,selected_shape1,select_inflow_outflow_month
                            else:
                                col1, col2 = expander1.columns([1,1])
                                
                                # SELECT COMP
                                selected_chart_comp = col1.selectbox("Select Company 1", tuple(total_first_comp))

                                selected_chart_comp2 = col2.selectbox("Select Company 2", tuple(total_second_comp),total_second_comp[0])
                                
                                col1, col2 = expander1.columns([1,1])
                                # SELECTED TYPE
                                selected_type = col1.selectbox("Select Type", tuple(total_data_type))
                                
                                select_inflow_outflow_month = col2.multiselect("Select Month", month_list_for_inflow_outflow, month_list_for_inflow_outflow)

                                return selected_chart_comp,selected_chart_comp2,selected_type,select_inflow_outflow_month

                        def select_comp2():
                            """ tack input for two companys in single line"""
                            col1, col2 = expander1.columns([1,1])
                            # SELECT COMP
                            selected_chart_comp = col1.selectbox("Select Company 1", tuple(total_first_comp))

                            selected_chart_comp2 = col2.selectbox("Select Company 2", tuple(total_second_comp),total_second_comp[0])

                            return selected_chart_comp,selected_chart_comp2
                        
                        def select_comp2_for_stock():
                            """ tack input for two companys in single line"""
                            col1, col2 = expander1.columns([1,1])
                            # SELECT COMP
                            selected_chart_comp = col1.selectbox("Select Company 1", tuple(total_first_comp_for_stock))

                            selected_chart_comp2 = col2.selectbox("Select Company 2", tuple(total_second_comp_for_stock),total_second_comp_for_stock[0])

                            return selected_chart_comp,selected_chart_comp2

                        def shape_report_user_inputs():
                            """ tack input for two shape and company in single line """
                            
                            col1, col2,col3 = expander1.columns([1,1,1])
                            selected_shape1 = col1.selectbox("Select Shape 1", tuple(final_first_shape))
                            selected_shape2 = col2.selectbox("Select Shape 2", tuple(final_second_shape))

                            selected_chart_comp = col3.selectbox("Select Company", tuple(total_comp_without_none))

                            return selected_shape1,selected_shape2,selected_chart_comp
                        
                        def shape_report():
                            """ tack input for two shape, company,mode and status"""
                            col1, col2 = expander1.columns([1,1])

                            selected_shape1 = col1.selectbox("Select Shape 1", tuple(final_first_shape))
                            selected_shape2 = col2.selectbox("Select Shape 2", tuple(final_second_shape))

                            col1, col2, col3 = expander1.columns([1,1,1])

                            selected_chart_comp = col1.selectbox("Select Company", tuple(total_comp_without_none))
                            selected_mode = col2.selectbox("Select Mode", tuple(total_mode))
                            selected_status = col3.multiselect("Select status", total_status,["Sale"])
                            
                            status_list = []
                            if "Sale" in selected_status:
                                status_list.append("SALE")
                            if "New Arrival" in selected_status:
                                status_list.append("NEW ARRIVAL")
                            if "Stock" in selected_status:
                                status_list.append("STOCK")
                            if "All" in selected_status:
                                status_list = final_status

                            return selected_chart_comp,selected_mode,status_list,selected_shape1,selected_shape2

                        def sale_report():
                            """tack input of two company, x excise, parameter and mode"""
                            
                            col1, col2 = expander1.columns([1,1])
                            # SELECT COMP
                            selected_chart_comp = col1.selectbox("Select Company 1", tuple(total_first_comp))

                            selected_chart_comp2 = col2.selectbox("Select Company 2", tuple(total_second_comp),total_second_comp[0])
                        
                            col1, col2, col3 = expander1.columns([1,1,1])

                            selected_x = col1.selectbox("Select X Excise", tuple(total_params))
                            selected_color = col2.selectbox("Select Parameter", tuple(total_params))
                            selected_mode = col3.selectbox("Select Mode", tuple(total_mode))
                            
                            return selected_chart_comp,selected_chart_comp2,selected_x,selected_color,selected_mode

                        def get_data_for_chnage_price_report(data,value_type,comp):
                            """ create report of start date to end date day diffance in price

                                Args:
                                    data (DataFrame): Pandas DataFrame
                                    value_type (str): type of value
                            """
                            
                            st.markdown("<h3 style='text-align: center;'>Company %s</h3>" % comp, unsafe_allow_html=True)
                            data = data.loc[(data["COMP_NO"]==comp)]

                            # data = data.sort_values(["PACKET_NO","Date"])
                            # data = data.drop_duplicates(["PACKET_NO","Date"])

                            data["DISC_PER"] = data.apply(lambda x: round(x["DISC_PER"],1),axis=1)
                            
                            
                            if value_type=="Disc%":
                                value_type = "DISC_PER"
                            else:
                                value_type = "NET_RATE"
                            data["Size"] = data.apply(lambda x: "Doss" if x["WGT"]<1 else "1.00 - 1.99" if (x["WGT"]>=1 and x["WGT"]<2) else "2.00 - 2.99" if (x["WGT"]>=2 and x["WGT"]<3) else "3.00 - 3.99" if (x["WGT"]>=3 and x["WGT"]<4) else "4.00 - 4.99" if (x["WGT"]>=4 and x["WGT"]<5) else "5.00+", axis=1)
                            data1 = data.pivot_table(index=["PACKET_NO", "X_LAB", "SHAPE1", "Size", "Band", "COLOR_A", "PURITY_A", "FLS", "CUT_ACTUAL", "POLISH", "SYMM"], 
                            columns='Date', 
                            values=str(value_type)).reset_index()
                            
                            n1 = list(data1.columns[10:len(data1.columns)])
                            d1=data1[n1]

                            x = pd.DataFrame()
                            for i in range(0,len(n1)+1):
                                try:
                                    x[n1[i+1]] = round(d1[n1[i]]-d1[n1[i+1]],1)
                                except:
                                    pass
                            dt1 = x

                            dt1 = dt1.fillna(0)

                            dt1['overall_change'] = dt1.sum(axis=1)
                            dt1['overall_change'] = dt1['overall_change'].round(2)
                            # dt1.to_clipboard()
                            n1 = list(data1.columns[0:10])
                            # n1 = list(data1.columns)
                            left_1 = data1[n1]
                            dt1["PACKET_NO"] = data1["PACKET_NO"]

                            df1 = pd.merge(left_1, dt1, how ='left', on="PACKET_NO")
                            df1.to_clipboard()
                            if value_type == "NET_RATE":
                                df1["Categ"] = dt1.apply(lambda x: "Tight" if x["overall_change"]>0.49 else "Loose" if x["overall_change"]<-0.49 else "Same", axis=1)
                                def color_survived(val):
                                    color = "#FFFFFF"
                                    if val<=0.49 and val>=-0.49:
                                        color="#FFFFFF"
                                    elif val>0.49:
                                        color="#C4E6CD"
                                    elif val<-0.49:
                                        color="#FCBCBE"
                                    else:
                                        color="#FFFFFF"
                                    # color = 'green' if val<0 else 'red'
                                    return f'background-color: {color}'
                            else:
                                df1["Categ"] = dt1.apply(lambda x: "Tight" if x["overall_change"]<-0.49 else "Loose" if x["overall_change"]>0.49 else "Same", axis=1)
                                def color_survived(val):
                                    color = "#FFFFFF"
                                    if val<=0.49 and val>=-0.49:
                                        color="#FFFFFF"
                                    elif val<-0.49:
                                        color="#C4E6CD"
                                    elif val>0.49:
                                        color="#FCBCBE"
                                    else:
                                        color="#FFFFFF"
                                    # color = 'green' if val<0 else 'red'
                                    return f'background-color: {color}'
                            
                            df1["point"] = dt1.apply(lambda x: "-4 Down" if x["overall_change"]<=-4.5 else "-4" 
                                                     if x["overall_change"]>=-4.49 and x["overall_change"]<-3.49 else "-3"
                                                     if x["overall_change"]>=-3.49 and x["overall_change"]<-2.49 else "-2"
                                                     if x["overall_change"]>=-2.49 and x["overall_change"]<-1.49 else "-1"
                                                     if x["overall_change"]>=-1.49 and x["overall_change"]<-0.49 else "0"
                                                     if x["overall_change"]>=-0.49 and x["overall_change"]<0.49 else "1"
                                                     if x["overall_change"]<=1.49 and x["overall_change"]>0.49 else "2"
                                                     if x["overall_change"]<=2.49 and x["overall_change"]>1.49 else "3"
                                                     if x["overall_change"]<=3.49 and x["overall_change"]>2.49 else "4"
                                                     if x["overall_change"]<=4.49 and x["overall_change"]>4.49 else "4 UP", axis=1)
                            
                            def get_pivot_for_data(data_fram,type_of_report,piv_col):
                                """ create pivot table for count and value as per selection"""
                                
                                if type_of_report == "count":
                                    return_data = data_fram.pivot_table(index=["X_LAB"], 
                                            columns=piv_col, 
                                            values="PACKET_NO",
                                            aggfunc={"PACKET_NO": "count"},
                                            fill_value=0,
                                            margins=False).reset_index()
                                    return return_data
                                else:
                                    return_data = data_fram.pivot_table(index=["Size"], 
                                            columns=piv_col, 
                                            values="PACKET_NO",
                                            aggfunc={"PACKET_NO": "count"},
                                            fill_value=0,
                                            margins=False).reset_index()
                                    return return_data
                            
                            pd.set_option("styler.render.max_elements", 1000000)
                            pivot_data = get_pivot_for_data(df1,"count","Categ")
                            pivot_for_band_data = get_pivot_for_data(df1,"band","Categ")
                            pivot_for_point_data = get_pivot_for_data(df1,"band","point")
                            
                            st.markdown("""
                                        <style>
                                            .table_1 {
                                                width:100%; 
                                                }
                                            .table_header{
                                                text-align: center;
                                                font-weight: bold;
                                                background-color: #287E8F;
                                                color: #FFFFFF;
                                                font-size: 12px;
                                            }
                                            .sub_total{
                                                text-align: center;
                                                font-weight: bold;
                                                font-size: 12px;
                                                background-color: #5297a5;
                                                color: #FFFFFF;
                                            }
                                            .table_head{
                                                text-align: center;
                                                font-weight: bold;
                                                font-size: 12px;
                                            }
                                            .table_data_style{
                                                text-align: center;
                                                font-size: 12px;
                                            }
                                            td, th{
                                                width: 1%;
                                            }
                                            tr{
                                                height: 12px;
                                            }
                                            tr:nth-child(even) {background-color: #f2f2f2;}
                                        </style>
                                        """, unsafe_allow_html=True)
                            total = sum([sum(pivot_data["Tight"]),sum(pivot_data["Same"]),sum(pivot_data["Loose"])])
                            table_head = """<tr><th class="table_header">Category</th><th class="table_header"># of stone</th><th class="table_header">%</th></tr>"""
                            table_data = """<tr><td class="table_head">Tight</td><td class="table_data_style">%s</td><td class="table_data_style">%s</td></tr><tr><td class="table_head">Same</td><td class="table_data_style">%s</td><td class="table_data_style">%s</td></tr><tr><td class="table_head">Loose</td><td class="table_data_style">%s</td><td class="table_data_style">%s</td></tr><tr><td class="table_head">Total</td><td class="table_head">%s</td><td class="table_head">%s</td></tr>""" % (sum(pivot_data["Tight"]),str(str(round(sum(pivot_data["Tight"])/total*100)) + "%"),sum(pivot_data["Same"]),str(str(round(sum(pivot_data["Same"])/total*100)) + "%"),sum(pivot_data["Loose"]),str(str(round(sum(pivot_data["Loose"])/total*100)) + "%"),total,str(str(round(total/total)*100) + "%"))
                            final_table_tag_str = "%s%s" % (table_head,table_data)
                            table_html_string = """
                                        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                                        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                                        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                                        <table class="table-borderless table-responsive card-1 p-4">%s</table>""" % final_table_tag_str
                            st.markdown("<h4 style='text-align: Left;'>Summary Table Acording to Pricing Category.</h4>", unsafe_allow_html=True)
                            st.markdown((((''.join(table_html_string).replace("'","")).replace(",","")).replace("[","")).replace("]",""), unsafe_allow_html=True)
                            
                            table_head = """<tr><th class="table_header">Size</th><th class="table_header">Category</th><th class="table_header"># of stone</th><th class="table_header">%</th></tr>"""
                            
                            # catag_head = """<td class="table_head">Tight</td><td class="table_head">Same</td><td class="table_head">Loose</td>"""
                            size_list = ["1.00 - 1.99","2.00 - 2.99","3.00 - 3.99","4.00 - 4.99","5.00+","Doss"]
                            
                            table_data = []
                            final_sum = sum([sum(pivot_for_band_data["Tight"]), sum(pivot_for_band_data["Same"]),sum(pivot_for_band_data["Loose"])])
                            for i in size_list:
                                size_wise_dt = pivot_for_band_data.loc[(pivot_for_band_data["Size"]==i)]
                                temp_size_head = ["""<td class="table_head" rowspan=3>%s</td>""" % i]
                                
                                total = sum([sum(size_wise_dt["Tight"]), sum(size_wise_dt["Same"]),sum(size_wise_dt["Loose"])])

                                if len(size_wise_dt)>0:
                                    for j in ["Tight","Same","Loose"]:
                                        # table_catag_row.append("""<td class="table_header">%s</td><td class="table_data_style">%s</td><td class="table_data_style">%s</td>""" % (j,sum(size_wise_dt[j]),str(str(round(sum(size_wise_dt[j])/total))) + "%"))
                                        catag_wise_per = round(sum(size_wise_dt[j])/total*100)
                                        day_col = "#FFFFFF"
                                        if catag_wise_per>=50:
                                            day_col = "#FCBCBE"

                                        if j == "Tight":
                                            table_data.append("""<tr>%s<td class="table_head">%s</td><td class="table_data_style">%s</td><td class="table_data_style" style="background-color:%s;">%s</td></tr>""" % ("".join(temp_size_head),j,sum(size_wise_dt[j]),day_col,str(str(catag_wise_per)) + "%"))
                                        else:
                                            table_data.append("""<tr><td class="table_head">%s</td><td class="table_data_style">%s</td><td class="table_data_style" style="background-color:%s;">%s</td></tr>""" % (j,sum(size_wise_dt[j]),day_col,str(str(catag_wise_per)) + "%"))
                                    table_data.append("""<tr><td class="sub_total" colspan="2">%s Total</td><td class="sub_total">%s</td><td class="sub_total">%s</td></tr>""" % (i,total,str(str(round(total/final_sum*100))) + "%"))
                            table_data.append("""<tr><td class="table_head" colspan="2">Total</td><td class="table_data_style">%s</td><td class="table_data_style">100%s</td></tr>""" % (final_sum,str("%")))
                            final_table_tag_str = "%s%s" % (table_head,table_data)
                            table_html_string = """
                                        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                                        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                                        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                                        <table class="table-borderless table-responsive card-1 p-4">%s</table>""" % final_table_tag_str
                            st.markdown("<h4 style='text-align: Left;'>Size Wise Pricing Category.</h4>", unsafe_allow_html=True)
                            st.markdown((((''.join(table_html_string).replace("'","")).replace(",","")).replace("[","")).replace("]",""), unsafe_allow_html=True)
                            
                            point_list = ["-4 Down", "-4", "-3","-2","-1","0","1","2","3","4","4 UP"]
                            point_head_list = []
                            point_total_val_list = []
                            point_total_per_list = []
                            point_head_list.append("""<th class="table_header">Size</th>""")
                            for j in point_list:
                                point_head_list.append("""<th class="table_header">%s</th>""" % str(j))
                                try:
                                    point_total_val_list.append("""<th class="sub_total">%s</th>""" % str(sum(pivot_for_point_data[j])))
                                    point_total_per_list.append("""<th class="sub_total">%s</th>""" % str(str(round(sum(pivot_for_point_data[j])/final_sum*100)) + "%"))
                                except:
                                    point_total_val_list.append("""<td class="sub_total">0</td>""")
                                    point_total_per_list.append("""<td class="sub_total">0%s</td>""" % "%")
                            point_head_list.append("""<th class="table_header">Total</th>""")
                            point_val_table_data = []
                            point_per_table_data = []

                            # final_sum = sum([sum(pivot_for_band_data["Tight"]), sum(pivot_for_band_data["Same"]),sum(pivot_for_band_data["Loose"])])
                            for i in size_list:
                                size_wise_dt = pivot_for_point_data.loc[(pivot_for_point_data["Size"]==i)]
                                if len(size_wise_dt)>0:
                                    temp_size_head = ["""<td class="table_head">%s</td>""" % i]
                                    total = 0
                                    point_data_val_list = []
                                    point_data_per_list = []

                                    for j in point_list:
                                        try:
                                            total = total + sum(size_wise_dt[str(j)])
                                            point_data_val_list.append("""<td class="table_data_style">%s</td>""" % str(sum(size_wise_dt[str(j)])))
                                        except:
                                            point_data_val_list.append("""<td class="table_data_style">0</td>""")
                                    
                                    for j in point_list:
                                        try:
                                            point_data_per_list.append("""<td class="table_data_style">%s</td>""" % str(str(round(sum(size_wise_dt[str(j)]/total*100))) + "%"))
                                        except:
                                            point_data_per_list.append("""<td class="table_data_style">0%s</td>""" % "%")
                                    
                                    row_total_val = ["""<td class="table_data_style">%s</td>""" % total]
                                    row_total_per = ["""<td class="table_data_style">%s</td>""" % str(str(round(total/final_sum*100)) + "%")]
                                    
                                    point_val_table_data.append("""<tr>%s%s%s</tr>""" % ("".join(temp_size_head),"".join(point_data_val_list),"".join(row_total_val)))
                                    point_per_table_data.append("""<tr>%s%s%s</tr>""" % ("".join(temp_size_head),"".join(point_data_per_list),"".join(row_total_per)))

                            point_val_table_data_str = """<tr>%s</tr>%s<tr><td class="sub_total">Total</td>%s<td class="sub_total">%s</td></tr>""" % ("".join(point_head_list),"".join(point_val_table_data),"".join(point_total_val_list),final_sum)
                            point_per_table_data_str = """<tr>%s</tr>%s<tr><td class="sub_total">Total</td>%s<td class="sub_total">%s</td></tr>""" % ("".join(point_head_list),"".join(point_per_table_data),"".join(point_total_per_list),"100%")
                            # point_per_table_data_str = """"<tr>%s</tr>%s""" % ("".join(point_head_list),"".join(point_per_table_data))

                            table_html_string = """
                                        <table class="table-borderless table-responsive card-1 p-4">%s</table>""" % point_val_table_data_str
                            st.markdown("<h4 style='text-align: Left;'>Brifly Variation Sheet.</h4>", unsafe_allow_html=True)
                            st.markdown((((''.join(table_html_string).replace("'","")).replace(",","")).replace("[","")).replace("]",""), unsafe_allow_html=True)
                            
                            table_html_string = """
                                        <table class="table-borderless table-responsive card-1 p-4">%s</table>""" % point_per_table_data_str
                            st.markdown("<h4 style='text-align: Left;'>Brifly Variation Sheet(In%).</h4>", unsafe_allow_html=True)
                            st.markdown((((''.join(table_html_string).replace("'","")).replace(",","")).replace("[","")).replace("]",""), unsafe_allow_html=True)

                            values = ['{:.2f}'] * (len(list(df1.columns[10:len(df1.columns)]))-2)
                            
                            result_dict = dict(zip(list(df1.columns[10:len(df1.columns)-2]), values))

                            n1 = list(list(df1.columns[0:10]) + list(df1.columns[len(df1.columns)-3:len(df1.columns)]) + list(df1.columns[10:len(df1.columns)-3]))
                            
                            df1 = df1[n1]

                            n1 = list(list(df1.columns[10:11]) + list(df1.columns[13:len(df1.columns)]))
                            
                            st.dataframe(df1.style.format(result_dict).applymap(color_survived, subset=n1))
                        
                        def get_shape_filtered_data(df,shape):
                            """ filter shape in datafram and return datafram
                            
                                Args:
                                    df (dataframe): dataframe to filter
                                    shape (str): shape to filter
                            """
                            df = df.loc[(df['SHAPE1'] == shape)]
                            # df = df.loc[(df['SHAPE1'].isin(shape))]
                            return df
                        
                        def get_report_formate(data_frame,type_fun):
                            """ create formate html formate for shapwise report
                            
                                Args:
                                    data_frame (dataframe): dataframe to create report
                                    type_fun (str): type of report to create
                            """
                            
                            data_frame = data_frame.loc[(data_frame["TYPE"]==str(type_fun))]
                            # range_seq = ["0.01 - 0.03","0.04 - 0.07", "0.08 - 0.14", "0.15 - 0.17", "0.18 - 0.22", "0.23 - 0.29", "0.30 - 0.39", "0.40 - 0.49", "0.50 - 0.69", "0.70 - 0.89", "0.90 - 0.99", "1.00 - 1.49", "1.50 - 1.99", "2.00 - 2.99", "3.00 - 3.99", "4.00 - 4.99", "5.00 - 99.99"]
                            range_seq = ["5.00 - 99.99","4.00 - 4.99","3.00 - 3.99", "2.00 - 2.99", "1.50 - 1.99", "1.00 - 1.49", "0.90 - 0.99", "0.70 - 0.89", "0.50 - 0.69", "0.40 - 0.49", "0.30 - 0.39", "0.23 - 0.29", "0.18 - 0.22", "0.15 - 0.17", "0.08 - 0.14", "0.04 - 0.07", "0.01 - 0.03"]
                            color_seq = ["D", "E", "F", "G", "H", "I", "J", "K", "L", "M","N","FANCY"]
                            purity_seq = ['FL','IF','VVS1','VVS2','VS1','VS2','SI1','SI2']
                            data_frame['Size'] = data_frame['WGT'].apply(lambda x: '0.01-0.03' if x <= 0.03 else
                                                    '0.04 - 0.07' if x <= 0.07 else
                                                    '0.08 - 0.14' if x <= 0.14 else
                                                    '0.15 - 0.17' if x <= 0.17 else
                                                    '0.18 - 0.22' if x <= 0.22 else
                                                    '0.23 - 0.29' if x <= 0.29 else
                                                    '0.30 - 0.39' if x <= 0.39 else
                                                    '0.40 - 0.49' if x <= 0.49 else
                                                    '0.50 - 0.69' if x <= 0.69 else
                                                    '0.70 - 0.89' if x <= 0.89 else
                                                    '0.90 - 0.99' if x <= 0.99 else
                                                    '1.00 - 1.49' if x <= 1.49 else
                                                    '1.50 - 1.99' if x <= 1.99 else
                                                    '2.00 - 2.99' if x <= 2.99 else
                                                    '3.00 - 3.99' if x <= 3.99 else
                                                    '4.00 - 4.99' if x <= 4.99 else
                                                    '5.00 - 99.99')
                            data_frame = data_frame.loc[(data_frame["COLOR_A"].isin(color_seq))]
                            data_frame = data_frame.loc[(data_frame["PURITY_A"].isin(purity_seq))]
                            df4 = pd.pivot_table(data=data_frame, index=['Size','COLOR_A'],
                                                        columns=['PURITY_A'],
                                                        values='PACKET_NO',
                                                        aggfunc={'PACKET_NO': 'count'},
                                                        fill_value=0,
                                                        margins=False).reset_index()
                            
                            df5 = pd.pivot_table(data=data_frame, index=['Size','COLOR_A'],
                                                        columns=['PURITY_A'],
                                                        values='SALE_DAYS',
                                                        aggfunc={'SALE_DAYS': 'mean'},
                                                        fill_value=0,
                                                        margins=False).reset_index()
                          
                            table_head = """<tr><th class="table_head"> </th><th class="table_head">FL</th><th class="table_head">IF</th><th class="table_head">VVS1</th><th class="table_head">VVS2</th><th class="table_head">VS1</th><th class="table_head">VS2</th><th class="table_head">SI1</th><th class="table_head">SI2</th></tr>"""
                            table_rows = []
                            for size_t in range_seq:
                                # if size_t in data_frame['Band'].unique():
                                t = data_frame.loc[(data_frame['Size']==str(size_t))]
                                total = sum(t['count'])
                                
                                range_head_str = """<tr><th class="table_header" colspan="5">%s</th><th class="table_header" colspan="2">Total:</th><th class"table_header" colspan="2">%s</th></tr>""" % (''.join(str(size_t)),total)
                                
                                col_row=[]
                                for color_t in color_seq:
                                    table_data = []
                                    col_data = '<td class="table_head">%s</td>' % ''.join(str(color_t))
                                    for purity_t in purity_seq:
                                        temp_d = df4.loc[((df4['Size']==str(size_t)) & (df4['COLOR_A']==str(color_t)))]
                                        temp_days = df5.loc[(df5['Size']==str(size_t))]
                                        temp_days = temp_days.loc[(temp_days['COLOR_A']==str(color_t))]
                                        try:
                                            day_col = ""
                                            try:
                                                if sum(temp_days[str(purity_t)]) <= 30:
                                                    day_col = "#63BE7B"
                                                elif sum(temp_days[str(purity_t)]) <= 60:
                                                    day_col = "#9EDAB2"
                                                elif sum(temp_days[str(purity_t)]) <= 90:
                                                    day_col = "#EFF4AA"
                                                elif sum(temp_days[str(purity_t)]) <= 120:
                                                    day_col = "#F7DB35"
                                                elif sum(temp_days[str(purity_t)]) <= 150:
                                                    day_col = "#F99F67"
                                                else:
                                                    day_col = "#F77525"
                                            except:
                                                day_col = "#FFFFFF"
                                            try:
                                                if sum(temp_days[str(purity_t)]) == 0:
                                                    table_data.append('<td class="table_data_style">%s</td>' % " ")
                                                else:
                                                    table_data.append('<td class="table_data_style" style="background-color:%s;">%s</td>' % (day_col, sum(temp_d[str(purity_t)])))
                                            except:
                                                table_data.append('<td class="table_data_style">%s</td>' % " ")
                                        except:
                                            table_data.append('<td class="table_data_style">%s</td>' % " ")
                                    col_row.append(str("<tr>%s%s</tr>" % (''.join(col_data),''.join(table_data))))
                                table_rows.append("%s%s%s" % (''.join(range_head_str),''.join(table_head),''.join(col_row)))
                                # else:
                                #     range_head_str = """<tr><th class="table_header" colspan="5">%s</th><th class="table_header" colspan="2">Total:</th><th class"table_header" colspan="2">0</th></tr>""" % (''.join(str(size_t)))
                                #     col_row=[]
                                #     for color_t in color_seq:
                                #         table_data = []
                                #         col_data = '<td class="table_head">%s</td>' % ''.join(str(color_t))
                                #         for purity_t in purity_seq:
                                #             table_data.append('<td class="table_data_style">%s</td>' % " ")
                                #         col_row.append(str("<tr>%s%s</tr>" % (''.join(col_data),''.join(table_data))))
                                #     table_rows.append("%s%s%s" % (''.join(range_head_str),''.join(table_head),''.join(col_row)))
                            # margin: 1px 1px 1px 1px;
                            st.markdown("""
                                        <style>
                                            .table_1 {
                                                width:100%; 
                                                }
                                            .table_header{
                                                text-align: center;
                                                font-weight: bold;
                                                font-size: 12px;
                                                padding: 0.5px;
                                            }
                                            .table_head{
                                                text-align: center;
                                                font-weight: bold;
                                                font-size: 12px;
                                                padding: 0.5px;
                                            }
                                            .table_data_style{
                                                text-align: center;
                                                font-size: 12px;
                                                font-weight: bold;
                                                padding: 0.5px;
                                            }
                                            td, th{
                                                width: 0%;
                                            }
                                            tr{
                                                height: 12px;
                                            }
                                            tr:nth-child(even) {background-color: #f2f2f2;}
                                        </style>
                                        """, unsafe_allow_html=True)
                            
                            table_html_string = """
                                        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                                        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                                        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                                        <table class="table-borderless table-responsive card-1 p-4">%s</table> """ % ''.join(str(table_rows))
                            st.markdown((((''.join(table_html_string).replace("'","")).replace(",","")).replace("[","")).replace("]",""), unsafe_allow_html=True)

                        def get_tradescreen_formate(data_frame, type_fun, comp_fun):
                            """ create tradescreen formte by using html code with two diffrent formate one for group and detailed
                            
                                Args:
                                    data_frame (pandas.DataFrame): data frame to be converted into tradescreen format
                                    type_fun (str): type of the data Record
                                    comp_fun (int): comparison of the data frame
                            """
                            
                            st.markdown("<h3 style='text-align: center;'>Company %s</h3>" % comp_fun, unsafe_allow_html=True)
                            data_frame = data_frame.loc[(data_frame["COMP_NO"]==comp_fun)]
                            data_frame = data_frame.loc[(data_frame["TYPE"]==type_fun)]

                            data_frame['LAB1']=data_frame['X_LAB'].apply(lambda x: 1 if x=="GIA" else 2)

                            data_frame.sort_values(by=['PACKET_NO', 'LAB1'])
                            data_frame = data_frame.drop_duplicates(subset=['PACKET_NO', 'TYPE'])

                            data_frame.drop(['LAB1'], axis=1)

                            range_seq = ["5.00 - 99.99","4.00 - 4.99","3.00 - 3.99", "2.00 - 2.99", "1.50 - 1.99", "1.00 - 1.49", "0.90 - 0.99", "0.70 - 0.89", "0.50 - 0.69", "0.40 - 0.49", "0.30 - 0.39", "0.23 - 0.29", "0.18 - 0.22", "0.15 - 0.17", "0.08 - 0.14", "0.04 - 0.07", "0.01 - 0.03"]
                            color_seq = ["D", "E", "F", "G", "H", "I", "J", "K", "L", "M","N","FANCY"]
                            purity_seq = ['FL','IF','VVS1','VVS2','VS1','VS2','SI1','SI2']
                            data_frame['Size'] = data_frame['WGT'].apply(lambda x: '0.01-0.03' if x <= 0.03 else
                                                    '0.04 - 0.07' if x <= 0.07 else
                                                    '0.08 - 0.14' if x <= 0.14 else
                                                    '0.15 - 0.17' if x <= 0.17 else
                                                    '0.18 - 0.22' if x <= 0.22 else
                                                    '0.23 - 0.29' if x <= 0.29 else
                                                    '0.30 - 0.39' if x <= 0.39 else
                                                    '0.40 - 0.49' if x <= 0.49 else
                                                    '0.50 - 0.69' if x <= 0.69 else
                                                    '0.70 - 0.89' if x <= 0.89 else
                                                    '0.90 - 0.99' if x <= 0.99 else
                                                    '1.00 - 1.49' if x <= 1.49 else
                                                    '1.50 - 1.99' if x <= 1.99 else
                                                    '2.00 - 2.99' if x <= 2.99 else
                                                    '3.00 - 3.99' if x <= 3.99 else
                                                    '4.00 - 4.99' if x <= 4.99 else
                                                    '5.00 - 99.99')
                            data_frame = data_frame.loc[(data_frame["COLOR_A"].isin(color_seq))]
                            data_frame = data_frame.loc[(data_frame["PURITY_A"].isin(purity_seq))]
                            
                            def get_pivot_for_data(df,agg_type,agg_val):
                                """create synamic pivot table acording to parametor
                                    
                                    Args:
                                        df (pandas.DataFrame): data frame to be converted into pivot table
                                        agg_type (str): type of the aggregation
                                        agg_val (str): value of the aggregation
                                """
                                return_data = df.pivot_table(index=["Size","COLOR_A"], 
                                        columns="PURITY_A", 
                                        values=agg_val,
                                        aggfunc={agg_val: agg_type},
                                        fill_value=0,
                                        margins=False).reset_index()
                                return return_data
                            
                            st.markdown("""
                                        <style>
                                            .table_1 {
                                                width:100%; 
                                                }
                                            .table_header{
                                                text-align: center;
                                                font-weight: bold;
                                                background-color: #287E8F;
                                                color: #FFFFFF;
                                                font-size: 14px;
                                            }
                                            .sub_total{
                                                text-align: center;
                                                font-weight: bold;
                                                font-size: 14px;
                                                background-color: #B8CCE4;
                                            }
                                            .table_head{
                                                text-align: center;
                                                font-weight: bold;
                                                font-size: 14px;
                                            }
                                            .table_data_style{
                                                text-align: center;
                                                font-size: 14px;
                                            }
                                            td, th{
                                                width: 1%;
                                            }
                                            tr{
                                                height: 12px;
                                            }
                                            tr:nth-child(even) {background-color: #f2f2f2;}
                                        </style>
                                        """, unsafe_allow_html=True)

                            table_head = """<tr><th class="table_head"> </th><th class="table_head">FL</th><th class="table_head">IF</th><th class="table_head">VVS1</th><th class="table_head">VVS2</th><th class="table_head">VS1</th><th class="table_head">VS2</th><th class="table_head">SI1</th><th class="table_head">SI2</th></tr>"""
                            table_rows = []
                            min_price_data = get_pivot_for_data(data_frame,"min","NET_RATE")
                            max_price_data = get_pivot_for_data(data_frame,"max","NET_RATE")
                            max_disc_data = get_pivot_for_data(data_frame,"max","DISC_PER")
                            min_disc_data = get_pivot_for_data(data_frame,"min","DISC_PER")
                            mean_val_data = get_pivot_for_data(data_frame,"mean","NET_RATE")
                            count_val_data = get_pivot_for_data(data_frame,"count","PACKET_NO")
                            total_val_data = get_pivot_for_data(data_frame,"sum","Net Value")
                            total_crt_data = get_pivot_for_data(data_frame,"sum","WGT")
                            for size_t in range_seq:
                                # if size_t in data_frame['Band'].unique():
                                t = data_frame.loc[(data_frame['Size']==str(size_t))]
                                total = sum(t['count'])
                                
                                # range_header_str = """<tr><td class="table_header" colspan="9">%s</td></tr>""" % (''.join(str(size_t)))
                                range_head_str = """<tr><td class="table_header" colspan="5">%s</td><td class="table_header" colspan="2">Total:</td><td class="table_header" colspan="2">%s</td></tr>""" % (''.join(str(size_t)),str(total))
                                
                                col_row=[]
                                for color_t in color_seq:
                                    table_data = []
                                    col_data = '<td class="table_head">%s</td>' % ''.join(str(color_t))
                                    for purity_t in purity_seq:
                                        min_price = min_price_data.loc[((min_price_data['Size']==str(size_t)) & (min_price_data['COLOR_A']==str(color_t)))]
                                        max_price = max_price_data.loc[((max_price_data['Size']==str(size_t)) & (max_price_data['COLOR_A']==str(color_t)))]
                                        max_disc = max_disc_data.loc[((max_disc_data['Size']==str(size_t)) & (max_disc_data['COLOR_A']==str(color_t)))]
                                        min_disc = min_disc_data.loc[((min_disc_data['Size']==str(size_t)) & (min_disc_data['COLOR_A']==str(color_t)))]
                                        mean_rate = mean_val_data.loc[((mean_val_data['Size']==str(size_t)) & (mean_val_data['COLOR_A']==str(color_t)))]
                                        count_val = count_val_data.loc[((count_val_data['Size']==str(size_t)) & (count_val_data['COLOR_A']==str(color_t)))]
                                        total_val = total_val_data.loc[((total_val_data['Size']==str(size_t)) & (total_val_data['COLOR_A']==str(color_t)))]
                                        total_crt = total_crt_data.loc[((total_crt_data['Size']==str(size_t)) & (total_crt_data['COLOR_A']==str(color_t)))]
                                        
                                        if sum(mean_rate[str(purity_t)])>0:
                                            try:
                                                table_data.append('<td class="table_data_style">$%s <span style="color:rgb(99, 190, 123);">%s</span></br>$%s <span style="color:rgb(99, 190, 123);">%s</span></br>$%s/%s</br>$%s/%s</td>' % (round(sum(min_price[str(purity_t)])), str(str(sum(min_disc[str(purity_t)])) + "%"), round(sum(max_price[str(purity_t)])), str(str(sum(max_disc[str(purity_t)])) + "%"), round(sum(mean_rate[str(purity_t)])), sum(count_val[str(purity_t)]),round(sum(total_val[str(purity_t)])),round(sum(total_crt[str(purity_t)]),2)))
                                            except:
                                                table_data.append('<td class="table_data_style">%s</td>' % " ")
                                        else:
                                            table_data.append('<td class="table_data_style">%s</td>' % " ")
                                    col_row.append(str("<tr>%s%s</tr>" % (''.join(col_data),''.join(table_data))))
                                table_rows.append("""%s%s%s""" % (''.join(range_head_str),''.join(table_head),''.join(col_row)))
                            
                            table_html_string = """
                                        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                                        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                                        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                                        <table class="table-borderless table-responsive card-1 p-4">%s</table> """ % ''.join(str(table_rows))
                            st.markdown((((''.join(table_html_string).replace("'","")).replace(",","")).replace("[","")).replace("]",""), unsafe_allow_html=True)

                        def get_sticky(selected_lab, selected_shape, selected_band, selected_color, selected_purity, selected_fls, selected_polish,selected_cut,selected_symm):
                            """ to show stiky at bottom of screen this stiky have all filter which are perform in main data
                                
                                Args:
                                    selected_lab (str): selected lab
                                    selected_shape (str): selected shape
                                    selected_band (str): selected band
                                    selected_color (str): selected color
                                    selected_purity (str): selected purity
                                    selected_fls (str): selected fls
                                    selected_polish (str): selected polish
                                    selected_cut (str): selected cut
                                    selected_symm (str): selected symmetry
                            """
                            
                            filter_text_list = []

                            if len(selected_lab) != len(final_lab):
                                filter_text_list.append("""<span class="bold_text">Lab: </span><span class="white_col">%s.</span>""" % " , ".join(selected_lab))
                            if len(selected_shape) != len(final_shape):
                                filter_text_list.append("""<span class="bold_text">Shape: </span><span class="white_col">%s.</span>""" % " , ".join(selected_shape))
                            if len(selected_band) != len(final_range):
                                filter_text_list.append("""<span class="bold_text">Size: </span><span class="white_col">%s.</span>""" % " , ".join(selected_band))
                            if len(selected_color) != len(final_color):
                                filter_text_list.append("""<span class="bold_text">Color: </span><span class="white_col">%s.</span>""" % " , ".join(selected_color))
                            if len(selected_purity) != len(final_purity):
                                filter_text_list.append("""<span class="bold_text">Purity: </span><span class="white_col">%s.</span>""" % " , ".join(selected_purity))
                            if len(selected_fls) != len(final_fls):
                                filter_text_list.append("""<span class="bold_text">FLS: </span><span class="white_col">%s.</span>""" % " , ".join(selected_fls))
                            if len(selected_polish) != len(final_polish):
                                filter_text_list.append("""<span class="bold_text">Polish: </span><span class="white_col">%s.</span>""" % " , ".join(selected_polish))
                            if len(selected_cut) != len(final_cut):
                                filter_text_list.append("""<span class="bold_text">CUT: </span><span class="white_col">%s.</span>""" % " , ".join(selected_cut))
                            if len(selected_symm) != len(final_symm):
                                filter_text_list.append("""<span class="bold_text">SYMM: </span><span class="white_col">%s.</span>""" % " , ".join(selected_symm))

                            if len(filter_text_list)>0:
                                # table_data = """<tr><td style="background-color: #63BE7B;"><=30</td></tr>
                                                        # <tr><td style="background-color: #9EDAB2;"><=60</td></tr>
                                                        # <tr><td style="background-color: #EFF4AA;"><=90</td></tr>
                                                        # <tr><td style="background-color: #F7DB35;"><=120</td></tr>
                                                        # <tr><td style="background-color: #F99F67;"><=150</td></tr>
                                                        # <tr><td style="background-color: #F77525;">150+</td></tr>"""
                                st.markdown("""
                                        <style>
                                            div.sticky {
                                                position: fixed;
                                                bottom: 0;
                                                left: 0;
                                                width: 100%;
                                                height: 50px;
                                                }
                                            .div_bg{
                                                padding: 5px;
                                                background-color: #287E8F;
                                                border-radius: 10px;
                                            }
                                            .bold_text{
                                                font-weight: bold;
                                                color: #FFFFFF;
                                            }
                                            .white_col{
                                                color: #FFFFFF;
                                            }
                                            </style>
                                    """, unsafe_allow_html=True)
                                table_html_string = """
                                            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                                            <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                                            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                                            <div class="sticky div_bg">%s</div>""" % ''.join(str(filter_text_list))
                                filter_text_list = []
                                st.markdown(((''.join(table_html_string).replace("'","")).replace("[","")).replace("]",""), unsafe_allow_html=True)

                        def get_rap_formate(df,for_selected_type):
                            """ return rap formated pivot data table of given data in df perameter

                                Args:
                                    df (pd.DataFrame): data frame to be converted to rap format
                                    for_selected_type (str): type of data to be selected from df
                            """
                            
                            if for_selected_type=="Net Value":
                                for_selected_type = "NET_VALUE"
                            
                            col_type = "COLOR_A"
                            clar_type = "PURITY"

                            df.groupby([clar_type, 'Band', col_type])[[str(for_selected_type)]].sum()
                            
                            df4 = pd.pivot_table(data=df, index=['Band',col_type],
                                                    columns=[clar_type],
                                                    values=for_selected_type,
                                                    aggfunc={for_selected_type: for_aggfunc},
                                                    fill_value=0,
                                                    margins=False).reset_index()
                            
                            pass
                        
                        #  ======================== this bloc for create output as user selected report type ========================
                        if selected_report_type == "Sale/New Arrival Report":

                            selected_chart_comp,selected_chart_comp2,selected_mode,selected_type = treand_report_selection()
                            for_head_print_type,for_selected_type,for_aggfunc = print_type(selected_type)
                            expander_col1,expander_col2,expander_col3 = expander1.columns([1,2,2])
                            if expander_col1.button("View Report"):
                                print(str(str(datetime.today().replace(microsecond=0)) + " | " + str(local_ip) + " | " + str(selected_report_type)))
                                log(selected_report_type,selected_start_date,selected_end_date,selected_shape,selected_color,selected_purity,selected_fls,selected_band,f'Company: {selected_chart_comp}, Mod: {selected_mode}, Type: {selected_type}')
                                create_db_log(selected_report_type,selected_start_date,selected_end_date,selected_shape,selected_color,selected_purity,selected_fls,selected_band, selected_chart_comp, selected_chart_comp2, selected_mode, selected_type, selected_lab,None,None,None,None,None,None,None,None,None,None,None,None,local_ip)
                                mode = report_mode(selected_mode)
                                
                                # FILTER DATA BY USER SELECTED
                                temp_data = filter_data_with_user_selected(df3, selected_lab, selected_shape, selected_band, selected_color, selected_purity, selected_fls, selected_polish,selected_cut,selected_symm)
                                
                                df1 = get_sorted_data_frane(mode,temp_data,for_selected_type,for_aggfunc,selected_from_year,selected_from_data_range,selected_data_range,selected_year)
                                
                                try:
                                    if selected_chart_comp == selected_chart_comp2:
                                        st.warning("Please Select Different Company.")
                                    elif selected_chart_comp == None:
                                        get_demand_supply_chart(mode,df1,selected_chart_comp2,selected_type)
                                    elif selected_chart_comp2 == None:
                                        get_demand_supply_chart(mode,df1,selected_chart_comp,selected_type)
                                    else:
                                        col1, col2 = st.columns([1,1])
                                        with col1:
                                            get_demand_supply_chart(mode,df1,selected_chart_comp,selected_type)
                                        with col2:
                                            get_demand_supply_chart(mode,df1,selected_chart_comp2,selected_type)
                                    
                                    get_sticky(selected_lab, selected_shape, selected_band, selected_color, selected_purity, selected_fls, selected_polish,selected_cut,selected_symm)
                                    expander_col2.markdown("<br/>", unsafe_allow_html=True)
                                    expander_col2.markdown(str('<div style="text-align-last: end; font-weight: bold; padding-bottom:0; margin-bottom: 0;">Report Generated At: ' + str(datetime.today().replace(microsecond=0)) + '</div>'), unsafe_allow_html=True)
                                    expander_col3.markdown("<br/>", unsafe_allow_html=True)
                                    expander_col3.markdown(str('<div style="text-align-last: end; font-weight: bold; padding-bottom:0; margin-bottom: 0;">Last Updated: ' + str(list(temp_data['last_updated'].unique())[0]) + '</div>'), unsafe_allow_html=True)
                                except:
                                    st.error("Data Filter is Missing.....")
                                del selected_chart_comp,selected_mode,selected_type,for_selected_type,for_aggfunc,for_head_print_type
                        elif selected_report_type == "Trend Report in %":
                            
                            selected_chart_comp,selected_chart_comp2,selected_mode,selected_type = treand_report_selection()
                            for_head_print_type,for_selected_type,for_aggfunc = print_type(selected_type)
                            expander_col1,expander_col2,expander_col3 = expander1.columns([1,2,2])
                            if expander_col1.button("View Report"):
                                print(str(str(datetime.today().replace(microsecond=0)) + " | " + str(local_ip) + " | " + str(selected_report_type)))
                                log(selected_report_type,selected_start_date,selected_end_date,selected_shape,selected_color,selected_purity,selected_fls,selected_band,f'Company: {selected_chart_comp}, Mod: {selected_mode}, Type: {selected_type}')
                                create_db_log(selected_report_type,selected_start_date,selected_end_date,selected_shape,selected_color,selected_purity,selected_fls,selected_band, selected_chart_comp, selected_chart_comp2, selected_mode, selected_type, selected_lab,None,None,None,None,None,None,None,None,None,None,None,None,local_ip)                            
                                mode = report_mode(selected_mode)
                                
                                # FILTER DATA BY USER SELECTED
                                temp_data = filter_data_with_user_selected(df3, selected_lab, selected_shape, selected_band, selected_color, selected_purity, selected_fls, selected_polish,selected_cut,selected_symm)

                                df1 = get_sorted_data_frane(mode,temp_data,for_selected_type,for_aggfunc,selected_from_year,selected_from_data_range,selected_data_range,selected_year)
                                
                                try:
                                    if selected_chart_comp == selected_chart_comp2:
                                        st.warning("Please Selecte Different Comapany.")
                                    elif selected_chart_comp == None:
                                        get_trend_chart(mode,df1,selected_chart_comp2, selected_type)
                                    elif selected_chart_comp2 == None:
                                        get_trend_chart(mode,df1,selected_chart_comp, selected_type)
                                    else:
                                        col1, col2 = st.columns([1,1])
                                        with col1:
                                            get_trend_chart(mode,df1,selected_chart_comp, selected_type)
                                        with col2:
                                            get_trend_chart(mode,df1,selected_chart_comp2, selected_type)
                                    
                                    get_sticky(selected_lab, selected_shape, selected_band, selected_color, selected_purity, selected_fls, selected_polish,selected_cut,selected_symm)
                                    expander_col2.markdown("<br/>", unsafe_allow_html=True)
                                    expander_col2.markdown(str('<div style="text-align-last: end; font-weight: bold; padding-bottom:0; margin-bottom: 0;">Report Generated At: ' + str(datetime.today().replace(microsecond=0)) + '</div>'), unsafe_allow_html=True)
                                    expander_col3.markdown("<br/>", unsafe_allow_html=True)
                                    expander_col3.markdown(str('<div style="text-align-last: end; font-weight: bold; padding-bottom:0; margin-bottom: 0;">Last Updated: ' + str(list(temp_data['last_updated'].unique())[0]) + '</div>'), unsafe_allow_html=True)
                                except:
                                    st.error("Data Filter is Missing.....")
                                del selected_chart_comp,selected_mode,selected_type,for_head_print_type,for_selected_type,for_aggfunc,temp_data,df1
                                # else:
                                #     st.error("Data Filter is Missing.....")
                        elif selected_report_type == "Heat Map of PPC Report":
                            
                            selected_chart_comp,selected_chart_comp2,selected_chart_band = heat_report_selection()
                            st.markdown("<h3 style='text-align: center;'>Heat Map Of PPC</h3>", unsafe_allow_html=True)
                            
                            expander_col1,expander_col2,expander_col3 = expander1.columns([1,2,2])
                            if expander_col1.button("View Report"):
                                print(str(str(datetime.today().replace(microsecond=0)) + " | " + str(local_ip) + " | " + str(selected_report_type)))
                                log(selected_report_type,selected_start_date,selected_end_date,selected_shape,selected_color,selected_purity,selected_fls,selected_band,f'Company: {selected_chart_comp}')
                                create_db_log(selected_report_type,selected_start_date,selected_end_date,selected_shape,selected_color,selected_purity,selected_fls,selected_band, selected_chart_comp, selected_chart_comp2, None, None, selected_lab,None,None,None,None,None,None,None,None,None,selected_chart_band,None,None,local_ip)
                                # FILTER DATA BY USER SELECTED
                                temp_data = filter_data_with_user_selected(df3, selected_lab, selected_shape, selected_band, selected_color, selected_purity, selected_fls, selected_polish,selected_cut,selected_symm)

                                try:
                                    if selected_chart_comp == selected_chart_comp2:
                                        st.warning("Please Selecte Different Comapany.")
                                    elif selected_chart_comp == None:
                                        df1=temp_data[temp_data['COMP_NO']==selected_chart_comp2]
                                        get_heat_map(df1,selected_chart_band,selected_chart_comp2)
                                    elif selected_chart_comp2 == None:
                                        df2=temp_data[temp_data['COMP_NO']==selected_chart_comp]
                                        get_heat_map(df2,selected_chart_band,selected_chart_comp)
                                    else:
                                        col1, col2 = st.columns([1,1])
                                        with col1:
                                            if selected_chart_comp == "Manufacturing":
                                                cno_1 = temp_data[temp_data['COMP_NO']==1]
                                                cno_2 = temp_data[temp_data['COMP_NO']==2]
                                                cno_7 = temp_data[temp_data['COMP_NO']==7]
                                                cno_9 = temp_data[temp_data['COMP_NO']==9]

                                                df1 = pd.concat([cno_1, cno_2, cno_7, cno_9])
                                                df1['COMP_NO']="Manufacturing"
                                            else:
                                                df1 = temp_data[temp_data['COMP_NO']==selected_chart_comp]
                                            get_heat_map(df1,selected_chart_band,selected_chart_comp)
                                        with col2:
                                            if selected_chart_comp2 == "Manufacturing":
                                                cno_1 = temp_data[temp_data['COMP_NO']==1]
                                                cno_2 = temp_data[temp_data['COMP_NO']==2]
                                                cno_7 = temp_data[temp_data['COMP_NO']==7]
                                                cno_9 = temp_data[temp_data['COMP_NO']==9]
                                                df2 = pd.concat([cno_1, cno_2, cno_7, cno_9])
                                                df2['COMP_NO']="Manufacturing"
                                            else:
                                                df2 = temp_data[temp_data['COMP_NO']==selected_chart_comp2]
                                            get_heat_map(df2,selected_chart_band,selected_chart_comp2)
                                    
                                    get_sticky(selected_lab, selected_shape, selected_band, selected_color, selected_purity, selected_fls, selected_polish,selected_cut,selected_symm)
                                    
                                    expander_col2.markdown("<br/>", unsafe_allow_html=True)
                                    expander_col2.markdown(str('<div style="text-align-last: end; font-weight: bold; padding-bottom:0; margin-bottom: 0;">Report Generated At: ' + str(datetime.today().replace(microsecond=0)) + '</div>'), unsafe_allow_html=True)
                                    expander_col3.markdown("<br/>", unsafe_allow_html=True)
                                    expander_col3.markdown(str('<div style="text-align-last: end; font-weight: bold; padding-bottom:0; margin-bottom: 0;">Last Updated: ' + str(list(temp_data['last_updated'].unique())[0]) + '</div>'), unsafe_allow_html=True)
                                except:
                                    st.error("Data Filter is Missing.....")
                        elif selected_report_type == "Sale Comparison Report":
                            
                            selected_mode,selected_status = buble_report_without_comp()
                            expander_col1,expander_col2,expander_col3 = expander1.columns([1,2,2])
                            if expander_col1.button("View Report"):
                                print(str(str(datetime.today().replace(microsecond=0)) + " | " + str(local_ip) + " | " + str(selected_report_type)))
                                log(selected_report_type,selected_start_date,selected_end_date,selected_shape,selected_color,selected_purity,selected_fls,selected_band,f'Mod: {selected_mode}')
                                create_db_log(selected_report_type,selected_start_date,selected_end_date,selected_shape,selected_color,selected_purity,selected_fls,selected_band, None, None, selected_mode, None, selected_lab,None,None,None,None,None,None,None,None,selected_status,None,None,None,local_ip)                            
                                mode = report_mode(selected_mode)
                                
                                # FILTER DATA BY USER SELECTED
                                temp_data = filter_data_with_user_selected(df3, selected_lab, selected_shape, selected_band, selected_color, selected_purity, selected_fls, selected_polish,selected_cut,selected_symm)
                                if selected_status:
                                    try:
                                        get_buble_chart(mode,temp_data,selected_status)
                                        
                                        get_sticky(selected_lab, selected_shape, selected_band, selected_color, selected_purity, selected_fls, selected_polish,selected_cut,selected_symm)

                                        expander_col2.markdown("<br/>", unsafe_allow_html=True)
                                        expander_col2.markdown(str('<div style="text-align-last: end; font-weight: bold; padding-bottom:0; margin-bottom: 0;">Report Generated At: ' + str(datetime.today().replace(microsecond=0)) + '</div>'), unsafe_allow_html=True)
                                        expander_col3.markdown("<br/>", unsafe_allow_html=True)
                                        expander_col3.markdown(str('<div style="text-align-last: end; font-weight: bold; padding-bottom:0; margin-bottom: 0;">Last Updated: ' + str(list(temp_data['last_updated'].unique())[0]) + '</div>'), unsafe_allow_html=True)
                                    except:
                                        st.error("Data Filter is Missing.....")
                                else:
                                    st.error("Data Filter is Missing.....")
                        elif selected_report_type == "Zone Wise Sale Report":
                            selected_chart_comp,selected_type = pie_report_selection()
                            for_head_print_type,for_selected_type,for_aggfunc = print_type(selected_type)
                        
                            expander_col1,expander_col2,expander_col3 = expander1.columns([1,2,2])
                            if expander_col1.button("View Report"):
                                print(str(str(datetime.today().replace(microsecond=0)) + " | " + str(local_ip) + " | " + str(selected_report_type)))
                                log(selected_report_type,selected_start_date,selected_end_date,selected_shape,selected_color,selected_purity,selected_fls,selected_band,f"Company: {selected_chart_comp}, Type: '{selected_type}'")
                                create_db_log(selected_report_type,selected_start_date,selected_end_date,selected_shape,selected_color,selected_purity,selected_fls,selected_band, selected_chart_comp, None, None, selected_type, selected_lab,None,None,None,None,None,None,None,None,None,None,None,None,local_ip)
                                # FILTER DATA BY USER SELECTED
                                temp_data = filter_data_with_user_selected(df3, selected_lab, selected_shape, selected_band, selected_color, selected_purity, selected_fls, selected_polish,selected_cut,selected_symm)

                                try:
                                    get_pie_chart(for_selected_type,temp_data,for_aggfunc,selected_chart_comp)
                                    
                                    get_sticky(selected_lab, selected_shape, selected_band, selected_color, selected_purity, selected_fls, selected_polish,selected_cut,selected_symm)

                                    expander_col2.markdown("<br/>", unsafe_allow_html=True)
                                    expander_col2.markdown(str('<div style="text-align-last: end; font-weight: bold; padding-bottom:0; margin-bottom: 0;">Report Generated At: ' + str(datetime.today().replace(microsecond=0)) + '</div>'), unsafe_allow_html=True)
                                    expander_col3.markdown("<br/>", unsafe_allow_html=True)
                                    expander_col3.markdown(str('<div style="text-align-last: end; font-weight: bold; padding-bottom:0; margin-bottom: 0;">Last Updated: ' + str(list(temp_data['last_updated'].unique())[0]) + '</div>'), unsafe_allow_html=True)

                                except:
                                    st.error("Data Filter is Missing.....")
                        elif selected_report_type == "Sale Percentage Report":
                            
                            selected_chart_comp,selected_chart_comp2,selected_type,selected_perms = report_selection_with_two_comp()
                            for_head_print_type,for_selected_type,for_aggfunc = print_type(selected_type)

                            expander_col1,expander_col2,expander_col3 = expander1.columns([1,2,2])
                            if expander_col1.button("View Report"):
                                print(str(str(datetime.today().replace(microsecond=0)) + " | " + str(local_ip) + " | " + str(selected_report_type)))
                                log(selected_report_type,selected_start_date,selected_end_date,selected_shape,selected_color,selected_purity,selected_fls,selected_band,f"Company-1: {selected_chart_comp}, Company-2: {selected_chart_comp2}, Type: '{selected_type}'")
                                create_db_log(selected_report_type,selected_start_date,selected_end_date,selected_shape,selected_color,selected_purity,selected_fls,selected_band, selected_chart_comp, selected_chart_comp2, None, selected_type, selected_lab,None,None,None,None,None,selected_perms,None,None,None,None,None,None,local_ip)                            
                                try:
                                    get_shape_wise_Comparison_chart(for_selected_type,df3,for_aggfunc,selected_chart_comp,selected_chart_comp2,selected_perms)
                                    
                                    get_sticky(selected_lab, selected_shape, selected_band, selected_color, selected_purity, selected_fls, selected_polish,selected_cut,selected_symm)
                                    expander_col2.markdown("<br/>", unsafe_allow_html=True)
                                    expander_col2.markdown(str('<div style="text-align-last: end; font-weight: bold; padding-bottom:0; margin-bottom: 0;">Report Generated At: ' + str(datetime.today().replace(microsecond=0)) + '</div>'), unsafe_allow_html=True)
                                    expander_col3.markdown("<br/>", unsafe_allow_html=True)
                                    expander_col3.markdown(str('<div style="text-align-last: end; font-weight: bold; padding-bottom:0; margin-bottom: 0;">Last Updated: ' + str(list(df3['last_updated'].unique())[0]) + '</div>'), unsafe_allow_html=True)
                                except:
                                    st.error("Data Filter is Missing.....")
                        elif selected_report_type == "Sale Proportion Report":
                            
                            selected_chart_comp,selected_chart_comp2,selected_type,selected_perms = report_selection_with_two_comp()
                            for_head_print_type,for_selected_type,for_aggfunc = print_type(selected_type)
                            
                            expander_col1,expander_col2,expander_col3 = expander1.columns([1,2,2])
                            if expander_col1.button("View Report"):
                                print(str(str(datetime.today().replace(microsecond=0)) + " | " + str(local_ip) + " | " + str(selected_report_type)))
                                log(selected_report_type,selected_start_date,selected_end_date,selected_shape,selected_color,selected_purity,selected_fls,selected_band,f"Company-1: {selected_chart_comp}, Company-2: {selected_chart_comp2}, Type: '{selected_type}'")
                                create_db_log(selected_report_type,selected_start_date,selected_end_date,selected_shape,selected_color,selected_purity,selected_fls,selected_band, selected_chart_comp, selected_chart_comp2, None, selected_type, selected_lab,None,None,None,None,None,selected_perms,None,None,None,None,None,None,local_ip)
                                # FILTER DATA BY USER SELECTED
                                filter_data_with_user_selected.clear()
                                try:
                                    get_shape_wise_proportion_chart(for_selected_type,df3,for_aggfunc,selected_chart_comp,selected_chart_comp2,selected_perms,selected_type)
                                    
                                    get_sticky(selected_lab, selected_shape, selected_band, selected_color, selected_purity, selected_fls, selected_polish,selected_cut,selected_symm)
                                    expander_col2.markdown("<br/>", unsafe_allow_html=True)
                                    expander_col2.markdown(str('<div style="text-align-last: end; font-weight: bold; padding-bottom:0; margin-bottom: 0;">Report Generated At: ' + str(datetime.today().replace(microsecond=0)) + '</div>'), unsafe_allow_html=True)
                                    expander_col3.markdown("<br/>", unsafe_allow_html=True)
                                    expander_col3.markdown(str('<div style="text-align-last: end; font-weight: bold; padding-bottom:0; margin-bottom: 0;">Last Updated: ' + str(list(df3['last_updated'].unique())[0]) + '</div>'), unsafe_allow_html=True)
                                except:
                                    st.error("Data Filter is Missing.....")
                        elif selected_report_type == "Import Report":
                            
                            # Brief Import Export Report
                            selected_mode,selected_type = report_without_comp()
                            for_head_print_type,for_selected_type,for_aggfunc = print_type(selected_type)
                            
                            expander_col1,expander_col2,expander_col3 = expander1.columns([1,2,2])
                            if expander_col1.button("View Report"):
                                print(str(str(datetime.today().replace(microsecond=0)) + " | " + str(local_ip) + " | " + str(selected_report_type)))
                                log(selected_report_type,selected_start_date,selected_end_date,selected_shape,selected_color,selected_purity,selected_fls,selected_band,f'Mod: {selected_mode}, Type: {selected_type}')
                                create_db_log(selected_report_type,selected_start_date,selected_end_date,selected_shape,selected_color,selected_purity,selected_fls,selected_band, None, None, selected_mode, selected_type, selected_lab,None,None,None,None,None,None,None,None,None,None,None,None,local_ip)
                                mode = report_mode(selected_mode)

                                # FILTER DATA BY USER SELECTED
                                temp_data = filter_data_with_user_selected(df3, selected_lab, selected_shape, selected_band, selected_color, selected_purity, selected_fls, selected_polish,selected_cut,selected_symm)
                                
                                df1 = get_sorted_data_frane(mode,temp_data,for_selected_type,for_aggfunc,selected_from_year,selected_from_data_range,selected_data_range,selected_year)
                                
                                try:
                                    get_table_of_data(df1,selected_mode,selected_companys_to_load_data)

                                    get_sticky(selected_lab, selected_shape, selected_band, selected_color, selected_purity, selected_fls, selected_polish,selected_cut,selected_symm)
                                    expander_col2.markdown("<br/>", unsafe_allow_html=True)
                                    expander_col2.markdown(str('<div style="text-align-last: end; font-weight: bold; padding-bottom:0; margin-bottom: 0;">Report Generated At: ' + str(datetime.today().replace(microsecond=0)) + '</div>'), unsafe_allow_html=True)
                                    expander_col3.markdown("<br/>", unsafe_allow_html=True)
                                    expander_col3.markdown(str('<div style="text-align-last: end; font-weight: bold; padding-bottom:0; margin-bottom: 0;">Last Updated: ' + str(list(temp_data['last_updated'].unique())[0]) + '</div>'), unsafe_allow_html=True)
                                except:
                                    st.error("Data Filter is Missing.....")
                        elif selected_report_type == "InFlow OutFlow Report":
                            # SELECT Chart Type
                            selected_chart = expander1.selectbox("SELECT Report", ("InFlow-OutFlow", "Parameter wise InFlow-OutFlow"))
                            
                            month_list_for_inflow_outflow = list(set(df3['Month'].unique()))
                            
                            if selected_chart == "Parameter wise InFlow-OutFlow":
                                selected_chart_comp,selected_chart_comp2,selected_type,selected_perms,selected_shape1,inflow_outflow_month = inflow_outflow_report_selection(selected_chart,month_list_for_inflow_outflow)
                                create_db_log(selected_report_type,selected_start_date,selected_end_date,selected_shape,selected_color,selected_purity,selected_fls,selected_band, selected_chart_comp, selected_chart_comp2, None, selected_type, selected_lab,None,None,None,selected_chart,inflow_outflow_month,selected_perms,selected_shape1,None,None,None,None,None,local_ip)
                                if selected_perms == "TABLE_PER":
                                    name = "Table"
                                else:
                                    name = selected_perms
                            else:
                                selected_chart_comp,selected_chart_comp2,selected_type,inflow_outflow_month = inflow_outflow_report_selection(selected_chart,month_list_for_inflow_outflow)
                                create_db_log(selected_report_type,selected_start_date,selected_end_date,selected_shape,selected_color,selected_purity,selected_fls,selected_band, selected_chart_comp, selected_chart_comp2, None, selected_type, selected_lab,None,None,None,selected_chart,inflow_outflow_month,None,None,None,None,None,None,None,local_ip)
                                name = "Shape"

                            for_head_print_type,for_selected_type,for_aggfunc = print_type(selected_type)
                            
                            expander_col1,expander_col2,expander_col3 = expander1.columns([1,2,2])
                            if expander_col1.button("View Report"):
                                print(str(str(datetime.today().replace(microsecond=0)) + " | " + str(local_ip) + " | " + str(selected_report_type)))
                                log(selected_report_type,selected_start_date,selected_end_date,selected_shape,selected_color,selected_purity,selected_fls,selected_band,f"Company-1: {selected_chart_comp}, Company-2: {selected_chart_comp2}, Type: '{selected_type}'")
                                # FILTER DATA BY USER SELECTED
                                temp_data = filter_data_with_user_selected(df3, selected_lab, selected_shape, selected_band, selected_color, selected_purity, selected_fls, selected_polish,selected_cut,selected_symm)
                                if inflow_outflow_month:
                                    temp_data = temp_data[temp_data['Month'].isin(inflow_outflow_month)]
                                    
                                    try:
                                        st.markdown("<h3 style='text-align: center;'>%s wise InFlow/OutFlow Report</h3>" % name, unsafe_allow_html=True)
                                        if selected_chart == "Parameter wise InFlow-OutFlow":
                                            if selected_chart_comp == selected_chart_comp2:
                                                st.warning("Please Selecte Different Comapany.")
                                            elif selected_chart_comp == None:
                                                get_inflow_outflow(temp_data,selected_chart_comp2,for_selected_type,selected_type,selected_perms,selected_shape1)
                                            elif selected_chart_comp2 == None:
                                                get_inflow_outflow(temp_data,selected_chart_comp,for_selected_type,selected_type,selected_perms,selected_shape1)
                                            else:
                                                col1, col2 = st.columns([1,1])
                                                with col1:
                                                    get_inflow_outflow(temp_data,selected_chart_comp,for_selected_type,selected_type,selected_perms,selected_shape1)
                                                with col2:
                                                    get_inflow_outflow(temp_data,selected_chart_comp2,for_selected_type,selected_type,selected_perms,selected_shape1)
                                                
                                                get_sticky(selected_lab, selected_shape, selected_band, selected_color, selected_purity, selected_fls, selected_polish,selected_cut,selected_symm)
                                                expander_col2.markdown("<br/>", unsafe_allow_html=True)
                                                expander_col2.markdown(str('<div style="text-align-last: end; font-weight: bold; padding-bottom:0; margin-bottom: 0;">Report Generated At: ' + str(datetime.today().replace(microsecond=0)) + '</div>'), unsafe_allow_html=True)
                                                expander_col3.markdown("<br/>", unsafe_allow_html=True)
                                                expander_col3.markdown(str('<div style="text-align-last: end; font-weight: bold; padding-bottom:0; margin-bottom: 0;">Last Updated: ' + str(list(temp_data['last_updated'].unique())[0]) + '</div>'), unsafe_allow_html=True)
                                        else:
                                            if selected_chart_comp == selected_chart_comp2:
                                                st.warning("Please Selecte Different Comapany.")
                                            elif selected_chart_comp == None:
                                                get_inflow_outflow(temp_data,selected_chart_comp2,for_selected_type,selected_type,"SHAPE1")
                                            elif selected_chart_comp2 == None:
                                                get_inflow_outflow(temp_data,selected_chart_comp,for_selected_type,selected_type,"SHAPE1")
                                            else:
                                                col1, col2 = st.columns([1,1])
                                                with col1:
                                                    get_inflow_outflow(temp_data,selected_chart_comp,for_selected_type,selected_type,"SHAPE1")
                                                with col2:
                                                    get_inflow_outflow(temp_data,selected_chart_comp2,for_selected_type,selected_type,"SHAPE1")
                                            
                                            get_sticky(selected_lab, selected_shape, selected_band, selected_color, selected_purity, selected_fls, selected_polish,selected_cut,selected_symm)
                                            expander_col2.markdown("<br/>", unsafe_allow_html=True)
                                            expander_col2.markdown(str('<div style="text-align-last: end; font-weight: bold; padding-bottom:0; margin-bottom: 0;">Report Generated At: ' + str(datetime.today().replace(microsecond=0)) + '</div>'), unsafe_allow_html=True)
                                            expander_col3.markdown("<br/>", unsafe_allow_html=True)
                                            expander_col3.markdown(str('<div style="text-align-last: end; font-weight: bold; padding-bottom:0; margin-bottom: 0;">Last Updated: ' + str(list(temp_data['last_updated'].unique())[0]) + '</div>'), unsafe_allow_html=True)
                                    except:
                                        st.error("Data Filter is Missing.....")
                                else:
                                    st.error("Data Filter is Missing.....")
                            # comp1,comp2,parms,type
                        elif selected_report_type == "Shape wise Report":
                            selected_chart = expander1.selectbox("Select Report", ("Compare Two Shape", "Sale%","Compare Two Shape by Quick Sale"))
                            if selected_chart == "Sale%":
                                selected_chart_comp,selected_chart_comp2,selected_x,selected_color_1,selected_mode = sale_report()
                                expander_col1,expander_col2,expander_col3 = expander1.columns([1,2,2])
                                if expander_col1.button("View Report"):
                                    print(str(str(datetime.today().replace(microsecond=0)) + " | " + str(local_ip) + " | " + str(selected_report_type)))
                                    create_db_log(selected_report_type,selected_start_date,selected_end_date,selected_shape,selected_color,selected_purity,selected_fls,selected_band, selected_chart_comp, selected_chart_comp2, selected_mode, None, selected_lab,None,None,None,selected_chart,None,selected_color_1,None,None,None,None,None,None,local_ip)
                                    mode = report_mode(selected_mode)
                                    
                                    # FILTER DATA BY USER SELECTED
                                    temp_data = filter_data_with_user_selected(df3, selected_lab, selected_shape, selected_band, selected_color, selected_purity, selected_fls, selected_polish,selected_cut,selected_symm)
                                    try:
                                        if selected_chart_comp == selected_chart_comp2:
                                            st.warning("Please Select Different Company.")
                                        elif selected_chart_comp == None:
                                            get_sale_chart(temp_data,selected_chart_comp2,mode,selected_x,selected_color_1)
                                        elif selected_chart_comp2 == None:
                                            get_sale_chart(temp_data,selected_chart_comp,mode,selected_x,selected_color_1)
                                        else:
                                            col1, col2 = st.columns([1,1])
                                            with col1:
                                                get_sale_chart(temp_data,selected_chart_comp,mode,selected_x,selected_color_1)
                                            with col2:
                                                get_sale_chart(temp_data,selected_chart_comp2,mode,selected_x,selected_color_1)
                                        
                                        get_sticky(selected_lab, selected_shape, selected_band, selected_color, selected_purity, selected_fls, selected_polish,selected_cut,selected_symm)
                                        expander_col2.markdown("<br/>", unsafe_allow_html=True)
                                        expander_col2.markdown(str('<div style="text-align-last: end; font-weight: bold; padding-bottom:0; margin-bottom: 0;">Report Generated At: ' + str(datetime.today().replace(microsecond=0)) + '</div>'), unsafe_allow_html=True)
                                        expander_col3.markdown("<br/>", unsafe_allow_html=True)
                                        expander_col3.markdown(str('<div style="text-align-last: end; font-weight: bold; padding-bottom:0; margin-bottom: 0;">Last Updated: ' + str(list(temp_data['last_updated'].unique())[0]) + '</div>'), unsafe_allow_html=True)
                                    except:
                                        st.error("Data Filter is Missing.....")
                            elif selected_chart == "Compare Two Shape":
                                selected_chart_comp,selected_mode,selected_status,selected_shape1,selected_shape2 = shape_report()
                                expander_col1,expander_col2,expander_col3 = expander1.columns([1,2,2])
                                if expander_col1.button("View Report"):
                                    create_db_log(selected_report_type,selected_start_date,selected_end_date,selected_shape,selected_color,selected_purity,selected_fls,selected_band, selected_chart_comp, None, selected_mode, None, selected_lab,None,None,None,selected_chart,None,None,selected_shape1,selected_shape2,selected_status,None,None,None,local_ip)
                                    mode = report_mode(selected_mode)
                                    
                                    # FILTER DATA BY USER SELECTED
                                    temp_data = filter_data_with_user_selected(df3, selected_lab, selected_shape, selected_band, selected_color, selected_purity, selected_fls, selected_polish,selected_cut,selected_symm)
                                    
                                    try:
                                        if selected_shape1 == selected_shape2:
                                            st.warning("Please Selecte Different Comapany.")
                                        elif selected_shape1 == None:
                                            get_shape_chart(temp_data,selected_chart_comp,mode,selected_status,selected_shape2)
                                        elif selected_shape2 == None:
                                            get_shape_chart(temp_data,selected_chart_comp,mode,selected_status,selected_shape1)
                                        else:
                                            col1, col2 = st.columns([1,1])

                                            with col1:
                                                get_shape_chart(temp_data,selected_chart_comp,mode,selected_status,selected_shape1)
                                            with col2:
                                                get_shape_chart(temp_data,selected_chart_comp,mode,selected_status,selected_shape2)
                                    except:
                                        st.error("Data Filter is Missing.....")
                                    get_sticky(selected_lab, selected_shape, selected_band, selected_color, selected_purity, selected_fls, selected_polish,selected_cut,selected_symm)
                                    st.markdown("<br/>", unsafe_allow_html=True)
                                    with st.chat_message("User"):
                                        footer_part(list(temp_data['last_updated'].unique()),selected_lab, selected_shape, selected_band, selected_color, selected_purity, selected_fls,selected_report_type)
                            else:
                                selected_shape1,selected_shape2,selected_chart_comp = shape_report_user_inputs()
                                expander_col1,expander_col2,expander_col3 = expander1.columns([1,2,2])
                                if expander_col1.button("View Report"):

                                    def current_stock(comp_fun):
                                        monthly_collection_letest_stock = db["letest_stock"]
                                        res = monthly_collection_letest_stock.find({"COMP_NO": comp_fun})
                                        temp_new_d= pl.DataFrame(res)
                                        today_stock = temp_new_d.to_pandas()
                                        del res,temp_new_d
                                        return today_stock

                                    create_db_log(selected_report_type,selected_start_date,selected_end_date,selected_shape,selected_color,selected_purity,selected_fls,selected_band, selected_chart_comp, None, None, None, selected_lab,None,None,None,selected_chart,None,None,selected_shape1,selected_shape2,None,None,None,None,local_ip)
                                    temp_data = filter_data_with_user_selected(df3, selected_lab, selected_shape, selected_band, selected_color, selected_purity, selected_fls, selected_polish,selected_cut,selected_symm)
                                    temp_data = temp_data.loc[(temp_data["COMP_NO"]==selected_chart_comp)]
                                    # temp_data = temp_data.loc[(temp_data["TYPE"]=="SALE")]
                                    try:
                                        table_data = """<tr><td style="background-color: #63BE7B;"><=30</td></tr>
                                                        <tr><td style="background-color: #9EDAB2;"><=60</td></tr>
                                                        <tr><td style="background-color: #EFF4AA;"><=90</td></tr>
                                                        <tr><td style="background-color: #F7DB35;"><=120</td></tr>
                                                        <tr><td style="background-color: #F99F67;"><=150</td></tr>
                                                        <tr><td style="background-color: #F77525;">150+</td></tr>"""
                                        st.markdown("""
                                                <style>
                                                    div.sticky_bar {
                                                        position: fixed;
                                                        bottom: 60px;
                                                        left: 0;
                                                        width: 100px;
                                                        }
                                                    </style>
                                            """, unsafe_allow_html=True)
                                        table_html_string = """
                                            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                                            <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                                            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                                            <div class="sticky_bar"><table class="table-borderless table-responsive card-1 p-4">%s</table></div>""" % ''.join(str(table_data))
                                        
                                        stock_data = current_stock(selected_chart_comp)
                                        stock_data = filter_data_with_user_selected(stock_data, selected_lab, selected_shape, selected_band, selected_color, selected_purity, selected_fls, selected_polish,selected_cut,selected_symm)                                    
                                        stock_data["count"] = 1
                                        st.markdown((((''.join(table_html_string).replace("'","")).replace(",","")).replace("[","")).replace("]",""), unsafe_allow_html=True)
                                        if selected_shape1 == selected_shape2:
                                            st.warning("Please Selecte Different Shape.")
                                        elif selected_shape1 == None:
                                            final_data1 = get_shape_filtered_data(temp_data,selected_shape2)
                                            stock_data = get_shape_filtered_data(stock_data,selected_shape2)
                                                
                                            st.markdown("<h3 style='text-align: center;'>Shape: %s </h3>" % selected_shape2, unsafe_allow_html=True)
                                            col3,col4 = st.columns(2)
                                            with col3:
                                                st.markdown("<h3 style='text-align: center;'>SALE</h3>", unsafe_allow_html=True)
                                                get_report_formate(final_data1,"SALE")
                                            with col4:
                                                st.markdown("<h3 style='text-align: center;'>STOCK</h3>", unsafe_allow_html=True)                                            
                                                get_report_formate(stock_data,"STOCK")
                                        elif selected_shape2 == None:
                                            final_data2 = get_shape_filtered_data(temp_data,selected_shape1)
                                            stock_data = get_shape_filtered_data(stock_data,selected_shape1)
                                                
                                            st.markdown("<h3 style='text-align: center;'>Shape: %s </h3>" % selected_shape1, unsafe_allow_html=True)
                                            col3,col4 = st.columns(2)
                                            with col3:
                                                st.markdown("<h3 style='text-align: center;'>SALE</h3>", unsafe_allow_html=True)
                                                get_report_formate(final_data2,"SALE")
                                            with col4:
                                                st.markdown("<h3 style='text-align: center;'>STOCK</h3>", unsafe_allow_html=True)
                                                
                                                get_report_formate(stock_data,"STOCK")
                                        else:
                                            col1,col2 = st.columns([1,1])
                                            with col1:
                                                final_data1 = get_shape_filtered_data(temp_data,selected_shape1)
                                                stock_data1 = get_shape_filtered_data(stock_data,selected_shape1)
                                                st.markdown("<h3 style='text-align: center;'>Shape: %s </h3>" % selected_shape1, unsafe_allow_html=True)
                                                col3,col4 = st.columns(2)
                                                with col3:
                                                    st.markdown("<h3 style='text-align: center;'>SALE</h3>", unsafe_allow_html=True)
                                                    get_report_formate(final_data1,"SALE")
                                                with col4:
                                                    st.markdown("<h3 style='text-align: center;'>STOCK</h3>", unsafe_allow_html=True)
                                                    get_report_formate(stock_data1,"STOCK")

                                            with col2:
                                                final_data2 = get_shape_filtered_data(temp_data,selected_shape2)
                                                stock_data1 = get_shape_filtered_data(stock_data,selected_shape2)
                                                
                                                st.markdown("<h3 style='text-align: center;'>Shape: %s </h3>" % selected_shape2, unsafe_allow_html=True)
                                                col3,col4 = st.columns(2)
                                                with col3:
                                                    st.markdown("<h3 style='text-align: center;'>SALE</h3>", unsafe_allow_html=True)
                                                    get_report_formate(final_data2,"SALE")
                                                with col4:
                                                    st.markdown("<h3 style='text-align: center;'>STOCK</h3>", unsafe_allow_html=True)
                                                    get_report_formate(stock_data1,"STOCK")
                                        get_sticky(selected_lab, selected_shape, selected_band, selected_color, selected_purity, selected_fls, selected_polish,selected_cut,selected_symm)
                                    except:
                                        st.error("Data Filter is Missing.....")
                        elif selected_report_type == "Stock Dashboard":
                            selected_chart_comp,selected_chart_comp2 = select_comp2_for_stock()
                            expander_col1,expander_col2,expander_col3 = expander1.columns([1,2,2])
                            if expander_col1.button("View Report"):
                                print(str(str(datetime.today().replace(microsecond=0)) + " | " + str(local_ip) + " | " + str(selected_report_type)))
                                log(selected_report_type,selected_start_date,selected_end_date,selected_shape,selected_color,selected_purity,selected_fls,selected_band,f'Company: {selected_chart_comp}')
                                temp_data = filter_data_with_user_selected(df3, selected_lab, selected_shape, selected_band, selected_color, selected_purity, selected_fls, selected_polish,selected_cut,selected_symm)
                                
                                try:
                                    if selected_chart_comp == selected_chart_comp2:
                                        st.warning("Please Select Different Company.")
                                    elif selected_chart_comp == None:
                                        sum_of_count_crt_net_value_stock(temp_data,selected_chart_comp2)
                                    elif selected_chart_comp2 == None:
                                        sum_of_count_crt_net_value_stock(temp_data,selected_chart_comp)
                                    else:
                                        col1, col2 = st.columns([1,1])
                                        with col1:
                                            sum_of_count_crt_net_value_stock(temp_data,selected_chart_comp)
                                        with col2:
                                            sum_of_count_crt_net_value_stock(temp_data,selected_chart_comp2)
                                    
                                    get_sticky(selected_lab, selected_shape, selected_band, selected_color, selected_purity, selected_fls, selected_polish,selected_cut,selected_symm)
                                    expander_col2.markdown("<br/>", unsafe_allow_html=True)
                                    expander_col2.markdown(str('<div style="text-align-last: end; font-weight: bold; padding-bottom:0; margin-bottom: 0;">Report Generated At: ' + str(datetime.today().replace(microsecond=0)) + '</div>'), unsafe_allow_html=True)
                                    expander_col3.markdown("<br/>", unsafe_allow_html=True)
                                    expander_col3.markdown(str('<div style="text-align-last: end; font-weight: bold; padding-bottom:0; margin-bottom: 0;">Last Updated: ' + str(list(temp_data['last_updated'].unique())[0]) + '</div>'), unsafe_allow_html=True)
                                except:
                                    st.error("Data Filter is Missing.....")
                        elif selected_report_type == "Change in Price (Disc%/PPC)":
                            selected_chart_comp,selected_chart_comp2 = select_comp2_for_stock()
                            col1,col2,col3 = expander1.columns(3)

                            selected_date1 = col1.date_input("Select From Date Range")
                            selected_date2 = col2.date_input("Select To Date Range")
                            selected_change_type = col3.selectbox("Select Mode",tuple(["Disc%","PPC"]))
                            expander_col1,expander_col2,expander_col3 = expander1.columns([1,2,2])
                            if expander_col1.button("View Report"):
                                print(str(str(datetime.today().replace(microsecond=0)) + " | " + str(local_ip) + " | " + str(selected_report_type)))
                                log(selected_report_type,selected_start_date,selected_end_date,selected_shape,selected_color,selected_purity,selected_fls,selected_band,f'Company: {selected_chart_comp}')
                                create_db_log(selected_report_type,selected_start_date,selected_end_date,selected_shape,selected_color,selected_purity,selected_fls,selected_band, selected_chart_comp, selected_chart_comp2, None, None, selected_lab,None,None,None,None,None,None,None,None,None,None,None,None,local_ip)
                                tbl_data = get_selected_data(selected_end_date, selected_start_date,selected_companys_to_load_data,"sun")
                                temp_data = filter_data_with_user_selected(tbl_data, selected_lab, selected_shape, selected_band, selected_color, selected_purity, selected_fls, selected_polish,selected_cut,selected_symm)
                                temp_data = temp_data.loc[(temp_data["TYPE"]=="STOCK")]
                                temp_data['LAB1'] = temp_data.apply(lambda x: 1 if x['LAB'] == 'GIA' else 2, axis=1)
                                    
                                temp_data = temp_data.sort_values(["PACKET_NO","LAB1"])
                                temp_data = temp_data.drop_duplicates(["PACKET_NO","Date"])

                                try:
                                    temp_data['Date'] = temp_data.apply(lambda x: datetime.strptime(str(x['Date']), "%d-%m-%Y").strftime('%Y-%m-%d'), axis=1)
                                except:
                                    temp_data['Date'] = temp_data.apply(lambda x: datetime.strptime(str(x['Date']), "%Y-%m-%d").date(), axis=1)

                                temp_data = temp_data.loc[(temp_data["Date"]>=selected_date1)]
                                temp_data = temp_data.loc[(temp_data["Date"]<=selected_date2)]
                                
                                try:
                                    table_data = """<tr><td style="background-color: #FCBCBE;">Loose</td></tr>
                                                    <tr><td style="background-color: #C4E6CD;">Tight</td></tr>
                                                    <tr><td style="background-color: #FFFFFF;">Same</td></tr>"""
                                    st.markdown("""
                                            <style>
                                                div.sticky_bar {
                                                    position: fixed;
                                                    bottom: 60px;
                                                    right: 0;
                                                    width: 100px;
                                                    }
                                                </style>
                                        """, unsafe_allow_html=True)
                                    table_html_string = """
                                        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                                        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                                        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                                        <div class="sticky_bar"><table class="table-borderless table-responsive card-1 p-4">%s</table></div>""" % ''.join(str(table_data))
                                    
                                    st.markdown((((''.join(table_html_string).replace("'","")).replace(",","")).replace("[","")).replace("]",""), unsafe_allow_html=True)
                                    
                                    if selected_chart_comp == selected_chart_comp2:
                                        st.warning("Please Select Different Company.")
                                    elif selected_chart_comp == None:
                                        get_data_for_chnage_price_report(temp_data,selected_change_type,selected_chart_comp2)
                                    elif selected_chart_comp2 == None:
                                        get_data_for_chnage_price_report(temp_data,selected_change_type,selected_chart_comp)
                                    else:
                                        col1, col2 = st.columns([1,1])
                                        with col1:
                                            get_data_for_chnage_price_report(temp_data,selected_change_type,selected_chart_comp)
                                        with col2:
                                            get_data_for_chnage_price_report(temp_data,selected_change_type,selected_chart_comp2)
                                    
                                    get_sticky(selected_lab, selected_shape, selected_band, selected_color, selected_purity, selected_fls, selected_polish,selected_cut,selected_symm)
                                    expander_col2.markdown("<br/>", unsafe_allow_html=True)
                                    expander_col2.markdown(str('<div style="text-align-last: end; font-weight: bold; padding-bottom:0; margin-bottom: 0;">Report Generated At: ' + str(datetime.today().replace(microsecond=0)) + '</div>'), unsafe_allow_html=True)
                                    expander_col3.markdown("<br/>", unsafe_allow_html=True)
                                    expander_col3.markdown(str('<div style="text-align-last: end; font-weight: bold; padding-bottom:0; margin-bottom: 0;">Last Updated: ' + str(list(temp_data['last_updated'].unique())[0]) + '</div>'), unsafe_allow_html=True)
                                except:
                                    st.error("Data Filter is Missing.....")
                        elif selected_report_type == "Full Stock Report":
                            full_stock, select_full_stock_location,select_full_stock_stone_location = get_full_stock_data()

                            col1,col2,col3 = expander1.columns([1,1,1])

                            select_full_stock_stone_location = select_full_stock_stone_location.tolist()
                            select_full_stock_location = select_full_stock_location.tolist()
                            select_full_stock_stone_location[:0] = ["All"]
                            select_full_stock_location[:0] = ["All"]

                            selected_full_stock_stone_location = col1.multiselect("Select Stone Location", select_full_stock_stone_location,["All"])
                            selected_full_stock_location = col2.multiselect("Select MFG Location", select_full_stock_location,["All"])
                            selected_full_stock_stage = col3.multiselect("Select Stage", select_full_stock_stage,["STOCK"])
                            col1,col2 = expander1.columns([1,1])
                            selected_type = col1.selectbox("Select Type", tuple(total_data_type))
                            selected_radio_type = col2.radio("Select Report",["Group","Detail"])

                            expander_col1,expander_col2,expander_col3 = expander1.columns([1,2,2])
                            if expander_col1.button("View Report"):
                                print(str(str(datetime.today().replace(microsecond=0)) + " | " + str(local_ip) + " | " + str(selected_report_type)))
                                if 'All' in selected_full_stock_stone_location:
                                    temp_stone_location_list = select_full_stock_stone_location
                                    temp_stone_location_list.remove("All")
                                    selected_full_stock_stone_location = temp_stone_location_list
                                    del temp_stone_location_list

                                if 'All' in selected_full_stock_location:
                                    temp_mfg_location_list = select_full_stock_location
                                    temp_mfg_location_list.remove("All")
                                    selected_full_stock_location = temp_mfg_location_list
                                    del temp_mfg_location_list
                                
                                if 'All' in selected_full_stock_stage:
                                    temp_stage_list = select_full_stock_stage
                                    temp_stage_list.remove("All")
                                    selected_full_stock_stage = temp_stage_list
                                    del temp_stage_list
            
                                full_stock1 = full_stock.loc[(full_stock['STONE_LOCATION'].isin(selected_full_stock_stone_location))]
                                full_stock1 = full_stock1.loc[(full_stock1['STAGE'].isin(selected_full_stock_stage))]
                                full_stock1 = full_stock1.loc[(full_stock1['MFG_LOCATION'].isin(selected_full_stock_location))]
                                
                                full_stock1 = full_stock1.loc[(full_stock1['RANGE'].isin(selected_band))]
                                full_stock1["LAB"] = full_stock1.apply(lambda x: "GIA" if x["LAB"]=="GIA" else "OTHER", axis=1)
                                full_stock1.to_clipboard()
                                full_stock1['CUT'] = full_stock1.apply(lambda x: "EX" if x['CUT'] == "-" else "EX" if x["CUT"] == None else x['CUT'], axis=1)
                                # full_stock1['CUT'] = full_stock1.apply(lambda x: "EX" if x['CUT'] == "-" else "EX" if x["CUT"] == "None" else x['CUT'], axis=1)
                                full_stock1 = full_stock1.loc[full_stock1['LAB'].isin(selected_lab)]
                                full_stock1 = full_stock1[full_stock1['SHAPE1'].isin(selected_shape)]
                                full_stock1 = full_stock1[full_stock1['COLOR_A'].isin(selected_color)]
                                full_stock1 = full_stock1[full_stock1['PURITY'].isin(selected_purity)]
                                full_stock1 = full_stock1[full_stock1['FLS'].isin(selected_fls)]
                                full_stock1 = full_stock1[full_stock1['POLISH'].isin(selected_polish)]
                                full_stock1 = full_stock1[full_stock1['CUT'].isin(selected_cut)]
                                full_stock1 = full_stock1[full_stock1['SYMM'].isin(selected_symm)]

                                for_head_print_type,for_selected_type,for_aggfunc = print_type(selected_type)
                                del for_head_print_type
                                if selected_full_stock_stage and selected_full_stock_location:
                                    try:
                                        full_stock_report(full_stock1,selected_full_stock_stage,for_selected_type,for_aggfunc,selected_radio_type)
                                    except:
                                        st.error("Data Filter is Missing.....")
                                else:
                                    st.error("Data Filter is Missing.....")
                                
                                get_sticky(selected_lab, selected_shape, selected_band, selected_color, selected_purity, selected_fls, selected_polish,selected_cut,selected_symm)

                                expander_col2.markdown("<br/>", unsafe_allow_html=True)
                                expander_col2.markdown(str('<div style="text-align-last: end; font-weight: bold; padding-bottom:0; margin-bottom: 0;">Report Generated At: ' + str(datetime.today().replace(microsecond=0)) + '</div>'), unsafe_allow_html=True)
                                # expander_col3.markdown("<br/>", unsafe_allow_html=True)
                                # expander_col3.markdown(str('<div style="text-align-last: end; font-weight: bold; padding-bottom:0; margin-bottom: 0;">Last Updated: ' + str(datetime.today().replace(microsecond=0,second=0,minute=0,hour=0)) + '</div>'), unsafe_allow_html=True)
                        elif selected_report_type == "Quick Sale Report":
                            selected_chart_comp,selected_chart_comp2 = select_comp2_for_stock()
                                                
                            expander_col1,expander_col2,expander_col3 = expander1.columns([1,2,2])
                            if expander_col1.button("View Report"):
                                print(str(str(datetime.today().replace(microsecond=0)) + " | " + str(local_ip) + " | " + str(selected_report_type)))
                                log(selected_report_type,selected_start_date,selected_end_date,selected_shape,selected_color,selected_purity,selected_fls,selected_band,f'Company: {selected_chart_comp}')
                                create_db_log(selected_report_type,selected_start_date,selected_end_date,selected_shape,selected_color,selected_purity,selected_fls,selected_band, selected_chart_comp, selected_chart_comp2, None, None, selected_lab,None,None,None,None,None,None,None,None,None,None,None,None,local_ip)
                                temp_data = filter_data_with_user_selected(df3, selected_lab, selected_shape, selected_band, selected_color, selected_purity, selected_fls, selected_polish,selected_cut,selected_symm)
                                
                                if selected_chart_comp == selected_chart_comp2:
                                    st.warning("Please Selecte Different Comapany.")
                                elif selected_chart_comp == None:
                                    get_cumulative_chart(temp_data,selected_chart_comp2)
                                elif selected_chart_comp2 == None:
                                    get_cumulative_chart(temp_data,selected_chart_comp)
                                else:
                                    col1, col2 = st.columns([1,1])
                                    with col1:
                                        get_cumulative_chart(temp_data,selected_chart_comp)
                                    with col2:
                                        get_cumulative_chart(temp_data,selected_chart_comp2)
                                
                                get_sticky(selected_lab, selected_shape, selected_band, selected_color, selected_purity, selected_fls, selected_polish,selected_cut,selected_symm)
                                expander_col2.markdown("<br/>", unsafe_allow_html=True)
                                expander_col2.markdown(str('<div style="text-align-last: end; font-weight: bold; padding-bottom:0; margin-bottom: 0;">Report Generated At: ' + str(datetime.today().replace(microsecond=0)) + '</div>'), unsafe_allow_html=True)
                                expander_col3.markdown("<br/>", unsafe_allow_html=True)
                                expander_col3.markdown(str('<div style="text-align-last: end; font-weight: bold; padding-bottom:0; margin-bottom: 0;">Last Updated: ' + str(list(temp_data['last_updated'].unique())[0]) + '</div>'), unsafe_allow_html=True)
                        elif selected_report_type == "Tradescreen":
                            col1, col2 = expander1.columns(2)
                            # SELECT COMP
                            selected_chart_comp = col1.selectbox("Select Company 1", tuple(total_first_comp))
                            selected_type = col2.selectbox("Select Type", tuple(["SALE", "STOCK"]))

                            expander_col1,expander_col2,expander_col3 = expander1.columns([1,2,2])
                            if expander_col1.button("View Report"):
                                print(str(str(datetime.today().replace(microsecond=0)) + " | " + str(local_ip) + " | " + str(selected_report_type)))
                                log(selected_report_type,selected_start_date,selected_end_date,selected_shape,selected_color,selected_purity,selected_fls,selected_band,f'Company: {selected_chart_comp}')
                                create_db_log(selected_report_type,selected_start_date,selected_end_date,selected_shape,selected_color,selected_purity,selected_fls,selected_band, selected_chart_comp, None, None, None, selected_lab,None,None,None,None,None,None,None,None,None,None,None,None,local_ip)
                                
                                def current_stock(comp_fun):
                                    monthly_collection_letest_stock = db["letest_stock"]
                                    res = monthly_collection_letest_stock.find({"COMP_NO": comp_fun})
                                    temp_new_d= pl.DataFrame(res)
                                    today_stock = temp_new_d.to_pandas()
                                    del res,temp_new_d
                                    return today_stock
                                
                                # FILTER DATA BY USER SELECTED
                                if selected_type == "STOCK":
                                    temp_data = current_stock(selected_chart_comp)
                                    temp_data["count"] = 1
                                else:
                                    temp_data = df3
                                temp_data = filter_data_with_user_selected(temp_data, selected_lab, selected_shape, selected_band, selected_color, selected_purity, selected_fls, selected_polish,selected_cut,selected_symm)
                                
                                table_data = """<div>
                                        Min PPC <span style="color: green;">Min Disc%</span></br>
                                        Max PPC <span style="color: green;">Max Disc%</span></br>
                                        AVG PPC / Pcs</br>
                                        Value / CTS
                                            </div>"""
                                st.markdown("""
                                        <style>
                                            div.sticky_tradescreen {
                                                position: fixed;
                                                bottom: 30px;
                                                left: 3px;
                                                width: 100px;
                                                font-size: 12px;
                                                }
                                            </style>
                                    """, unsafe_allow_html=True)
                                table_html_string = """
                                    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                                    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                                    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                                    <div class="sticky_tradescreen"><table class="table-borderless table-responsive card-1 p-4">%s</table></div>""" % ''.join(str(table_data))

                                st.markdown((((''.join(table_html_string).replace("'","")).replace(",","")).replace("[","")).replace("]",""), unsafe_allow_html=True)

                                get_tradescreen_formate(temp_data,selected_type,selected_chart_comp)
                                
                                get_sticky(selected_lab, selected_shape, selected_band, selected_color, selected_purity, selected_fls, selected_polish,selected_cut,selected_symm)

                                expander_col2.markdown("<br/>", unsafe_allow_html=True)
                                expander_col2.markdown(str('<div style="text-align-last: end; font-weight: bold; padding-bottom:0; margin-bottom: 0;">Report Generated At: ' + str(datetime.today().replace(microsecond=0)) + '</div>'), unsafe_allow_html=True)
                                expander_col3.markdown("<br/>", unsafe_allow_html=True)
                                expander_col3.markdown(str('<div style="text-align-last: end; font-weight: bold; padding-bottom:0; margin-bottom: 0;">Last Updated: ' + str(list(temp_data['last_updated'].unique())[0]) + '</div>'), unsafe_allow_html=True)
                        elif selected_report_type == "Cno1 and Cno.2 Stock summary":
                            
                            col1,col2,col3,col4 = expander1.columns(4)
                            
                            selected_change_type = col1.selectbox("Select Mode",tuple(["Disc%","PPC"]))
                            selected_size_band_type = col2.selectbox("Select Size Band", tuple(["Rap Size", "Pricing Size", "Website Size"]))
                            # SELECT COMP
                            selected_chart_comp = col3.selectbox("Select Company 1", tuple(total_first_comp_for_stock))

                            # selected_date1 = col1.date_input("Select From Date Range")
                            # selected_date2 = col2.date_input("Select To Date Range")
                            
                            selected_sub_report_type = col4.selectbox("Select Report", tuple(["Daily", "Monthly"]))
                            col1,col2,col3,col4 = expander1.columns(4)
                            selected_range_type = col1.selectbox("Select Range", tuple(["1+", "Pointer"]))
                            if selected_sub_report_type == "Monthly":
                                selected_status_type = "STOCK"
                                selected_chart_comp2 = selected_chart_comp
                                selected_sub_report_start_date = col2.date_input("Select From Date Range")
                                selected_sub_report_end_date = col3.date_input("Select To Date Range")
                            else:
                                selected_status_type = col2.selectbox("Select Type",tuple(["SALE","STOCK"]))
                                selected_chart_comp2 = col3.selectbox("Select Company 2", tuple(total_second_comp_for_stock),total_second_comp_for_stock[0])
                                selected_sub_report_start_date = datetime.today()
                                selected_sub_report_end_date = datetime.today()
                            # selected_type = col4.selectbox("Select Type", tuple([]))
                            expander_col1,expander_col2,expander_col3 = expander1.columns([1,2,2])
                            # for_head_print_type,for_selected_type,for_aggfunc = print_type(selected_type)
                            if expander_col1.button("View Report"):
                                print(str(str(datetime.today().replace(microsecond=0)) + " | " + str(local_ip) + " | " + str(selected_report_type)))
                                log(selected_report_type,selected_start_date,selected_end_date,selected_shape,selected_color,selected_purity,selected_fls,selected_band,f'Company: {selected_chart_comp}')
                                create_db_log(selected_report_type,selected_start_date,selected_end_date,selected_shape,selected_color,selected_purity,selected_fls,selected_band, selected_chart_comp, selected_chart_comp2, None, None, selected_lab,None,None,None,None,None,None,None,None,None,None,None,None,local_ip)
                                start_date = str(datetime.now().date())
                                
                                def current_stock(comp_fun):
                                    """ run quiery for letest stock and filter data by given comp_fun"""
                                    
                                    monthly_collection_letest_stock = db["letest_stock"]
                                    res = monthly_collection_letest_stock.find({"COMP_NO": comp_fun})
                                    temp_new_d= pl.DataFrame(res)
                                    today_stock = temp_new_d.to_pandas()
                                    del res,temp_new_d
                                    return today_stock
                                
                                def filter_data_stock_summary(fun_temp_data,selected_lab, selected_shape, selected_band, selected_color, selected_purity, selected_fls, selected_polish,selected_cut,selected_symm):
                                    """ this function will filter data and remove duplicate and change date formate"""
                                    
                                    fun_temp_data = filter_data_with_user_selected(fun_temp_data, selected_lab, selected_shape, selected_band, selected_color, selected_purity, selected_fls, selected_polish,selected_cut,selected_symm)
                                    
                                    fun_temp_data['LAB1'] = fun_temp_data.apply(lambda x: 1 if x['LAB'] == 'GIA' else 2, axis=1)
                                        
                                    fun_temp_data = fun_temp_data.sort_values(["PACKET_NO","LAB1"])
                                    fun_temp_data = fun_temp_data.drop_duplicates(["PACKET_NO","Date"])

                                    try:
                                        fun_temp_data['Date'] = fun_temp_data.apply(lambda x: datetime.strptime(str(x['Date']), "%d-%m-%Y").strftime('%Y-%m-%d'), axis=1)
                                    except:
                                        fun_temp_data['Date'] = fun_temp_data.apply(lambda x: datetime.strptime(str(x['Date']), "%Y-%m-%d").date(), axis=1)
                                    
                                    return fun_temp_data
                                
                                def get_stock_summary_monthly(fun_date,fun_date1,selected_type,def_comp_fun):
                                    """ this function will filter data in beetween first date to last date"""
                                    
                                    fun_temp_data = get_selected_data(fun_date1, fun_date,[def_comp_fun],"sun")
                                    
                                    fun_temp_data = fun_temp_data.loc[(fun_temp_data["TYPE"]==selected_type)]
                                    
                                    return fun_temp_data
                                
                                # temp_data = temp_data.loc[(temp_data["Date"]>=selected_date1)]
                                # temp_data = temp_data.loc[(temp_data["Date"]<=selected_date2)]
                                
                                def define_data_range(def_data,range_type):
                                    """ add size band according to range type selection"""
                                    
                                    if range_type == "Rap Size":
                                        def_data['Band'] = def_data.apply(lambda x: 'Doss' 
                                                            if x['WGT'] < 1 else '1.00-1.19' 
                                                            if x['WGT'] < 1.2 else '1.20-1.49' 
                                                            if x['WGT'] < 1.5 else '1.50-1.99' 
                                                            if x['WGT'] < 2 else '2.00-2.99' 
                                                            if x['WGT'] < 3 else '3.00-3.99' 
                                                            if x['WGT'] < 4 else '4.00-4.99' 
                                                            if x['WGT'] < 5 else '5.00-9.99' 
                                                            if x['WGT'] < 10 else '10+', axis=1)
                                    elif range_type == "Pricing Size":
                                          def_data['Band'] = def_data.apply(lambda x: "0.150 - 0.179" if x["WGT"] <= 0.179 else
                                                    "0.180 - 0.199" if x["WGT"] <= 0.199 else
                                                    "0.200 - 0.229" if x["WGT"] <= 0.229 else
                                                    "0.230 - 0.249" if x["WGT"] <= 0.249 else
                                                    "0.250 - 0.299" if x["WGT"] <= 0.299 else
                                                    "0.300 - 0.349" if x["WGT"] <= 0.349 else
                                                    "0.350 - 0.399" if x["WGT"] <= 0.399 else
                                                    "0.400 - 0.449" if x["WGT"] <= 0.449 else
                                                    "0.450 - 0.499" if x["WGT"] <= 0.499 else
                                                    "0.500 - 0.599" if x["WGT"] <= 0.599 else
                                                    "0.600 - 0.699" if x["WGT"] <= 0.699 else
                                                    "0.700 - 0.749" if x["WGT"] <= 0.749 else
                                                    "0.750 - 0.799" if x["WGT"] <= 0.799 else
                                                    "0.800 - 0.849" if x["WGT"] <= 0.849 else
                                                    "0.850 - 0.899" if x["WGT"] <= 0.899 else
                                                    "0.900 - 0.949" if x["WGT"] <= 0.949 else
                                                    "0.950 - 0.999" if x["WGT"] <= 0.999 else
                                                    "1.000 - 1.009" if x["WGT"] <= 1.009 else
                                                    "1.010 - 1.099" if x["WGT"] <= 1.099 else
                                                    "1.100 - 1.179" if x["WGT"] <= 1.179 else
                                                    "1.180 - 1.299" if x["WGT"] <= 1.299 else
                                                    "1.300 - 1.399" if x["WGT"] <= 1.399 else
                                                    "1.400 - 1.479" if x["WGT"] <= 1.479 else
                                                    "1.480 - 1.499" if x["WGT"] <= 1.499 else
                                                    "1.500 - 1.599" if x["WGT"] <= 1.599 else
                                                    "1.600 - 1.699" if x["WGT"] <= 1.699 else
                                                    "1.700 - 1.799" if x["WGT"] <= 1.799 else
                                                    "1.800 - 1.899" if x["WGT"] <= 1.899 else
                                                    "1.900 - 1.979" if x["WGT"] <= 1.979 else
                                                    "1.980 - 1.999" if x["WGT"] <= 1.999 else
                                                    "2.000 - 2.009" if x["WGT"] <= 2.009 else
                                                    "2.010 - 2.099" if x["WGT"] <= 2.099 else
                                                    "2.100 - 2.199" if x["WGT"] <= 2.199 else
                                                    "2.200 - 2.299" if x["WGT"] <= 2.299 else
                                                    "2.300 - 2.399" if x["WGT"] <= 2.399 else
                                                    "2.400 - 2.499" if x["WGT"] <= 2.499 else
                                                    "2.500 - 2.599" if x["WGT"] <= 2.599 else
                                                    "2.600 - 2.699" if x["WGT"] <= 2.699 else
                                                    "2.700 - 2.799" if x["WGT"] <= 2.799 else
                                                    "2.800 - 2.899" if x["WGT"] <= 2.899 else
                                                    "2.900 - 2.979" if x["WGT"] <= 2.979 else
                                                    "2.980 - 2.999" if x["WGT"] <= 2.999 else
                                                    "3.000 - 3.009" if x["WGT"] <= 3.009 else
                                                    "3.010 - 3.099" if x["WGT"] <= 3.099 else
                                                    "3.100 - 3.199" if x["WGT"] <= 3.199 else
                                                    "3.200 - 3.399" if x["WGT"] <= 3.399 else
                                                    "3.400 - 3.499" if x["WGT"] <= 3.499 else
                                                    "3.500 - 3.699" if x["WGT"] <= 3.699 else
                                                    "3.700 - 3.799" if x["WGT"] <= 3.799 else
                                                    "3.800 - 3.899" if x["WGT"] <= 3.899 else
                                                    "3.900 - 3.979" if x["WGT"] <= 3.979 else
                                                    "3.980 - 3.999" if x["WGT"] <= 3.999 else
                                                    "4.000 - 4.009" if x["WGT"] <= 4.009 else
                                                    "4.010 - 4.099" if x["WGT"] <= 4.099 else
                                                    "4.100 - 4.199" if x["WGT"] <= 4.199 else
                                                    "4.200 - 4.399" if x["WGT"] <= 4.399 else
                                                    "4.400 - 4.499" if x["WGT"] <= 4.499 else
                                                    "4.500 - 4.699" if x["WGT"] <= 4.699 else
                                                    "4.700 - 4.799" if x["WGT"] <= 4.799 else
                                                    "4.800 - 4.899" if x["WGT"] <= 4.899 else
                                                    "4.900 - 4.979" if x["WGT"] <= 4.979 else
                                                    "4.980 - 4.999" if x["WGT"] <= 4.999 else
                                                    "5.000 - 5.009" if x["WGT"] <= 5.009 else
                                                    "5.010 - 5.499" if x["WGT"] <= 5.499 else
                                                    "5.500 - 5.999" if x["WGT"] <= 5.999 else
                                                    "6.000 - 6.009" if x["WGT"] <= 6.009 else
                                                    "6.010 - 6.999" if x["WGT"] <= 6.999 else
                                                    "7.000 - 7.009" if x["WGT"] <= 7.009 else
                                                    "7.010 - 7.999" if x["WGT"] <= 7.999 else
                                                    "8.000 - 8.009" if x["WGT"] <= 8.009 else
                                                    "8.010 - 8.999" if x["WGT"] <= 8.999 else
                                                    "9.000 - 9.009" if x["WGT"] <= 9.009 else
                                                    "9.010 - 9.999" if x["WGT"] <= 9.999 else
                                                    "10.000 - 10.009" if x["WGT"] <= 10.00 else
                                                    "10.010 - 14.999" if x["WGT"] <= 14.99 else
                                                    "15.000 - 19.999" if x["WGT"] <= 19.99 else
                                                    "20.000 - 24.999" if x["WGT"] <= 24.99 else
                                                    "25.000 - 29.999" if x["WGT"] <= 29.99 else "30.000 - 99.999", axis=1)
                                    else:
                                        def_data['Band'] = def_data['WGT'].apply(lambda x: '0.01-0.23' if x <= 0.22 else
                                                                    '0.23-0.29' if x <= 0.29 else
                                                                    '0.30-0.34' if x <= 0.34 else
                                                                    '0.35-0.39' if x <= 0.39 else
                                                                    '0.40-0.49' if x <= 0.49 else
                                                                    '0.50-0.59' if x <= 0.59 else
                                                                    '0.60-0.69' if x <= 0.69 else
                                                                    '0.70-0.79' if x <= 0.79 else
                                                                    '0.80-0.89' if x <= 0.89 else
                                                                    '0.90-0.94' if x <= 0.94 else
                                                                    '0.95-0.99' if x <= 0.99 else
                                                                    '1.00-1.09' if x <= 1.09 else
                                                                    '1.10-1.17' if x <= 1.17 else
                                                                    '1.18-1.29' if x <= 1.29 else
                                                                    '1.30-1.39' if x <= 1.39 else
                                                                    '1.40-1.49' if x <= 1.49 else
                                                                    '1.50-1.69' if x <= 1.69 else
                                                                    '1.70-1.99' if x <= 1.99 else
                                                                    '2.00-2.49' if x <= 2.49 else
                                                                    '2.50-2.99' if x <= 2.99 else
                                                                    '3.00-3.99' if x <= 3.99 else
                                                                    '4.00-4.99' if x <= 4.99 else
                                                                    '5.00-5.99' if x <= 5.99 else
                                                                    '6+')
                                    return def_data
                                
                                if selected_sub_report_type == "Daily":
                                    if selected_status_type == "SALE":
                                        end_date = datetime.now().date() - timedelta(days = 1)
                                        # start_date.strftime('%a')

                                        Std = end_date - timedelta(days = 30)
                                        # if Std.strftime('%a') == "Sun":
                                        #     Std = Std - timedelta(days = 1)
                                        
                                        temp_data1 = get_stock_summary_monthly(Std,end_date,selected_status_type,selected_chart_comp)
                                        temp_data2 = get_stock_summary_monthly(Std,end_date,selected_status_type,selected_chart_comp2)
                                    else:
                                        temp_data1 = current_stock(selected_chart_comp)
                                        # st.write(temp_data1)
                                        temp_data2 = current_stock(selected_chart_comp2)
                                    
                                    
                                    # temp_data2 = filter_data_stock_summary(temp_data2, selected_lab, selected_shape, selected_band, selected_color, selected_purity, selected_fls, selected_polish,selected_cut,selected_symm)
                                else:
                                    temp_data1 = get_stock_summary_monthly(selected_sub_report_start_date,selected_sub_report_start_date,selected_status_type,selected_chart_comp)
                                    temp_data2 = get_stock_summary_monthly(selected_sub_report_end_date,selected_sub_report_end_date,selected_status_type,selected_chart_comp)
                                    
                                temp_data1 = filter_data_stock_summary(temp_data1, selected_lab, selected_shape, selected_band, selected_color, selected_purity, selected_fls, selected_polish,selected_cut,selected_symm)
                                temp_data2 = filter_data_stock_summary(temp_data2, selected_lab, selected_shape, selected_band, selected_color, selected_purity, selected_fls, selected_polish,selected_cut,selected_symm)
                                
                                if selected_range_type == "1+":
                                    temp_data1 = temp_data1[temp_data1['WGT'] >= 1.00]
                                    temp_data2 = temp_data2[temp_data2['WGT'] >= 1.00]
                                else:
                                    temp_data1 = temp_data1[temp_data1['WGT'] <= 1.00]
                                    temp_data2 = temp_data2[temp_data2['WGT'] <= 1.00]
                                
                                
                                # temp_data1 = temp_data1.groupby(['Band', 'PURITY_A', "COLOR_A"])[["DISC_PER"]].mean()
                                # temp_data1.to_clipboard()
                                if selected_size_band_type == "Rap Size" and selected_range_type == "1+":
                                    # range_seq = ["5.00 - 99.99","4.00 - 4.99","3.00 - 3.99", "2.00 - 2.99", "1.50 - 1.99", "1.00 - 1.49", "0.90 - 0.99", "0.70 - 0.89", "0.50 - 0.69", "0.40 - 0.49", "0.30 - 0.39", "0.23 - 0.29", "0.18 - 0.22", "0.15 - 0.17", "0.08 - 0.14", "0.04 - 0.07", "0.01 - 0.03"]
                                    range_seq = ['1.00-1.19','1.20-1.49','1.50-1.99','2.00-2.99','3.00-3.99','4.00-4.99','5.00-9.99','10+']
                                elif selected_size_band_type == "Rap Size" and selected_range_type == "Pointer":
                                    # range_seq = ["5.00 - 99.99","4.00 - 4.99","3.00 - 3.99", "2.00 - 2.99", "1.50 - 1.99", "1.00 - 1.49", "0.90 - 0.99", "0.70 - 0.89", "0.50 - 0.69", "0.40 - 0.49", "0.30 - 0.39", "0.23 - 0.29", "0.18 - 0.22", "0.15 - 0.17", "0.08 - 0.14", "0.04 - 0.07", "0.01 - 0.03"]
                                    range_seq = ['Doss']
                                elif selected_size_band_type == "Pricing Size" and selected_range_type == "1+":
                                    range_seq = ["1.000 - 1.009","1.010 - 1.099","1.100 - 1.179","1.180 - 1.299","1.300 - 1.399","1.400 - 1.479","1.480 - 1.499","1.500 - 1.599","1.600 - 1.699","1.700 - 1.799","1.800 - 1.899","1.900 - 1.979","1.980 - 1.999","2.000 - 2.009","2.010 - 2.099","2.100 - 2.199","2.200 - 2.299","2.300 - 2.399","2.400 - 2.499","2.500 - 2.599","2.600 - 2.699","2.700 - 2.799","2.800 - 2.899","2.900 - 2.979","2.980 - 2.999","3.000 - 3.009","3.010 - 3.099","3.100 - 3.199","3.200 - 3.399","3.400 - 3.499","3.500 - 3.699","3.700 - 3.799","3.800 - 3.899","3.900 - 3.979","3.980 - 3.999","4.000 - 4.009","4.010 - 4.099","4.100 - 4.199","4.200 - 4.399","4.400 - 4.499","4.500 - 4.699","4.700 - 4.799","4.800 - 4.899","4.900 - 4.979","4.980 - 4.999","5.000 - 5.009","5.010 - 5.499","5.500 - 5.999","6.000 - 6.009","6.010 - 6.999","7.000 - 7.009","7.010 - 7.999","8.000 - 8.009","8.010 - 8.999","9.000 - 9.009","9.010 - 9.999","10.000 - 10.009","10.010 - 14.999","15.000 - 19.999","20.000 - 24.999","25.000 - 29.999","30.000 - 99.999"]
                                elif selected_size_band_type == "Pricing Size" and selected_range_type == "Pointer":
                                    range_seq = ["0.150 - 0.179","0.180 - 0.199","0.200 - 0.229","0.230 - 0.249","0.250 - 0.299","0.300 - 0.349","0.350 - 0.399","0.400 - 0.449","0.450 - 0.499","0.500 - 0.599","0.600 - 0.699","0.700 - 0.749","0.750 - 0.799","0.800 - 0.849","0.850 - 0.899","0.900 - 0.949","0.950 - 0.999"]
                                elif selected_size_band_type == "Website Size" and selected_range_type == "Pointer":
                                    range_seq = ['0.01-0.23','0.23-0.29','0.30-0.34','0.35-0.39','0.40-0.49','0.50-0.59','0.60-0.69','0.70-0.79','0.80-0.89','0.90-0.94','0.95-0.99']
                                else:
                                    range_seq = ['1.00-1.09','1.10-1.17','1.18-1.29','1.30-1.39','1.40-1.49','1.50-1.69','1.70-1.99','2.00-2.49','2.50-2.99','3.00-3.99','4.00-4.99','5.00-5.99','6+',]
                                
                                color_seq = ["D", "E", "F", "G", "H", "I", "J", "K", "L", "M","N","FANCY"]
                                purity_seq = ['FL','IF','VVS1','VVS2','VS1','VS2','SI1','SI2']
                                
                                def get_table_of_stock_summary(data_frame, range_type, fun_comp, agg_val):
                                    """ return html table of data in rap formate"""

                                    st.markdown("<h3 style='text-align: center;'>Company - %s</h3>" % fun_comp, unsafe_allow_html=True)
                                    if agg_val == "Disc%":
                                        agg_val = "DISC_PER"
                                    else:
                                        agg_val = "NET_RATE"

                                    data_frame['LAB1']=data_frame['X_LAB'].apply(lambda x: 1 if x=="GIA" else 2)

                                    data_frame.sort_values(by=['PACKET_NO', 'LAB1'])
                                    data_frame = data_frame.drop_duplicates(subset=['PACKET_NO', 'TYPE'])

                                    data_frame.drop(['LAB1'], axis=1)

                                    data_frame = data_frame.loc[(data_frame["COLOR_A"].isin(color_seq))]
                                    data_frame = data_frame.loc[(data_frame["PURITY_A"].isin(purity_seq))]
                                    
                                    data_frame = define_data_range(data_frame, range_type)
                                    disc_data = pd.pivot_table(data=data_frame, index=['Band',"COLOR_A"],
                                                        columns=["PURITY_A"],
                                                        values= str(agg_val),
                                                        aggfunc={ str(agg_val): "mean"},
                                                        fill_value=0,
                                                        margins=False).reset_index()
                                                                   
                                    st.markdown("""
                                                <style>
                                                    .table_1 {
                                                        width:100%; 
                                                        }
                                                    .table_header{
                                                        text-align: center;
                                                        font-weight: bold;
                                                        background-color: #287E8F;
                                                        color: #FFFFFF;
                                                        font-size: 14px;
                                                    }
                                                    .sub_total{
                                                        text-align: center;
                                                        font-weight: bold;
                                                        font-size: 14px;
                                                        background-color: #B8CCE4;
                                                    }
                                                    .table_head{
                                                        text-align: center;
                                                        font-weight: bold;
                                                        font-size: 14px;
                                                    }
                                                    .table_data_style{
                                                        text-align: center;
                                                        font-size: 14px;
                                                    }
                                                    td, th{
                                                        width: 1%;
                                                    }
                                                    tr{
                                                        height: 12px;
                                                    }
                                                    tr:nth-child(even) {background-color: #f2f2f2;}
                                                </style>
                                                """, unsafe_allow_html=True)

                                    table_head = """<tr><th class="table_head"> </th><th class="table_head">FL</th><th class="table_head">IF</th><th class="table_head">VVS1</th><th class="table_head">VVS2</th><th class="table_head">VS1</th><th class="table_head">VS2</th><th class="table_head">SI1</th><th class="table_head">SI2</th></tr>"""
                                    table_rows = []
                                    
                                    for size_t in range_seq:                                        
                                        range_head_str = """<tr><td class="table_header" colspan="9">%s</td></tr>""" % (''.join(str(size_t)))
                                        
                                        col_row=[]
                                        for color_t in color_seq:
                                            table_data = []
                                            col_data = '<td class="table_head">%s</td>' % ''.join(str(color_t))
                                            for purity_t in purity_seq:
                                                avg_disc = disc_data.loc[((disc_data['Band']==str(size_t)) & (disc_data['COLOR_A']==str(color_t)))]
                                                if abs(sum(avg_disc[str(purity_t)]))>0:
                                                    try:
                                                        table_data.append('<td class="table_data_style">%s</td>' % round(sum(avg_disc[str(purity_t)])))
                                                    except:
                                                        table_data.append('<td class="table_data_style">%s</td>' % " ")
                                                else:
                                                    table_data.append('<td class="table_data_style">%s</td>' % " ")
                                            col_row.append(str("<tr>%s%s</tr>" % (''.join(col_data),''.join(table_data))))
                                        table_rows.append("""%s%s%s""" % (''.join(range_head_str),''.join(table_head),''.join(col_row)))
                            
                                    table_html_string = """
                                                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                                                <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                                                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                                                <table class="table-borderless table-responsive card-1 p-4">%s</table> """ % ''.join(str(table_rows))
                                    st.markdown((((''.join(table_html_string).replace("'","")).replace(",","")).replace("[","")).replace("]",""), unsafe_allow_html=True)
                                    return disc_data

                                st.markdown("<h3 style='text-align: center;'>Today Stock and Last 1 Month Sale Data Only GIA</h3>", unsafe_allow_html=True)

                                col1, col2, col3 = st.columns([1, 1, 1])
                                with col1:
                                    first_cno = get_table_of_stock_summary(temp_data1, selected_size_band_type, selected_chart_comp, selected_change_type)
                                with col2:    
                                    second_cno = get_table_of_stock_summary(temp_data2, selected_size_band_type, selected_chart_comp2, selected_change_type)
                                with col3:
                                    st.markdown("<h3 style='text-align: center;'>DIS wise DIFF CN-%s & CN-%s</h3>" % (selected_chart_comp, selected_chart_comp2), unsafe_allow_html=True)
                                    
                                    st.markdown("""
                                                <style>
                                                    .table_1 {
                                                        width:100%; 
                                                        }
                                                    .table_header{
                                                        text-align: center;
                                                        font-weight: bold;
                                                        background-color: #287E8F;
                                                        color: #FFFFFF;
                                                        font-size: 14px;
                                                    }
                                                    .sub_total{
                                                        text-align: center;
                                                        font-weight: bold;
                                                        font-size: 14px;
                                                        background-color: #B8CCE4;
                                                    }
                                                    .table_head{
                                                        text-align: center;
                                                        font-weight: bold;
                                                        font-size: 14px;
                                                    }
                                                    .table_data_style{
                                                        text-align: center;
                                                        font-size: 14px;
                                                    }
                                                    td, th{
                                                        width: 1%;
                                                    }
                                                    tr{
                                                        height: 12px;
                                                    }
                                                    tr:nth-child(even) {background-color: #f2f2f2;}
                                                </style>
                                                """, unsafe_allow_html=True)

                                    table_head = """<tr><th class="table_head"> </th><th class="table_head">FL</th><th class="table_head">IF</th><th class="table_head">VVS1</th><th class="table_head">VVS2</th><th class="table_head">VS1</th><th class="table_head">VS2</th><th class="table_head">SI1</th><th class="table_head">SI2</th></tr>"""
                                    table_rows = []
                                    
                                    for size_t in range_seq:                                        
                                        range_head_str = """<tr><td class="table_header" colspan="9">%s</td></tr>""" % (''.join(str(size_t)))
                                        
                                        col_row=[]
                                        for color_t in color_seq:
                                            table_data = []
                                            col_data = '<td class="table_head">%s</td>' % ''.join(str(color_t))
                                            for purity_t in purity_seq:
                                                first_avg_disc = first_cno.loc[((first_cno['Band']==str(size_t)) & (first_cno['COLOR_A']==str(color_t)))]
                                                second_avg_disc = second_cno.loc[((second_cno['Band']==str(size_t)) & (second_cno['COLOR_A']==str(color_t)))]
                                                
                                                if abs(sum(first_avg_disc[str(purity_t)]))>0 and abs(sum(second_avg_disc[str(purity_t)]))>0:
                                                    if selected_change_type == "PPC":
                                                        avg_diff = (abs(sum(second_avg_disc[str(purity_t)])) - abs(sum(first_avg_disc[str(purity_t)]))) / abs(sum(first_avg_disc[str(purity_t)])) * 100
                                                    else:
                                                        avg_diff = abs(sum(first_avg_disc[str(purity_t)])) - abs(sum(second_avg_disc[str(purity_t)]))
                                                    if abs(round(avg_diff))>0:
                                                        try:
                                                            if round(avg_diff)<-5:
                                                                table_data.append('<td class="table_data_style"><span style="color: #d17804">%s</span></td>' % round(avg_diff))
                                                            elif round(avg_diff)<0:
                                                                table_data.append('<td class="table_data_style"><span style="color: #03ad23">%s</span></td>' % round(avg_diff))
                                                            elif round(avg_diff)>0:
                                                                table_data.append('<td class="table_data_style"><span style="color: #d1080f">%s</span></td>' % round(avg_diff))
                                                            else:
                                                                table_data.append('<td class="table_data_style">%s</td>' % round(avg_diff))
                                                        except:
                                                            table_data.append('<td class="table_data_style">%s</td>' % " ")
                                                    else:
                                                        table_data.append('<td class="table_data_style">%s</td>' % " ")
                                                else:
                                                    table_data.append('<td class="table_data_style">%s</td>' % " ")
                                            col_row.append(str("<tr>%s%s</tr>" % (''.join(col_data),''.join(table_data))))
                                        table_rows.append("""%s%s%s""" % (''.join(range_head_str),''.join(table_head),''.join(col_row)))
                            
                                    table_html_string = """
                                                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                                                <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                                                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                                                <table class="table-borderless table-responsive card-1 p-4">%s</table> """ % ''.join(str(table_rows))
                                    st.markdown((((''.join(table_html_string).replace("'","")).replace(",","")).replace("[","")).replace("]",""), unsafe_allow_html=True)
                                
                                # table_rows = []
                                
                                # table_data = """<tr><td style="background-color: #FCBCBE;">Loose</td></tr>
                                #                 <tr><td style="background-color: #C4E6CD;">Tight</td></tr>
                                #                 <tr><td style="background-color: #FFFFFF;">Same</td></tr>"""
                                # st.markdown("""
                                #         <style>
                                #             div.sticky_bar {
                                #                 position: fixed;
                                #                 bottom: 60px;
                                #                 right: 0;
                                #                 width: 100px;
                                #                 }
                                #             </style>
                                #     """, unsafe_allow_html=True)
                                # table_html_string = """
                                #     <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                                #     <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                                #     <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                                #     <div class="sticky_bar"><table class="table-borderless table-responsive card-1 p-4">%s</table></div>""" % ''.join(str(table_data))
                                
                                # st.markdown((((''.join(table_html_string).replace("'","")).replace(",","")).replace("[","")).replace("]",""), unsafe_allow_html=True) 
                            
                                get_sticky(selected_lab, selected_shape, selected_band, selected_color, selected_purity, selected_fls, selected_polish,selected_cut,selected_symm)

                                expander_col2.markdown("<br/>", unsafe_allow_html=True)
                                expander_col2.markdown(str('<div style="text-align-last: end; font-weight: bold; padding-bottom:0; margin-bottom: 0;">Report Generated At: ' + str(datetime.today().replace(microsecond=0)) + '</div>'), unsafe_allow_html=True)
                                expander_col3.markdown("<br/>", unsafe_allow_html=True)
                                expander_col3.markdown(str('<div style="text-align-last: end; font-weight: bold; padding-bottom:0; margin-bottom: 0;">Last Updated: ' + str(list(temp_data1['last_updated'].unique())[0]) + '</div>'), unsafe_allow_html=True)
                                # get_rap_formate(temp_data)
                        else:
                            selected_chart_comp,selected_chart_comp2 = select_comp2()
                            expander_col1,expander_col2,expander_col3 = expander1.columns([1,2,2])
                            if expander_col1.button("View Report"):
                                print(str(str(datetime.today().replace(microsecond=0)) + " | " + str(local_ip) + " | " + str(selected_report_type)))
                                log(selected_report_type,selected_start_date,selected_end_date,selected_shape,selected_color,selected_purity,selected_fls,selected_band,f'Company: {selected_chart_comp}')
                                create_db_log(selected_report_type,selected_start_date,selected_end_date,selected_shape,selected_color,selected_purity,selected_fls,selected_band, selected_chart_comp, selected_chart_comp2, None, None, selected_lab,None,None,None,None,None,None,None,None,None,None,None,None,local_ip)
                                # FILTER DATA BY USER SELECTED
                                temp_data = filter_data_with_user_selected(df3, selected_lab, selected_shape, selected_band, selected_color, selected_purity, selected_fls, selected_polish,selected_cut,selected_symm)
                                
                                # filter_data_with_user_selected.clear()
                                try:
                                    if selected_chart_comp == selected_chart_comp2:
                                        st.warning("Please Select Different Company.")
                                    elif selected_chart_comp == None:
                                        sum_of_count_crt_net_value(temp_data,selected_chart_comp2,selected_lab, selected_shape, selected_band, selected_color, selected_purity, selected_fls, selected_polish,selected_cut,selected_symm)
                                    elif selected_chart_comp2 == None:
                                        sum_of_count_crt_net_value(temp_data,selected_chart_comp,selected_lab, selected_shape, selected_band, selected_color, selected_purity, selected_fls, selected_polish,selected_cut,selected_symm)
                                    else:
                                        col1, col2 = st.columns([1,1])
                                        with col1:
                                            sum_of_count_crt_net_value(temp_data,selected_chart_comp,selected_lab, selected_shape, selected_band, selected_color, selected_purity, selected_fls, selected_polish,selected_cut,selected_symm)
                                        with col2:
                                            sum_of_count_crt_net_value(temp_data,selected_chart_comp2,selected_lab, selected_shape, selected_band, selected_color, selected_purity, selected_fls, selected_polish,selected_cut,selected_symm)                                    
                                except:
                                    st.error("Data Filter is Missing.....")
                                get_sticky(selected_lab, selected_shape, selected_band, selected_color, selected_purity, selected_fls, selected_polish,selected_cut,selected_symm)

                                expander_col2.markdown("<br/>", unsafe_allow_html=True)
                                expander_col2.markdown(str('<div style="text-align-last: end; font-weight: bold; padding-bottom:0; margin-bottom: 0;">Report Generated At: ' + str(datetime.today().replace(microsecond=0)) + '</div>'), unsafe_allow_html=True)
                                expander_col3.markdown("<br/>", unsafe_allow_html=True)
                                expander_col3.markdown(str('<div style="text-align-last: end; font-weight: bold; padding-bottom:0; margin-bottom: 0;">Last Updated: ' + str(list(temp_data['last_updated'].unique())[0]) + '</div>'), unsafe_allow_html=True)
                    else:
                        # EXECUTE HTML CODE 
                        st.error("Data Not Found!")
                else:
                    st.warning("Please Select Company!")
            # except:
            #     st.error("Please Select Proper Month!")
            else:
                # EXECUTE HTML CODE 
                st.error("Please Select Proper Month!")
        don = pass_class()

    # =========================== Report Selection Cut Redefine ===========================
    elif report=="Cut Redefine" and team_email[email] == password:
        with open("\\\\Sfs.net\\BIA\\BIA_FT\\shani\\project\\web site\\Cut_Redefined\\assests\\Pricing Sample.xlsx", "rb") as f:
            st.sidebar.download_button("Sample File", data=f, file_name="sample.xlsx")

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

        if name is not None:
            df = code_a.call(filepath)
            create_db_log(None,None,None,None,None,None,None,None, None, None, None, None, None,None,None,None,None,None,None,None,None,None,None,filepath,None,local_ip)
            st.dataframe(df)
            excel_data = create_excel_file(df)
            st.download_button(label='Download Excel File', data=excel_data, file_name='Price Data.xlsx', mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    
    # =========================== Report Selection Pricing ===========================
    elif report=="Pricing" and team_email[email] == password:
        with open("\\\\Sfs.net\\BIA\\BIA_FT\\shani\\project\\web site\\pricing\\assests\\Pricing Sample.xlsx", "rb") as f:
            st.sidebar.download_button("Sample File", data=f, file_name="sample.xlsx")

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
           
        #path = st.text_input("Give filepath:")
        if name is not None:
            create_db_log(None,None,None,None,None,None,None,None, None, None, None, None, None,None,None,None,None,None,None,None,None,None,None,filepath,None,local_ip)
            df = sys_disc.call(filepath)
            st.dataframe(df)
            excel_data = create_excel_file(df)
            st.download_button(label='Download Excel File', data=excel_data, file_name='data.xlsx', mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    
    # =========================== Report Selection Light ===========================
    elif report=="Light" and light_email[email] == password:
        
        def create_excel_file(df):
            output = BytesIO()
            writer = pd.ExcelWriter(output, engine='xlsxwriter')
            df.to_excel(writer, index=False, sheet_name='Sheet1')
            writer.close()  # Close the Excel writer object
            output.seek(0) 
            return output.getvalue()

        def calculate_color_percentages(image):
    
            if image.shape[2] == 4:
                image = cv2.cvtColor(image, cv2.COLOR_BGRA2RGB)
            else:
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            pixels = image.reshape((-1, 3))
            pixels = [tuple(pixel) for pixel in pixels if np.any(pixel)]
            
            if not pixels:  
                return {"Red": 0, "Green": 0, "Blue": 0, "White": 0, "Black": 0}
            
            primary_color_counts = {"Red": 0, "Green": 0, "Blue": 0, "White": 0, "Black": 0}
            for pixel in pixels:
                r, g, b = pixel
                if r > 220 and g > 220 and b > 220:
                    primary_color_counts["White"] += 1
                elif r < 30 and g < 30 and b < 30:
                    primary_color_counts["Black"] += 1
                elif max(r, g, b) == r:
                    primary_color_counts["Red"] += 1
                elif max(r, g, b) == g:
                    primary_color_counts["Green"] += 1
                elif max(r, g, b) == b:
                    primary_color_counts["Blue"] += 1
            
            total_pixels = len(pixels)
            return {color: (count / total_pixels) * 100 for color, count in primary_color_counts.items()}
        
        def calculate_color_counts(image):
            if image.shape[2] == 4:
                image = cv2.cvtColor(image, cv2.COLOR_BGRA2RGB)
            else:
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            pixels = image.reshape((-1, 3))
            pixels = [tuple(pixel) for pixel in pixels if np.any(pixel)]

            if not pixels:
                return {"Red": 0, "Green": 0, "Blue": 0, "White": 0, "Black": 0}

            primary_color_counts = {"Red": 0, "Green": 0, "Blue": 0, "White": 0, "Black": 0}
            for pixel in pixels:
                r, g, b = pixel
                if r > 220 and g > 220 and b > 220:
                    primary_color_counts["White"] += 1
                elif r < 30 and g < 30 and b < 30:
                    primary_color_counts["Black"] += 1
                elif max(r, g, b) == r:
                    primary_color_counts["Red"] += 1
                elif max(r, g, b) == g:
                    primary_color_counts["Green"] += 1
                elif max(r, g, b) == b:
                    primary_color_counts["Blue"] += 1

            return primary_color_counts
        
        def calculate_normalized_proportions(row_color_counts, total_color_counts):
            normalized_proportions = {
                color: (row_color_counts[color] / total_pixels) * 100 if total_color_counts[color] != 0 else 0
                for color in total_color_counts
            }
            return normalized_proportions

        def draw_grid(image, rows, cols):
        
            image_with_grid = image.copy()

            height, width, _ = image_with_grid.shape
            for i in range(1, rows):
                cv2.line(image_with_grid, (0, i * height // rows), (width, i * height // rows), (0, 255, 0), 2)
            for j in range(1, cols):
                cv2.line(image_with_grid, (j * width // cols, 0), (j * width // cols, height), (0, 255, 0), 2)

            return image_with_grid
        
        option = st.sidebar.selectbox("Select Shape",['OV','OV4',"MQ","PS"])
        picture = st.file_uploader('Browse',accept_multiple_files=True)
        path = st.text_input("Give filepath:")
        
        if st.button("Check Light"):
            create_db_log(None,None,None,None,None,None,None,None, None, None, None, None, None,None,None,None,None,None,None,option,None,None,None,path,str(picture),local_ip)
            if len(picture)==1:
                name = None
                if picture is None:
                    st.text("Upload Picture")
                else:
                    name = picture[0].name

                if name is not None:
                    filepath = os.path.join(path, name)
                    image = cv2.imread(filepath)
                    
                    image = remove(image)
                    rows, cols = 12, 12

                    total_color_counts = calculate_color_counts(image)
                    total_pixels = sum(total_color_counts.values())
                    overall_color_percentages = calculate_color_percentages(image)

                    row_proportions = []
                    row_boundaries = np.linspace(0, image.shape[0], rows + 1)
                    row_boundaries = np.round(row_boundaries).astype(int)

                    for i in range(rows):
                        if (i==5) | (i==6):
                            start_row = row_boundaries[i]
                            end_row = row_boundaries[i+1]
                            grid_row = image[start_row:end_row, :, :]
                            row_color_counts = calculate_color_counts(grid_row)
                            proportions = calculate_normalized_proportions(row_color_counts, total_color_counts)
                            row_proportions.append(proportions)
                    
                    df = pd.DataFrame(row_proportions)
                    val = [5,6]
                    insert_index = df.columns.get_loc('Red')
                    df.insert(insert_index,'Sr_No',val)
                    
                    data = df.iloc[0] + df.iloc[1]
                    new_df = pd.DataFrame([data], columns=df.columns)
                    image_with_grid = draw_grid(image, rows, cols)
                    overall_df = pd.DataFrame([overall_color_percentages])
                    overall_df = overall_df.round(2)
                    bluef = round(overall_df['Blue'].iloc[0],2)
                    redf = round(overall_df['Red'].iloc[0],2)
                    greenf = round(overall_df['Green'].iloc[0],2)
                    whitef = round(overall_df['White'].iloc[0],2)
                    blackf = round(overall_df['Black'].iloc[0],2)

                    new_df = new_df.round(2)

                    if option == 'OV' or option == 'MQ':
                        col1,col2 = st.columns([1,1])
                        bluee = round(new_df['Blue'].iloc[0],2)
                        redd = round(new_df['Red'].iloc[0],2)
                        greenn = round(new_df['Green'].iloc[0],2)
                        whitee = round(new_df['White'].iloc[0],2)
                        blackk = round(new_df['Black'].iloc[0],2)
                        

                        m=proportion_ov_middle2.determine_light(whitee,blackk,bluee,redd,greenn)
                                    
                        middle_light = proportion_ov_middle2.light_m(m)

                        m2 = proportion_ov_copy2.determine_light(bluef,redf,greenf,blackf)
        
                        overall_light = proportion_ov_copy2.light(m2)
                        light_blue=proportion_ov_copy2.determine_blue_light(bluef)
                        x=proportion_ov_copy2.blue_new(light_blue)
                        X=int(x)
                        str1 = str(X)
                        str2 = "Light_blue: "
                        str1 =str( str2 + str1)
                        if middle_light>overall_light:
                            
                            li = middle_light
                        elif X >= overall_light:
                            
                            li =X  
                        else:
                            li = middle_light

                        with col1:
                            st.header(f"Light Blue: {X}")
                        with col2:
                            st.header(f"Final_light: {li}")
                    
                        with col1:
                            st.header("Full Proportion")
                            st.dataframe(overall_df[overall_df.columns[overall_df.loc[0].argsort()[::-1]]])
                        with col2:
                            st.header("Grid Row Wise Proportion")
                            st.dataframe(new_df)

                    elif option == 'OV4':
                        col1,col2 = st.columns([1,1])
                        bluee = round(new_df['Blue'].iloc[0],2)
                        redd = round(new_df['Red'].iloc[0],2)
                        greenn = round(new_df['Green'].iloc[0],2)
                        whitee = round(new_df['White'].iloc[0],2)
                        blackk = round(new_df['Black'].iloc[0],2)

                        m=proportion_ov4_middle2.determine_light(whitee,blackk,bluee,redd,greenn)
                            
                        middle_light = proportion_ov4_middle2.light_m(m)

                        m2 = proportion_ov4_copy2.determine_light(bluef,redf,greenf,whitef,blackf)
        
                        overall_light = proportion_ov4_copy2.light(m2)
                        
                        light_blue=proportion_ov4_copy2.determine_blue_light(bluef)
                        x=proportion_ov4_copy2.blue_new(light_blue)
                        X = [int(item) for item in x]  # Converts all elements of the list to integers

                        st.text(X)
                        str1 = str(x)
                        str2 = "Light_blue: "
                        str1 =str( str2 + str1)
                        st.text(str1)
                        st.text("final_light")

                        light=[]
                        if middle_light > overall_light:
                            light= middle_light
                        elif any(item >= overall_light for item in X):
                            light=X
                        else:
                            light= middle_light

                        with col1:
                            st.header(f"Light Blue: {X}")
                            st.header("Full Proportion")
                            st.dataframe(overall_df[overall_df.columns[overall_df.loc[0].argsort()[::-1]]])
                        with col2:
                            st.header(f"Final_light: {light}")
                            st.header("Grid Row Wise Proportion")
                            st.dataframe(new_df)

                    elif option == 'PS':
                        col1,col2 = st.columns([1,1])
                        image = cv2.imread(filepath)

                        image = remove(image)
                        rows, cols = 13,13

                        total_color_counts = calculate_color_counts(image)
                        total_pixels = sum(total_color_counts.values())
                        overall_color_percentages = calculate_color_percentages(image)

                        row_proportions2 = []
                        row_boundaries = np.linspace(0, image.shape[0], rows + 1)
                        row_boundaries = np.round(row_boundaries).astype(int)

                        for i in range(rows):
                            if (i==3) | (i==4)|(i==5):
                                start_row = row_boundaries[i]
                                end_row = row_boundaries[i+1]
                                grid_row = image[start_row:end_row, :, :]
                                row_color_counts = calculate_color_counts(grid_row)
                                proportions = calculate_normalized_proportions(row_color_counts, total_color_counts)
                                row_proportions2.append(proportions)
                        
                        df2 = pd.DataFrame(row_proportions2)
                        val = [3,4,5]
                        insert_index = df2.columns.get_loc('Red')
                        df2.insert(insert_index,'Sr_No',val)

                        data2 = df2.iloc[0] + df2.iloc[1]+df2.iloc[2]
                        new_df2 = pd.DataFrame([data2], columns=df2.columns)
                        new_df2 = new_df2.round(2)   


                        image_with_grid = draw_grid(image, rows, cols)
                        overall_df = pd.DataFrame([overall_color_percentages])
                        overall_df = overall_df.round(2)
                    
                        bluef = round(overall_df['Blue'].iloc[0],2)

                        whitef = round(overall_df['White'].iloc[0],2)
                        blackf = round(overall_df['Black'].iloc[0],2)


                        
                        bluee = round(new_df2['Blue'].iloc[0],2)

                        whitee = round(new_df2['White'].iloc[0],2)

                        m=proportion_ps_middle.determine_light(whitee,bluee)
                                    
                        middle_light = proportion_ps_middle.light_m(m)

                        m2 = proportion_ps_copy.determine_light(bluef,whitef,blackf)   
                        overall_light = proportion_ps_copy.light(m2)

                        
                        light_blue=proportion_ps_copy.determine_blue_light(bluef)
                        x=proportion_ps_copy.blue_new(light_blue)
                        X=int(x)
                        str1 = str(X)
                        str2 = "Light_blue: "
                        str1 =str( str2 + str1)
                        if middle_light >= overall_light:
                            Y=middle_light
                        elif X >= overall_light:
                            
                            Y=X
                        else:
                            
                            Y= overall_light
                        with col1:
                            st.header(f"Light Blue: {X}")
                        with col2:
                            st.header(f"Final_light: {Y}")
                        with col1:
                            st.header("Full Proportion")
                            st.dataframe(overall_df[overall_df.columns[overall_df.loc[0].argsort()[::-1]]])
                        with col2:
                            st.header("Grid Row Wise Proportion")
                            st.dataframe(new_df2)       
                    st.image(cv2.cvtColor(image_with_grid, cv2.COLOR_BGR2RGB), caption='Image with Grid', use_column_width=True)
                else:
                    pass
            else:
                overall_df = pd.DataFrame()
                packet_no=[]
                pack=[]
                red1=[]
                Red=[]
                Green=[]
                Blue=[]
                Black=[]
                White=[]
                green1=[]
                blue1=[]
                white1=[]
                black1=[]
                final_light_df = pd.DataFrame()
                
                File_name = []
                Light_blue = []
                Final_light = []

                if option != 'PS':
                    for filename in picture:
                        name = filename.name
                        if (name.endswith('.jpg')) | (name.endswith('.png')) | (name.endswith('.JPG')) | (name.endswith('.PNG')):
                            filepath = os.path.join(path, name)
                            image = cv2.imread(filepath)
                            rows, cols = 12, 12

                            total_color_counts = calculate_color_counts(image)
                            total_pixels = sum(total_color_counts.values())
                            overall_color_percentages = calculate_color_percentages(image)

                            overall_df = pd.DataFrame([overall_color_percentages])
                            dataa = overall_df.iloc[0]
                            pack.append(name)
                            Red.append(dataa[0])
                            Green.append(dataa[1])
                            Blue.append(dataa[2])
                            White.append(dataa[3])
                            Black.append(dataa[4])

                            row_proportions = []
                            row_boundaries = np.linspace(0, image.shape[0], rows + 1)
                            row_boundaries = np.round(row_boundaries).astype(int)

                            for i in range(rows):
                                if (i==5) | (i==6):
                                    start_row = row_boundaries[i]
                                    end_row = row_boundaries[i+1]
                                    grid_row = image[start_row:end_row, :, :]
                                    row_color_counts = calculate_color_counts(grid_row)
                                    proportions = calculate_normalized_proportions(row_color_counts, total_color_counts)
                                    row_proportions.append(proportions)
                            
                            df = pd.DataFrame(row_proportions)
                            val = [5,6]
                            insert_index = df.columns.get_loc('Red')
                            df.insert(insert_index,'Sr_No',val)
                            
                            data = df.iloc[0] + df.iloc[1]
                            
                            packet_no.append(name)
                            red1.append(data[1])
                            green1.append(data[2])
                            blue1.append(data[3])
                            white1.append(data[4])
                            black1.append(data[5])

                    new_df = pd.DataFrame()
                    new_overall_df = pd.DataFrame()
                    new_overall_df['Packet_No']=pack
                    new_overall_df['Full_Red'] = Red
                    new_overall_df['Full_Green'] = Green
                    new_overall_df['Full_Blue'] = Blue
                    new_overall_df['Full_White'] = White
                    new_overall_df['Full_Black'] = Black
                    new_df['Packet_No']= packet_no
                    new_df['Middle_Red'] = red1
                    new_df['Middle_Green'] = green1
                    new_df['Middle_Blue'] = blue1
                    new_df['Middle_White'] = white1
                    new_df['Middle_Black'] = black1 

                    new_overall_df = new_overall_df.sort_values(["Packet_No"])
                    new_df = new_df.sort_values(["Packet_No"])

                    
                    for i in range(len(new_df)):
                        if option == 'OV' or option == 'MQ':
                            # middle light
                            bluee = round(new_df['Middle_Blue'].iloc[i],2)
                            redd = round(new_df['Middle_Red'].iloc[i],2)
                            greenn = round(new_df['Middle_Green'].iloc[i],2)
                            whitee = round(new_df['Middle_White'].iloc[i],2)
                            blackk = round(new_df['Middle_Black'].iloc[i],2)
                            
                            m=proportion_ov_middle2.determine_light(whitee,blackk,bluee,redd,greenn)                
                            middle_light = proportion_ov_middle2.light_m(m)

                            # full light
                            bluef = round(new_overall_df['Full_Blue'].iloc[i],2)
                            redf = round(new_overall_df['Full_Red'].iloc[i],2)
                            greenf = round(new_overall_df['Full_Green'].iloc[i],2)
                            blackf = round(new_overall_df['Full_Black'].iloc[i],2)

                            m2 = proportion_ov_copy2.determine_light(bluef,redf,greenf,blackf)
                            overall_light = proportion_ov_copy2.light(m2)
                            light_blue=proportion_ov_copy2.determine_blue_light(bluef)
                            
                            x=proportion_ov_copy2.blue_new(light_blue)
                            X=int(x)
                            str1 = str(X)
                            
                            if middle_light>overall_light:
                                li = middle_light
                            elif X >= overall_light:
                                li =X  
                            else:
                                li = middle_light

                            # create data frame
                            if new_df['Packet_No'].iloc[i] == new_overall_df['Packet_No'].iloc[i]:
                                File_name.append(new_df['Packet_No'].iloc[i])
                                Light_blue.append(X)
                                Final_light.append(li)

                        elif option == 'OV4':
                            # middle light
                            bluee = round(new_df['Middle_Blue'].iloc[i],2)
                            redd = round(new_df['Middle_Red'].iloc[i],2)
                            greenn = round(new_df['Middle_Green'].iloc[i],2)
                            whitee = round(new_df['Middle_White'].iloc[i],2)
                            blackk = round(new_df['Middle_Black'].iloc[i],2)

                            m=proportion_ov4_middle2.determine_light(whitee,blackk,bluee,redd,greenn)
                                    
                            middle_light = proportion_ov4_middle2.light_m(m)
                            
                            # full light
                            bluef = round(new_overall_df['Full_Blue'].iloc[i],2)
                            redf = round(new_overall_df['Full_Red'].iloc[i],2)
                            greenf = round(new_overall_df['Full_Green'].iloc[i],2)
                            blackf = round(new_overall_df['Full_Black'].iloc[i],2)
                            whitef = round(new_overall_df['Full_White'].iloc[i],2)

                            m2 = proportion_ov4_copy2.determine_light(bluef,redf,greenf,whitef,blackf)
                
                            overall_light = proportion_ov4_copy2.light(m2)
                            
                            light_blue=proportion_ov4_copy2.determine_blue_light(bluef)
                            x=proportion_ov4_copy2.blue_new(light_blue)
                            st.write("X")
                            X = [int(item) for item in x]  # Converts all elements of the list to integers

                            light=[]
                            if middle_light > overall_light:
                                light= middle_light
                            elif any(item >= overall_light for item in X):
                                light=X
                            else:
                                light= middle_light

                            # create data frame
                            if new_df['Packet_No'].iloc[i] == new_overall_df['Packet_No'].iloc[i]:
                                File_name.append(new_df['Packet_No'].iloc[i])
                                Light_blue.append(X)
                                Final_light.append(light)
                elif option == 'PS':
                    for filename in picture:
                        name = filename.name
                        if (name.endswith('.jpg')) | (name.endswith('.png')) | (name.endswith('.JPG')) | (name.endswith('.PNG')):
                            filepath = os.path.join(path, name)
                            image = cv2.imread(filepath)

                            image = remove(image)
                            rows, cols = 13,13

                            total_color_counts = calculate_color_counts(image)
                            total_pixels = sum(total_color_counts.values())
                            overall_color_percentages = calculate_color_percentages(image)

                            overall_df = pd.DataFrame([overall_color_percentages])
                            dataa = overall_df.iloc[0]
                            pack.append(name)
                            Red.append(dataa[0])
                            Green.append(dataa[1])
                            Blue.append(dataa[2])
                            White.append(dataa[3])
                            Black.append(dataa[4])

                            row_proportions2 = []
                            row_boundaries = np.linspace(0, image.shape[0], rows + 1)
                            row_boundaries = np.round(row_boundaries).astype(int)

                            for i in range(rows):
                                if (i==3) | (i==4)|(i==5):
                                    start_row = row_boundaries[i]
                                    end_row = row_boundaries[i+1]
                                    grid_row = image[start_row:end_row, :, :]
                                    row_color_counts = calculate_color_counts(grid_row)
                                    proportions = calculate_normalized_proportions(row_color_counts, total_color_counts)
                                    row_proportions2.append(proportions)
                            
                            df2 = pd.DataFrame(row_proportions2)
                            val = [3,4,5]
                            insert_index = df2.columns.get_loc('Red')
                            df2.insert(insert_index,'Sr_No',val)

                            data2 = df2.iloc[0] + df2.iloc[1] + df2.iloc[2]

                            packet_no.append(name)
                            red1.append(data2[1])
                            green1.append(data2[2])
                            blue1.append(data2[3])
                            white1.append(data2[4])
                            black1.append(data2[5])
                    new_df = pd.DataFrame()
                    new_overall_df = pd.DataFrame()
                    new_overall_df['Packet_No']=pack
                    new_overall_df['Full_Red'] = Red
                    new_overall_df['Full_Green'] = Green
                    new_overall_df['Full_Blue'] = Blue
                    new_overall_df['Full_White'] = White
                    new_overall_df['Full_Black'] = Black
                    new_df['Packet_No']= packet_no
                    new_df['Middle_Red'] = red1
                    new_df['Middle_Green'] = green1
                    new_df['Middle_Blue'] = blue1
                    new_df['Middle_White'] = white1
                    new_df['Middle_Black'] = black1 
                    
                    new_overall_df = new_overall_df.sort_values(["Packet_No"])
                    new_df = new_df.sort_values(["Packet_No"])
                    
                    
                    for i in range(len(new_df)):
                        
                        # middle light
                        bluee = round(new_df['Middle_Blue'].iloc[i],2)
                        whitee = round(new_df['Middle_White'].iloc[i],2)

                        m=proportion_ps_middle.determine_light(whitee,bluee)
                                        
                        middle_light = proportion_ps_middle.light_m(m)

                        # full light
                        bluef = round(new_overall_df['Full_Blue'].iloc[i],2)
                        blackf = round(new_overall_df['Full_Black'].iloc[i],2)
                        whitef = round(new_overall_df['Full_White'].iloc[i],2)

                        m2 = proportion_ps_copy.determine_light(bluef,whitef,blackf)   
                        overall_light = proportion_ps_copy.light(m2)

                        light_blue=proportion_ps_copy.determine_blue_light(bluef)
                        x=proportion_ps_copy.blue_new(light_blue)
                        X=int(x)

                        if middle_light >= overall_light:
                            Y=middle_light
                        elif X >= overall_light:
                            Y=X
                        else:
                            Y= overall_light
                        
                        # create data frame
                        if new_df['Packet_No'].iloc[i] == new_overall_df['Packet_No'].iloc[i]:
                            File_name.append(new_df['Packet_No'].iloc[i])
                            Light_blue.append(X)
                            Final_light.append(Y)

                final_light_df['File_name'] = File_name
                final_light_df['Light_blue'] = Light_blue
                final_light_df['Final_light'] = Final_light

                st.write(final_light_df)
                st.download_button(
                    label="Download Data",
                    data=create_excel_file(final_light_df),
                    file_name="Light Data.xlsx",
                    mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                )
    else:
        st.error("User and Password is incorrect")