#  python script 4 BankChurners Dataset

def print_hello(name):
    print(f'Hello {name}')

if __name__ == '__main__':
    print_hello('World')
    print('This is a Python script 4 BankChurners Dataset')

# as in *main.py* > https://liveuniba.sharepoint.com/:u:/r/sites/FMUK_DataAnalysisforManagement_2024-25/Class%20Materials/work/Python/main.py?csf=1&web=1&e=yYHdOe
# install packages: pandas (installs numpy as well),matplotlib, scipy, openpyxl, sqlalchemy, (mysqlclient), pymysql

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sqlalchemy as sqla
import seaborn as sns

# loading
data = pd.read_csv("BankChurners.csv")

# Terminal
# some prints
print("\nDATA TYPES HERE:")
print(data.dtypes)
print("\nDATA COMPLEX INFO HERE:")
print(data.info())

# previously... Analysis of Education Level, Marital Status, Gender, and Income Category etc.
# now in Py... Analysis of a relationship between Credit_Limit and Total_Trans_Amt


# Plot no1 - scatter plot
# dark background
sns.set_style("darkgrid")
plt.style.use("dark_background")

# Set Times New Roman font globally for this plot
plt.rcParams['font.family'] = 'Times New Roman'

# Card_Category must be uppercase
data["Card_Category"] = data["Card_Category"].str.upper()

# custom neon green palette
custom_palette = {
    "BLUE": "#00FFCC",       # Aqua
    "SILVER": "#39FF14",     # Neon green
    "GOLD": "#66FF66",       # Light green
    "PLATINUM": "#ADFF2F"    # Yellow-green
}


# scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=data,
    x="Credit_Limit",
    y="Total_Trans_Amt",
    hue="Card_Category",
    palette=custom_palette,
    alpha=0.7,
    edgecolor=None,
)

# titles
plt.title("Credit Limit vs Total Transaction Amount", fontsize=16, weight='bold')
plt.xlabel("Credit Limit", fontsize=12,fontstyle='italic')
plt.ylabel("Total Transaction Amount", fontsize=12, fontstyle='italic')
plt.legend(title="CARD CATEGORY", loc='upper right')

# okayy lets go
plt.tight_layout()
plt.show()

# back in Terminal
# pearson
correlation = data[["Credit_Limit", "Total_Trans_Amt"]].corr().iloc[0, 1]
print(f"PEARSON correlation between Credit Limit and Total Transaction Amount: {round(correlation, 2)}")
# interpretation
if correlation > 0.5:
    print("→ strong positive link.")
elif correlation > 0.3:
    print("→ moderate positive link.")
elif correlation > 0.1:
    print("→ weak positive link.")
elif correlation > -0.1:
    print("→ very little to no correlation.")
elif correlation > -0.3:
    print("→ weak negative link.")
elif correlation > -0.5:
    print("→ moderate negative link.")
else:
    print("→ strong negative link.")

# Plot No2 - boxplot
# trying Times New Roman
plt.rcParams['font.family'] = 'Times New Roman'

# categorizing CL here
def credit_limit_category(cl):
    if cl < 3000:
        return 'Low'
    elif cl < 10000:
        return 'Medium'
    else:
        return 'High'

# apply
data['CL_Category'] = data['Credit_Limit'].apply(credit_limit_category)

# order categories
category_order = ['Low', 'Medium', 'High']

# custom palette
grey_palette = {
    "Low": "#252525",      # dark grey
    "Medium": "#969696",   # medium grey
    "High": "#FFFFFF"      # white
}

# plot
plt.figure(figsize=(8, 5))
sns.boxplot(
    data=data,
    x='CL_Category',
    y='Total_Trans_Amt',
    hue='CL_Category',
    order=category_order,
    palette=grey_palette,
    legend=False
)

# titles
plt.title("Total Transactions by Credit Limit Category", fontsize=14, weight='bold')
plt.xlabel("Credit Limit", fontstyle='italic')
plt.ylabel("Total Transaction Amount", fontstyle='italic')

# okayy lets go
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# back in Terminal
# loading BankChurners.CSV
print("\nBankChurners.csv HERE:")
data = pd.read_csv('BankChurners.csv')
print(data.head())  # first 5 rows

# RANDOM SELECT(S)
print("\nRANDOM SELECT HERE:")
print(data.loc[:, ['Credit_Limit', 'Total_Trans_Amt']])  # all rows, only two columns
print(data[1:5][['Credit_Limit', 'Total_Trans_Amt']])  # rows 1–4, only selected columns

# DESCRIPTIVE STATS
print("\nDESCRIPTIVE STATS HERE:")
df_stats = data[['Credit_Limit', 'Total_Trans_Amt']]

print("MIN:")
print(df_stats.min())

print("\nMAX:")
print(df_stats.max())

print("\nMEAN:")
print(df_stats.mean())

print("\nMEDIAN:")
print(df_stats.median())

print("\nMODE:")
print(df_stats.mode())


# DESCRIBE
print("\nDESCRIBE HERE:")
print(df_stats.describe())

# end