# -*- coding: utf-8 -*-
"""
@author: Juan Castro
juancastropazos@gmail.com
"""

import os, sys


'''
INSERT WORK DIRECTORY DE LA CARPETA Alphacast.io
'''
os.chdir('C:\\Users\\juan_\\Dropbox\\Mi PC (LAPTOP-H9MAOJRB)\\Desktop\\Alphacast.io')


os.chdir('INSERT WD de la carpeta Alphacast.io')
os.getcwd() # para chequear


'''
DATA CLEANING
'''

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



'''
ANALYSIS
'''

'--> PLOTS'

import matplotlib.pyplot as plt


means['BM_mensual'].plot(linewidth=2.5)
plt.title('Base Monetaria Mensual',
          size=15,
          loc='left',
          pad=15)
plt.ylabel(None)
plt.yticks(rotation=0)
plt.xlabel('Periodos')
plt.show()

means['IPC'].plot(linewidth=2.5)
plt.title('IPC',
          size=15,
          loc='left',
          pad=15)
plt.ylabel('Pctaje(%)',
           rotation=45, size=10)
plt.yticks(rotation=45)
plt.xlabel('Periodos')
plt.show()

means['BM_cte'].plot(linewidth=2.5)
plt.title('BM Precios Corrientes',
          size=15,
          loc='left',
          pad=15)
plt.ylabel('Variación(%)',
           rotation=45, size=10)
plt.yticks(rotation=45)
plt.xlabel('Periodos')
plt.show()

means['rate'].plot(linewidth=2.5)
plt.title('Tasa de Variación',
          size=15,
          loc='left',
          pad=15)
plt.ylabel('Pctaje(%)',
           rotation=45, size=10)
plt.yticks(rotation=45)
plt.xlabel('Periodos')
plt.show()

means['IntAnual_rate'].plot(linewidth=2.5)
plt.title('Variación Interanual',
          size=15,
          loc='left',
          pad=15)
plt.ylabel('Pctaje(%)',
           rotation=45, size=10)
plt.yticks(rotation=45)
plt.xlabel('Periodos')
plt.show()

'BOXPLOTs - IPC'
'IPC por Año y IPC groupby Mes'

idx = pd.date_range('2017-01', periods=49, freq='M').strftime('%Y') 
IPC_df = pd.DataFrame(means['IPC'])
a = [i for i in range(1,13)]*4
a.append(1)
IPC_df['Año'] = idx
IPC_df['Mes'] = a
del idx, a

IPC_df.boxplot(by='Año', column=['IPC'], grid=False, rot=45, fontsize=15)
IPC_df.boxplot(by='Mes', grid=False)











