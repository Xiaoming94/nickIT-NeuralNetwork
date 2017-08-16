import numpy as np
import sqlite3
import os

datadirpath = os.path.join(".", "data")

def prerun():
	ready = True
	notReady = False
	if not os.path.exists(datadirpath):
		print("Missing data dir \n creating")
		os.makedirs(datadirpath)
	if os.listdir(datadirpath) == []:
		print("Your data directory is empty")
		return notReady

ready = prerun()
if not ready:
	print("Not ready to run")
	sys.exit()


print("==== Script Done ====")
