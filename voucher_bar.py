import pandas as pd
import matplotlib.pyplot as plt 

plt.style.use('ggplot')

df = pd.DataFrame({
    "Payment Method" : [
    "Credit",
    "Cash",
    "Debit",
    "Mobile Wallet",
    "Voucher"
],
    "Items Sold" : [3,11,16,13,2],
})

df = df.sort_values("Items Sold")
bar_colours = ["red" if x=="Voucher" else "blue" for x in df["Payment Method"]]

plt.bar("Payment Method", "Items Sold", data = df, color=bar_colours)
plt.title("Items Sold Per Payment method")
plt.xlabel("Payment Method")
plt.ylabel("Items Sold")
plt.show()