#!/usr/bin/python3

import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.lines as mlines



path = './assessments'
filelist = os.listdir(path)

for file in filelist:
        
        # Read files and convert to dataframe 
        df_new = pd.read_csv(filename1)
        print(df_new)

        df_old = pd.read_csv(filename2)
        print(df_old)

        # Slice the new dataframe into 3 sections
        df1 = df_new.iloc[0:9, :]
        df2 = df_new.iloc[9:14, :]
        df3 = df_new.iloc[14:16, :]

        # Slice the old dataframe into 3 sections
        df1old = df_old.iloc[0:9, :]
        df2old = df_old.iloc[9:14, :]
        df3old = df_old.iloc[14:16, :]

        # Set the plot size
        fig = plt.gcf()
        fig.set_size_inches(11, 13)

        # Plot the new data
        _ = plt.plot(df1['Domain'], df1['T score'], color='black', marker='.', markersize=12, label='June 2019')
        _ = plt.plot(df2['Domain'], df2['T score'], color='black', marker='.', markersize=12)
        _ = plt.plot(df3['Domain'], df3['T score'], color='black', marker='.', markersize=12)
        dot = mlines.Line2D([], [], color='black', marker='.', markersize=12, label=new)

        # Plot the old data
        _ = plt.plot(df1old['Domain'], df1old['T score'], color='black', marker='^', markersize=10, linestyle='--', label='December 2018')
        _ = plt.plot(df2old['Domain'], df2old['T score'], color='black', marker='^', markersize=10, linestyle='--')
        _ = plt.plot(df3old['Domain'], df3old['T score'], color='black', marker='^', markersize=10, linestyle='--')
        tri = mlines.Line2D([], [], color='black', marker='^', markersize=10, label=old)

        # Adjust plot settings to match PDDBI
        _ = plt.legend(handles=(dot, tri))
        _ = plt.ylim(10, 100)
        _ = plt.xlabel('Domain')
        _ = plt.ylabel('T score')
        _ = plt.grid(axis='y', which='major', linestyle='-')
        _ = plt.grid(axis='y', which='minor', linestyle='--')
        _ = plt.axhspan(40, 60, alpha=0.25, color='blue')
        _ = plt.tick_params(labelright=True, which='both')
        _ = plt.axvline(x=8.5, color='gray', linewidth=1)
        _ = plt.axvline(x=13.5, color='gray', linewidth=1)
        _ = plt.title('PDDBI-PX T-Score Profile')
        _ = plt.annotate('Approach/Withdrawl Problems', (2.5, 98))
        _ = plt.annotate('Receptive/Expressive', (10.0, 98))
        _ = plt.annotate('Social Communication Abilities', (9.5, 96))
        _ = plt.tight_layout()
        _ = plt.savefig(graph_name)
        _ = plt.show()
        _ = plt.close()


