import pandas as pd

df = pd.read_csv('/home/afzal/python/IAIS/задача для DE/admin_lev6.txt.csv', delimiter=';')
t=''
for i in df.columns:
    if i[-1]=='D':
        t+=f'StructField("{i}", IntegerType(), True),\n'
    else: t+=f'StructField("{i}", StringType(), True),\n' 
print(t)