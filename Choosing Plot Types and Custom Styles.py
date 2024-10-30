import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

spotify_data = pd.read_csv('C:/Users/Jade Tong/Desktop/KAGGLE/3. Data Visualization/DV datasets/spotify.csv', index_col="Date", parse_dates=True)

#%% Line chart 
plt.figure(figsize=(12,6))
sns.lineplot(data=spotify_data)

#%% 将主题换成暗模式
# Change the style of the figure to the "dark" theme
sns.set_style("dark")

# Line chart 
plt.figure(figsize=(12,6))
sns.lineplot(data=spotify_data)

#Seaborn has five different themes: 
    #(1)"darkgrid", 
    #(2)"whitegrid", 
    #(3)"dark", 
    #(4)"white", and 
    #(5)"ticks"














