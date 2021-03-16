# -*- coding: utf-8 -*-
"""
@author: Juan Castro
juancastropazos@gmail.com
"""

'''
IPC's
'''
import xlrd
import os

loc = (os.getcwd() +'\\Data\\sh_ipc_aperturas.xls')
# se levanta los xls desde otra carpeta

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

Gba = sheet.row_values(8,1)
Pampa = sheet.row_values(59,1)
NorO = sheet.row_values(108,1)
NorE = sheet.row_values(157,1)
Cuyo = sheet.row_values(206,1)
Pata = sheet.row_values(255,1)

ls = [Gba,
      Pampa,
      NorO,
      NorE,
      Cuyo,
      Pata
]

sheet = wb.sheet_by_index(3)
Ponderadores = sheet.row_values(19,1)
Ponderadores


import numpy as np
import pandas as pd


numpy_data = np.array(ls)
numpy_data = np.transpose(numpy_data)
numpy_data
numpy_data = numpy_data*Ponderadores

date = pd.Series(pd.period_range("1/1/2017", freq="M", periods=49))

df = pd.DataFrame(data=numpy_data, index=date, columns=["GBA",
                                            "Pampa",
                                            'NorOeste',
                                            'NorEste',
                                            'Cuyo',
                                            'Pata'])

del Cuyo, Gba, NorE, NorO, numpy_data, Pampa, Pata, loc, wb, sheet, date, ls, Ponderadores


'''
BASE MONETARIA
'''
import pandas as pd
import numpy as np

data = pd.read_excel(os.getcwd() +'\\Data\\seriese.xls') 

date = data.iloc[:, 0]
date = date[8:4472]
date = date.dropna()

base = pd.DataFrame(data['Unnamed: 28'])
base = base[8:4472]
base = base.dropna()

base['mes'] = pd.to_datetime(date, errors='coerce').dt.strftime('%Y-%m')    
base = base.set_index(base['mes'])
base['Unnamed: 28'] = base['Unnamed: 28'].astype(float)
base = base['2017-00': '2021-01']

base = base.rename(columns={'Unnamed: 28':'BaseMonetaria',
                            'mes':'MES'})


means = base.groupby('MES')['BaseMonetaria'].mean()
len(means)

base = base.drop('MES', axis=1)
means = means.rename('BM_mensual')
means = pd.DataFrame(means)

del data, date


'''
VARIABLES MANAGMENT
'''

idx = pd.date_range('2017-01', periods=49, freq='M')

ipc = np.array(df.sum(axis=1))
BM_cte = means['BM_mensual'] / ipc

means['IPC'] = ipc
means['BM_cte'] = BM_cte
means['rate'] = np.array(means['BM_cte'].pct_change())*100
means['IntAnual_rate'] = np.array((means['BM_cte'].pct_change(periods=12)))*100


del idx, ipc, BM_cte

























