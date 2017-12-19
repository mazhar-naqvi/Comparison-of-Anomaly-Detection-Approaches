import cuckoopy
import sys

#Reads file and adds items to a list
def read_data(string,mode):
	no_of_lines=0
	datfile = open (string,mode)
	data=[]
	for l in datfile:
		data.append([])
		no_of_lines=no_of_lines+1
		for i in l.split():
			data[-1].append(i)
	t=[data,no_of_lines]
	return t 

#Inserts elements into the cuckoo filter
def insert(data,length,cf,window_size):
	for i in range(0,length-window_size+1):
		start=i
		end=start+window_size
		this_window=data[start:end]
		str_this_window=[str(a) for a in this_window]
		item=','.join(str_this_window)
		#print(item)
		if not cf.contains(item):
			cf.insert(str(item))

#find if the element is present in the cuckoo filter
def assert_cf(data,length,cf,window_size):
	present=0
	not_present=0
	for i in range(0,length-window_size+1):
		start=i
		end=start+window_size
		this_window=data[start:end]
		str_this_window=[str(a) for a in this_window]
		item=','.join(str_this_window)
		if not cf.contains(item):
			#print("No anamolous behaviour detected")
			#print("Anamolous behaviour detected")
			#print("Anomalous sequence: ")
			print(item)

#Read the training file
training_file=read_data("training.txt","r")
training_data=training_file[0]
training_len=training_file[1]

#create a cuckoo filter
cf = cuckoopy.CuckooFilter(capacity=100000,bucket_size=1000, fingerprint_size=1)

#Train the cuckoo filter
insert(training_data,training_len,cf,5)

#Read the test file
test_file=read_data("anom.txt","r")
test_data=test_file[0]
test_len=test_file[1]

#test if the elements of test data are present in the cuckoo filter
assert_cf(test_data,test_len,cf,5)
