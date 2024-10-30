############看分布情况

import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

#数据为三种鸢尾花Iris-setosa、Iris-versicolor和Iris-virginica各50条的记录
iris_data = pd.read_csv('C:/Users/Jade Tong/Desktop/KAGGLE/3. Data Visualization/DV datasets/iris.csv', index_col="Id")
iris_data.head()
#数据有4个特征：花萼长度(sepal length)、花萼宽度(sepal width)、花瓣长度(petal length)和花瓣宽度(petal width)

#%% 直方图
# Histogram 
sns.histplot(iris_data['Petal Length (cm)'])

#%% 概率密度图 （用sns.kdeplot）
# KDE plot (kernel density estimate)
sns.kdeplot(data=iris_data['Petal Length (cm)'], shade=True)

#%% 二维概率密度图（用sns.jointplot）
sns.jointplot(x=iris_data['Petal Length (cm)'], y=iris_data['Sepal Width (cm)'], kind="kde")
##注意图上方的曲线为x坐标变量的概率密度曲线，右方的曲线为y坐标变量的概率密度曲线

#%% 多个特征的直方图合并到一个
# Histograms for each species
sns.histplot(data=iris_data, x='Petal Length (cm)', hue='Species')

# Add title
plt.title("Histogram of Petal Lengths, by Species")

#%% 多个特征的概率密度曲线合并到一个
# KDE plots for each species
sns.kdeplot(data=iris_data, x='Petal Length (cm)', hue='Species', shade=True)

# Add title
plt.title("Distribution of Petal Lengths, by Species")




