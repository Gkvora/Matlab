import streamlit as st
#@st.cache_data(show_spinner="Processing File")
def call(filepath,sheetname,last_updated_date):
    import streamlit as st
    with st.spinner("Processing  File"):   
        import time
        from datetime import datetime,date
        curr_date = date.today()
        import numpy as np 
        import warnings 
        warnings.filterwarnings('ignore')
        import pandas as pd
        import pyodbc # type: ignore
        conn1 = pyodbc.connect(Driver="{ODBC Driver 18 for SQL Server}", Server="192.168.70.146\\FSD",
                            Database="SALE_DISC", UID="analysis", port="1433", PWD="ai@2021",encrypt="no", autocommit=True)
        fancy = pd.read_excel(filepath,sheet_name=f'{sheetname}')
        print("/*/*/*/*/",fancy.columns)

        # print(filepath)
        # print(sheetname)
        print(len(fancy['Packet No']))
        a = list(fancy['Packet No'].astype(str))
        a = ";".join(a)
        Query1 = f"EXEC dbo.SP_GET_REPORT_DATA_FILL_TEST \
                            @FROM_DATE= '2020-01-01', \
                            @TO_DATE= '{curr_date}', \
                            @COMP_NO= '1', \
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
        all = pd.read_sql(Query1, conn1)
        all.sort_values(by=['PACKET_NO','TRANS_DATE'],ascending=[True,False],inplace=True)
        all.drop_duplicates(subset= 'PACKET_NO',inplace=True)
        print(all.shape,"/*/*/***")
        new_all = all.rename(columns={'COMP_NO':'CNO','X_LAB':'Lab','SHAPE':'Shape','WGT':'Carat','COLOR':'Color','PURITY':'Clarity','POLISH':'Pol','SYMM':'Sym','FLS':'Fls','CALC_NET_RATE':'NEW ARRIVAL PRICE','TYPE':'Type','TRANS_DATE':'New arrival Date','MFG_LOCATION':'Mfg Location','LENGTH':'Length','WIDTH':'Width','DEPTH_PER':'Depth %','TABLE_PER':'Table%','RATIO':'Ratio','PACKET_NO':'Packet No',"COLOR_DESC":"SET"})
        new_all['Rap_Range'] = '-'
        #new_all['SET'] = '-'
        new_all['COL_GROUP'] = '-'
        new_all['Sale Date'] = new_all['New arrival Date']
        new_all['SALE  OR CURRENT PRICE'] =new_all['NEW ARRIVAL PRICE']
        new_all['SET'] =new_all.apply(lambda x: x['COLOR_ACTUAL'] if x['SET']=="" else x['SET'],axis=1)
        new_all['Color'] = new_all['SET'].replace({'FY': 'FANCY YELLOW EVEN','FPP': 'FANCY PINK PURPLE','FLPK': 'FANCY LIGHT PINK, EVEN',
                                            'FIY': 'FANCY INTENSE YELLOW','FY': 'FANCY YELLOW','FVY': 'FANCY VIVID YELLOW','FLY': 'FANCY LIGHT YELLOW',
                                            'FLBY': 'FANCY LIGHT BROWNISH YELLOW','BLUE': 'FANCY LIGHT BLUE','INT YEL':'FANCY INTENSE YELLOW',
                                                'FPB':'FANCY LIGHT PINKISH BROWN','PINK':'FANCY LIGHT PURPLISH PINK','VLP':'VERY LIGHT PINK',
                                            'FLBGY':'FANCY BROWNISH GRENISH YELLOW','VLG':'VERY LIGHT GREY','FGB':'FANCY GRAYISH BLUE',
                                            'FBY':'FANCY BROWNISH YELLOW','FP':'FANCY PINK','FB':'FANCY BLUE','FLG':'FANCY LIGHT GREY',
                                            'YEL':'FANCY YELLOW EVEN','GY':'VERY LIGHT PINK','FBGY':'FANCY BROWNISH GRENISH YELLOW',
                                            'LGY':'LIGHT GRAY'
                })
        new_all['Color'] = new_all['Color'].replace({'FANCY YELLOW EVEN':'FANCY YELLOW'})
        new_all = new_all[['CNO','Lab','Packet No','Shape','Carat','Rap_Range','Color',"SET",'COL_GROUP','Clarity','Pol','Sym','Fls','NEW ARRIVAL PRICE','SALE  OR CURRENT PRICE','Type','New arrival Date','Sale Date','Mfg Location','Length','Width','Ratio','Depth %','Table%']]

        Query2 = f"EXEC dbo.SP_GET_REPORT_DATA_FILL_TEST \
                            @FROM_DATE= '{last_updated_date}', \
                            @TO_DATE= '{curr_date}', \
                            @COMP_NO= '1', \
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

        new_arr = pd.read_sql(Query2, conn1)
        new_df = new_arr.copy()
        # new_df['COLOR'] = new_df['COLOR'].str.replace(r'[+-]', '', regex=True)
        new_df = new_df[~new_df['COLOR'].isin(['D', 'E', 'F', 'G', 'H','I', 'J','K','L','M','Q-R','O-P', 'U-V','N','S-T','YZ','Y-Z','FT','LT','VL','IN','QR','ST','OP',"W-X"])]
        #new_df['LAB_Sort'] = np.where(new_df['LAB']=='GIA',1,2)
        new_df.sort_values(by=['PACKET_NO','TRANS_DATE'],ascending=[True,False],inplace=True)
        new_df.drop_duplicates(subset= 'PACKET_NO',inplace=True)
        new_df.rename(columns={'PACKET_NO':'Packet No'},inplace=True)
        new_df['TRANS_DATE'] = pd.to_datetime(new_df['TRANS_DATE'])
        new_df = new_df.rename(columns={'COMP_NO':'CNO','X_LAB':'Lab','SHAPE':'Shape','WGT':'Carat','COLOR':'Color','PURITY':'Clarity','POLISH':'Pol','SYMM':'Sym','FLS':'Fls','CALC_NET_RATE':'NEW ARRIVAL PRICE','TYPE':'Type','TRANS_DATE':'New arrival Date','MFG_LOCATION':'Mfg Location','LENGTH':'Length','WIDTH':'Width','DEPTH_PER':'Depth %','TABLE_PER':'Table%','RATIO':'Ratio','PACKET_NO':'Packet No',"COLOR_DESC":"SET"})
        new_df['Rap_Range'] = '-'
        # new_df['SET'] = '-'
        new_df['COL_GROUP'] = '-'
        new_df['Sale Date'] = new_df['New arrival Date']
        new_df['SALE  OR CURRENT PRICE'] =new_df['NEW ARRIVAL PRICE']
        new_df['SET'] =new_df.apply(lambda x: x['COLOR_ACTUAL'] if x['SET']=="" else x['SET'],axis=1)
        new_df['Color'] = new_df['SET'].replace({'FY': 'FANCY YELLOW EVEN','FPP': 'FANCY PINK PURPLE','FLPK': 'FANCY LIGHT PINK, EVEN',
                                            'FIY': 'FANCY INTENSE YELLOW','FY': 'FANCY YELLOW','FVY': 'FANCY VIVID YELLOW','FLY': 'FANCY LIGHT YELLOW',
                                            'FLBY': 'FANCY LIGHT BROWNISH YELLOW','BLUE': 'FANCY LIGHT BLUE','INT YEL':'FANCY INTENSE YELLOW',
                                                'FPB':'FANCY LIGHT PINKISH BROWN','PINK':'FANCY LIGHT PURPLISH PINK','VLP':'VERY LIGHT PINK',
                                            'FLBGY':'FANCY BROWNISH GRENISH YELLOW','VLG':'VERY LIGHT GREY','FGB':'FANCY GRAYISH BLUE',
                                            'FBY':'FANCY BROWNISH YELLOW','FP':'FANCY PINK','FB':'FANCY BLUE','FLG':'FANCY LIGHT GREY',
                                            'YEL':'FANCY YELLOW EVEN','GY':'VERY LIGHT PINK','FBGY':'FANCY BROWNISH GRENISH YELLOW',
                                            'LGY':'LIGHT GRAY'
                })       

        new_dff = new_df[['CNO','Lab','Packet No','Shape','Carat','Rap_Range','Color',"SET",'COL_GROUP','Clarity','Pol','Sym','Fls','NEW ARRIVAL PRICE','SALE  OR CURRENT PRICE','Type','New arrival Date','Sale Date','Mfg Location','Length','Width','Ratio','Depth %','Table%'
        ]]####,'Mfg Location' ,'New arriva lDate' ,'NEW ARRIVAL PRICE'

        b = list(new_df['Packet No'].astype(str))
        b = ";".join(b)
        if b!="":
            print("Hi")
            Query1 = f"EXEC dbo.SP_GET_REPORT_DATA_FILL_TEST \
                                @FROM_DATE= '2020-01-01', \
                                @TO_DATE= '{curr_date}', \
                                @COMP_NO= '1', \
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
            new = pd.read_sql(Query1, conn1)
            
            new_=new.copy()
            new_.sort_values(by=['PACKET_NO','TRANS_DATE'],ascending=[True,False],inplace=True)
            new_.drop_duplicates(subset= 'PACKET_NO',inplace=True)
            
            new_ = new_.rename(columns={'COMP_NO':'CNO','X_LAB':'Lab','SHAPE':'Shape','WGT':'Carat','COLOR':'Color','PURITY':'Clarity','POLISH':'Pol','SYMM':'Sym','FLS':'Fls','CALC_NET_RATE':'NEW ARRIVAL PRICE','TYPE':'Type','TRANS_DATE':'New arrival Date','MFG_LOCATION':'Mfg Location','LENGTH':'Length','WIDTH':'Width','DEPTH_PER':'Depth %','TABLE_PER':'Table%','RATIO':'Ratio','PACKET_NO':'Packet No',"COLOR_DESC":"SET"})
            new_['Rap_Range'] = '-'
            #new_['SET'] = '-'
            new_['COL_GROUP'] = '-'
            new_['Sale Date'] = new_['New arrival Date']
            new_['SALE  OR CURRENT PRICE'] =new_['NEW ARRIVAL PRICE']
            new_['SET'] =new_.apply(lambda x: x['COLOR_ACTUAL'] if x['SET']=="" else x['SET'],axis=1)
            new_['Color'] = new_['SET'].replace({'FY': 'FANCY YELLOW EVEN','FPP': 'FANCY PINK PURPLE','FLPK': 'FANCY LIGHT PINK, EVEN',
                                                'FIY': 'FANCY INTENSE YELLOW','FY': 'FANCY YELLOW','FVY': 'FANCY VIVID YELLOW','FLY': 'FANCY LIGHT YELLOW',
                                                'FLBY': 'FANCY LIGHT BROWNISH YELLOW','BLUE': 'FANCY LIGHT BLUE','INT YEL':'FANCY INTENSE YELLOW',
                                                    'FPB':'FANCY LIGHT PINKISH BROWN','PINK':'FANCY LIGHT PURPLISH PINK','VLP':'VERY LIGHT PINK',
                                                'FLBGY':'FANCY BROWNISH GRENISH YELLOW','VLG':'VERY LIGHT GREY','FGB':'FANCY GRAYISH BLUE',
                                                'FBY':'FANCY BROWNISH YELLOW','FP':'FANCY PINK','FB':'FANCY BLUE','FLG':'FANCY LIGHT GREY',
                                                'YEL':'FANCY YELLOW EVEN','GY':'VERY LIGHT PINK','FBGY':'FANCY BROWNISH GRENISH YELLOW',
                                                'LGY':'LIGHT GRAY'
                    })
            new_ = new_[['CNO','Lab','Packet No','Shape','Carat','Rap_Range','Color',"SET",'COL_GROUP','Clarity','Pol','Sym','Fls','SALE  OR CURRENT PRICE','Type','New arrival Date','Sale Date','Mfg Location','Length','Width','Ratio','Depth %','Table%'
            ]]####,'Mfg Location' ,'New arriva lDate' ,'NEW ARRIVAL PRICE'

        for_merge_file=new_df.iloc[:,[5,7,97]]
        for_merge_file.rename(columns={'New arrival Date':'TRANS_DATE'},inplace=True)

        if b!="":
            new_df1 = pd.merge(new_,for_merge_file,how='left',on='Packet No')
            new_df1['New arrival Date'] = new_df1["TRANS_DATE"]
            new_df1['NEW ARRIVAL PRICE'] = new_df1["NEW ARRIVAL PRICE"]
            new_final = new_df1[['CNO','Lab','Packet No','Shape','Carat','Rap_Range','Color',"SET",'COL_GROUP','Clarity','Pol','Sym','Fls',"NEW ARRIVAL PRICE",'SALE  OR CURRENT PRICE','Type','New arrival Date','Sale Date','Mfg Location','Length','Width','Ratio','Depth %','Table%']]
            Query1 = f"EXEC dbo.SP_GET_REPORT_DATA_FILL_TEST \
                                @FROM_DATE= '2020-01-01', \
                                @TO_DATE= '{curr_date}', \
                                @COMP_NO= '1', \
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
            new_date = pd.read_sql(Query1, conn1)
            new_date.sort_values(by=['PACKET_NO','TRANS_DATE'],ascending=[True,False],inplace=True)
            new_date.drop_duplicates(subset= 'PACKET_NO',inplace=True)
            new_date.rename(columns={'PACKET_NO':'Packet No'},inplace=True)
            new_all = pd.merge(new_all,new_date,how='left',on='Packet No')
            new_all.drop(columns=['New arrival Date','NEW ARRIVAL PRICE'],inplace=True)
            new_all.rename(columns={'TRANS_DATE':'New arrival Date','CALC_NET_RATE':'NEW ARRIVAL PRICE'},inplace=True)
            
            new_all =new_all[['CNO','Lab','Packet No','Shape','Carat','Rap_Range','Color',"SET",'COL_GROUP','Clarity','Pol','Sym','Fls',"NEW ARRIVAL PRICE",'SALE  OR CURRENT PRICE','Type','New arrival Date','Sale Date','Mfg Location','Length','Width','Ratio','Depth %','Table%']]
            
            new_final['New arrival Date'] = new_final['New arrival Date'].astype(str)
            final = pd.concat([new_final,new_all])
            final['Sale Date'] = final['Sale Date'].astype(str)
            new_final['Sale Date'] = new_final['Sale Date'].astype(str)

        else:
            #new_final['New arrival Date'] = new_final['New arrival Date'].astype(str)
            final = new_all.copy()
            final['Sale Date'] = final['Sale Date'].astype(str)
            new_final = pd.DataFrame(columns=[final.columns])
            
        #new_final['New arrival Date'] = new_final['New arrival Date'].astype(str)
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
        final['Rap_Range'] = final['Carat'].apply(categorize_carat)   
        new_final['Rap_Range'] = new_final['Carat'].apply(categorize_carat) 
        final.reset_index(drop=True,inplace=True)


        
        
        return new_final,final
