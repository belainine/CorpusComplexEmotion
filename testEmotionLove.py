
#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import pickle
import csv


dir_path = os.path.dirname(os.path.realpath(__file__))
def getData():
	dictEmo={'fear': 0, 'sadness': 0,  'surprise': 0, 'joy': 0, 'love': 0}
	discriptionPsychExp=['joy', 'fear', 'anger', 'sadness', 'disgust', 'shame', 'guilt']

	keys=dictEmo.keys()
	files=['CSVEmoTxt\\'+f+'.csv' for f in keys]
	#file_name=next(iter(files))
	result=list()
	for i,file_name in enumerate(keys):
		f='CSVEmoTxt\\'+file_name+'.csv'
		with open(f, newline='') as csvfile:
			spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
			tmp=[ [ set() if row[1]=='NO' else {file_name} ,row[2]]   for  row in spamreader]
			result.append(tmp)

	resultdict=result[0]
	listLabels= 'fear,joy,sadness'.split(',')
	listLabelsOther= 'anger,disgust,shame,guilt'.split(',')
	for elt in result:
		for i in range(len(elt)):
			resultdict[i][0]=resultdict[i][0]|elt[i][0]
	res=list()
	for elt in resultdict:
	   
		dictEmo={'fear': 0, 'sadness': 0,  'surprise': 0, 'joy': 0, 'love': 0,'anger':0,'disgust':0,'shame':0,'guilt':0,'anticipation':0,'trust':0}
		for e in elt[0]:
			dictEmo[e]=1
			if e=='love':
				dictEmo['trust']=1
				dictEmo['joy']=1
			res.append((dictEmo,elt[1]))   
	return (res)
                

getData()