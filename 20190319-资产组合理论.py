
import pandas as pd
import matplotlib.pyplot as plt

stock=pd.read_excel("stock.xlsx",index_col="Trddt")
cumreturn=(1+stock).cumprod() #实现累乘功能

stock.plot()
plt.title("Daily return of the stocks in the portfolio")
plt.legend(loc="lower center",bbox_to_anchor=(0.5,-0.3),ncol=3,fancybox=True,shadow=True)
# plt.show()

cumreturn.plot()
plt.title("Cumulative return of the stocks in the portfolio")
plt.legend(loc="best")
# plt.show()

print(stock.corr())

