import csv
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from statsmodels.stats.outliers_influence import variance_inflation_factor as vif
import seaborn as sns
df1=pd.read_csv("/home/yn/デスクトップ/kadai/temp.csv")
df2=pd.read_csv("/home/yn/デスクトップ/kadai/powerV2.csv")


selected_index = ["平均気温", "降水量", "降雪量"]
#selected_index=["平均気温","最高気温","最低気温","降水量","日照時間","降雪量","平均風速","平均蒸気圧","平均湿度","平均現地気圧"]

x2=df1.loc[:,selected_index].values
x_corr = df1.loc[:,selected_index ].corr()

y=df2.loc[:,["average"]].values

plt.figure()
plt.rcParams['font.family'] = 'IPAexMincho'
sns.heatmap(x_corr,square=True,annot=True)
plt.show()

vifs=[vif(x2,i) for i in range(0,len(selected_index))]
print(pd.DataFrame(vifs,index=selected_index,columns=["VIF"]))


x_added_constant=sm.add_constant(x2)
model=sm.OLS(y,x_added_constant)
result=model.fit()
print("RESULT")
print(result.summary())