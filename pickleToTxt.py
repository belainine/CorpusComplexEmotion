#!/usr/bin/python
# -*- coding: utf-8 -*-
import pickle
import DictionnairePlutchik
import dialydialog
import testEmotionLove
import AffectiveText
import wordnetdata
"""

Converting data from pickle file to text file

usage: python script.py 

To save it to a txt file, run with 
usage: python script.py new_file.txt


Peur + joie = fear': 1, 'joy :1 ='culpabilité'= guilt
Peur + Dégoût =  fear + disgust = honte = shame

"""

# Set the path to the pickle file 
file_name = "./PsychExp/raw.pickle" 
def readDatasetPsychExp(file_name):
	# Open and read the pickle file 
	fd=open(file_name, "rb")
	data = pickle.load(fd,  encoding='latin1')

	### Read 
	try:
		texts = [x.encode('utf-8') for x in data['texts']]
		labels = [[ 1 if elt else 0 for elt in x['label']]  for x in data['info']]
		
	except UnicodeDecodeError as e:
		texts = [x for x in data['texts']]
		labels = [x['label'] for x in data['info']]
	return labels,texts

labels,texts=readDatasetPsychExp(file_name)
listLabels= 'joy,fear,anger,sadness,disgust,shame,guilt,surprise,trust,anticipation'.split(',')
# 'sadness', 'surprise', 'trust','anticipation', 'joy', 'fear', 'disgust', 'anger'
dataset={'labels':list(),'texts':list()}
for i in range(len(texts)):
	#print({ key:int(val) for key,val in zip(listLabels,labels[i]) })
	#print( labels[i], texts[i].decode())
	dic={ key:int(val) for key,val in zip(listLabels,labels[i]+[0]*3) }
	if dic['shame']:
		dic['fear'] =1 ; dic['disgust']=1
	if dic['guilt']:
		dic['fear'] =1 ; dic['joy']=1
	dic['love']=0
	if( 1 in dic.values()):
		dataset['labels'].append(dic)
		dataset['texts'].append(texts[i].decode())
n=len(texts)
labels,texts=readDatasetPsychExp('SE0714/raw.pickle')

listLabels= 'fear,joy,sadness'.split(',')
listLabelsOther= 'anger,disgust,shame,guilt,surprise,trust,anticipation'.split(',')
#dataset={'labels':list(),'texts':list()}
for i in range(len(texts)):
	dictLabels={ key:int(val) for key,val in zip(listLabels,labels[i]) }
	dictLabels=dict(list(dictLabels.items()) + list({ key:int(val) for key,val in zip(listLabelsOther,[0]*7) }.items())) 
	#print(dictLabels)
	#print( labels[i], texts[i].decode())
	dictLabels['love']=0
	if( 1 in dictLabels.values()):
		dataset['labels'].append(dictLabels)
		dataset['texts'].append(texts[i].decode())

#print(len(dataset['labels']),len(texts),n)

#dataset={'labels':list(),'texts':list()}
res=testEmotionLove.getData()
for d, txt in res :
	dataset['labels'].append(d)
	dataset['texts'].append(txt)

res=AffectiveText.getData()


dataset['labels']+=res['labels']
dataset['texts']+=res['texts']


file_name='annotation\\bigrams_annotated\\sebastian.annotated'
file_dict='annotation\\patterns_annotated\\sebastian.annotated'


result1=DictionnairePlutchik.readFromCorpus(file_name)

for l,v in zip(result1['labels'],result1['texts']):
	l['love']=0
	dataset['labels'].append(l)
	dataset['texts'].append(v)

#dataset={'labels':list(),'texts':list()}

result=DictionnairePlutchik.readFromDictionary(file_dict)
#print(result)


for l,v in zip(result['labels'],result['texts']):
	l['love']=0
	dataset['labels'].append(l)
	dataset['texts'].append(v)


	


