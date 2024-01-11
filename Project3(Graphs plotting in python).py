import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


path="E:\\Web Dev\\Practice\\Data Analysis\\Customers data.csv"
data = pd.read_csv(path, encoding='latin-1')

# Get 50% random samples 
# print(data.sample(frac=0.50))
# print(data.isnull())
# sns.heatmap(data.isnull())      
# sns.histplot(data.isnull())

# histogram 
# plt.figure(figsize=(6, 4))
# sns.histplot(data['City'].dropna(), bins=1)
# plt.title('Distribution of Salaries')
# plt.xlabel('City')
# plt.ylabel('Number of Customers')
# plt.show()

# plt.figure(figsize=(6,4))
# sns.histplot(data['City'].dropna(),bins=1) # bins=gap betwween bars and dropna=droping null values
# plt.title("Salaries")
# plt.xlabel("Salry")
# plt.ylabel("Years")
# plt.show()

# pie chart 
# year_counts = data['Salary'].value_counts().dropna()
# plt.figure(figsize=(6, 4))
# plt.pie(year_counts, labels=year_counts.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
# plt.title('Distribution of Salary')
# plt.show()

# drop all missing values 
# print(data.dropna(how='any',inplace=True))
# print(data.shape)

# check duplicate data 
# dup=data.duplicated().any()
# print(dup)  
# print(data)
# print(data.drop_duplicates())

# data2=data.drop(['Name'], axis=1)
# print(data2) 
# print("Old data columns: ",len(data.columns)) 
# print("New data columns: ",len(data2.columns)) 

# Univariate Analysis= perf analysis on one variable at a time

        # City Distribution 
# plt.figure(figsize=(6,4))
# plt.title("City Distribution")
# plt.xlabel("City")
# plt.ylabel("Number of employes")
# # sns.histplot(data['City'],kde=True)
# sns.histplot(data['City'],kde=True)
# plt.show()

# Bivariate Analysis= perf analysis on 2 variables 

# sns.boxplot(x='City', y='Salary',data=data)
# plt.figure(figsize=(6,4))
# plt.title("City Distribution")
# plt.xlabel("City")
# plt.ylabel("Salary")
# plt.show()

# sns.boxenplot(x='City', y='Salary',data=data)
# plt.figure(figsize=(6,4))
# plt.title("City Distribution")
# plt.xlabel("City")
# plt.ylabel("Salary")
# plt.show()


# salary and city relation with dots type graph 
# sns.catplot(x='City', y='Salary',data=data)
# plt.figure(figsize=(6,4))
# plt.title("City Distribution")
# plt.xlabel("City") 
# plt.ylabel("Salary")
# plt.show()

# how many persons having same salary 
# sns.countplot(x='Salary',data=data)
# plt.figure(figsize=(6,4))
# plt.title("City Distribution")
# plt.xlabel("City")
# plt.ylabel("Salary")
# plt.show()


# sns.countplot(x='Salary',data=data)
# plt.figure(figsize=(6,4))
# plt.title("City Distribution")
# plt.xlabel("City")
# plt.ylabel("Salary")
# plt.show()

# replace values 
# import numpy as np
# data=data.replace(to_replace=['?'],value=['Australia'],inplace=True)
# print(data)

# print(data.groupby('Country')['Salary'].mean().sort_values(ascending=False))
print(data['Name'].sort_values())
