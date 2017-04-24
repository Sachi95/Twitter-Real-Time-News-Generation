import sys
import time
import datetime
import warnings
import os
warnings.filterwarnings("ignore")
def check(s):
	for i in s:
		if i>='a' and i<='z':
			return True
		if i>='0' and i<='9':
			return True
		if i>='A' and i<='Z':
			return True
	return False
def process(path1,path2,path3,name):
	#path1 contains raw tweets
	#path2 contains topics
	#path3 contains time
	time = []
	filename = FINAL_FOLDER + name.strip()
	WRITE_HANDLER = open(filename,'w')
	for line in open(path3,'r'):
		line = line.strip('\t\n\r')
		if(check(line)) :
			time.append(float(line))
	#for i in time :
	#	print (i)
	for line in open(path2,'r'):
		s1 = line.split(" ")

	#for el in s1:
	#	el = el.strip('\t\n\r')
	#	if(check(el)):
	#		print (el)
	
	max_cntr = 0
	time_arrival = -1
	tweet_heading =""
	idx=0
	for line in open(path1,'r'):
		#print (line)
		orig = line
		line = line.lower();
		line = line.strip('\t\n\r')
		if(check(line)==False):
			continue
		#print (line)
		#print ("-----")
		s2 = set(line.split(" "))
		cntr = 0
		for el in s1:	
			el = el.strip('\t\n\r')
			for el2 in s2:
				el2 = el2.strip('\t\n\r')
				if (check(el) and check(el2) and el==el2):
					cntr+=1
					#print (el+" "+el2)
		if cntr>max_cntr:
			max_cntr = cntr
			tweet_heading = orig
			time_arrival = time[idx]

		else :
			if cntr==max_cntr:
				if time_arrival < time[idx]:
					time_arrival = time[idx]
					tweet_heading = orig
	WRITE_HANDLER.write(tweet_heading)		
	#print (tweet_heading)
DATA_FOLDER = "/home/olivesmoak/Project/NEW_FOLDER/"
TOPIC_FOLDER ="/home/olivesmoak/Project/TOPICS/"
TIME_FOLDER = "/home/olivesmoak/Project/TIME/"
FINAL_FOLDER = "/home/olivesmoak/Project/FINAL_FOLDER/"
#flg = 1
for root, dirs, files in os.walk(DATA_FOLDER): # gets all the files from subfolders recrsively
	#if flg==0:
	#	break
	for name in files:
		#if flg==0:
		#	break
		#flg = 0
		path1 = os.path.join(root, name)
		path2 = os.path.join(TOPIC_FOLDER, name)
		path3 = os.path.join(TIME_FOLDER, name)
		process(path1,path2,path3,name)
