import pandas as pd
import matplotlib.pyplot as plt


# Read the file and convert to a data frame
filename = 'PDDBI_new.csv'
df_new = pd.read_csv(filename)
print(df_new)

# Slice the new dataframe into 3 sections
df1 = df_new.iloc[0:9, :]
df2 = df_new.iloc[9:14, :]
df3 = df_new.iloc[14:16, :]

# Construct a plot of the T score versus the Domain for the NEW DATA
plt.plot(df1['Domain'], df1['T score'], color='black', marker='.', markersize=12)
plt.plot(df2['Domain'], df2['T score'], color='black', marker='.', markersize=12)
plt.plot(df3['Domain'], df3['T score'], color='black', marker='.', markersize=12)

# Adjust plot labels
plt.xlabel('Domain')
plt.ylabel('T score')
plt.title('PDDBI-PX T-Score Profile')

# Display the plot
plt.show()
