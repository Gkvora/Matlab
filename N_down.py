import streamlit as st
#@st.cache_data(show_spinner="Processing File")
def callndown(filepath,sheetname,last_updated_date):
    with st.spinner("Processing  File"):

        import pandas as pd
        import numpy as np
        import warnings
        import pyodbc # type: ignore
        warnings.filterwarnings('ignore')
        from datetime import date

        # n_down = pd.read_excel(r"F:\Fancy_Col -DISCUSS UPDATED  06-09.xlsx",skiprows=2,sheet_name='N-' )
        n_down = pd.read_excel(filepath,sheet_name=f'{sheetname}' )

        pd.set_option('display.max_columns',None)
        n_down.head(3)
        current_date = date.today()

        # new_arrival
        # NEW ARRIVAL
        conn1 = pyodbc.connect(Driver="{ODBC Driver 18 for SQL Server}", Server="192.168.70.146\\FSD",
                                Database="SALE_DISC", UID="analysis",Encrypt="no", port="1433", PWD="ai@2021", autocommit=True)
        sqlquery1 = f"""EXEC dbo.SP_GET_REPORT_DATA_FILL_TEST 
                    @FROM_DATE = '{last_updated_date}', 
                    @TO_DATE = '{current_date}', 
                    @COMP_NO= '1', 
                    @STOCK_TYPE = '1', 
                    @PACKET_NO ='' , 
                    @SIZE = '', 
                    @SHAPE = '', 
                    @COLOR = '', 
                    @PURITY = '', 
                    @CUT = '', 
                    @POLISH = '', 
                    @SYMM = '', 
                    @FLS = '', 
                    @X_LAB = NULL, 
                    @FILLTYPE = 'NEW'"""

        NA = pd.read_sql(sqlquery1, conn1)

        NA['sort'] = NA['X_LAB'].apply(lambda x: 1 if x=='GIA' else 2)
        NA =  NA.sort_values(by=['PACKET_NO','sort','TRANS_DATE'],ascending=[True,True,False])
        NA = NA.drop_duplicates(subset='PACKET_NO')
        NA = NA[NA['COLOR'].isin(['N','O-P', 'Y-Z', 'U-V', 'W-X', 'S-T','Q-R',"N","O","P","Q",
                                "R","S","T","U","V","W","X","Y","Z"])]
        NA.shape

        n_down[n_down.columns[2]] = n_down[n_down.columns[2]].astype(str)
        na_price_per_carat = pd.merge(NA,n_down.iloc[:,[2,10]],left_on='PACKET_NO',right_on=n_down.columns[2],how= 'left')
        na_price_per_carat = na_price_per_carat.drop(columns='Packet No')

        na_price_per_carat['Price/ct'] = np.where(na_price_per_carat['Price/ct'].isna()==True,na_price_per_carat['CALC_NET_RATE'],na_price_per_carat['Price/ct'])
        na_price_per_carat.to_clipboard()

        new_arrival = na_price_per_carat.copy()
        new_arrival = new_arrival.rename(columns={'X_LAB':'Lab',
                                    'ROWNO':'SrNo',
                                    'SHAPE':'Shape',
                                    'WGT':'Carat',
                                    'PACKET_NO':'Packet No',
                                    'COLOR':'Col',
                                    'PURITY':'Clarity',
                                    'CALC_NET_RATE':'Sale or Current Price',
                                    'CALC_DISC_PER':'Disc %',
                                    'POLISH':'Pol',
                                    'RATE':'Rap.($)',
                                    'SYMM':'Sym',
                                    'FLS':'Fls',
                                    'STAGE':'STAGE1',
                                    'TYPE':'STAGE',
                                    'TRANS_DATE':'Sale date',
                                    'LENGTH':'Length',
                                    'WIDTH':'Width',
                                    'DEPTH_PER':'Depth %',
                                    'TABLE_PER':'Table %',
                                    'RATIO':'Ratio'})
        new_arrival['Rap_Range'] = '-'
        new_arrival.rename(columns={'PACKET_NO':'Packet No'},inplace=True)
        new_arrival = new_arrival[['SrNo', 'Lab', 'Packet No', 'Shape', 'Carat', 'Rap_Range', 'Col',
            'Clarity', 'Rap.($)', 'Disc %', 'Price/ct', 'Sale or Current Price',
            'Pol', 'Sym', 'Fls', 'STAGE', 'Sale date', 'Length', 'Width', 'Ratio',
            'Depth %', 'Table %']]
        print(len(new_arrival.columns))
        n_down.reset_index(drop=True, inplace=True)
        new_arrival.reset_index(drop=True, inplace=True)
        n_down = pd.concat([n_down,new_arrival])
        # n_down = n_down['SrNo'].reset_index(inplace=True)
        print(n_down.shape)
        n_down.to_clipboard()

        all_packets = []
        for i in (n_down['Packet No']):
            all_packets.append(i)

        all_packets = n_down['Packet No'].astype(str).tolist()
        all_packets_string = ";".join(all_packets)
        print(len(all_packets_string))  # Output the final string

        # STOCK
        # conn1 = pyodbc.connect(Driver="{ODBC Driver 17 for SQL Server}", Server="192.168.70.146\\FSD",
        #                         Database="SALE_DISC", UID="analysis",Encrypt="no", port="1433", PWD="ai@2021", autocommit=True)
        sqlquery1 = f"""EXEC dbo.SP_GET_REPORT_DATA_FILL_TEST 
                    @FROM_DATE = '2020-01-01', 
                    @TO_DATE = '{current_date}', 
                    @COMP_NO= '1', 
                    @STOCK_TYPE = '4', 
                    @PACKET_NO ='{all_packets_string}' , 
                    @SIZE = '', 
                    @SHAPE = '', 
                    @COLOR = '', 
                    @PURITY = '', 
                    @CUT = '', 
                    @POLISH = '', 
                    @SYMM = '', 
                    @FLS = '', 
                    @X_LAB = NULL, 
                    @FILLTYPE = 'NEW'"""

        stock = pd.read_sql(sqlquery1, conn1)
        stock.shape

        stock['sort'] = stock['X_LAB'].apply(lambda x: 1 if x=='GIA' else 2)
        # stock =  stock.sort_values(by=['TRANS_DATE','PACKET_NO','sort'],ascending=[False,True,True]) 
        stock = stock.sort_values(by=['PACKET_NO','sort','TRANS_DATE'],ascending=[True,True,False]) 
        stock = stock.drop_duplicates(subset='PACKET_NO')
        stock.shape

        # n_down.iloc[:,[2]].head()
        print(stock['PACKET_NO'].dtype)
        print(n_down[n_down.columns[2]].dtype)
        n_down[n_down.columns[2]] = n_down[n_down.columns[2]].astype(str)

        price_per_carat = pd.merge(stock,n_down.iloc[:,[2,10]],left_on='PACKET_NO',right_on=n_down.columns[2],how= 'left')
        price_per_carat = price_per_carat.drop(columns='Packet No')

        df = price_per_carat.copy()
        df = df.rename(columns={'X_LAB':'Lab',
                                    'ROWNO':'SrNo',
                                    'SHAPE':'Shape',
                                    'WGT':'Carat',
                                    'PACKET_NO':'Packet No',
                                    'COLOR':'Col',
                                    'PURITY':'Clarity',
                                    'CALC_NET_RATE':'Sale or Current Price',
                                    'CALC_DISC_PER':'Disc %',
                                    'POLISH':'Pol',
                                    'RATE':'Rap.($)',
                                    'SYMM':'Sym',
                                    'FLS':'Fls',
                                    'STAGE':'STAGE1',
                                    'TYPE':'STAGE',
                                    'TRANS_DATE':'Sale date',
                                    'LENGTH':'Length',
                                    'WIDTH':'Width',
                                    'DEPTH_PER':'Depth %',
                                    'TABLE_PER':'Table %',
                                    'RATIO':'Ratio'})
        df['Rap_Range'] = '-'
        # df['Price/ct'] = n_down['Price/ct']
        df.rename(columns={'PACKET_NO':'Packet No'},inplace=True)

        df = df[['SrNo', 'Lab', 'Packet No', 'Shape', 'Carat', 'Rap_Range', 'Col',
            'Clarity', 'Rap.($)', 'Disc %', 'Price/ct', 'Sale or Current Price',
            'Pol', 'Sym', 'Fls', 'STAGE', 'Sale date', 'Length', 'Width', 'Ratio',
            'Depth %', 'Table %']]
        print(len(df.columns))

        df['sort'] = df['Lab'].apply(lambda x: 1 if x=='GIA' else 2)
        df =  df.sort_values(by=['Packet No','sort','Sale date'],ascending=[True,True,False])
        df = df.drop_duplicates(subset='Packet No')
        df = df.drop(columns='sort')
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
            
        df['Rap_Range'] = df['Carat'].apply(categorize_carat)
        new_arrival['Rap_Range'] = new_arrival['Carat'].apply(categorize_carat)
        new_arrival_packets = list(new_arrival['Packet No'])
        new_arr = df[df['Packet No'].isin(new_arrival_packets)]
        dff=  df[~df['Packet No'].isin(new_arrival_packets)]
        df= pd.concat([new_arr,dff])
        seqq=range(1,len(df)+1) 
        df.drop(columns=['SrNo'],inplace=True)
        df['SrNo'] = seqq
        #df.rename(columns={'Price/ct':'NEW ARRIVAL PRICE'},inplace=True)
        df = df[['SrNo', 'Lab', 'Packet No', 'Shape', 'Carat', 'Rap_Range', 'Col',
            'Clarity', 'Rap.($)', 'Disc %', 'Price/ct', 'Sale or Current Price',
            'Pol', 'Sym', 'Fls', 'STAGE', 'Sale date', 'Length', 'Width', 'Ratio',
            'Depth %', 'Table %']]
        df.to_clipboard()
        return df,new_arrival
    