'''
result=dialydialog.readdialydialog(dialydialog.dialogues_text,dialydialog.dialogues_emotion)
for l,v in zip(result['labels'],result['texts']):
	l['love']=0
	dataset['labels'].append(l)
	dataset['texts'].append(v)

dataset1=wordnetdata.wordnetAllExampls()
dataset['labels']+=dataset1['labels']
dataset['texts']+=dataset1['texts']
'''




"""
randomise data
"""
"""
randliste=list( (k,v)  for k,v in zip(dataset['labels'],dataset['texts']))

temp=[]
for i in range(len(randliste)):
	if i % 2 ==0 :
		temp.append(randliste[i])
	else:
		temp=[randliste[i]]+temp
print(dataset['labels'][:2])
dataset['labels']=[k for k,v in temp]
dataset['texts']=[v for k,v in temp]
print(dataset['labels'][-3:])


"""



"""

"""
pickle.dump( dataset, open( "datasetshameguilt.pickle", "wb" ) )


{'trust': 0, 'sadness': 0, 'surprise': 0, 'love': 0, 'anger': 0, 'disgust': 0, 'guilt': 0, 'joy': 1, 'anticipation': 0, 'shame': 0, 'fear': 0}

joy_sadness=['joy', 'sadness']
trust_disgust=['trust', 'disgust']
fear_anger=['fear','anger']
anticipation_surprise=['anticipation','surprise']

dataset_joy_sadness={'texts':list(),'info':list()}
dataset_trust_disgust={'texts':list(),'info':list()}
dataset_fear_anger={'texts':list(),'info':list()}
dataset_anticipation_surprise={'texts':list(),'info':list()}
import numpy as np
for i in range(len(dataset['labels'])):
	
	temp=[dataset['labels'][i][js] for js in joy_sadness]
	if( False):
		print('Erreur '+'',(temp),dataset['texts'][i])
	else:
		temp+=[0] if 1 in temp else [1]
		dataset_joy_sadness['texts'].append(dataset['texts'][i])
		dataset_joy_sadness['info'].append({'label':np.array(temp)})
	#print(np.array(temp))
	temp=[dataset['labels'][i][js] for js in trust_disgust]
	if( False):
		print('Erreur '+'',(temp),dataset['texts'][i])
	else:
		dataset_trust_disgust['texts'].append(dataset['texts'][i])
		temp+=[0] if 1 in temp else [1]
		dataset_trust_disgust['info'].append({'label':np.array(temp)})

	#print(np.array(temp))
	temp=[dataset['labels'][i][js] for js in fear_anger]
	if( False):
		print('Erreur '+'',(temp),dataset['texts'][i])	
	else:
		dataset_fear_anger['texts'].append(dataset['texts'][i])
		temp+=[0] if 1 in temp else [1]
		dataset_fear_anger['info'].append({'label':np.array(temp)})

	#print(np.array(temp))
	temp=[dataset['labels'][i][js] for js in anticipation_surprise]
	if( False):
		print('Erreur '+'',(temp),dataset['texts'][i])		
	else:
		dataset_anticipation_surprise['texts'].append(dataset['texts'][i])
		temp+=[0] if 1 in temp else [1]
		#print(temp)
		
		#	print(np.array(temp),dataset['texts'][i])
		dataset_anticipation_surprise['info'].append({'label':np.array(temp)})
