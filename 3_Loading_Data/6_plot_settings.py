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

# Adjust y-axis limit settings
plt.ylim(10, 100)

# Add grid lines
plt.grid(axis='y', which='major', linestyle='-')
plt.grid(axis='y', which='minor', linestyle='--')

# Add blue shading between T Score 40 - 60
plt.axhspan(40, 60, alpha=0.25, color='blue')

# Add tick marks to the left and right side of chart
plt.tick_params(labelright=True, which='both')

# Add vertical lines
plt.axvline(x=8.5, color='gray', linewidth=1)
plt.axvline(x=13.5, color='gray', linewidth=1)

# Annotations
plt.annotate('Approach/Withdrawl Problems', (2.5, 98))
plt.annotate('Receptive/Expressive', (10.0, 98))
plt.annotate('Social Communication Abilities', (9.5, 96))

# Set the plot size
fig = plt.gcf()
fig.set_size_inches(11, 13)

# Display the plot
plt.show()
