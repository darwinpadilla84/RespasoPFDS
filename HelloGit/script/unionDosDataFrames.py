# Ejemplo real
import pandas as pd
import numpy as np

dr1=pd.read_csv("C:/Users/padillad/Downloads/VL_GENERAL_DP (1).csv")
dr2=pd.read_csv("C:/Users/padillad/Downloads/VL_GENERAL_DP (2).csv")

# Cambiar nombres todas las columnas dr1
dr1.columns=['PROVINCIA_US', 'CANTON_US','EDIFICIO_US','ESPECIALIZACION_US', 'TOTAL NDD']
#dr1.columns
dr2.columns=['PROVINCIA_US', 'CANTON_US','EDIFICIO_US','ESPECIALIZACION_US', 'TOTAL NDD ASESINATO']
#dr2.columns

# Crear códigos únicos
dr1['COD']=dr1.PROVINCIA_US+dr1.CANTON_US+dr1.EDIFICIO_US+dr1.ESPECIALIZACION_US
dr1.head()
dr2=dr2.drop(['PROVINCIA_US', 'CANTON_US', 'EDIFICIO_US', 'ESPECIALIZACION_US'],axis=1)

# Union de data frame
df=pd.merge(dr1,dr2,how='left').drop('COD',axis=1)

# Exportar csv
df.to_csv('C:/Users/padillad/Downloads/infoAdministrativo.csv',index=False)
