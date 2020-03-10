#!/usr/bin/python3

import os
import pandas as pd

where = os.getcwd()
print(where)
what = os.listdir(where)
print(what)
path = './assessments/'
#os.chdir(path)
folders = os.listdir(path)
print(folders)
for folder in folders:

	os.chdir(folder)

	df_new = pd.read_csv('new')
	print(df_new)

	df_old = pd.read_csv('old')
	print(df_old)

	os.chdir('..')
