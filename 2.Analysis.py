# -*- coding: utf-8 -*-
"""
@author: Juan Castro
juancastropazos@gmail.com
"""

import os

'''
INSERT WORK DIRECTORY DE LA CARPETA Alphacast.io
'''
os.chdir('C:\\Users\\juan_\\Dropbox\\Mi PC (LAPTOP-H9MAOJRB)\\Desktop\\Alphacast.io')


os.chdir('INSERT WD de la carpeta Alphacast.io')
os.getcwd() # para chequear

exec(open('1.DataCleaning.py').read())

'''
ANALYSIS
'''

'PLOTS'

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
plt.title('Tasa de Variación BM',
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



