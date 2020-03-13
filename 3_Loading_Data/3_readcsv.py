import pandas as pd

# Read the file and convert to a data frame
filename = 'PDDBI_new.csv'
df = pd.read_csv(filename)
print(df)
