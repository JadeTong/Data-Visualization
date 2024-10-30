import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

#保险数据，看为什么有些客户交多点钱
insurance_data = pd.read_csv('C:/Users/Jade Tong/Desktop/KAGGLE/3. Data Visualization/DV datasets/insurance.csv')
insurance_data.head()

#%% 画散点图
sns.scatterplot(x=insurance_data['bmi'], y=insurance_data['charges'])
#从散点图上可看出BMI和保险费具有正相关关系，可拟合一条回归线，用sns.regplot
sns.regplot(x=insurance_data['bmi'], y=insurance_data['charges']) 

#%% 用颜色分类的散点
sns.scatterplot(x=insurance_data['bmi'], y=insurance_data['charges'], 
                hue=insurance_data['smoker'])
#从散点图上可看出nonsmokers to tend to pay slightly more with increasing BMI, smokers pay MUCH more.
#分别拟合两条回归线，吸烟的斜率更大
sns.lmplot(x="bmi", y="charges", hue="smoker", data=insurance_data) #注意跟sns.regplot有不同

#%% 类别散点图 categorical scatter plot，用sns.swarmplot
sns.swarmplot(x=insurance_data['smoker'],
              y=insurance_data['charges'])

#  on average, non-smokers are charged less than smokers, and
#  the customers who pay the most are smokers; whereas the customers who pay the least are non-smokers.