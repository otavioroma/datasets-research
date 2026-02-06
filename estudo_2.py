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

# Read the file into a variable fifa_data
fifa_data = pd.read_csv(fifa_filepath, index_col="Date", parse_dates=True)
# %%
list(fifa_data.columns)
# %%
plt.figure(figsize=(14,6))
plt.title("Isso é um teste")
sns.lineplot(data=fifa_data)
#sns.lineplot(data=fifa_data['BRA'], label="BRA")
#sns.lineplot(data=fifa_data['ARG'], label="ARG")

plt.xlabel("TESTERRRR")
plt.ylabel("Pontuação")
# %%
