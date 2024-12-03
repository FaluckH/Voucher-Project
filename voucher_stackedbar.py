import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("ggplot")

df = pd.DataFrame({
   "Monday":[56,13,1,10,10],
   "Tuesday":[77,23,4,10,10],
   "Wednesday":[35,48,9,10,10],
   "Thursday": [65,45,19,10,10],
    "Friday": [65,45,19,10,10],
    "Saturday": [65,45,19,10,10],
    "Sunday": [65,45,19,10,10] 

}, index=["Cash", "Credit", "Debit", "Mobile Wallet", "Voucher"])
 
df =  df.T
print(df)
my_plot = df.plot.bar(stacked=True)
plt.savefig("daily_spenditures.png", bbox_inches = "tight")

plt.title("Weekly Income")
plt.xlabel("Days Of The Week")
plt.ylabel("Number of Sales")

plt.show()