import sys
import os
import re
import string
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk import pos_tag
import linecache


def clean(path, filename):

	with open(path) as f:
	    for i, l in enumerate(f):
	            pass
	    x=i+1
	    k=0
	    i=2
	    j=1
	    initial=linecache.getline(path, 1)
	    cleanfile = DUP_REMOVE_DATA + filename.strip()
	    clean= open (cleanfile,'w')
	    clean.write(initial)
	    while i<(x+1):
	        a=linecache.getline(path, i)
	        while j<i:
	            b=linecache.getline(path, j)
	            t1=set(a.split(" "))
	            t2=set(b.split(" "))
	            t3=t1.intersection(t2)
	            if len(t3)>0.5*len(t1):
	                k=k+1
	            j=j+1
	        if k==0:
	                clean= open (cleanfile,'a')
	                clean.write(a)
	                clean.write('\n')
	        k=0
	        j=1
	        i=i+1
			
#DATA_FOLDER = sys.argv[1]
DATA_FOLDER = "/home/olivesmoak/Project/NEW_FOLDER/"
#CLEANED_DATA = sys.argv[2]
DUP_REMOVE_DATA = "/home/olivesmoak/Project/DUP_REMOVE_FOLDER/"
for root, dirs, files in os.walk(DATA_FOLDER): # gets all the files from subfolders recrsively
	for name in files:
		absolute_path = os.path.join(root, name)
		if os.path.isfile(absolute_path) and name != ".DS_Store":
			filename = clean(absolute_path, name)
			#preprocess(filename, name) -- Call seperate tag code for this task
			
					

