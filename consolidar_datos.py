import pandas as pd
import os

path = r"C:\Users\abdel\OneDrive\Documentos\05 Hospedaje"
files = os.listdir(path)
files_xlsx = [f for f in files if f[-4:] == 'xlsx']

df_list = []
for f in files_xlsx:
    data = pd.read_excel(os.path.join(path, f))
    df_list.append(data)
df = pd.concat(df_list)

output_path = r"C:\Users\abdel\Desktop\output_file.xlsx"
df.to_excel(output_path, index=False)

# Librerías descargadas: pandas, os, openpyxl