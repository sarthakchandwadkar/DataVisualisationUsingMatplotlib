import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("QueryResults.csv", names = ['DATE', 'TAG', 'POSTS'], header = 0)

#view first and last five rows
print(df.head())
print(df.tail())

#for checking the dimenions
print("Dimensions: ", df.shape)

#Checking the count of non-Nan values
print("Count: ",df.count())

#Number of entries and posts by programming language
print("Group by result: ", df.groupby("TAG").sum())

#Checking for how many months of entry exixt per programming language
print("Number of entries: ", df.groupby("TAG").count())


#Data Cleaning
#Date Column
print(df['DATE'][1])

#inspecting the type of data
print("Data Type ",type(df[ 'DATE'][1]))

#Type conversion of entire column
df. DATE = pd.to_datetime (df.DATE)
print(df.head ())

print("Updated Data Type ",type(df[ 'DATE'][1]))

#Data manipulation
reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')
print(reshaped_df.columns)
print(reshaped_df.head())

#Dealing with NaN values
reshaped_df.fillna(0, inplace=True)
print(reshaped_df. isna().values.any ())

#Data Visualisation
plt.plot(reshaped_df.index, reshaped_df.java)
plt.figure(figsize=(16,10))
plt.plot(reshaped_df.index, reshaped_df.java)
plt. figure (figsize= (16,10))
plt.xticks (fontsize=14)
plt.yticks (fontsize=14)
plt. plot (reshaped_df.index,reshaped_df.java)
plt. plot (reshaped_df.index,reshaped_df.python)
plt.show()

#Plotting all programming languages on same chart
for column in reshaped_df.columns:
    plt.plot(reshaped_df.index, reshaped_df[column], linewidth=3, label=reshaped_df[column].name)
plt.show()

#Smoothing Proces

roll_df = reshaped_df.rolling(window=6).mean()

plt.figure(figsize=(16, 10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)

# plot the roll_df instead
for column in roll_df.columns:
    plt.plot(roll_df.index, roll_df[column],
             linewidth=3, label=roll_df[column].name)

plt.legend(fontsize=16)
plt.show()






