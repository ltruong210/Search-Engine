import os 
import re

path = 'D:\Study\Information Retrieval\WEBPAGES_CLEAN\0'

def tokenize(file_name):
    tokens = {}
    stopwords = open('stopwords.txt').read().close()
    for file in os.listdir(path):
        pattern = re.compile('[\W_]+')
        tokens[file] = open(file, 'r').read().lower();
        tokens[file] = pattern.sub(' ', tokens[file])
