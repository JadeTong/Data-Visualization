import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

#%%用美国运输局记录的飞行延迟
flight_filepath = "C:/Users/Jade Tong/Desktop/KAGGLE/3. Data Visualization/DV datasets/flight_delays.csv"
flight_data = pd.read_csv(flight_filepath, index_col="Month")
flight_data

#%% 画条形图（spirit airlines的平均延迟，代号NK）
# Set the width and height of the figure
plt.figure(figsize=(10,6))

# Add title
plt.title("Average Arrival Delay for Spirit Airlines Flights, by Month")

# Bar chart showing average arrival delay for Spirit Airlines flights by month
sns.barplot(x=flight_data.index, y=flight_data['NK'])  ##要用flight_data.index而不是flight_data.Month

# Add label for vertical axis
plt.ylabel("Arrival delay (in minutes)")

#%% heatmap 热力图
# Set the width and height of the figure
plt.figure(figsize=(14,7))

# Add title
plt.title("Average Arrival Delay for Each Airline, by Month")

# Heatmap showing average arrival delay for each airline by month
sns.heatmap(flight_data, annot=True)

# Add label for horizontal axis
plt.xlabel("Airline")