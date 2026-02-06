#%%
import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
print("Setup Complete")
# %%
# Path of the file to read
fifa_filepath = r"C:\Users\otavi\Downloads\fifa.csv"
fifa_data = pd.read_csv(fifa_filepath, index_col="Date", parse_dates=True)
# %%
fifa_data
# %%
# Set the width and height of the figure
plt.figure(figsize=(10,6))

# Add title
plt.title("Teste de Gráfico de Barras")

# Bar chart showing average arrival delay for Spirit Airlines flights by month
sns.barplot(x=fifa_data.index, y=fifa_data['BRA'], palette="GnBu_r")

# Add label for vertical axis
plt.ylabel("TESTETETESTE")
plt.xlabel("OIOIOI")
# %%
# Set the width and height of the figure
plt.figure(figsize=(14,7))

# Add title
plt.title("É um teste")

# Heatmap showing average arrival delay for each airline by month
sns.heatmap(data=fifa_data, annot=True)

# Add label for horizontal axis
plt.xlabel("Argentina")
# %%
