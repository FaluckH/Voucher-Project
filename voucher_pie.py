import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("ggplot")
payment_methods = [ "Cash" , "Credit" , "Debit" , "Mobile Wallet", "Voucher" ]
amount_spent = [52,36,28,11,56]
plt.pie(amount_spent, labels=payment_methods, autopct="%.2f%%" , explode=([0, 0 , 0 , 0, 0.1]))
plt.title("Weekly Income")
plt.show()