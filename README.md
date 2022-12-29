# CSCI 8790 Project 1
## Name: Sheung Hang Sean Kan
## ID: 811282984
### 1. Assumption
The assumption made in this project are as follows:
#### 1.1 Hash function
The hash functions within the bloom filter are capable of allocate the strings into the bit array with uniform probability.
#### 1.2 Stability of the false positive rate
The false positive rate is assumed to be stable as the tested size of each bloom filter (with different number of input strings) is set to be 15000.
### 2. Instruction for running the code
####  2.1 Requirement
The required environment is listed in the requirements.txt file. Users can use the command
```
$ pip install -r requirements.txt
```
to install every needed packages to run the program.
#### 2.2 Project Members
The project members are as follows:
##### 2.2.1 BloomFilter.py
The implementation of BloomFilter class.
##### 2.2.2 Project_1.ipynb
The performance study experiment.
##### 2.2.3 wlist_match11.txt
The list of strings used in the performance study experiment.
