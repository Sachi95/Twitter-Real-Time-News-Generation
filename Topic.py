import sys
import os
import re
import string
import nltk        
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from gensim import corpora, models
import gensim

stemmer = PorterStemmer()
def process(topics,Uname):
	filename = TOPIC_FOLDER + Uname.strip()
	WRITE_HANDLER = open(filename,'w')
	flg = 0
	result="";
	for ch in topics:
		if ch =="\"":
			if result=="\n" or result=="\t":
				continue
			if result!="":
				#print (result)
				WRITE_HANDLER.write(result +' ')
			flg = 1 - flg
			result =""
		else :
			if flg==1 :
				result += ch

def stem_tokens(tokens, stemmer):
	stemmed = []
	for item in tokens:
		stemmed.append(stemmer.stem(item))
	return stemmed

def tokenize(text):
	
	text = re.sub("[^a-zA-Z]", " ", text) # Removing numbers and punctuation
	text = re.sub(" +"," ", text) # Removing extra white space
	text = re.sub("\\b[a-zA-Z0-9]{10,100}\\b"," ",text) # Removing very long words above 10 characters
	text = re.sub("\\b[a-zA-Z0-9]{0,1}\\b"," ",text) # Removing single characters (e.g k, K)
	tokens = nltk.word_tokenize(text.strip())
	tokens = nltk.pos_tag(tokens)
	# Uncomment next line to use stemmer
	#tokens = stem_tokens(tokens, stemmer)
	return tokens

stopset = stopwords.words('english')
#for w in stopset :
#    print (w)
freq_words = ['http','https','amp','com','co','th']
for i in freq_words :
    stopset.append(i)

def analyze(fileObj,Uname) :
	filename = LDA_FOLDER + Uname.strip()
	WRITE_HANDLER = open(filename, 'w')
	#print (filename)
	text_corpus = []
	for doc in fileObj :
		temp_doc = tokenize(doc.strip())
		current_doc = []
		for word in range(len(temp_doc)) :
			if temp_doc[word][0] not in stopset and temp_doc[word][1] == 'NN':
				current_doc.append(temp_doc[word][0])        

		text_corpus.append(current_doc)


	dictionary = corpora.Dictionary(text_corpus)
	#dictionary.save_as_text("outfile",sort_by_word=True)
	corpus = [dictionary.doc2bow(text) for text in text_corpus]
	ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=1, id2word = dictionary,passes=60)
	WRITE_HANDLER.write('Topics for ' + Uname + '\n')
	for topics in ldamodel.print_topics(num_topics=1, num_words=10) :
		#print (topics, '\n')
		WRITE_HANDLER.write(' '.join(str(s) for s in topics) + '\n')
		for s in topics :
			process(str(s),Uname)
	

DATA_FOLDER = "/home/olivesmoak/Project/CLEANED_FOLDER/"
LDA_FOLDER = "/home/olivesmoak/Project/LDA_FOLDER/"
TOPIC_FOLDER = "/home/olivesmoak/Project/TOPICS/"

for root, dirs, files in os.walk(DATA_FOLDER): # gets all the files from subfolders recrsively
	for name in files:
		absolute_path = os.path.join(root, name)
		if os.path.isfile(absolute_path) and name != ".DS_Store":
			filename = absolute_path
			file = open(filename)
			analyze(file,name)
			#preprocess(filename, name) -- Call seperate tag code for this task
