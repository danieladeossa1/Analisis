import pandas as pd
import numpy as np
dicnotas={
    'Nombre':['Vanessa','Luis','Pepita'],
    'Edad':[25,23,22],
    'Profesor':['Juan','Pedro','Luis'],
    'Logica':[3.6,4,5],
    'Moviles':[4,5,2.2],
    'Web':[2,1.5,4.8],
    'Analisis':[4,3.9,5],
    'Lenguajes':[2.6,5,1.8]
}
dfnotas=pd.DataFrame(dicnotas)
print(dfnotas) 

#Mostrar dataframe a lo largo (para transporner la info)
dflargo= dfnotas.melt(id_vars=['Nombre','Edad','Profesor'],var_name='Asignatura',value_name='Nota')
print(dflargo)

#Campo calculado con condiciones
dflargo['Observacion']=["Gana" if nota >= 3 else "Pierde" for nota in dflargo ['Nota']]
print(dflargo)

#Con metodo where de numpy
dflargo['Competente']=np.where(dflargo['Nota']< 3, "No","Si")
print(dflargo)