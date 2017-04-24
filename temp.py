from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

import sys
import os
import re
from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.luhn import LuhnSummarizer
from gensim.summarization import summarize


def process(path, filename):
	#print("Cleaning "+path)
	#print (path)
	filename = DATA_FOLDER + filename.strip()
	WRITE_HANDLER = open(filename, 'w')
	LANGUAGE = "english"
	file = path #name of the plain-text file
	parser = PlaintextParser.from_file(file, Tokenizer(LANGUAGE))
	
	stemmer = Stemmer(LANGUAGE)

	summarizer = Summarizer(stemmer)
	summarizer.stop_words = get_stop_words(LANGUAGE)

	#summarizer = LuhnSummarizer()

	#summary = summarizer(parser.document, 4) #Summarize the document with 5 sentences

	#new_line = ""
	#for line in open(path, 'r'):
	#	new_line += line;
	#summary = summarize(str(new_line), word_count=50) #Summarize the document with max 100 words
	for sentence in summarizer(parser.document, 5):
		WRITE_HANDLER.write(str(sentence) + '\n\n')				


CLEANED_DATA = "/home/olivesmoak/Project/DUP_REMOVE_FOLDER/"
DATA_FOLDER = "/home/olivesmoak/Project/SUMMY_FOLDER/"
for root, dirs, files in os.walk(CLEANED_DATA): # gets all the files from subfolders recrsively
	for name in files:
		absolute_path = os.path.join(root, name)
		if os.path.isfile(absolute_path) and name != ".DS_Store":
			filename = process(absolute_path, name)
			#preprocess(filename, name) -- Call seperate tag code for this task