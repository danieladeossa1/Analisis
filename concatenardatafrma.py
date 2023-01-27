import pandas as pd
import numpy as np
df1= pd.DataFrame({
    "Vendedor":['Mario','Maria','Luis','Luisa'],
    "Zona":['Norte','Sur','Oriente','Occidente'],
    "Venta":[4500,2500,1800,3600]
},
index=[0,1,2,3])

df2= pd.DataFrame({
    "Vendedor":['Luis','Mario','Luisa','Luis'],
    "Zona":['Sur','Norte','Occidente','Oriente'],
    "Venta":[2500,1500,2800,7600]
},
index=[4,5,6,7])


df3= pd.DataFrame({
    "Vendedor":['Luisa','Maria','Luis','Mario'],
    "Zona":['Oriente','Sur','Norte','Occidente'],
    "Venta":[7500,8500,6800,4760]
},
index=[8,9,10,11])
print(df1)
print(df2)
print(df3)

frames=[df1,df2,df3]
print("Concatenación de los 3 DFs")
dfresult= pd.concat(frames,keys=["s1","s2","s3"])
print(dfresult)
mkeys=["suc1","suc2","suc3"]
dfresult= pd.concat([df1,df2,df3],keys=mkeys)
print(dfresult)
#Mostrar las ventas de la sucursal 
print("Ventas de la sucursal 1, basado en df concatenado")
print(dfresult.loc['suc1'])
print("Ventas de la sucursal 2, basado en df concatenado")
print(dfresult.loc['suc2'])
print("Ventas de la sucursal 3, basado en df concatenado")
print(dfresult.loc['suc3'])

#Mostrar las ventas de Luis, solo para las columnas de Zona y Venta
print("Ventas de Luis, solo para las columnas de Zona y Venta")
print(dfresult.query('Vendedor == "Luis"')[['Zona','Venta']])
