import requests
import json
import csv
import time
import datetime
import dbconnect
import psycopg2
import numpy as np
import pandas as pd
from string import punctuation
import string
import nltk
def main():
    dbconnect.connect()
    mylist = dbconnect.getdeminfo()
    joined_string = dict()
    for num, i in enumerate(mylist):  
        joined_string[num] = "".join(i)  

    word = dict()
    dic = dict() 

    for num, line in enumerate(joined_string.values()):
        word[num] = line

    for num, line in enumerate(word.values()):
        word[num] = line.replace("\n",'')

    for num, line in enumerate(word.values()):
        word[num] = line.replace(",",'')
        
    for num, line in enumerate(word.values()):
        word[num] = line.replace(".",'')
    
    for num, line in enumerate(word.values()):
        word[num] = line.replace("!",'')

     for num, line in enumerate(word.values()):
        word[num] = line.replace("?",'')

    for num, line in enumerate(word.values()):
        word[num] = line.replace("[removed]",'')

    for num, line in enumerate(word.values()):
        word[num] = line.replace("[",'')

    for num, line in enumerate(word.values()):
        word[num] = line.replace("]",'')
    
    for num, line in enumerate(word.values()):
        word[num] = line.replace('"','')
       

    for num, line in enumerate(word.values()):
	    word[num] = line.split() 
    tags = set(['NN','NNS','NNP','NNPS','JJ','JJR','JJS']) #remain nonus and adjective
    for num, line in enumerate(word.values()):
        pos_tags =nltk.pos_tag(line)
        word[num] =[word for word,pos in pos_tags if pos in tags] 
    

    for item in word.values():   
        word_low = [s.lower() for s in item]
        for i in word_low:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
    
    dic = sorted(dic.items(),key = lambda items:items[1],reverse = True)
    dic = dic[:100] #top100
    dictdata = dict()
    for l in dic:
        dictdata[l[0]] = l[1]
    print(dictdata)
if __name__ == '__main__':
    main()
    