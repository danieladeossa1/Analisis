import pandas as pd
import numpy as np
import openpyxl


#punto 1 y 3
print("--Punto 1 y 2 --")
listaprecio=[2000,4000,8000,4000,2000,3000,6000]
listaarticulo=['CPU','PORTAIL','PANTALLA','IPAD','CELULAR','PORTATIL','PANTALLA']
print(listaprecio)
print(listaarticulo)

#punto 3
print("--Punto 3--")
serieprecio=pd.Series(listaprecio)
serieprecio1=pd.Series(data=listaprecio,index=['CPU','PORTAIL','PANTALLA','IPAD','CELULAR','PORTATIL','PANTALLA'])
print(serieprecio1)

#series punto 4
print("--punto 4--")
seriesarticulos=pd.Series(listaarticulo)
seriesarticulos1=pd.Series(data=listaarticulo,index=[2000,4000,8000,4000,2000,3000,6000])
print(seriesarticulos1)

#Punto 5
print("--punto 5--")
print(seriesarticulos.iloc[1])

#Punto 6
print("--punto 6--")
dataventas={'Vendedor':['Daniela','Natalia','Sergio','Susana','Daniela','Sergio'],'Zona':['Norte','Sur','Occidente','Oriente','Sur','Norte'],
            'Año':[2023,2022,2021,2020,2023,2021],'Valor':[1000,5000,6000,1000,3000,6000]}
dfventas=pd.DataFrame(dataventas)
print(dfventas)

#punto 7
print("--punto 7--")
print(dfventas.query('Zona != "Sur"'))

#punto 8
print("--punto 8--")
print(dfventas.query('Zona == "Norte"'))

#Punto 9
print("--punto 9--")
Z1="Occidente"
Z2="Oriente"
print(dfventas.query('Zona == @Z1 or Zona == @Z2')[['Zona','Valor']])

#Punto 10
print("--punto 10--")
Z3="Sur"
print(dfventas.query('Zona == @Z3')[['Zona','Valor']])

#Punto 11
print("--punto 11--")
dfventas['Comision']=dfventas['Valor']*0.02
print(dfventas)

#Punto 12 (Columan axis = 1 y fila axis=0)
print("--punto 12--")
dfventas.drop('Comision',axis=1, inplace=True)
print(dfventas)

#Punto 13
print("--punto 13--")
print(dfventas.loc[(dfventas['Año']== 2020) & (dfventas['Valor']>121)][['Vendedor','Zona','Año','Valor',]])

#Punto 14
print("--punto 14--")
print(dfventas.loc[(dfventas['Año']== 2021) & (dfventas['Valor']>121)][['Año','Valor']])

#Punto 15
print("--punto 15--")
print(dfventas.loc[dfventas['Vendedor']== 'Daniela'][['Vendedor','Zona','Valor']])

#Punto 16
print("--punto 16--")
print(dfventas.groupby('Vendedor').describe())


#Punto 17
print("--punto 17--")
print(dfventas.groupby('Zona').describe())

#Punto 18
print("--punto 18--")
print(dfventas.groupby('Zona').mean())

#Punto 19
print("--punto 19--")
print(dfventas.groupby('Año').max('Valor'))

#Punto 20
print("--punto 20--")
print(dfventas.groupby('Vendedor').min('Valor'))


#Punto 21
print("--punto 21--")
print(dfventas.groupby('Año').std())

#importar datos de un libro de excel
archivo='poliza.xlsx'
datos=pd.read_excel(archivo)
dfexcel=pd.DataFrame(datos)
print("Póliza importada de excel")
print(dfexcel)
print(dfexcel.groupby('Numero_Poliza').mean())

