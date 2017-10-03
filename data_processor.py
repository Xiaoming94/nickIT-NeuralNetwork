import numpy as np
import sqlite3
import os
import random

datadirpath = os.path.join(".", "data")
dataset = "english"

def prerun():
	ready = True
	notReady = False
	if not os.path.exists(datadirpath):
		print("Missing data dir \n creating")
		os.makedirs(datadirpath)
	if os.listdir(datadirpath) == []:
		print("Your data directory is empty")
		return notReady
	return ready

def process_data(dataset):
	data_path = os.path.join(datadirpath, dataset + ".txt")
	datafile = open(data_path)
	data_arr = datafile.read().split("\n")
	return data_arr

def rand_words(data_arr,lower,higher,count):
	letters = set()
	[[letters.add(c) for c in word] for word in data_arr]
	letters = sorted(list(letters))
	rand_sequences = []
	word_lengths = np.random.randint(low=lower,high=higher,size=count)
	for length in word_lengths:
		sequence = [random.choice(letters) for i in range(length)]
		sequence = "".join(sequence)
		rand_sequences.append(sequence)

	return rand_sequences

ready = prerun()
if not ready:
	print("Not ready to run")
	sys.exit()

readable = process_data("english")
not_readable = rand_words(data,1,20,len(readable))



print("==== Script Done ====")
