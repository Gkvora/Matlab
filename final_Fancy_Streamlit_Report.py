import streamlit as st
import time
# python -m streamlit run "G:/Gautam/Streamlit/final_Fancy_Streamlit Report.py"
#  python -m streamlit run "\\sfs.net\bia\BIA_FT\PARIKSHIT\Project\Fancy_stream\main.py"
#@st.cache_data(show_spinner="Processing File")

def callcn2(filepath,sheetname,last_updated_date):
    import streamlit as st
    with st.spinner("Processing  File"):
        import pyodbc # type: ignore
        import pandas as pd
        import numpy as np
        import datetime 
        from datetime import date
        import re
        import warnings
        warnings.filterwarnings('ignore')
        curr_date = date.today()
        conn1 = pyodbc.connect(Driver="{ODBC Driver 18 for SQL Server}", Server="192.168.70.146\\FSD",
                                Database="SALE_DISC", UID="analysis", port="1433", PWD="ai@2021", autocommit=True,encrypt="no")

        fancy = pd.read_excel(filepath,sheet_name=f'{sheetname}')
        fancy['Packet No'] = fancy['Packet No'].astype(str)
        a = list(fancy['Packet No'].str.replace(".0",""))
        a = ";".join(a) 
        
        ##1 change date as per sold list dates:
        Query1 = f"EXEC dbo.SP_GET_REPORT_DATA_FILL_TEST \
                                    @FROM_DATE= '2020-01-01', \
                                    @TO_DATE= '{curr_date}', \
                                    @COMP_NO= '2', \
                                    @STOCK_TYPE = '4', \
                                    @PACKET_NO = '{a}', \
                                    @SIZE = '', \
                                    @SHAPE = '', \
                                    @COLOR = '', \
                                    @PURITY = '', \
                                    @CUT = '', \
                                    @POLISH = '', \
                                    @SYMM = '', \
                                    @FLS = '', \
                                    @X_LAB = NULL, \
                                    @FILLTYPE = 'NEW' "
        stock = pd.read_sql(Query1, conn1)

        stock.sort_values(by=['PACKET_NO','TRANS_DATE'],ascending=[True,False],inplace=True)
        stock.drop_duplicates(subset= 'PACKET_NO',inplace=True)

        stock_1 = stock.rename(columns={'PACKET_NO':'Packet No','COMP_NO':'CNO','X_LAB':'Lab','SHAPE':'Shape','WGT':'Carat','COLOR':'Col','PURITY':'Clarity','POLISH':'Pol','SYMM':'Sym','FLS':'Fls','TYPE':'Type','TRANS_DATE':'New arriva lDate','MFG_LOCATION':'Mfg Location','LENGTH':'Length','WIDTH':'Width','DEPTH_PER':'Depth %','TABLE_PER':'Table%','RATIO':'Ratio'})
        stock_1['Rap_Range'] = '-'
        stock_1['SET'] = stock_1['COLOR_DESC']
        stock_1['COL_GROUP'] = '-'
        stock_1['Sale Date'] = stock_1['New arriva lDate']
        stock_1['SALE  OR CURRENT PRICE'] =stock_1['CALC_NET_RATE']
        stock_1['SET'] =stock_1.apply(lambda x: x['COLOR_ACTUAL'] if x['SET']=="" else x['SET'],axis=1)
        stock_1 = stock_1[['CNO','Lab','Packet No','Shape','Carat','Rap_Range','Col','SET','COL_GROUP','Clarity','Pol','Sym','Fls','SALE  OR CURRENT PRICE','Type','Sale Date','Length','Width','Ratio','Depth %','Table%']]

        Query3 = f"EXEC dbo.SP_GET_REPORT_DATA_FILL_TEST \
                                    @FROM_DATE= '{last_updated_date}', \
                                    @TO_DATE= '{curr_date}', \
                                    @COMP_NO= '2', \
                                    @STOCK_TYPE = '1', \
                                    @PACKET_NO ='' , \
                                    @SIZE = '', \
                                    @SHAPE = '', \
                                    @COLOR = '', \
                                    @PURITY = '', \
                                    @CUT = '', \
                                    @POLISH = '', \
                                    @SYMM = '', \
                                    @FLS = '', \
                                    @X_LAB = NULL, \
                                    @FILLTYPE = 'NEW' "

        New = pd.read_sql(Query3, conn1)

        df_New = New.copy() 
        df3_New = df_New[~df_New['COLOR'].isin(['D', 'E', 'F', 'G', 'H','I', 'J','K','L','M','Q-R','O-P', 'U-V','N','S-T','Y-Z','YZ','FT','LT','VL','IN','QR','ST','OP','W-X'])]
        df3_New['COLOR'] = df3_New['COLOR'].replace(r'[+-]', '', regex=True)
        df3_New = df3_New[~df3_New['COLOR'].isin(['D', 'E', 'F', 'G', 'H','I', 'J','K','L','M','Q-R','O-P', 'U-V','N','S-T','Y-Z','YZ','FT','LT','VL','IN','QR','ST','OP','W-X'])]
        df3_New.sort_values(by=['PACKET_NO','TRANS_DATE'],ascending=[True,False],inplace=True)
        df3_New.drop_duplicates(subset= 'PACKET_NO',inplace=True)
        df3_New.rename(columns={'PACKET_NO':'Packet No'},inplace=True)
        df3_New['TRANS_DATE'] = pd.to_datetime(df3_New['TRANS_DATE'])

        stock_2 = df3_New.rename(columns={'PACKET_NO':'Packet No','COMP_NO':'CNO','X_LAB':'Lab','SHAPE':'Shape','WGT':'Carat','COLOR':'Col','PURITY':'Clarity','POLISH':'Pol','SYMM':'Sym','FLS':'Fls','CALC_NET_RATE':'NEW ARRIVAL PRICE','TYPE':'Type','TRANS_DATE':'New arriva lDate','MFG_LOCATION':'Mfg Location','LENGTH':'Length','WIDTH':'Width','DEPTH_PER':'Depth %','TABLE_PER':'Table%','RATIO':'Ratio'})
        stock_2['Rap_Range'] = '-'
        stock_2['SET'] = '-'
        stock_2['COL_GROUP'] = '-'
        stock_2['Sale Date'] = stock_2['New arriva lDate']
        stock_2['SALE  OR CURRENT PRICE'] =stock_2['NEW ARRIVAL PRICE']
        stock_2 = stock_2[['CNO','Lab','Packet No','Shape','Carat','Rap_Range','Col','SET','COL_GROUP','Clarity','Pol','Sym','Fls','NEW ARRIVAL PRICE','SALE  OR CURRENT PRICE','Type','Sale Date','Length','Width','Ratio','Depth %','Table%']]

        b = list(stock_2['Packet No'].astype(str))
        b = ";".join(b)
        if b!="":
            ## change date as per sold list dates:
            Query4 = f"EXEC dbo.SP_GET_REPORT_DATA_FILL_TEST \
                                        @FROM_DATE= '2020-01-01', \
                                        @TO_DATE= '{curr_date}', \
                                        @COMP_NO= '2', \
                                        @STOCK_TYPE = '4', \
                                        @PACKET_NO = '{b}', \
                                        @SIZE = '', \
                                        @SHAPE = '', \
                                        @COLOR = '', \
                                        @PURITY = '', \
                                        @CUT = '', \
                                        @POLISH = '', \
                                        @SYMM = '', \
                                        @FLS = '', \
                                        @X_LAB = NULL, \
                                        @FILLTYPE = 'NEW' "
            new = pd.read_sql(Query4, conn1)

            new.sort_values(by=['PACKET_NO','TRANS_DATE'],ascending=[True,False],inplace=True)
            new.drop_duplicates(subset= 'PACKET_NO',inplace=True)

            stock_3 = new.rename(columns={'PACKET_NO':'Packet No','COMP_NO':'CNO','X_LAB':'Lab','SHAPE':'Shape','WGT':'Carat','COLOR':'Col','PURITY':'Clarity','POLISH':'Pol','SYMM':'Sym','FLS':'Fls','CALC_NET_RATE':'NEW ARRIVAL PRICE','TYPE':'Type','TRANS_DATE':'New arriva lDate','MFG_LOCATION':'Mfg Location','LENGTH':'Length','WIDTH':'Width','DEPTH_PER':'Depth %','TABLE_PER':'Table%','RATIO':'Ratio'})
            stock_3['Rap_Range'] = '-'
            stock_3['SET'] = stock_3['COLOR_DESC']
            stock_3['COL_GROUP'] = '-'
            stock_3['Sale Date'] = stock_3['New arriva lDate']
            stock_3['SALE  OR CURRENT PRICE'] =stock_3['NEW ARRIVAL PRICE']
            stock_3['SET'] =stock_3.apply(lambda x: x['COLOR_ACTUAL'] if x['SET']=="" else x['SET'],axis=1)
            stock_3 = stock_3[['CNO','Lab','Packet No','Shape','Carat','Rap_Range','Col','SET','COL_GROUP','Clarity','Pol','Sym','Fls','SALE  OR CURRENT PRICE','Type','Sale Date','Length','Width','Ratio','Depth %','Table%']]

        for_merge_file = stock_2.iloc[:,[2,13]]

        if b!="":
            new_df1 = pd.merge(stock_3,for_merge_file,how='left',on='Packet No')
            New_Arrival_Data = new_df1[['CNO','Lab','Packet No','Shape','Carat','Rap_Range','Col','SET','COL_GROUP','Clarity','Pol','Sym','Fls','NEW ARRIVAL PRICE','SALE  OR CURRENT PRICE','Type','Sale Date','Length','Width','Ratio','Depth %','Table%']]

            ## change date as per sold list dates:
            Query2 = f"EXEC dbo.SP_GET_REPORT_DATA_FILL_TEST \
                                        @FROM_DATE= '2020-01-01', \
                                        @TO_DATE= '{curr_date}', \
                                        @COMP_NO= '2', \
                                        @STOCK_TYPE = '1', \
                                        @PACKET_NO = '{a}', \
                                        @SIZE = '', \
                                        @SHAPE = '', \
                                        @COLOR = '', \
                                        @PURITY = '', \
                                        @CUT = '', \
                                        @POLISH = '', \
                                        @SYMM = '', \
                                        @FLS = '', \
                                        @X_LAB = NULL, \
                                        @FILLTYPE = 'NEW' "
            new123 = pd.read_sql(Query2, conn1)     
            
            new123.sort_values(by=['PACKET_NO','TRANS_DATE'],ascending=[True,False],inplace=True)
            new123.drop_duplicates(subset= 'PACKET_NO',inplace=True)    

            new_price_df = new123.iloc[:,[7,97]] 
            new_price_df = new_price_df.rename(columns={'PACKET_NO':'Packet No','CALC_NET_RATE':'NEW ARRIVAL PRICE'})
            print("GKGKGKGKGKGKGKGKGKGKGKGK")
            stock_1_final = pd.merge(stock_1,new_price_df,how='left',on='Packet No')
            stock_1_final = stock_1_final[['CNO','Lab','Packet No','Shape','Carat','Rap_Range','Col','SET','COL_GROUP','Clarity','Pol','Sym','Fls','NEW ARRIVAL PRICE','SALE  OR CURRENT PRICE','Type','Sale Date','Length','Width','Ratio','Depth %','Table%']]
 
            print(stock_1.shape)
  
            #New_Arrival_Data_1 = New_Arrival_Data.drop('NEW ARRIVAL PRICE',axis=1)  

            FINAL_DATAFRAME = pd.concat([New_Arrival_Data,stock_1_final])
        else:
            print("GKGKGKGKGKGKGKGKGKGKGKGK")
            FINAL_DATAFRAME = stock_1.copy()
            New_Arrival_Data = pd.DataFrame(columns=[FINAL_DATAFRAME.columns])

        def categorize_carat(carat):
            if carat < 0.04:
                return "0.01 - 0.03"
            elif carat < 0.08:
                return "0.04 - 0.07"
            elif carat < 0.15:
                return "0.08 - 0.14"
            elif carat < 0.18:
                return "0.15 - 0.17"
            elif carat < 0.23:
                return "0.18 - 0.22"
            elif carat < 0.30:
                return "0.23 - 0.29"
            elif carat < 0.40:
                return "0.30 - 0.39"
            elif carat < 0.50:
                return "0.40 - 0.49"
            elif carat < 0.70:
                return "0.50 - 0.69"
            elif carat < 0.90:
                return "0.70 - 0.89"
            elif carat < 1.00:
                return "0.90 - 0.99"
            elif carat < 1.50:
                return "1.00 - 1.49"
            elif carat < 2.00:
                return "1.50 - 1.99"
            elif carat < 3.00:
                return "2.00 - 2.99"
            elif carat < 4.00:
                return "3.00 - 3.99"
            elif carat < 5.00:
                return "4.00 - 4.99"
            else:
                return "5.00 - 99.99"
        FINAL_DATAFRAME['Rap_Range'] = FINAL_DATAFRAME['Carat'].apply(categorize_carat)   
        New_Arrival_Data['Rap_Range'] = New_Arrival_Data['Carat'].apply(categorize_carat)  
        return New_Arrival_Data,FINAL_DATAFRAME    










































