import numpy as np
import sqlite3
import os

datadirpath = os.path.join(".", "data")

def prerun():
	if not os.path.exists(datadirpath):
		print("Missing data dir \n creating")
		os.makedirs(datadirpath)


prerun()
print("==== Script Done ====")
