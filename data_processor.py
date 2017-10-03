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

def create_alphabet(data_arr):
	alphabet = set()
	[[alphabet.add(c) for c in word] for word in data_arr]
	alphabet = sorted(list(alphabet))
	print("Number of letters read: %s" % len(alphabet))
	print("Our alphabet is:")
	print(alphabet)
	return alphabet

def rand_words(alphabet,lower,higher,count):
	rand_sequences = []
	word_lengths = np.random.randint(low=lower,high=higher,size=count)
	for length in word_lengths:
		sequence = [random.choice(alphabet).lower() for i in range(length)]
		sequence = "".join(sequence)
		rand_sequences.append(sequence)

	return rand_sequences

def label_data(data,label):
	if label == "readable":
		return construct_labels(data,[1,0])
	else:
		return construct_labels(data,[0,1])
def construct_labels(data,label):
	data_count = len(data)
	labels = []
	for count in range(data_count):
		print(f"labeled {count} of {data_count} data points", end="\r")
		labels.append(np.array(label))

	print()
	return labels


ready = prerun()
if not ready:
	print("Not ready to run")
	sys.exit()

print("reading data")
readable = process_data("english")
readable.extend(process_data("swedish"))
print("creating alphabet")
alphabet = create_alphabet(readable)
print("generating rubish")
not_readable = rand_words(alphabet,1,20,len(readable))
print("labeling readable words")
labels = label_data(readable,"readable")
print("labeling non-readable-words")
labels.extend(label_data(not_readable,"not-readable"))


print("==== Script Done ====")
