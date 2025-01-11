def call(file_path):
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    import warnings
    warnings.filterwarnings('ignore')

    pln = pd.read_excel(file_path)
    pln.rename(columns={'No.':'NO','No':'NO'},inplace=True)
    #seqq = range(1, len(pln) + 1)
    #seqq = list(seqq)
    #pln['Sr_No'] =seqq
    df=pln.copy()

    # columns_to_check = ['KEY_TO_SYMBOL']
    # if not any(col_name in pln.columns for col_name in columns_to_check):
    #     pln['KEY_TO_SYMBOL'] = np.nan
        
    # columns_to_check = ['SHADE','Shade']
    # if not any(col_name in pln.columns for col_name in columns_to_check):
    #     pln['SHADE'] = np.nan
    # columns_to_check = ['TO']
    # if not any(col_name in pln.columns for col_name in columns_to_check):
    #     pln['TO'] = np.nan
    # columns_to_check = ['PO']
    # if not any(col_name in pln.columns for col_name in columns_to_check):
    #     pln['PO'] = np.nan
    # columns_to_check = ['CO']
    # if not any(col_name in pln.columns for col_name in columns_to_check):
    #     pln['CO'] = np.nan
    # columns_to_check = ['CN']
    # if not any(col_name in pln.columns for col_name in columns_to_check):
    #     pln['CN'] = np.nan
    # columns_to_check = ['CW']
    # if not any(col_name in pln.columns for col_name in columns_to_check):
    #     pln['CW'] = np.nan
    # columns_to_check = ['SN']
    # if not any(col_name in pln.columns for col_name in columns_to_check):
    #     pln['SN'] = np.nan
    # columns_to_check = ['SW']
    # if not any(col_name in pln.columns for col_name in columns_to_check):
    #     pln['SW'] = np.nan
    # columns_to_check = ['POLISH','Pol','POL']
    # if not any(col_name in pln.columns for col_name in columns_to_check):
    #     pln['POLISH'] = np.nan

    # columns_to_check = ['NO','No.']
    # if not any(col_name in pln.columns for col_name in columns_to_check):
    #     pln['NO'] = np.nan

    # columns_to_check = ['GIRDLE_PER', 'Girdle_per', 'Girdle (%)', 'Girdle %']
    # if not any(col_name in pln.columns for col_name in columns_to_check):
    #     pln['GIRDLE_PER'] = np.nan
    # columns_to_check = ['SYM', 'Sym']
    # if not any(col_name in pln.columns for col_name in columns_to_check):
    #     pln['SYM'] = np.nan

    # columns_to_check = ['CUT', 'Cut ','Cut']
    # if not any(col_name in pln.columns for col_name in columns_to_check):
    #     pln['CUT'] = np.nan
    # columns_to_check = ['COL', 'COLOR','Col','Color']
    # if not any(col_name in pln.columns for col_name in columns_to_check):
    #     pln['COLOR'] = np.nan
    # columns_to_check = ['FLS', 'fls','Fls']
    # if not any(col_name in pln.columns for col_name in columns_to_check):
    #     pln['FLS'] = np.nan
    # columns_to_check = ['RATIO', 'ratio','Ratio']
    # if not any(col_name in pln.columns for col_name in columns_to_check):
    #     pln['RATIO'] = np.nan
    # columns_to_check = ['EXP_CTS', 'CARAT' ,'Carat' ,'carat','Pol. Cts','Pol. Cts']
    # if not any(col_name in pln.columns for col_name in columns_to_check):
    #     pln['EXP_CTS'] = np.nan
    # columns_to_check = ['TABLE_PER', 'Table %','Table (%)']
    # if not any(col_name in pln.columns for col_name in columns_to_check):
    #     pln['TABLE_PER'] = np.nan
    # columns_to_check = ['DEPTH_PER', 'Depth %','Depth (%)']
    # if not any(col_name in pln.columns for col_name in columns_to_check):
    #     pln['DEPTH_PER'] = np.nan
    
    pln.rename(columns={'Unnamed: 0':'Sr_No','ROWNO':'NO','Shp':'SHAPE','COL':'COLOR','Col':'COLOR','Prty':'PURITY','Purity':'PURITY','Clarity':'PURITY','SYMM':'SYM','Fls':'FLS','shade':'SHADE',
                    'Cut':'CUT','Pol':'POLISH','length':'LENGTH','width':'WIDTH','Width':'WIDTH','Length':'LENGTH','Depth_Per':'DEPTH_PER','Table_Per':
                    'TABLE_PER','Ratio':'RATIO','ratio':'RATIO','Depth %':'DEPTH_PER','Table %':'TABLE_PER','Depth (%)':'DEPTH_PER','Table (%)':'TABLE_PER',
                    'WGT':'EXP_CTS','CARAT':'EXP_CTS','Carat':'EXP_CTS','FSD_TOP':'TO','FSD_COP':'CO','FSD_POP':'PO','FSD_CN':'CN','FSD_CW':'CW',
                    'FSD_SW':'SW','FSD_SN':'SN','Girdle %':'GIRDLE_PER','GIRDLE %':'GIRDLE_PER','Girdle (%)':'GIRDLE_PER','KEY_TO_SYMBOLS':'KEY_TO_SYMBOL',
                    'key_to_symbol':'KEY_TO_SYMBOL','Pol. Cts':'EXP_CTS','No.':'NO','Shape':'SHAPE','Color':'COLOR'},
            inplace=True)

    # pln = pln[['Sr_No', 'SHAPE','EXP_CTS', 'SHADE','COLOR', 'PURITY', 'CUT', 'POLISH', 'SYM', 'FLS', 'LENGTH', 'WIDTH',
    #         'DEPTH_PER', 'TABLE_PER', 'RATIO', 'CN', 'SN', 'CW', 'SW', 'GIRDLE_PER', 'KEY_TO_SYMBOL','TO','CO','PO','TYPE2CERT','LUSTER']]

    # old_columns = list(pln.columns[1:21])
    # new_columns = ["Pol. Cts", "Shp" ,"Shade","Col", "Prty", "Cut", "Pol", "Sym", "Fls",
    #             "Length", "Width", "Depth (%)", "Table (%)", "Ratio", "CN", "SN",
    #             "CW", "SW", "Girdle (%)", "KEY_TO_SYMBOLS"]
    print(pln.columns)
    pln.rename(columns={'EXP_CTS':'Pol. Cts','SHAPE':'Shp','SHADE':'Shade','COLOR':'Col','PURITY':'Prty',
                        'CUT':'Cut','POLISH':'Pol','SYM':'Sym','LENGTH':'Length','WIDTH':'Width','DEPTH_PER':'Depth (%)',
                        "TABLE_PER":"Table (%)","RATIO":"Ratio","CN":"CN","SN":"SN","CW":'CW', "SW":"SW", "GIRDLE_PER":"Girdle (%)","KEY_TO_SYMBOL":"KEY_TO_SYMBOLS","Cut ":"Cut",'FLS':'Fls'},inplace=True)
    # pln = pln.rename(columns=dict(zip(old_columns, new_columns)))
    # df=pln.copy()

    pln['Shp'] = pln['Shp'].apply(lambda x: 'OV' if x == 'OV4' else x)
    pln['Shp'] = pln['Shp'].apply(lambda x: 'RA' if x == 'RN' else x)

    pln['Col'] = pln['Col'].astype(str)
    # Replace '+' with an empty string in 'Col' and 'Prty' columns
    pln['Col'] = pln['Col'].replace('+', '', regex=False)
    pln['Prty'] = pln['Prty'].astype(str)
    pln['Prty'] = pln['Prty'].replace('+', '', regex=False)

    # Replace '-' with an empty string in 'Col' and 'Prty' columns
    pln['Col'] = pln['Col'].replace('-', '', regex=False)
    pln['Prty'] = pln['Prty'].replace('-', '', regex=False)

    allowed_values = ['D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']

    pln['Col'] = np.where(~pln['Col'].isin(allowed_values), 'M', pln['Col'])

    cut_mapping = {
        'X1': 'EX-1', 'X2': 'EX-2', 'X3': 'EX-3', 'X4': 'EX-3',
        'V1': 'VG-1', 'V2': 'VG-2',
        'G1': 'GD-1', 'G2': 'GD-2', 'G3': 'GD-3',
        'FR': 'FR', 'PR': 'PR'
    }

    print(pln.columns)
    pln['Cut'] = pln['Cut'].replace(cut_mapping)


    cut_mapping = {
        'EX': 'EX-2',
        'VG': 'VG-2',
        'GD': 'GD-2',
        'FR': 'FR',
        'PR': 'PR',
        '-': 'PR'
    }

    # Use np.where to mimic nested ifelse conditions
    pln['Cut'] = np.where(pln['Cut'] == 'EX', 'EX-2',
                        np.where(pln['Cut'] == 'VG', 'VG-2',
                                np.where(pln['Cut'] == 'GD', 'GD-2',
                                            np.where(pln['Cut'] == 'FR', 'FR',
                                                    np.where(pln['Cut'].isin(['PR', '-']), 'PR', pln['Cut'])
                                                    )
                                        )
                                )
                        )

    pln['Sym'] = pln['Sym'].replace({'X': 'EX', 'V': 'VG', 'G': 'GD'})

    # Replace values in 'Pol' column
    pln['Pol'] = pln['Pol'].replace({'X': 'EX', 'V': 'VG', 'G': 'GD'})
    
    print(pln['Pol. Cts'])
    # Create 'Carat' column
    pln['Carat'] = pln['Pol. Cts']

    # Filter out rows with non-null 'Shp' values
    pln = pln[pln['Shp'].notna()]

    import numpy as np

    carat_bins = np.array([0.179, 0.199, 0.229, 0.249, 0.299, 0.349, 0.399, 0.449, 0.499, 
                        0.599, 0.699, 0.749, 0.799, 0.849, 0.899, 0.949, 0.999, 1.009, 
                        1.099, 1.179, 1.299, 1.399, 1.479, 1.499, 1.599, 1.699, 1.799, 
                        1.899, 1.979, 1.999, 2.009, 2.099, 2.199, 2.299, 2.399, 2.499, 
                        2.599, 2.699, 2.799, 2.899, 2.979, 2.999, 3.009, 3.099, 3.199, 
                        3.399, 3.499, 3.699, 3.799, 3.899, 3.979, 3.999, 4.009, 4.099, 
                        4.199, 4.399, 4.499, 4.699, 4.799, 4.899, 4.979, 4.999, 5.009, 
                        5.499, 5.999, 6.009, 6.999, 7.009, 7.999, 8.009, 8.999, 9.009, 
                        9.999, 10.009, 14.999, 19.999, 24.999, 29.999])

    carat_range_labels = np.array(["0.150 - 0.179", "0.180 - 0.199", "0.200 - 0.229", "0.230 - 0.249",
                                    "0.250 - 0.299", "0.300 - 0.349", "0.350 - 0.399", "0.400 - 0.449",
                                    "0.450 - 0.499", "0.500 - 0.599", "0.600 - 0.699", "0.700 - 0.749",
                                    "0.750 - 0.799", "0.800 - 0.849", "0.850 - 0.899", "0.900 - 0.949",
                                    "0.950 - 0.999", "1.000 - 1.009", "1.010 - 1.099", "1.100 - 1.179",
                                    "1.180 - 1.299", "1.300 - 1.399", "1.400 - 1.479", "1.480 - 1.499",
                                    "1.500 - 1.599", "1.600 - 1.699", "1.700 - 1.799", "1.800 - 1.899",
                                    "1.900 - 1.979", "1.980 - 1.999", "2.000 - 2.009", "2.010 - 2.099",
                                    "2.100 - 2.199", "2.200 - 2.299", "2.300 - 2.399", "2.400 - 2.499",
                                    "2.500 - 2.599", "2.600 - 2.699", "2.700 - 2.799", "2.800 - 2.899",
                                    "2.900 - 2.979", "2.980 - 2.999", "3.000 - 3.009", "3.010 - 3.099",
                                    "3.100 - 3.199", "3.200 - 3.399", "3.400 - 3.499", "3.500 - 3.699",
                                    "3.700 - 3.799", "3.800 - 3.899", "3.900 - 3.979", "3.980 - 3.999",
                                    "4.000 - 4.009", "4.010 - 4.099", "4.100 - 4.199", "4.200 - 4.399",
                                    "4.400 - 4.499", "4.500 - 4.699", "4.700 - 4.799", "4.800 - 4.899",
                                    "4.900 - 4.979", "4.980 - 4.999", "5.000 - 5.009", "5.010 - 5.499",
                                    "5.500 - 5.999", "6.000 - 6.009", "6.010 - 6.999", "7.000 - 7.009",
                                    "7.010 - 7.999", "8.000 - 8.009", "8.010 - 8.999", "9.000 - 9.009",
                                    "9.010 - 9.999", "10.000 - 10.009", "10.010 - 14.999", "15.000 - 19.999",
                                    "20.000 - 24.999", "25.000 - 29.999", "30.000 - 99.999"])

    pln['Range'] = carat_range_labels[np.digitize(pln['Carat'], carat_bins, right=True)]


    pln['BASE_ID'] = pln['Shp'].astype(str) + pln['Range'].astype(str) + pln['Col'].astype(str) + pln['Prty'].astype(str)

    #pln['BASE_ID'] = pln['Shp'].astype(str) + pln['Range'].astype(str) + pln['Col'].astype(str) + pln['Prty'].astype(str)

    BASE_NEW = pd.read_excel("//sfs.net/bia/BIA_DWH/parameters/BASE PRICE.xlsx")

    pln = pd.merge(pln, BASE_NEW.iloc[:, [0, 5]], left_on='BASE_ID', right_on=BASE_NEW.columns[0])
    pln['BASE%'] = pln.iloc[:, -1].fillna(0)

    pln = pln.loc[:, ~pln.columns.isin(['BASE_ID'])]

    pln['Girdle %'] = pln['Girdle (%)']

    # Fill NA values in 'Girdle %' with 0
    pln['Girdle %'] = pln['Girdle %'].fillna(0)
    pln['No'] = np.where((pln['Girdle %']>7.95) & (pln['Girdle %']<=15.00) ,2,
                        np.where(pln['Girdle %']>6.15,1,""))
    pln['ID'] = pln['Shp'].astype(str)+pln['Fls'].astype(str)+pln['No'].astype(str)

    GIRDLE_DIS = pd.read_excel("//sfs.net/bia/BIA_DWH/parameters/g%Girdle_Per_Disc.xlsx")
    if 'DISC_PER' in pln.columns:
        pln.drop(columns=['DISC_PER'],inplace=True)
    if 'DISC_PER_x' in pln.columns:
        pln.drop(columns=['DISC_PER_x'],inplace=True)
    if 'DISC_PER_y' in pln.columns:
        pln.drop(columns=['DISC_PER_y'],inplace=True)
    pln= pd.merge(pln, GIRDLE_DIS[['ID', 'DISC_PER']], on='ID', how='left')
    pln.drop(columns=['ID','Girdle %','No'],inplace=True)
    pln.rename(columns={'DISC_PER':'GIRDLE %'},inplace=True)
    pln['GIRDLE %'] = pln['GIRDLE %'].fillna(0)
    pln['Shade1'] = np.select(
        [
            pln['Shade'] == "Br",
            pln['Shade'] == "FtBr",
            pln['Shade'] == "LtBr",
            (pln['Shade'] == "FtYlBr") | (pln['Shade'] == "FtBrYl"),
            pln['Shade'] == "LtYlB",
            pln['Shade'] == "LtGnY",
            pln['Shade'] == "FtGnYl",
            pln['Shade'] == "FtGr",
            (pln['Shade'] == "LB") | (pln['Shade'] == "BRN1"),
            pln['Shade'] == "GREY"
        ],
        [
            "BR", "FTBR", "LBR", "VYB", "LYB", "LGN", "VLG", "VGY", "BR", "GY"
        ],
        default=pln['Shade']
    )
    pln['ID2'] = np.where(pln['Carat'] < 1, '0.30 - 0.99', '1.00 - 99.99')

    pln['Shape1'] = np.where(pln['Shp'] == 'RD', 'ROUND', 'FANCY')


    pln['SHADE_ID'] = pln['Shape1'] + pln['Fls'] + pln['Shade1'] + pln['ID2'] + pln['Col'] + pln['Prty']

    SHADE_NEW = pd.read_excel("//sfs.net/bia/BIA_DWH/parameters/SHADE_DISC.xlsx")

    
    pln = pd.merge(pln, SHADE_NEW.iloc[:, [0, 7]], left_on='SHADE_ID', right_on=SHADE_NEW.columns[0],how='left')
  
    pln['SHADE%'] = pln.iloc[:, -1].fillna(0)
    
    pln = pln.loc[:, ~pln.columns.isin(['SHADE_ID'])]


    if 'Type IICert' in pln.columns:
        pln['TYPE2%'] = np.where(
            (pln['Type IICert'].isna() | (pln['Type IICert'] == "")), 0,
            np.where(
                (pln['Col'] == 'D') & (pln['Prty'] == 'FL') & (pln['Range'].isin(['1.000 - 1.009', '1.010 - 1.099'])), -5,
                np.where(
                    (pln['Col'] == 'D') & (pln['Prty'] == 'FL') & (~pln['Range'].isin(['1.000 - 1.009', '1.010 - 1.099'])), -3,
                    np.where(
                        (pln['Col'] == 'D') & (pln['Prty'] == 'IF'), -1,
                        np.where(
                            (pln['Col'] == 'E') & (pln['Prty'] == 'FL'), -1,
                            np.where(
                                (pln['Col'] == 'E') & (pln['Prty'] == 'IF'), -1, 0
                            )
                        )
                    )
                )
            )
        )
    else:
        pln['TYPE2%']=np.nan

    pln['CN'] = ['CN' + str(x) if x in [0, 1, 2, 3, 4] else x for x in pln['CN']]
    pln['SN'] = ['SN' + str(x) if x in [0, 1, 2, 3, 4] else x for x in pln['SN']]
    pln['CW'] = ['CW' + str(x) if x in [0, 1, 2, 3, 4] else x for x in pln['CW']]
    pln['SW'] = ['SW' + str(x) if x in [0, 1, 2, 3, 4] else x for x in pln['SW']]

    pln['CN'].replace({'CN0.0':'CN0','CN1.0':'CN1','CN2.0':'CN2','CN3.0':'CN3','CN4.0':'CN4'},inplace=True)
    pln['SN'].replace({'SN0.0':'SN0','SN1.0':'SN1','SN2.0':'SN2','SN3.0':'SN3','SN4.0':'SN4'},inplace=True)
    pln['CW'].replace({'CW0.0':'CW0','CW1.0':'CW1','CW2.0':'CW2','CW3.0':'CW3','CW4.0':'CW4'},inplace=True)
    pln['SW'].replace({'SW0.0':'SW0','SW1.0':'SW1','SW2.0':'SW2','SW3.0':'SW3','SW4.0':'SW4'},inplace=True)


    pln['S1'] = np.where(pln['Carat'] < 1, '0.30 - 0.99', '1.00 - 30.99')


    pln['clar'] = np.where(pln['Prty'].isin(['I1', 'I2', 'I3', 'I4']), 'I', pln['Prty'])
   
    pln['CN_ID'] = pln['Shp'].astype(str) + pln['S1'].astype(str) + pln['Prty'].astype(str) + pln['Fls'].astype(str) + pln['CN'].astype(str)

    CN_NEW = pd.read_excel("//sfs.net/bia/BIA_DWH/parameters/NATS_DISC.xlsx")

    pln = pd.merge(pln, CN_NEW.iloc[:, [0, 6]], left_on='CN_ID', right_on=CN_NEW.columns[0], how='left')
    pln['CN%'] = pln.iloc[:, -1].fillna(0)

    pln = pln.drop(columns=['CN_ID'])

    pln['CN%'] = pln['CN%'].fillna(0)
    
    # Create 'CW_ID' column
    pln['CW_ID'] = pln['Shp'].astype(str) + pln['clar'].astype(str) + pln['CW'].astype(str)

    pln['CW_ID'] = pln['Shp'].astype(str) + pln['clar'].astype(str) + pln['CW'].astype(str)

    CW_NEW = pd.read_excel("//sfs.net/bia/BIA_DWH/parameters/NATS_DISC.xlsx", sheet_name=1)


    pln = pd.merge(pln, CW_NEW.iloc[:, [0, 4]], left_on='CW_ID', right_on=CW_NEW.columns[0], how='left')
    pln['CW%'] = pln.iloc[:, -1].fillna(0)
    pln.drop(columns=['PER%_x'],inplace=True)
    pln = pln.drop(columns=['CW_ID'])

    pln['SN_ID'] = pln['Shp'].astype(str) + pln['clar'].astype(str) + pln['SN'].astype(str)

    SN_NEW = pd.read_excel("//sfs.net/bia/BIA_DWH/parameters/NATS_DISC.xlsx", sheet_name=2)

    pln = pd.merge(pln, SN_NEW.iloc[:, [0, 4]], left_on="SN_ID", right_on=SN_NEW.columns[0], how="left")

    pln['SN%'] = pln.iloc[:, -1]
   

    pln = pln.drop("SN_ID", axis=1)

    pln['SN%'].fillna(0, inplace=True)

    pln['SW_ID'] = pln['clar'].astype(str) + pln['SW'].astype(str)

    SW_NEW = pd.read_excel("//sfs.net/bia/BIA_DWH/parameters/NATS_DISC.xlsx", sheet_name=3)

    pln = pd.merge(pln, SW_NEW.iloc[:, [0, 3]], left_on='SW_ID', right_on=SW_NEW.columns[0], how='left')

    pln['SW%'] = pln.iloc[:, -1]


    pln['SW%'].fillna(0, inplace=True)
   
    pln = pln.drop(columns=['clar'])

    y1 = pln[['CN%', 'CW%', 'SN%', 'SW%']]

    # Add 'NATS%' column with maximum values of 'y1'
    pln['NATS%'] = y1.max(axis=1)

    def calculate_TO1(row):
        if row['TO'] == 'Y':
            if row['Prty'] == 'VVS2':
                return 0.25
            elif row['Prty'] == 'VS1':
                return 0.25
            elif row['Prty'] == 'VS2':
                return 0.25
            elif row['Prty'] == 'SI1':
                return 0.5
            elif row['Prty'] == 'SI2':
                return 0.5
            elif row['Prty'] == 'SI3':
                return 0.5
            elif row['Prty'] == 'I1':
                return 0.5
        return None

    # Apply the function to create the 'TO1' column
    pln['TO1'] = pln.apply(calculate_TO1, axis=1)

    def calculate_PO1(row):
        if row['PO'] == 'Y':
            if row['Prty'] == 'VS1':
                return 0.2
            elif row['Prty'] == 'VS2':
                return 0.2
            elif row['Prty'] == 'SI1':
                return 0.25
            elif row['Prty'] == 'SI2':
                return 0.25
            elif row['Prty'] == 'SI3':
                return 0.25
            elif row['Prty'] == 'I1':
                return 0.25
        return None

    # Apply the function to create the 'PO1' column
    pln['PO1'] = pln.apply(calculate_PO1, axis=1)

    def calculate_CO1(row):
        if row['CO'] == 'Y':
            if row['Prty'] == 'VS1':
                return 0.2
            elif row['Prty'] == 'VS2':
                return 0.25
            elif row['Prty'] == 'SI1':
                return 0.25
            elif row['Prty'] == 'SI2':
                return 0.25
            elif row['Prty'] == 'SI3':
                return 0.25
            elif row['Prty'] == 'I1':
                return 0.25
        return None

    # Apply the function to create the 'CO1' column
    pln['CO1'] = pln.apply(calculate_CO1, axis=1)

    pln['Depth %'] = pd.to_numeric(pln['Depth (%)']).round(2)
    print(any(pln['Depth %']))
    # print(pln['Depth %'].isin([None,""," ",False]))
    # print()
    if any(pln['Depth %']):
        pln['Depth %']=0
        pln['dpt_EM']=0
        pln['dpt_RN']=0
        pln['dpt_AS']=0
        pln['dpt_BG']=0
        pln['dpt_CM']=0
        pln['dpt_CS']=0
        pln['dpt_EC']=0
        pln['dpt_HT']=0
        pln['dpt_OV']=0
        pln['dpt_PC']=0
        pln['dpt_PS']=0
        pln['dpt_MQ']=0
        pln['dpt_TP']=0
        pln['dpt_RD']=0
    else:
        
        conditions = [
            (pln['Depth %'] >= 53) & (pln['Depth %'] <= 62.09),
            (pln['Depth %'] >= 62.1) & (pln['Depth %'] <= 63.99),
            (pln['Depth %'] >= 64) & (pln['Depth %'] <= 67.99),
            (pln['Depth %'] >= 68) & (pln['Depth %'] <= 68.99),
            (pln['Depth %'] >= 69) & (pln['Depth %'] <= 69.99)
        ]

        choices = [1, 2, 3, 4, 5]

        pln['dpt_EM'] = np.select(conditions, choices, default=6)



        conditions = [
            (pln['Carat'] < 1) & (pln['Depth %'] <= 58.49),
            (pln['Carat'] < 1) & (pln['Depth %'] <= 59.99),
            (pln['Carat'] < 1) & (pln['Depth %'] <= 67.09),
            (pln['Carat'] < 1) & (pln['Depth %'] <= 68.69),
            (pln['Carat'] < 1) & (pln['Depth %'] <= 69.09),
            (pln['Carat'] < 1) & (pln['Depth %'] <= 99.99),
            (pln['Carat'] >= 1) & (pln['Depth %'] <= 58.49),
            (pln['Carat'] >= 1) & (pln['Depth %'] <= 59.99),
            (pln['Carat'] >= 1) & (pln['Depth %'] <= 67.09),
            (pln['Carat'] >= 1) & (pln['Depth %'] <= 68.69),
            (pln['Carat'] >= 1) & (pln['Depth %'] <= 68.99),
            (pln['Carat'] >= 1) & (pln['Depth %'] <= 69.99)
        ]

        choices = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]

        pln['dpt_RN'] = np.select(conditions, choices, default=7)

        conditions = [
            (pln['Depth %'] >= 56) & (pln['Depth %'] <= 61.39),
            (pln['Depth %'] >= 61.4) & (pln['Depth %'] <= 63.29),
            (pln['Depth %'] >= 63.3) & (pln['Depth %'] <= 66.59),
            (pln['Depth %'] >= 66.6) & (pln['Depth %'] <= 67.99),
            (pln['Depth %'] >= 68) & (pln['Depth %'] <= 69.59)
        ]

        choices = [1, 2, 3, 4, 5]

        pln['dpt_AS'] = np.select(conditions, choices, default=6)

        conditions = [
            (pln['Depth %'] >= 50) & (pln['Depth %'] <= 62.49),
            (pln['Depth %'] >= 62.5) & (pln['Depth %'] <= 63.49),
            (pln['Depth %'] >= 63.5) & (pln['Depth %'] <= 67.19),
            (pln['Depth %'] >= 67.2) & (pln['Depth %'] <= 69.19),
            (pln['Depth %'] >= 69.2) & (pln['Depth %'] <= 70.29)
        ]

        choices = [1, 2, 3, 4, 5]

        pln['dpt_BG'] = np.select(conditions, choices, default=6)

        conditions = [
            (pln['Depth %'] <= 62.00),
            (pln['Depth %'] <= 63.99),
            (pln['Depth %'] <= 66.99),
            (pln['Depth %'] <= 67.99),
            (pln['Depth %'] <= 68.99),
            (pln['Depth %'] <= 69.99)
        ]

        choices = [1, 2, 3, 4, 5, 6]

        pln['dpt_CM'] = np.select(conditions, choices, default=7)

        conditions_cs = [
            (pln['Depth %'] <= 62.49),
            (pln['Depth %'] <= 63.49),
            (pln['Depth %'] <= 66.99),
            (pln['Depth %'] <= 67.19),
            (pln['Depth %'] <= 68.99),
            (pln['Depth %'] <= 70.29)
        ]

        choices_cs = [1, 2, 3, 4, 5, 6]

        pln['dpt_CS'] = np.select([(pln['Depth %'] <= 62.49),
                                (pln['Depth %'] <= 63.49),
                                (pln['Depth %'] <= 66.99),
                                (pln['Depth %'] <= 67.19),
                                (pln['Depth %'] <= 68.99),
                                (pln['Depth %'] <= 70.29)],
                                [1, 2, 3, 4, 5, 6], 7)
        pln['dpt_EC'] = np.select([(pln['Depth %'] >= 57) & (pln['Depth %'] <= 62.09),
                                (pln['Depth %'] >= 62.1) & (pln['Depth %'] <= 63.99),
                                (pln['Depth %'] >= 64.0) & (pln['Depth %'] <= 67.99),
                                (pln['Depth %'] >= 68.0) & (pln['Depth %'] <= 68.99),
                                (pln['Depth %'] >= 69) & (pln['Depth %'] <= 69.99)],
                                [1, 2, 3, 4, 5], 6)
        conditions_ht = [
            (pln['Depth %'] >= 47) & (pln['Depth %'] <= 52.79),
            (pln['Depth %'] >= 52.8) & (pln['Depth %'] <= 54.39),
            (pln['Depth %'] >= 54.4) & (pln['Depth %'] <= 57.49),
            (pln['Depth %'] >= 57.5) & (pln['Depth %'] <= 58.49),
            (pln['Depth %'] >= 58.5) & (pln['Depth %'] <= 61.49),
            (pln['Depth %'] >= 61.5) & (pln['Depth %'] <= 63.4)
        ]

        choices_ht = [1, 2, 3, 4, 5, 6]

        pln['dpt_HT'] = np.select(conditions_ht, choices_ht, default=7)





        pln['dpt_OV'] = np.where(
            (pln['Depth %'] <= 57.09) & (pln['Carat'] >= 1), 1,
            np.where(
                (pln['Depth %'] <= 59.99) & (pln['Carat'] >= 1), 2,
                np.where(
                    (pln['Depth %'] <= 62.49) & (pln['Carat'] >= 1), 3,
                    np.where(
                        (pln['Depth %'] <= 62.89) & (pln['Carat'] >= 1), 4,
                        np.where(
                            (pln['Depth %'] <= 63.89) & (pln['Carat'] >= 1), 5,
                            np.where(
                                (pln['Depth %'] <= 64.89) & (pln['Carat'] >= 1), 6,
                                np.where(
                                    (pln['Depth %'] <= 65.49) & (pln['Carat'] >= 1), 7,
                                    np.where(
                                        (pln['Depth %'] <= 65.89) & (pln['Carat'] >= 1), 8,
                                        np.where(
                                            (pln['Depth %'] <= 67.89) & (pln['Carat'] >= 1), 9,
                                            np.where(
                                                (pln['Depth %'] <= 58.09) & (pln['Carat'] < 1), 1,
                                                np.where(
                                                    (pln['Depth %'] <= 59.99) & (pln['Carat'] < 1), 2,
                                                    np.where(
                                                        (pln['Depth %'] <= 62.49) & (pln['Carat'] < 1), 3,
                                                        np.where(
                                                            (pln['Depth %'] <= 63.95) & (pln['Carat'] < 1), 4,
                                                            np.where(
                                                                (pln['Depth %'] <= 65.49) & (pln['Carat'] < 1), 5,
                                                                np.where(
                                                                    (pln['Depth %'] <= 65.99) & (pln['Carat'] < 1), 6,
                                                                    np.where(
                                                                        (pln['Depth %'] <= 67.89) & (pln['Carat'] < 1), 7,
                                                                        np.where(
                                                                            (pln['Depth %'] <= 99.99) & (pln['Carat'] < 1), 8, 10
                                                                        )
                                                                    )
                                                                )
                                                            )
                                                        )
                                                    )
                                                )
                                            )
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            )
        )


        import numpy as np

        # Assuming pln is your DataFrame
        pln['dpt_PC'] = np.where(
            (pln['Depth %'] >= 61) & (pln['Depth %'] <= 66.09), 1,
            np.where(
                (pln['Depth %'] >= 66.1) & (pln['Depth %'] <= 67.79), 2,
                np.where(
                    (pln['Depth %'] >= 67.80) & (pln['Depth %'] <= 71.99), 3,
                    np.where(
                        (pln['Depth %'] >= 72.0) & (pln['Depth %'] <= 72.99), 4,
                        np.where(
                            (pln['Depth %'] >= 73.0) & (pln['Depth %'] <= 73.99), 5,
                            np.where(
                                (pln['Depth %'] >= 74.0) & (pln['Depth %'] <= 74.99), 6, 7
                            )
                        )
                    )
                )
            )
        )

        pln['dpt_PS'] = np.where(
            (pln['Depth %'] >= 53) & (pln['Depth %'] <= 58.09), 1,
            np.where(
                (pln['Depth %'] >= 58.1) & (pln['Depth %'] <= 59.99), 2,
                np.where(
                    (pln['Depth %'] >= 60.0) & (pln['Depth %'] <= 62.49), 3,
                    np.where(
                        (pln['Depth %'] >= 62.5) & (pln['Depth %'] <= 63.99), 4,
                        np.where(
                            (pln['Depth %'] >= 64.0) & (pln['Depth %'] <= 65.49), 5,
                            np.where(
                                (pln['Depth %'] >= 65.5) & (pln['Depth %'] <= 67.89), 6, 7
                            )
                        )
                    
                )
            )
        )
        )


        pln['dpt_MQ'] = np.where(
            (pln['Depth %'] >= 53) & (pln['Depth %'] <= 58.09), 1,
            np.where(
                (pln['Depth %'] >= 58.1) & (pln['Depth %'] <= 59.99), 2,
                np.where(
                    (pln['Depth %'] >= 60.0) & (pln['Depth %'] <= 62.49), 3,
                    np.where(
                        (pln['Depth %'] >= 62.5) & (pln['Depth %'] <= 63.99), 4,
                        np.where(
                            (pln['Depth %'] >= 64.0) & (pln['Depth %'] <= 65.49), 5,
                            np.where(
                                (pln['Depth %'] >= 65.5) & (pln['Depth %'] <= 67.89), 6, 7
                            )
                        )
                    )
                )
            )
        )



        pln['dpt_TP'] = np.where(
            (pln['Depth %'] >= 43) & (pln['Depth %'] <= 47.99), 1,
            np.where(
                (pln['Depth %'] >= 48) & (pln['Depth %'] <= 55.79), 2,
                np.where(
                    (pln['Depth %'] >= 55.8) & (pln['Depth %'] <= 65.99), 3, 4
                )
            )
        )

        pln['dpt_RD'] = np.where(
            (pln['Depth %'] <= 62.79) & (pln['Cut'].isin(['EX-4', 'EX-1', 'EX-2','EX-3'])), 1,
            np.where(
                (pln['Depth %'] <= 63.69) & (pln['Cut'].isin(['EX-4', 'EX-1', 'EX-2','EX-3'])), 2, ""
            )
        )


    dpt_all_FA = []

    for index, row in pln.iterrows():
        if row['Shp'] == 'EM':
            dpt_all_FA.append(row['dpt_EM'])
        elif row['Shp'] in ['RN', 'RA']:
            dpt_all_FA.append(row['dpt_RN'])
        elif row['Shp'] == 'AS':
            dpt_all_FA.append(row['dpt_AS'])
        elif row['Shp'] == 'BG':
            dpt_all_FA.append(row['dpt_BG'])
        # Repeat similar logic for other conditions
        elif row['Shp'] == 'CM':
            dpt_all_FA.append(row['dpt_CM'])
        elif row['Shp'] == 'OV':
            dpt_all_FA.append(row['dpt_OV'])
        elif row['Shp'] == 'PS':
            dpt_all_FA.append(row['dpt_PS'])
        elif row['Shp'] == 'HT':
            dpt_all_FA.append(row['dpt_HT'])
        elif row['Shp'] == 'MQ':
            dpt_all_FA.append(row['dpt_MQ'])
        elif row['Shp'] in ['EC', 'CE']:
            dpt_all_FA.append(row['dpt_EC'])
        elif row['Shp'] == 'TP':
            dpt_all_FA.append(row['dpt_TP'])
        elif row['Shp'] == 'PC':
            dpt_all_FA.append(row['dpt_PC'])
        elif row['Shp'] in ['CU','CS']:
            dpt_all_FA.append(row['dpt_CS'])
        else:
            dpt_all_FA.append(row['dpt_RD'])

    # Add the new 'dpt_all_FA' list to the original 'pln' DataFrame
    pln['dpt_all_FA'] = dpt_all_FA

    pln['cat'] = np.where(pln['Carat'] < 1, '0.30 - 0.99', '1.00 - 30.99')
  

    pln['dpt_id'] = pln['Shp'].astype(str) + pln['cat'].astype(str) + pln['Fls'].astype(str) + pln['dpt_all_FA'].astype(str)

    dpt_new = pd.read_excel("//sfs.net/bia/BIA_DWH/parameters/updated_parameters_1.xlsx", sheet_name='DEPTH_PER')


    pln = pd.merge(pln, dpt_new[['dpt_id', 'Per%']], on='dpt_id', how='left')


   
    pln[pln['Per%'].isna()]

   

    pln['Per%']=pln['Per%'].fillna(0)

  

    pln.rename(columns={'Per%':'DEPTH_PER'},inplace=True)

    pln['Table (%)'] = pd.to_numeric(pln['Table (%)'], errors='coerce')

    pln['Table (%)'] = pln['Table (%)'].round(2)
    if any(pln['Table (%)']):
        pln['Table (%)']=0
        pln['tbl_EM']=0
        pln['tbl_RN']=0
        pln['tbl_AS']=0
        pln['tbl_BG']=0
        pln['tbl_CM']=0
        pln['tbl_CS']=0
        pln['tbl_EC']=0
        pln['tbl_HT']=0
        pln['tbl_OV']=0
        pln['tbl_PC']=0
        pln['tbl_PS']=0
        pln['tbl_MQ']=0
        pln['tbl_TP']=0
        pln['tbl_RD']=0
    else:
        pln["tbl_EM"] = np.select(
            [
                (pln["Table (%)"] >= 1) & (pln["Table (%)"] <= 62.49),
                (pln["Table (%)"] >= 62.5) & (pln["Table (%)"] <= 67.49),
                (pln["Table (%)"] >= 67.5) & (pln["Table (%)"] <= 69.49),
                (pln["Table (%)"] >= 69.5) & (pln["Table (%)"] <= 99.99),
            ],
            [1, 2, 3, 4],
            default=5,
        )

        pln["tbl_RN"] = np.select(
            [
                (pln["Table (%)"] >= 1) & (pln["Table (%)"] <= 62.49),
                (pln["Table (%)"] >= 62.5) & (pln["Table (%)"] <= 67.49),
                (pln["Table (%)"] >= 67.5) & (pln["Table (%)"] <= 69.49),
            ],
            [1, 2, 3],
            default=4,
        )

        pln['tbl_AS'] = np.select([(pln['Table (%)'] >= 1) & (pln['Table (%)'] <= 58.49),
                                (pln['Table (%)'] >= 58.5) & (pln['Table (%)'] <= 61.49),
                                (pln['Table (%)'] >= 61.5) & (pln['Table (%)'] <= 68.49),
                                (pln['Table (%)'] >= 68.5) & (pln['Table (%)'] <= 69.49)],
                                [1, 2, 3, 4], default=5)

        pln['tbl_BG'] = np.select([(pln['Table (%)'] >= 1) & (pln['Table (%)'] <= 58.49),
                                (pln['Table (%)'] >= 58.5) & (pln['Table (%)'] <= 60.49),
                                (pln['Table (%)'] >= 60.5) & (pln['Table (%)'] <= 70.49),
                                (pln['Table (%)'] >= 70.5) & (pln['Table (%)'] <= 71.49)],
                                [1, 2, 3, 4], default=5)
        pln['tbl_CM'] = np.select([(pln['Table (%)'] >= 1) & (pln['Table (%)'] <= 59.49),
                                (pln['Table (%)'] >= 59.5) & (pln['Table (%)'] <= 62.49),
                                (pln['Table (%)'] >= 62.5) & (pln['Table (%)'] <= 68.49),
                                (pln['Table (%)'] >= 68.5) & (pln['Table (%)'] <= 69.49),
                                (pln['Table (%)'] >= 69.5) & (pln['Table (%)'] <= 99.99)],
                                [1, 2, 3, 4, 5], default=6)



        pln['tbl_CS'] = np.select([(pln['Table (%)'] >= 1) & (pln['Table (%)'] <= 58.49),
                                (pln['Table (%)'] >= 58.5) & (pln['Table (%)'] <= 61.49),
                                (pln['Table (%)'] >= 61.5) & (pln['Table (%)'] <= 68.49),
                                (pln['Table (%)'] >= 68.5) & (pln['Table (%)'] <= 69.49)],
                                [1, 2, 3, 4], default=5)


        pln['tbl_EC'] = np.select([(pln['Table (%)'] >= 1) & (pln['Table (%)'] <= 59.49),
                                (pln['Table (%)'] >= 59.5) & (pln['Table (%)'] <= 62.49),
                                (pln['Table (%)'] >= 62.5) & (pln['Table (%)'] <= 68.49),
                                (pln['Table (%)'] >= 68.5) & (pln['Table (%)'] <= 69.49),
                                (pln['Table (%)'] >= 69.5) & (pln['Table (%)'] <= 99.49)],
                                [1, 2, 3, 4,5], default=6)



        pln['tbl_MQ'] = np.select([(pln['Table (%)'] >= 1) & (pln['Table (%)'] <= 54.49),
                                (pln['Table (%)'] >= 54.5) & (pln['Table (%)'] <= 56.49),
                                (pln['Table (%)'] >= 56.5) & (pln['Table (%)'] <= 59.49),
                                (pln['Table (%)'] >= 59.5) & (pln['Table (%)'] <= 62.49),
                                (pln['Table (%)'] >= 62.5) & (pln['Table (%)'] <= 65.49)],
                                [1, 2, 3, 4, 5], default=6)


        pln['tbl_HT'] = np.select([(pln['Table (%)'] >= 1) & (pln['Table (%)'] <= 54.49),
                                (pln['Table (%)'] >= 54.5) & (pln['Table (%)'] <= 56.49),
                                (pln['Table (%)'] >= 56.5) & (pln['Table (%)'] <= 61.49),
                                (pln['Table (%)'] >= 61.5) & (pln['Table (%)'] <= 62.49),
                                (pln['Table (%)'] >= 62.5) & (pln['Table (%)'] <= 63.49)],
                                [1, 2, 3, 4, 5], default=6)


        pln['tbl_OV'] = np.select([(pln['Table (%)'] >= 1) & (pln['Table (%)'] <= 54.49),
                                (pln['Table (%)'] >= 54.5) & (pln['Table (%)'] <= 56.49),
                                (pln['Table (%)'] >= 56.5) & (pln['Table (%)'] <= 59.49),
                                (pln['Table (%)'] >= 59.5) & (pln['Table (%)'] <= 62.49),
                                (pln['Table (%)'] >= 62.5) & (pln['Table (%)'] <= 65.49),
                                (pln['Table (%)'] >= 65.5) & (pln['Table (%)'] <= 99.99)],
                                [1, 2, 3, 4, 5,6], default=7)



        pln['tbl_PC'] = np.select([(pln['Table (%)'] >= 1) & (pln['Table (%)'] <= 69.49),
                                (pln['Table (%)'] >= 69.5) & (pln['Table (%)'] <= 72.49),
                                (pln['Table (%)'] >= 72.5) & (pln['Table (%)'] <= 74.49)],
                                [1, 2, 3], default=4)


        pln['tbl_PS'] = np.select([(pln['Table (%)'] >= 1) & (pln['Table (%)'] <= 54.49),
                                (pln['Table (%)'] >= 54.5) & (pln['Table (%)'] <= 56.49),
                                (pln['Table (%)'] >= 56.5) & (pln['Table (%)'] <= 59.49),
                                (pln['Table (%)'] >= 59.5) & (pln['Table (%)'] <= 62.49),
                                (pln['Table (%)'] >= 62.5) & (pln['Table (%)'] <= 65.49),
                                (pln['Table (%)'] >= 65.5) & (pln['Table (%)'] <= 99.99)],
                                [1, 2, 3, 4, 5, 6], default=7)


        pln['tbl_TP'] = np.select([(pln['Table (%)'] < 65.5), (pln['Table (%)'] < 75.5)], [1, 2], default=3)

        conditions_tbl_RD = [
            (pln['Table (%)'] <= 60.49) & (pln['Cut'].isin(['EX-1', 'EX-2', 'EX-3', 'EX-4'])),
            (pln['Table (%)'] <= 61.99) & (pln['Cut'].isin(['EX-1', 'EX-2', 'EX-3', 'EX-4'])),
            (pln['Table (%)'] <= 99.99) & (pln['Cut'].isin(['EX-1', 'EX-2', 'EX-3', 'EX-4']))
        ]

        choices_tbl_RD = [1, 2, 3]
        pln['tbl_RD'] = np.select(conditions_tbl_RD, choices_tbl_RD, default='')

    tbl_all_FA = []


    for index, row in pln.iterrows():
        if row['Shp'] == 'EM':
            tbl_all_FA.append(row['tbl_EM'])
        elif row['Shp'] in ['RN', 'RA']:
            tbl_all_FA.append(row['tbl_RN'])
        elif row['Shp'] == 'AS':
            tbl_all_FA.append(row['tbl_AS'])
        elif row['Shp'] == 'BG':
            tbl_all_FA.append(row['tbl_BG'])
        # Repeat similar logic for other conditions
        elif row['Shp'] == 'CM':
            tbl_all_FA.append(row['tbl_CM'])
        elif row['Shp'] == 'OV':
            tbl_all_FA.append(row['tbl_OV'])
        elif row['Shp'] == 'PS':
            tbl_all_FA.append(row['tbl_PS'])
        elif row['Shp'] == 'HT':
            tbl_all_FA.append(row['tbl_HT'])
        elif row['Shp'] == 'MQ':
            tbl_all_FA.append(row['tbl_MQ'])
        elif row['Shp'] in ['EC', 'CE']:
            tbl_all_FA.append(row['tbl_EC'])
        elif row['Shp'] == 'TP':
            tbl_all_FA.append(row['tbl_TP'])
        elif row['Shp'] == 'RD':
            tbl_all_FA.append(row['tbl_RD'])
        elif row['Shp'] == 'PC':
            tbl_all_FA.append(row['tbl_PC'])
        elif row['Shp'] in ['CS','CU']:
            tbl_all_FA.append(row['tbl_CS'])
        else:
            tbl_all_FA.append('')

    pln['tbl_all_FA'] = tbl_all_FA

    pln['tbl_id'] = pln['Shp'].astype(str) + pln['cat'].astype(str) + pln['Fls'].astype(str) + pln['tbl_all_FA'].astype(str)

    excel_file_path = "//sfs.net/bia/BIA_DWH/parameters/updated_parameters_1.xlsx"

    tbl_new = pd.read_excel(excel_file_path, sheet_name='TABLE_PER')


    pln = pd.merge(pln, tbl_new.iloc[:, [0, 7]], left_on='tbl_id', right_on='tbl_id', how='left')
    pln['TABLE_PER'] = pln.iloc[:, -1]
    pln = pln.drop(columns=[pln.columns[-2]])

    pln['TABLE_PER'] = pln['TABLE_PER'].fillna(0).astype(int)


    if any(pln['Ratio']):
        pln['Ratio']=0
        pln['Rat_EM']=0
        pln['Rat_RN']=0
        pln['Rat_AS']=0
        pln['Rat_BG']=0
        pln['Rat_CM']=0
        pln['Rat_CS']=0
        pln['Rat_EC']=0
        pln['Rat_HT']=0
        pln['Rat_OV']=0
        pln['Rat_PC']=0
        pln['Rat_PS']=0
        pln['Rat_MQ']=0
        pln['Rat_TP']=0
        pln['Rat_RD']=0
    else:
        pln['Ratio'] = pd.to_numeric(pln['Ratio'].round(2), errors='coerce')

        pln['Rat_EM'] = np.select(
            [
                (pln['Ratio'] <= 1.33),
                (pln['Ratio'] <= 1.35),
                (pln['Ratio'] <= 1.37),
                (pln['Ratio'] <= 1.39),
                (pln['Ratio'] <= 1.45),
                (pln['Ratio'] <= 1.56),
                (pln['Ratio'] <= 1.99),
            ],
            [1, 2, 3, 4, 5, 6, 7],
            default=8
        )

        pln['Rat_AS'] = np.select(
            [
                (pln['Ratio'] >= 1) & (pln['Ratio'] <= 1.01),
                (pln['Ratio'] >= 1.02) & (pln['Ratio'] <= 1.02),
                (pln['Ratio'] >= 1.03) & (pln['Ratio'] <= 1.03),
            ],
            [1, 2, 3],
            default=4
        )

        pln['Rat_BG'] = np.select(
            [
                (pln['Ratio'] <= 1.79),
                (pln['Ratio'] <= 1.89),
                (pln['Ratio'] <= 1.99),
                (pln['Ratio'] <= 2.19)
            ],
            [
                1, 2, 3, 4
            ],
            default=5
        )

        pln['Rat_CM'] = np.select(
            [
                (pln['Ratio'] >= 1.00) & (pln['Ratio'] <= 1.04),
                (pln['Ratio'] >= 1.00) & (pln['Ratio'] <= 1.09),
                (pln['Ratio'] >= 1.00) & (pln['Ratio'] <= 1.14),
                (pln['Carat'] >= 1.00) & (pln['Ratio'] <= 1.19),
                (pln['Carat'] >= 1.00) & (pln['Ratio'] <= 1.24),
                (pln['Carat'] >= 1.00) & (pln['Ratio'] <= 1.26)
            ],
            [
                1, 2, 3, 4, 5, 6
            ],
            default=7
        )

        pln['Rat_CS'] = np.select(
            [
                (pln['Ratio'] >= 1) & (pln['Ratio'] <= 1.1),
                (pln['Ratio'] >= 1.14) & (pln['Ratio'] <= 1.16),
            ],
            [1, 2],
            default=3
        )


        pln['Rat_HT'] = np.select(
            [
                (pln['Ratio'] >= 0.77) & (pln['Ratio'] <= 0.82),
                (pln['Ratio'] >= 0.83) & (pln['Ratio'] <= 0.83),
                (pln['Ratio'] >= 0.84) & (pln['Ratio'] <= 0.84),
                (pln['Ratio'] >= 0.85) & (pln['Ratio'] <= 0.86),
                (pln['Ratio'] >= 0.87) & (pln['Ratio'] <= 0.89),
                (pln['Ratio'] >= 0.90) & (pln['Ratio'] <= 1)
            ],
            [
                1, 2, 3, 4, 5, 6
            ],
            default=7
        )

        pln['Rat_MQ'] = np.select(
            [
                (pln['Ratio'] >= 1.7) & (pln['Ratio'] <= 1.79),
                (pln['Ratio'] >= 1.8) & (pln['Ratio'] <= 1.89),
                (pln['Ratio'] >= 1.9) & (pln['Ratio'] <= 1.99),
                (pln['Ratio'] >= 2) & (pln['Ratio'] <= 2.1),
            ],
            [1, 2, 3, 4],
            default=5
        )

        pln['Rat_OV'] = np.select(
            [
                (pln['Ratio'] <= 1.33),
                (pln['Ratio'] <= 1.35),
                (pln['Ratio'] <= 1.37),
                (pln['Ratio'] <= 1.40),
                (pln['Ratio'] <= 1.45),
                (pln['Ratio'] <= 1.55),
            ],
            [1, 2, 3, 4, 5, 6],
            default=7
        )
        pln['Rat_OVM'] = np.select(
            [
                (pln['Ratio'] <= 1.33),
                (pln['Ratio'] <= 1.35),
                (pln['Ratio'] <= 1.37),
                (pln['Ratio'] <= 1.40),
                (pln['Ratio'] <= 1.45),
                (pln['Ratio'] <= 1.55),
            ],
            [1, 2, 3, 4, 5, 6],
            default=7
        )
        pln['Rat_PC'] = np.select(
            [
                (pln['Ratio'] >= 1) & (pln['Ratio'] <= 1.03),
            ],
            [1],
            default=2
        )

        pln['Rat_PS'] = np.select(
            [
                (pln['Ratio'] >= 1.4) & (pln['Ratio'] <= 1.44),
                (pln['Ratio'] >= 1.45) & (pln['Ratio'] <= 1.51),
                (pln['Ratio'] >= 1.52) & (pln['Ratio'] <= 1.55),
                (pln['Ratio'] >= 1.56) & (pln['Ratio'] <= 1.59),
                (pln['Ratio'] >= 1.6) & (pln['Ratio'] <= 1.69),
            ],
            [1, 2, 3, 4, 5],
            default=6
        )


        Rat_RN = np.select(
            [
                (pln['Ratio'] <= 1.24) & (pln['Carat'] < 1) | (pln['Ratio'] <= 1.23) & (pln['Carat'] >= 1),
                (pln['Ratio'] <= 1.27) & (pln['Carat'] < 1) | (pln['Ratio'] <= 1.25) & (pln['Carat'] >= 1),
                (pln['Ratio'] <= 1.29) & (pln['Carat'] < 1) | (pln['Ratio'] <= 1.28) & (pln['Carat'] >= 1),
                (pln['Ratio'] <= 1.34) & (pln['Carat'] < 1) | (pln['Ratio'] <= 1.31) & (pln['Carat'] >= 1),
                (pln['Ratio'] <= 1.39) & (pln['Carat'] < 1) | (pln['Ratio'] <= 1.33) & (pln['Carat'] >= 1),
                (pln['Ratio'] <= 1.49) & (pln['Carat'] < 1) | (pln['Ratio'] <= 1.35) & (pln['Carat'] >= 1),
                (pln['Ratio'] <= 9.99) & (pln['Carat'] < 1) | (pln['Ratio'] <= 1.29) & (pln['Carat'] >= 1),
                (pln['Ratio'] <= 1.37) & (pln['Carat'] >= 1),
                (pln['Ratio'] <= 1.39) & (pln['Carat'] >= 1),
            ],
            [
                1, 2, 3, 4, 5, 6, 7, 8, 9
            ],
            default=10
        )
        pln['Rat_RN'] = Rat_RN

        conditions_tp = [
            (pln['Ratio'] <= 1.59),
            (pln['Ratio'] <= 1.69),
            (pln['Ratio'] <= 1.79),
            (pln['Ratio'] <= 1.89),
            (pln['Ratio'] <= 1.99)
        ]

        choices_tp = [1, 2, 3, 4, 5]

        Rat_TP = np.select(conditions_tp, choices_tp, default=6)
        pln['Rat_TP'] = Rat_TP

        Rat_EC = np.select(
            [
                (pln['Ratio'] >= 1.00) & (pln['Ratio'] <= 1.23),
                (pln['Ratio'] >= 1.24) & (pln['Ratio'] <= 1.24),
                (pln['Ratio'] >= 1.25) & (pln['Ratio'] <= 1.26),
                (pln['Ratio'] >= 1.27) & (pln['Ratio'] <= 1.28),
                (pln['Ratio'] >= 1.29) & (pln['Ratio'] <= 1.32),
                (pln['Ratio'] >= 1.33) & (pln['Ratio'] <= 1.34),
                (pln['Ratio'] >= 1.35) & (pln['Ratio'] <= 1.39),
                (pln['Ratio'] >= 1.4) & (pln['Ratio'] <= 1.44)
            ],
            [
                1, 2, 3, 4, 5, 6, 7, 8
            ],
            default=9
        )
        pln['Rat_EC'] = Rat_EC

    Rat_all = []

    for index, row in pln.iterrows():
        if row['Shp'] == 'EM':
            Rat_all.append(row['Rat_EM'])
        elif row['Shp'] in ['RN', 'RA']:
            Rat_all.append(row['Rat_RN'])
        elif row['Shp'] == 'AS':
            Rat_all.append(row['Rat_AS'])
        elif row['Shp'] == 'BG':
            Rat_all.append(row['Rat_BG'])
        # Repeat similar logic for other conditions
        elif row['Shp'] == 'CM':
            Rat_all.append(row['Rat_CM'])
        elif row['Shp'] == 'OV':
            Rat_all.append(row['Rat_OV'])
        elif row['Shp'] == 'PS':
            Rat_all.append(row['Rat_PS'])
        elif row['Shp'] == 'HT':
            Rat_all.append(row['Rat_HT'])
        elif row['Shp'] == 'MQ':
            Rat_all.append(row['Rat_MQ'])
        elif row['Shp'] in ['EC', 'CE']:
            Rat_all.append(row['Rat_EC'])
        elif row['Shp'] == 'TP':
            Rat_all.append(row['Rat_TP'])
        elif row['Shp'] == 'PC':
            Rat_all.append(row['Rat_PC'])
        elif row['Shp'] in ['CS','CU']:
            Rat_all.append(row['Rat_CS'])
        else:
            Rat_all.append("")

    pln['Rat_all'] = Rat_all

    conditions_size = [
        (pln['Carat'] >= 1.00) & (pln['Carat'] < 1.18) & (pln['Shp'] == "CM"),
        (pln['Carat'] >= 1.18) & (pln['Shp'] == "CM"),
        (pln['Carat'] < 1),
    ]

    choices_size = [
        "1.00 - 1.179",
        "1.180 - 30.999",
        "0.30 - 0.99"
    ]
    print("size si start thase")
    Size = np.select(conditions_size, choices_size, default="1.00 - 30.99")
    Size = np.where(pln['Carat'] < 1, "0.30 - 0.99", "1.00 - 30.99")

    pln['Rat_id'] = pln['Shp'].astype(str) + pln['Fls'].astype(str) + Size + pln['Rat_all'].astype(str)


    Rat_new = pd.read_excel("//sfs.net/bia/BIA_DWH/parameters/updated_parameters_1.xlsx", sheet_name='Ratio', engine='openpyxl')


    pln = pd.merge(pln, Rat_new[['Rat_id', 'Per%']], on='Rat_id', how='left')

    pln['Per%'].fillna(0, inplace=True)
    pln.rename(columns={'Per%':'RATIO_PER'},inplace=True)
    pln['New_shape'] = np.where(pln['Shp'] == 'RD', 'RD', 'FA')

    Ec = pln[pln['Shp'].isin(['EC', 'CE'])]
    pln = pln[~pln['Shp'].isin(['EC', 'CE'])]


    Rat_new1 = pd.read_excel("//sfs.net/bia/BIA_DWH/parameters/updated_parameters_1.xlsx", sheet_name=3)

    Ec['Rat_id'] = Ec['Shp'] + Ec['Range'].astype(str) + Ec['Fls'] + Ec['Rat_EC'].astype(str)


    Ec = Ec.merge(Rat_new1.iloc[:, [8, 6]], on='Rat_id', how='left')


   
    Ec.columns.values[-1] = "RATIO_PER1"

   
    columns_to_remove = ["RATIO_PER", "New_shape"]
    Ec = Ec.drop(columns=columns_to_remove, errors='ignore')


    Ec.columns.values[-1] = "RATIO_PER"

    pln = pln.drop(columns=['New_shape'])

    pln = pd.concat([pln, Ec], ignore_index=True)

    
    pln['RATIO_PER'].fillna(0, inplace=True)

    pln['CN%'] = pd.to_numeric(pln['CN%'], errors='coerce')
    pln['CW%'] = pd.to_numeric(pln['CW%'], errors='coerce')
    pln['SN%'] = pd.to_numeric(pln['SN%'], errors='coerce')
    pln['SW%'] = pd.to_numeric(pln['SW%'], errors='coerce')

    pln['numbers'] = range(1, len(pln) + 1)
    pln.drop(columns=['PER%_x','PER%_y','PER%'],inplace=True)
    if 'DISC_PER_x' in pln.columns:
        pln.drop(columns=['DISC_PER_x'], inplace=True)
    if 'DISC_PER' in pln.columns:
        pln.drop(columns=['DISC_PER'], inplace=True)
    Fancy = pln[pln['Shp'] != "RD"].copy()
    Fancy['CUT%'] = 0
    Fancy['SYMM_ID'] = Fancy['Range'].astype(str) + Fancy['Col'].astype(str) + Fancy['Prty'].astype(str) + Fancy['Sym'].astype(str) + Fancy['Fls'].astype(str)
    # Assuming 'Fancy' is a pandas DataFrame.
    Sym_new = pd.read_excel("//sfs.net/bia/BIA_DWH/parameters/SYMM_DISC.xlsx", sheet_name=1)
    Fancy = Fancy.merge(Sym_new[['SYMM_ID', "PER%"]], on='SYMM_ID', how='left')
    Fancy.rename(columns={"PER%": 'SYMM%'}, inplace=True)
    Fancy.drop(columns=['SYMM_ID'], inplace=True)
    Fancy['SYMM%'] = Fancy['SYMM%'].fillna(0)

    Fancy['FLS_ID'] = Fancy['Shp'].astype(str) + Fancy['Range'].astype(str) + Fancy['Col'].astype(str) + Fancy['Prty'].astype(str) + Fancy['Fls'].astype(str)
    Fls_new = pd.read_excel("//sfs.net/bia/BIA_DWH/parameters/FLS_DISC.xlsx", sheet_name=1)
    Fancy = Fancy.merge(Fls_new[['FLS_ID','DISC_PER']], on='FLS_ID', how='left')
    print(Fancy.columns)
    # if 'DISC_PER_y' in Fancy.columns:
    #     Fancy.drop(columns=['DISC_PER_y'], inplace=True)
    # else:
    #     print('HI')
    # if 'DISC_PER_x' in Fancy.columns:
    #     Fancy.drop(columns=['DISC_PER_x'], inplace=True)
    # else:
    #     print('BYE')
    Fancy.rename(columns={"DISC_PER": 'FLS%'}, inplace=True)
    Fancy['FLS%'] = Fancy['FLS%'].fillna(0)



    #pln[pln['Shp'] == "RD"]

    ROUND = pln[pln['Shp'] == "RD"].copy()

    ROUND['CUT_ID'] = ROUND['Shp'].astype(str) + ROUND['Col'].astype(str) + ROUND['Prty'].astype(str) + ROUND['Cut'].astype(str)

    CUT_NEW = pd.read_excel("//sfs.net/bia/BIA_DWH/parameters/CUT_DISC.xlsx")

    ROUND = pd.merge(ROUND, CUT_NEW.iloc[:, [0, 5]], left_on='CUT_ID', right_on=CUT_NEW.columns[0], how='left')
    ROUND['CUT%'] = ROUND.iloc[:, -1]

    ROUND.drop(columns=['DISC_PER'],inplace=True)

    # Assuming ROUND is a DataFrame
    ROUND['SYMM_ID'] = ROUND['Shp'].astype(str) + ROUND['Col'].astype(str) + ROUND['Prty'].astype(str) + ROUND['Cut'].astype(str) + ROUND['Pol'].astype(str) + ROUND['Sym'].astype(str) + ROUND['Fls'].astype(str)


    SYM_new = pd.read_excel("//sfs.net/bia/BIA_DWH/parameters/SYMM_DISC.xlsx",sheet_name=0)

    SYM_new_columns = SYM_new.columns
    ROUND = pd.merge(ROUND, SYM_new.iloc[:, [0, 8]], left_on='SYMM_ID', right_on=SYM_new_columns[0], how='left')


    ROUND['SYMM%'] = ROUND.iloc[:, -1]

    # If 'SYMM%' column has NaN values, fill them with 0
    ROUND['SYMM%'] = ROUND['SYMM%'].fillna(0)


    ROUND.drop(columns=['PER%'],inplace=True)

    # Assuming ROUND is a DataFrame
    ROUND['FLS_ID'] = ROUND['Shp'].astype(str) + ROUND['Range'].astype(str)+ ROUND['Col'].astype(str) + ROUND['Prty'].astype(str) + ROUND['Fls'].astype(str) + ROUND['Cut'].astype(str)


    Fls_new =  pd.read_excel("//sfs.net/bia/BIA_DWH/parameters/FLS_DISC.xlsx",sheet_name=0)

    Fls_new_columns = Fls_new.columns
    ROUND = pd.merge(ROUND, Fls_new.iloc[:, [0, 7]], left_on='FLS_ID', right_on=Fls_new_columns[0], how='left')
    ROUND['FLS%'] = ROUND.iloc[:, -1]

    ROUND['FLS%'] = ROUND['FLS%'].fillna(0)

    columns_to_drop = ['CUT_ID', 'SYMM_ID']
    ROUND = ROUND.drop(columns=columns_to_drop, errors='ignore')

    ROUND.drop(columns=['DISC_PER'],inplace=True)

    Diameter=  pd.read_excel("//sfs.net/bia/BIA_DWH/parameters/RD-diameter.xlsx",sheet_name=0)

    Diameter = Diameter[(Diameter['CUT']=="EX-2")]
    #ROUND = ROUND[(ROUND['Cut']=="EX-1")| (ROUND['Cut']=="EX")]
    Diameter['DIA_ID'] = Diameter['DIA_ID'].astype(str)+Diameter['CUT'].astype(str)
    
    ROUND['Cut_off'] = 0
    print("roundiiii")
    # Define conditions and update 'Cut_off' based on conditions
    ROUND.loc[((ROUND['Carat'].isin([0.23, 0.24]) & (ROUND['Width'] >= 3.99)) |
            (ROUND['Carat'].isin([0.28, 0.29]) & (ROUND['Width'] >= 4.29)) |
            ((ROUND['Carat'].isin([0.3, 0.31, 0.32, 0.33, 0.34]) & (ROUND['Width'] >= 4.49) & (ROUND['Width'] < 4.59)) |
                (ROUND['Carat'].isin([0.35, 0.36, 0.37, 0.38]) & (ROUND['Width'] >= 4.59)) |
                (ROUND['Carat'].isin([0.4, 0.41, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48]) & (ROUND['Width'] >= 4.99)) |
                (ROUND['Carat'].isin([0.5, 0.51, 0.52, 0.53, 0.54]) & (ROUND['Width'] >= 5.39)) |
                (ROUND['Carat'].isin([0.6, 0.61, 0.62, 0.63, 0.64]) & (ROUND['Width'] >= 5.49)) |
                (ROUND['Carat'].isin([0.8, 0.81, 0.82, 0.83, 0.84, 0.85, 0.86, 0.87, 0.88,0.89]) & (ROUND['Width'] >= 5.99)) |
                (ROUND['Carat'].isin([0.9, 0.91, 0.92, 0.93, 0.94]) & (ROUND['Width'] >= 6.19) & (ROUND['Width'] < 6.29))), 'Cut_off')] = 1

    ROUND.loc[((ROUND['Carat'].isin([0.3, 0.31, 0.32, 0.33, 0.34]) & (ROUND['Width'] >= 4.59)) |
            (ROUND['Carat'].isin([0.35, 0.36, 0.37, 0.38]) & (ROUND['Width'] >= 4.69)) |
            (ROUND['Carat'].isin([0.9, 0.91, 0.92, 0.93, 0.94]) & (ROUND['Width'] >= 6.29))), 'Cut_off'] = 2

    ROUND.loc[((ROUND['Carat'].isin([1, 1.01, 1.02, 1.03, 1.04, 1.05]) & (ROUND['Width'] <= 6.29)) |
            (ROUND['Carat'].isin([1.06, 1.07, 1.08, 1.09]) & (ROUND['Width'] >= 6.59)) |
            (ROUND['Carat'].isin([1.1, 1.11, 1.12, 1.13, 1.14, 1.15, 1.16, 1.17]) & (ROUND['Width'] >= 6.59)) |
            (ROUND['Carat'].isin([1.18, 1.19, 1.20, 1.21, 1.22]) & (ROUND['Width'] < 6.70)) |
            (ROUND['Carat'].isin([1.23, 1.24, 1.25, 1.26, 1.27]) & (ROUND['Width'] >= 6.79) & (ROUND['Width'] < 6.99)) |
            (ROUND['Carat'].isin([1.28, 1.29]) & (ROUND['Width'] >= 6.79) & (ROUND['Width'] < 6.99)) |
            (ROUND['Carat'].isin([1.3, 1.31, 1.32, 1.33, 1.34]) & (ROUND['Width'] >= 6.99) & (ROUND['Width'] < 7.09)) |
            (ROUND['Carat'].isin([1.35, 1.36, 1.37]) & (ROUND['Width'] >= 6.99)) |
            (ROUND['Carat'].isin([1.38, 1.39]) & (ROUND['Width'] >= 7.08)) |
            (ROUND['Carat'].isin([1.4, 1.41, 1.42, 1.43, 1.44,1.45,1.46,1.47]) & (ROUND['Width'] >= 7.19) & (ROUND['Width'] < 7.30)) |
            (ROUND['Carat'].isin([1.50, 1.51, 1.52, 1.53, 1.54]) & (ROUND['Width'] < 7.26)) |
            (ROUND['Carat'].isin([1.70, 1.71, 1.72, 1.73, 1.74]) & (ROUND['Width'] >= 7.59)) |
            (ROUND['Carat'].isin([1.75, 1.76, 1.77, 1.78, 1.79]) & (ROUND['Width'] >= 7.69)) |
            (ROUND['Carat'].isin([1.80, 1.81, 1.82, 1.83, 1.84, 1.85]) & (ROUND['Width'] < 7.80)) |
            (ROUND['Carat'].isin([1.86, 1.87, 1.88, 1.89]) & (ROUND['Width'] >= 7.89) & (ROUND['Width'] < 8)) |
            (ROUND['Carat'].isin([1.90, 1.91, 1.92, 1.93, 1.94]) & (ROUND['Width'] >= 7.99)) |
            (ROUND['Carat'].isin([1.95, 1.96, 1.97, 1.98, 1.99]) & (ROUND['Width'] > 7.99)) |
            (ROUND['Carat'].isin([2.00, 2.01, 2.02, 2.03, 2.04]) & (ROUND['Width'] < 8.00)) |
            (ROUND['Carat'].isin([2.05, 2.06, 2.07, 2.08, 2.09]) & (ROUND['Width'] >= 8.19)) |
            (ROUND['Carat'].isin([2.10, 2.11, 2.12, 2.13, 2.14, 2.15, 2.16, 2.17, 2.18, 2.19]) & (ROUND['Width'] >= 8.29)) |
            (ROUND['Carat'].isin([2.20, 2.21, 2.22, 2.23, 2.24, 2.25, 2.26, 2.27, 2.28, 2.29]) & (ROUND['Width'] >= 8.39)) |
            (ROUND['Carat'].isin([2.30, 2.31, 2.32, 2.33, 2.34, 2.35, 2.36, 2.37, 2.38, 2.39]) & (ROUND['Width'] >= 8.49)) |
            (ROUND['Carat'].isin([2.40, 2.41, 2.42, 2.43, 2.44, 2.45, 2.46, 2.47, 2.48, 2.49]) & (ROUND['Width'] >= 8.59)) |
            (ROUND['Carat'].isin([2.50, 2.51, 2.52, 2.53]) & (ROUND['Width'] < 8.60)) |
            (ROUND['Carat'].isin([2.54, 2.55, 2.56, 2.57, 2.58, 2.59]) & (ROUND['Width'] >= 8.79)) |
            (ROUND['Carat'].isin([2.7, 2.71, 2.72, 2.73, 2.74, 2.75, 2.76, 2.77, 2.78, 2.79]) & (ROUND['Width'] >= 8.89)) |
            (ROUND['Carat'].isin([2.8, 2.81, 2.82, 2.83, 2.84, 2.85, 2.86, 2.87, 2.88, 2.89]) & (ROUND['Width'] >= 8.99)) |
            (ROUND['Carat'].isin([3.00, 3.01, 3.02, 3.03, 3.04, 3.05]) & (ROUND['Width'] < 9.00)) |
            (ROUND['Carat'].isin([3.10, 3.11, 3.12, 3.13, 3.14, 3.15, 3.16, 3.17, 3.18, 3.19]) & (ROUND['Width'] >= 9.49)) |
            (ROUND['Carat'].isin([3.20, 3.21, 3.22, 3.23, 3.24, 3.25, 3.26, 3.27, 3.28, 3.29]) & (ROUND['Width'] >= 9.69)) |
            (ROUND['Carat'].isin([3.80, 3.81, 3.82, 3.83, 3.84, 3.85, 3.86, 3.87, 3.88, 3.89]) & (ROUND['Width'] >= 9.99)) |
            (ROUND['Carat'].isin([3.90, 3.91, 3.92, 3.93, 3.94, 3.95, 3.96, 3.97, 3.98, 3.99]) & (ROUND['Width'] >= 9.99))), 'Cut_off'] = 1

    ROUND.loc[((ROUND['Carat'].isin([1, 1.01, 1.02, 1.03, 1.04, 1.05]) & (ROUND['Width'] >= 6.49) & (ROUND['Width'] < 6.6)) |
            (ROUND['Carat'].isin([1.18, 1.19, 1.20, 1.21, 1.22]) & (ROUND['Width'] >= 6.79) & (ROUND['Width'] < 6.9)) |
            (ROUND['Carat'].isin([1.23, 1.24, 1.25, 1.26, 1.27]) & (ROUND['Width'] >= 6.99)) |
            (ROUND['Carat'].isin([1.28, 1.29]) & (ROUND['Width'] >= 6.99)) |
            (ROUND['Carat'].isin([1.3, 1.31, 1.32, 1.33, 1.34]) & (ROUND['Width'] >= 7.09)) |
            (ROUND['Carat'].isin([1.4, 1.41, 1.42, 1.43, 1.44,1.45,1.46,1.47]) & (ROUND['Width'] >= 7.30)) |
            (ROUND['Carat'].isin([1.50, 1.51, 1.52, 1.53, 1.54]) & (ROUND['Width'] >= 7.49)) |
            (ROUND['Carat'].isin([1.86, 1.87, 1.88, 1.89]) & (ROUND['Width'] >= 7.99)) |
            (ROUND['Carat'].isin([2.00, 2.01, 2.02, 2.03, 2.04]) & (ROUND['Width'] >= 8.09) & (ROUND['Width'] < 8.20)) |
            (ROUND['Carat'].isin([2.50, 2.51, 2.52, 2.53]) & (ROUND['Width'] >= 8.69) & (ROUND['Width'] <= 8.79)) |
            (ROUND['Carat'].isin([3.00, 3.01, 3.02, 3.03, 3.04, 3.05]) & (ROUND['Width'] >= 9.29))), 'Cut_off'] = 2
    ROUND.loc[((ROUND['Carat'].isin([1, 1.01, 1.02, 1.03, 1.04, 1.05]) & (ROUND['Width'] >= 6.59)) |
            (ROUND['Carat'].isin([1.18, 1.19, 1.20, 1.21, 1.22]) & (ROUND['Width'] >= 6.89) & (ROUND['Width'] < 6.99)) |
            (ROUND['Carat'].isin([2.00, 2.01, 2.02, 2.03, 2.04]) & (ROUND['Width'] >= 8.19)) |
            (ROUND['Carat'].isin([2.50, 2.51, 2.52, 2.53]) & (ROUND['Width'] >= 8.8))), 'Cut_off'] = 3

    ROUND.loc[((ROUND['Carat'].isin([1.18, 1.19, 1.20, 1.21, 1.22]) & (ROUND['Width'] >= 6.99))), 'Cut_off'] = 4




    ROUND['DIA_ID'] = np.where(ROUND['Carat'] < 1,
                            ROUND['Cut_off'].astype(str) + ROUND['Carat'].astype(str) + ROUND['Col'].astype(str) + ROUND['Prty'].astype(str)+ROUND['Cut'].astype(str),
                            ROUND['Cut_off'].astype(str) + ROUND['Carat'].astype(str) + ROUND['Fls'].astype(str) + ROUND['Cut'].astype(str))


    merged_df = pd.merge(ROUND, Diameter[['DIA_ID', 'DISC_PER']], on='DIA_ID', how='left')

    # Create a new column 'Dia%' in the ROUND DataFrame based on the merged result
    ROUND['Dia%'] = merged_df['DISC_PER']

    # Drop columns "Cut_off" and "DIA_ID" from the ROUND DataFrame
    ROUND = ROUND.drop(columns=['Cut_off', 'DIA_ID'], errors='ignore')

    # Replace missing values in the 'Dia%' column with 0
    ROUND['Dia%'] = ROUND['Dia%'].fillna(0)


    Fancy['Dia'] = 0

    Fancy.rename(columns={'Dia':'Dia%'},inplace=True)

    mix = pd.concat([Fancy, ROUND], ignore_index=True)


    mix.head()

    mix = mix.drop(columns=['FLS_ID'], errors='ignore')

    KTS=pd.read_excel(r'\\sfs.net\bia\BIA_DWH\parameters\KTS.xlsx')


    mix['KEY_TO_SYMBOLS'] = mix['KEY_TO_SYMBOLS'].replace({'Indented Natural': 'IN',
                                                        'Natural': 'natural',
                                                        'Twinning Wisp': 'TWINNING WISP'}, regex=True)


    mix['Natural'] = np.nan
    mix['IN'] = np.nan
    mix['Twinning'] = np.nan
    mix['Cavity'] = np.nan
    mix['Chip'] = np.nan

    import re
    extraction_patterns = {
        'Natural': r'(natural)',
        'IN': r'(IN)',
        'Twinning': r'(TWINNING WISP)',
        'Cavity': r'(Cavity)',
        'Chip': r'(Chip)'
    }

    # Iterate over each row in the DataFrame
    for index, row in mix.iterrows():
        for column, pattern in extraction_patterns.items():
            if not pd.isna(row['KEY_TO_SYMBOLS']):
                match_result = re.search(pattern, row['KEY_TO_SYMBOLS'], flags=re.IGNORECASE)
                if match_result:
                    mix.at[index, column] = match_result.group(0)
                else:
                    mix.at[index, column] = ''
            else:
                mix.at[index, column] = ''

    mix['ID1'] = mix['Natural'] + np.where(mix['Shp'] == 'RD', 'ROUND', 'FANCY') + mix['Col'] + mix['Prty'] + mix['Fls']

    KTS_selected_columns = KTS.iloc[:, [0, 7]]
    
    mix = mix.merge(KTS_selected_columns, how='left', on='ID1')
    mix['Natural%'] = mix.iloc[:, -1]


    mix['ID1'] = mix['IN'] + np.where(mix['Shp'] == 'RD', 'ROUND', 'FANCY') + mix['Col'] + mix['Prty'] + mix['Fls']
    KTS_selected_columns = KTS.iloc[:, [0, 7]]
    #mix.drop(columns=['DISC_PER_x'],inplace=True)
    mix = mix.merge(KTS_selected_columns, how='left', on='ID1')
    mix['IN%'] = mix.iloc[:, -1]


    mix['ID1'] = mix['Cavity'] + np.where(mix['Shp'] == 'RD', 'ROUND', 'FANCY') + mix['Col'] + mix['Prty'] + mix['Fls']
    KTS_selected_columns = KTS.iloc[:, [0, 7]]
  
    mix = mix.merge(KTS_selected_columns, how='left', on='ID1')
    mix['Cavity%'] = mix.iloc[:, -1]


    mix['ID1'] = mix['Chip'] + np.where(mix['Shp'] == 'RD', 'ROUND', 'FANCY') + mix['Col'] + mix['Prty'] + mix['Fls']
    KTS_selected_columns = KTS.iloc[:, [0, 7]]
    mix.drop(columns=['DISC_PER_x'],inplace=True)
    mix = mix.merge(KTS_selected_columns, how='left', on='ID1')
    mix['Chip%'] = mix.iloc[:, -1]


    mix['ID1'] = mix['Twinning'] + np.where(mix['Shp'] == 'RD', 'ROUND', 'FANCY') + mix['Col'] + mix['Prty'] + mix['Fls']
    KTS_selected_columns = KTS.iloc[:, [0, 7]]
    mix = mix.merge(KTS_selected_columns, how='left', on='ID1')
    mix['Twin Wisp%'] = mix.iloc[:, -1]

    mix['EC%'] = np.where((mix['EYE_CLEAN'] == 'N') & (mix['Prty'].isin(['SI1'])), 2,
                        np.where((mix['EYE_CLEAN'] == 'N') & (mix['Prty'].isin(['SI2'])), 5, 0))

 
    mix['surface graining']=np.nan
    mix['Internal graining'] =np.nan
    mix['clarity based on IG'] = np.nan

    if 'REPORT_COMMENTS' not in mix.columns:
        mix['REPORT_COMMENTS'] = np.nan
    else:
        for i in range(len(mix)):
            if not pd.isna(mix['REPORT_COMMENTS'][i]):
                match_result = mix['REPORT_COMMENTS'][i].str.extract(r'(Surface|surface)')
                mix.at[i, 'surface graining'] = match_result.iloc[0] if not match_result.empty else ''
            else:
                mix.at[i, 'surface graining'] = '' if pd.isna(mix.at[i, 'surface graining']) else mix.at[i, 'surface graining']
                
                
    for i in range(len(mix)):
        if not pd.isna(mix['REPORT_COMMENTS'][i]):
            match_result = mix['REPORT_COMMENTS'][i].str.extract(r'(Internal|internal)')
            mix.at[i, 'Internal graining'] = match_result.iloc[0] if not match_result.empty else ''
        else:
            mix.at[i, 'Internal graining'] = '' if pd.isna(mix.at[i, 'Internal graining']) else mix.at[i, 'Internal graining']            
                
    for i in range(len(mix)):
        if not pd.isna(mix['REPORT_COMMENTS'][i]):
            match_result = mix['REPORT_COMMENTS'][i].str.extract(r'(Clarity grade is based on internal graining)')
            mix.at[i, 'clarity based on IG'] = match_result.iloc[0] if not match_result.empty else ''
        else:
            mix.at[i, 'clarity based on IG'] = '' if pd.isna(mix.at[i, 'clarity based on IG']) else mix.at[i, 'clarity based on IG']            
                            
                




    mix['Surface%'] = np.where((mix['Col'] <= 'F') & (mix['Prty'].isin(['FL', 'IF', 'VVS1', 'VVS2', 'VS1', 'VS2'])) & (mix['Fls'] == 'NON') & (~mix['surface graining'].isna()), 1, 0)
    mix['Internal%'] = np.where((mix['Col'] <= 'F') & (mix['Prty'].isin(['FL', 'IF', 'VVS1', 'VVS2', 'VS1', 'VS2'])) & (mix['Fls'] == 'NON') & (~mix['Internal graining'].isna()), 1, 0)

    mix['S+I'] = np.where(mix['Surface%'] + mix['Internal%'] >= 1, 1, 0)

    mix['clarity based on IG%'] = np.where((~mix['clarity based on IG'].isna()) & (mix['Fls'] == 'NON'), 3, 0)

    mix['Chip%'] = pd.to_numeric(mix['Chip%'], errors='coerce')
    mix['LUSTER'] = mix['LUSTER'].fillna('EX')
    mix = mix.drop(columns=['DISC_PER'])
    mix['LUSTER_ID'] = mix['Range'].astype(str)+mix['Prty'].astype(str)+mix['Fls'].astype(str)+mix['LUSTER'].astype(str)
    LUSTER_NEW = pd.read_excel("//sfs.net/bia/BIA_DWH/parameters/LUSTER_DISC.xlsx")
    print(LUSTER_NEW.columns)
    mix = mix.merge(LUSTER_NEW[['LUSTER_ID', 'DISC_PER']], on='LUSTER_ID', how='left')
    mix['BRL%'] = mix.iloc[:, -1]
    mix = mix.drop(columns = ['LUSTER_ID','DISC_PER'])

    # Here EC% is not added in x55


    # import pandas as pd

    # # Assuming 'mix' is a DataFrame
    # # Assuming 'BASE%', 'SYMM%', 'FLS%', 'DEPTH_PER', 'TABLE_PER', 'RATIO_PER', 'GIRDLE%', 'CN%', 'CW%', 'SN%', 'SW%', 'TO1', 'PO1', 'CO1', 'Natural%', 'IN%', 'Cavity%', 'Chip%', 'EC%', 'S+I', 'clarity based on IG%', 'Twin Wisp%' are columns in 'mix'

    x2 = mix[['BASE%', 'SYMM%', 'FLS%','SHADE%']]
    mix['SUMM'] = x2.sum(axis=1, skipna=True)

    x3 = mix[['DEPTH_PER', 'TABLE_PER', 'RATIO_PER', 'GIRDLE %']]
    mix['DTR'] = x3.sum(axis=1, skipna=True)
    mix['DTR'] = np.where(mix['DTR'] >=11, 10, mix['DTR'])

    x4 = mix[['CN%', 'CW%', 'SN%', 'SW%','BRL%']]
    mix['NATS'] = x4.max(axis=1, skipna=True)
    mix['NATS'] = np.where(mix['NATS'] == -np.inf, 0, mix['NATS'])

    x5 = mix[['TO1', 'PO1', 'CO1']]
    mix['OPEN'] = x5.max(axis=1, skipna=True)
    mix['OPEN'] = np.where(mix['OPEN'] == -np.inf, 0, mix['OPEN'])

    x55 = mix[['Natural%', 'IN%', 'Cavity%', 'Chip%','EC%','S+I', 'clarity based on IG%', 'Twin Wisp%']]
    mix['KTS'] = x55.sum(axis=1, skipna=True)

    x6 = mix[['SUMM', 'NATS', 'DTR']]
    mix['FANCY_DISC'] = x6.sum(axis=1, skipna=True)

    x7 = mix[['SUMM', "NATS",'DTR', 'CUT%',"Dia%"]]
    mix['ROUND_DISC'] = x7.sum(axis=1, skipna=True)

    mix['SYS_DISC'] = np.where(mix['Shp'] == 'RD', mix['ROUND_DISC'], mix['FANCY_DISC'])


    mix['DEPTH_PER'].unique()


    mix['mix_ID'] = mix['Shp'].astype(str) + mix['Col'].astype(str) + mix['Prty'].astype(str) + mix['Pol. Cts'].astype(str) + mix['Fls'].astype(str) + mix['Depth (%)'].astype(str) + mix['Table (%)'].astype(str) + mix['Ratio'].astype(str) + mix['Length'].astype(str) + mix['Width'].astype(str) + mix['Girdle (%)'].astype(str)
    mix['Final_Disc'] = mix['SYS_DISC'].astype(float).round(0)


    file_path = "//sfs.net/bia/BIA_DWH/parameters/EXTRAEFFECT.xlsx"
    Effect = pd.read_excel(file_path)
    Effect['FLS'] = Effect['FLS'].replace(np.nan, '')
    Effect['Effect_Id'] = Effect['SHAPE'] + Effect['SIZE'] + Effect['COLOR'] + Effect['PURITY'] + \
        Effect['FLS'].fillna(' ')

    # Assuming mix is another DataFrame
    mix['Effect_Id'] = np.where((mix['Pol. Cts'] >= 1.00) & (mix['Pol. Cts'] < 5.00),
                            mix['Shp'] + mix['Range'] + mix['Col'] + mix['Prty'] + mix['Fls'].fillna(' '),
                                mix['Shp'] + mix['Range'] + mix['Col'] + mix['Prty'] + '')
  
    mix.drop(columns=['DISC_PER_x','DISC_PER_y'],inplace=True)

    result = pd.merge(mix, Effect[['Effect_Id', 'DISC_PER']], on='Effect_Id', how='left')

   
    
    result.rename(columns={'DISC_PER_y':'DISC_PER'},inplace=True)
   
    
    mix['Extra_effect'] = result['DISC_PER']

    
    mix['Extra_effect'] = mix.apply(lambda row: 0 if row['Shp'] == 'TP' and row['Fls'] != 'NON' else row['Extra_effect'], axis=1)

    mix['DISC'] = mix.apply(lambda row: row['ROUND_DISC'] if row['Shp'] == 'RD' else row['FANCY_DISC'], axis=1)


    mix['Extra_effect'] = mix['Extra_effect'].fillna(0)

    mix['Final_Disc'] = -(mix['DISC'])

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

    # Assuming 'mix' is a pandas DataFrame already defined
    mix['RAP_BAND'] = mix['Carat'].apply(categorize_carat)

    mix['id'] = np.where(mix['Shp'] == 'RD', 'BR', 'PS') + mix['RAP_BAND'] + mix['Col'] + np.where(mix['Prty'].isin(['FL']), 'IF', mix['Prty'])

    Rap_price = pd.read_excel("//sfs.net/bia/BIA_DWH/cur_rap.xlsx", usecols=[0, 1])

    result = pd.merge(mix, Rap_price, left_on='id', right_on=Rap_price.columns[0], how='left')

    mix['RAP'] = result[result.columns[-1]]
    # df['Final_Disc'] = mix['Final_Disc']
    # df['RAP'] = mix['RAP']
    mix.to_clipboard()
    res = pd.merge(df,mix[['Sr_No','RAP','Final_Disc']],on='Sr_No',how='left')
    #mix= mix[columns]
    return res
    mix.to_clipboard(index=False, excel=True)