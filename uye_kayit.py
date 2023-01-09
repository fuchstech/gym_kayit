import pandas as pd
import numpy  as np

df = pd.read_excel("uye_kayitlari.xlsx",index_col=False)
df_dict= {"İsim Soyisim" : "Kerem Yıldız",
"Üyelik Başlangıç Tarihi": "02-01-2023",
"Üyelik Bitiş Tarihi" :"02-02-2023",
"Telefon Numarası": "555555555"}
yeni_df = pd.DataFrame(df_dict,index=[0])
print(yeni_df)