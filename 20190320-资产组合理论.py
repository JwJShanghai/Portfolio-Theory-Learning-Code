
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import linalg
from cvxopt import matrix, solvers

stock_1=pd.read_excel("stock.xlsx",index_col="Trddt")
stock=stock_1.iloc[0:int(stock_1.shape[0]/2),0:3]
stock_test=stock_1.iloc[int(stock_1.shape[0]/2):stock_1.shape[0],0:3]
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

class MeanVariance:
    def __init__(self,returns):
        self.returns=returns
    #定义构造器，传入收益率数据
    def minVar(self,goalreturn):
        
        covs=np.array(self.returns.cov())
        means=np.array(self.returns.mean())

        size = means.shape[0]

        P=2*matrix(covs)
        q=matrix(np.zeros(shape=(size,1)))
        A = matrix(np.column_stack((means,np.ones(shape=(size,1))))).T
        b = matrix(np.array([[goalreturn],[1]]))
        result = solvers.qp(P,q,A=A,b=b)
        return(result['x'])

stock_learn=MeanVariance(stock)
k=stock_learn.minVar(0.003)

real_return=np.array(stock_test)
ratio=np.array(k)

portfolio_return=np.dot(real_return,ratio)
market_return=np.array(stock_1.iloc[int(stock_1.shape[0]/2):stock_1.shape[0],3:])
market_cum=(1+market_return).cumprod()
cumulative_return=(1+portfolio_return).cumprod()
cum=pd.DataFrame(cumulative_return,columns=["portfolio"])
cum["market"]=market_cum
cum.plot()
plt.title("Return of the porfolio and the Market index")
plt.show()