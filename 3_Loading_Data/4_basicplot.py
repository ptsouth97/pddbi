import pandas as pd
import matplotlib.pyplot as plt


# Read the file and convert to a data frame
filename = 'test_data.csv'
df = pd.read_csv(filename)
print(df)

# Construct a plot of the T score versus the Domain
plt.plot(df['Domain'], df['T score'], color='black', marker='.', markersize=12)

# Adjust plot labels
plt.xlabel('Domain')
plt.ylabel('T score')
plt.title('PDDBI-PX T-Score Profile')

# Display the plot
plt.show()