def initDataSet(datasetPart,biEmotionListe, lessTo=10):
    for i in range(-len(datasetPart['info']),0,1):

        if (datasetPart['info'][i]['label'][0]==0 and datasetPart['info'][i]['label'][1]==0):
            if(i%10 >lessTo ):
                del datasetPart['info'][i]
                del datasetPart['texts'][i]
        
    dataset_temp={'texts':list(),'info':list()}
    for i in range(len(datasetPart['texts'])):
        
        if ((datasetPart['texts'][i] in datasetPart['texts'][i+1:] and  datasetPart['texts'][i]  not in dataset_temp['texts'])or( datasetPart['texts'][i]  in dataset_temp['texts'])) and (datasetPart['info'][i]['label'][2]==1) :
            dataset_temp['info'].append(datasetPart['info'][i])
            dataset_temp['texts'].append(datasetPart['texts'][i])
            temp={datasetPart['texts'][i]}#wordnetdata.getNewSentenses(datasetPart['texts'][i])
            for newSents in temp:
                dataset_temp['info'].append(datasetPart['info'][i])
                dataset_temp['texts'].append(newSents)
            '''
            '''
        elif (datasetPart['info'][i]['label'][2]==0 or (datasetPart['texts'][i] not in datasetPart['texts'][i+1:] and  datasetPart['texts'][i]  not in dataset_temp['texts']) ):
            
            dataset_temp['info'].append(datasetPart['info'][i])
            dataset_temp['texts'].append(datasetPart['texts'][i])
            '''
            '''
            if ( (datasetPart['info'][i]['label'][2]==0)):
                temp={datasetPart['texts'][i]}#wordnetdata.getNewSentenses(datasetPart['texts'][i])
                for newSents in temp:
                    dataset_temp['info'].append(datasetPart['info'][i])
                    dataset_temp['texts'].append(newSents)
            '''
            '''
        else:
            print('add-',datasetPart['texts'][i])
    datasetPart['info']=dataset_temp['info']
    datasetPart['texts']=dataset_temp['texts']
    datasetPart['train_ind']= 0.7
    datasetPart['val_ind']= 0.1
    datasetPart['test_ind']= 0.2
    datasetPart['tiket']=biEmotionListe
    #print('add',dataset_temp)
    return datasetPart

dataset_joy_sadness=initDataSet(dataset_joy_sadness,joy_sadness, lessTo=10)
dataset_trust_disgust=initDataSet(dataset_trust_disgust,trust_disgust, lessTo=10)
dataset_fear_anger=initDataSet(dataset_fear_anger,fear_anger, lessTo=10)
dataset_anticipation_surprise=initDataSet(dataset_anticipation_surprise,anticipation_surprise, lessTo=5)
def countElt(datasetPart):
	label=np.array([0,0,0])
	for i in range(len(datasetPart['info'])):
		#print(datasetPart['info'][i],datasetPart['texts'][i])
		label+=datasetPart['info'][i]['label']
	return label
def printData(datasetPart):
	for i in range(len(datasetPart['info'])):
		print(datasetPart['info'][i]['label'],datasetPart['texts'][i])		    
print(countElt(dataset_joy_sadness)*0.70)
print(countElt(dataset_trust_disgust)*0.70)
print(countElt(dataset_fear_anger)*0.70)
print(countElt(dataset_anticipation_surprise)*0.70)

print(countElt(dataset_joy_sadness)*0.15)
print(countElt(dataset_trust_disgust)*0.15)
print(countElt(dataset_fear_anger)*0.15)
print(countElt(dataset_anticipation_surprise)*0.15)

print(countElt(dataset_joy_sadness))
print(countElt(dataset_trust_disgust))
print(countElt(dataset_fear_anger))
print(countElt(dataset_anticipation_surprise))

pickle.dump( dataset_joy_sadness, open( "dataset_joy_sadness.pickle", "wb" ) )
pickle.dump( dataset_trust_disgust, open( "dataset_trust_disgust.pickle", "wb" ) )
pickle.dump( dataset_fear_anger, open( "dataset_fear_anger.pickle", "wb" ) )
pickle.dump( dataset_anticipation_surprise, open( "dataset_anticipation_surprise.pickle", "wb" ) )
#printData(dataset_joy_sadness)
print(len(dataset_anticipation_surprise['info'])==len(dataset_anticipation_surprise['texts']))
print(len(dataset_trust_disgust['info'])==len(dataset_trust_disgust['texts']))
print(len(dataset_joy_sadness['info'])==len(dataset_joy_sadness['texts']))
print(len(dataset_fear_anger['info'])==len(dataset_fear_anger['texts']))
