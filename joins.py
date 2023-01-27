import pandas as pd
import numpy as  np

technologies1 = {
    'Cursos':["Spark","PySpark","Python","pandas"],
    'Tarifa' :[250000,350000,450000,385000],
    'Duracion':['30dias','20dias','40dias','60dias'],
}
index_labels1=['r1','r2','r3','r4']
technologies2 = {
    'Cursos':["Spark","Java","Python","Go"],
    'Descuento':[2000,3000,4500,5100]
}
index_labels2=['r1','r6','r3','r5']
df1=pd.DataFrame(technologies1, index=index_labels1)
df2=pd.DataFrame(technologies2,index=index_labels2)
print(df1)
print(df2) 

#Join
dfjoinleft=df1.join(df2,lsuffix='_izq',rsuffix='_der')
print('DataFrame con inner left')
print(dfjoinleft)

#Inner Join
dfinnerjoin=df1.join(df2,lsuffix='_izq',rsuffix='_der',how='inner')
print(dfinnerjoin)

# Right join DataFrames, solo los de la derecha
dfrightjoin=df1.join(df2,lsuffix='_izq',rsuffix='_der',how='right')
print("Solo los de la derecha")
print(dfrightjoin)
dfoter=df1.join(df2,lsuffix="_izquierda",rsuffix="_derecha",how='outer')
print("Demo con Inner Outer")
print(dfoter)

# join por columnas
dfjoincol=df1.set_index('Cursos').join(df2.set_index('Cursos'), how='inner')
print(dfjoincol)

# Pivot Tables 
dfparapivot = pd.DataFrame({"Vendedor": ["Maria", "Luis", "Maria", "Luis", "Maria","Maria", "Maria", "Luis", "Luis"],
        "Zona": ["Norte", "Sur", "Norte", "Norte", "Sur","Sur", "Norte", "Sur", "Sur"],
        "Venta": [1000, 2000, 2000, 3000, 3000, 4000, 5000, 6000, 7000],
        "Comision": [100, 400, 500, 500, 600, 600, 800, 900, 900]
})
print(dfparapivot)

# Suma de Ventas y Comisión por Vendedor
tpvendedorsuma = pd.pivot_table(dfparapivot, index=['Vendedor'],aggfunc=np.sum)
print(tpvendedorsuma)

# Suma de Ventas y Comisión por Zona
tpzonasuma = pd.pivot_table(dfparapivot, index=['Zona'],aggfunc=np.sum)
print(tpzonasuma)
# Promedio de Ventas y Comisión por Vendedor
tpvendedorpromedio = pd.pivot_table(dfparapivot, index=['Vendedor'],aggfunc=np.average)
print(tpvendedorpromedio)
# Promedio de Ventas y Comisión por Zona
tpzonaprom = pd.pivot_table(dfparapivot, index=['Zona'],aggfunc=np.average)
print(tpzonaprom)
# Suma de Ventas y Comisión por Vendedor y Zona
tpvendedorzonasuma = pd.pivot_table(dfparapivot, index=['Vendedor','Zona'],aggfunc=np.sum)
print(tpvendedorzonasuma)
# Suma de Ventas y Comisión por Zona y Vendedor
tpzonavendedorsuma = pd.pivot_table(dfparapivot, index=['Zona','Vendedor'],aggfunc=np.sum)
print(tpzonavendedorsuma)
# Promedio de Ventas y Comisión por Vendedor y Zona
tpvendedorzonaprom = pd.pivot_table(dfparapivot, index=['Vendedor','Zona'],aggfunc=np.average)
print(tpvendedorzonaprom)
