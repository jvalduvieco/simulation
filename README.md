# simulacio_rgc
## Run
`python data_import.py input.csv output.csv`

## Importar a pandas
```
import pandas as pd
import numpy as np

input_data = pd.read_csv('RGC_complete.csv')
input_data['RENDA_MES'] = [x.replace('.', '') for x in input_data['RENDA_MES']]
input_data['RENDA_MES'] = [x.replace(',', '.') for x in input_data['RENDA_MES']]
input_data['RENDA_MES'] = input_data['RENDA_MES'].astype(float)
```

## JOIN results
```
results_RGC = pd.read_csv('results.csv')
results_join = input_data.join(results_RGC.set_index('ID_PERS'), on = 'ID_PERS')
```

## Distribució RENDA_MES

```
s = pd.Series(df['RENDA_MES'])
pd.Series.value_counts(s, bins=[0,250,500,750,1000,1250,1500,1750,2000,2250,2500,2750,3000], sort=False, ascending=True )`

```

```
Euros               # Usuaris
(-0.001, 250.0]     164707
(250.0, 500.0]        7649
(500.0, 750.0]       14867
(750.0, 1000.0]      19746
(1000.0, 1250.0]     16827
(1250.0, 1500.0]      7798
(1500.0, 1750.0]       958
(1750.0, 2000.0]        19
(2000.0, 2250.0]         0
(2250.0, 2500.0]         1
(2500.0, 2750.0]         0
(2750.0, 3000.0]         0
``` 

# Resultats
```
df = pd.read_csv('results.csv')
s = pd.Series(df['2.0'])
pd.Series.value_counts(s, bins=[0,250,500,750,1000,1250,1500,1750,2000,2250,2500,2750,3000], sort=False, ascending=True )
```

```
(-0.001, 250.0]     121420
(250.0, 500.0]        1317
(500.0, 750.0]        8350
(750.0, 1000.0]      67839
(1000.0, 1250.0]     33835
(1250.0, 1500.0]         0
(1500.0, 1750.0]         0
(1750.0, 2000.0]         0
(2000.0, 2250.0]         0
(2250.0, 2500.0]         0
```
