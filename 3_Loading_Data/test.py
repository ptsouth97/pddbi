#!/usr/bin/python3

import os
import pandas as pd

where = os.getcwd()
print("The current working directory is:")
print(where)
print()

what = os.listdir(where)
print("The files is the directory are:")
print(what)
print()

path = './assessments/'
print("Changing directories...")
os.chdir(path)

now = os.getcwd()
print("Now the current working directory is:")
print(now)
print()

folders = os.listdir(now)
print("The folders in the current working directory are:")
print(folders)
print()

for folder in folders:

	os.chdir(folder)

	df_new = pd.read_csv('new.csv')
	print(df_new)

	df_old = pd.read_csv('old.csv')
	print(df_old)

	os.chdir('..')
