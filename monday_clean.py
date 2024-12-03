import pandas as pd
 
df = pd.read_excel("monday_voucher_data.xlsx")
 
df = df.set_index("Transaction ID")
 
df = df.dropna(how="any")
df = df.drop_duplicates()

print(df)

