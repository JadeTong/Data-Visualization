import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
print("Setup Complete")

#%% load the data  六个国家（阿根廷、巴西、西班牙、法国、德国、意大利）的FIFA排名
# Path of the file to read
fifa_filepath = "C:/Users/Jade Tong/Desktop/KAGGLE/3. Data Visualization/DV datasets/fifa.csv"

# Read the file into a variable fifa_data
fifa_data = pd.read_csv(fifa_filepath, index_col="Date", parse_dates=True)

#%% Examine the data
fifa_data.head()

#%% Plot the data
# 调节图像的宽和高
plt.figure(figsize=(16,6))

# Line chart showing how FIFA rankings evolved over time 
sns.lineplot(data=fifa_data)