
import os
#!/usr/bin/python
import json
import pickle
dir_path = os.path.dirname(os.path.realpath(__file__))

file_name='annotation\\bigrams_annotated\\sebastian.annotated'
discriptionPsychExp=['joy', 'fear', 'anger', 'sadness', 'disgust', 'shame', 'guilt']
import csv
liste=['', 'trust', 'sadness', 'surprise', 'anticipation', 'joy', 'fear', 'disgust', 'anger']
ens=set(liste)
def readFromCorpus(file_name):
    result=list()
    dataset={'labels':list(),'texts':list()}
    with open(file_name, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter='\t', quotechar='|')
        for i, row in enumerate(spamreader):
            
            if(row[5]  in liste):
                row[3]=row[3].replace('``','').replace("'",'')
                l=[1 if e in row[5:6] else 0  for e in liste]
                d=dict([(k,v) for k,v in zip(liste,l)])
                del d['']
                result.append((d,row[3]))

                dataset['labels'].append(d)
                
                
    return dataset

file_dict='annotation\\patterns_annotated\\sebastian.annotated'
def readFromDictionary(file_dict):
    result=list()
    dataset={'labels':list(),'texts':list()}
    with open('vocabulary.json', encoding='utf-8') as data_file:
        data = json.loads(data_file.read())
    with open(file_dict, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter='\t', quotechar='|')
        for i, row in enumerate(spamreader):
            l=[1 if e in [r.split('_')[0] for r in row[1:] if len(r)>0 ] else 0  for e in liste]
            d=dict([(k,v) for k,v in zip(liste,l)])
            del d['']
            if row[0] in data.keys():
                result.append((d,row[0]))
                dataset['labels'].append(d)
                dataset['texts'].append('he is  '+ row[0])
                dataset['labels'].append(d)
                dataset['texts'].append('i am '+ row[0])
                
    file_wnaffect='annotation/wordnetaffect/wnaffectlemmas.txt'
    '''
    result=list()
    dataset={'labels':list(),'texts':list()}
    '''
    dataset1={'labels':list(),'texts':list()}
    with open(file_wnaffect,'r',encoding='utf-8') as file:
        
        for i, row in enumerate(file):
            row=row.replace('\t'," ")
            rows=row.strip().split(' ')
            
            lab=rows[0]
            l=[1 if e in [lab] else 0  for e in liste]
            
            d=dict([(k,v) for k,v in zip(liste,l)])
            
            for r in rows[1:]:
                r=r.strip().replace('_',' ')
                if r in data.keys() or ' ' in r:
                    
                    if r not in dataset1['texts']:
                       
                        dataset1['labels'].append(d)
                        dataset1['texts'].append( r)    
                    else:
                        index=0
                        for index in range(len(dataset1['texts'])):
                            if r==dataset1['texts'][index]:
                                dataset1['labels'][index][lab]=1
                                #print(r,dataset1['labels'][index])  
        with open('annotation/wordnetaffect/new_wnaffectlemmas.txt','w',encoding='utf-8') as filew:
            for ls,ts in zip(dataset1['labels'],dataset1['texts']):
                s=','.join([l for l,v in ls.items()  if v==1  ])
                filew.write(s+'#'+'  '+ts+'\n')

        dataset['labels']+=dataset1['labels']
        dataset['texts']+=dataset1['texts']
    file_wnaffect='annotation/wordnetaffect/wn-affect-lemmasBillal.labeled'
    '''
    result=list()
    dataset={'labels':list(),'texts':list()}
    '''
    
    
    with open(file_wnaffect,'r',encoding='utf-8') as file:
        listelabel=['', 'trust', 'sadness', 'surprise', 'anticipation', 'joy', 'fear', 'disgust', 'anger']
        for i, row in enumerate(file):
            row=row.replace('\t'," ")
            rows=row.strip().split('_')
            
            labs=rows[0].strip().split('#')
            for b in labs:
                if b not in listelabel:
                    print(b,'++++++++++++++++++++++')
            l=[1 if e in labs else 0  for e in liste]
            
            d=dict([(k,v) for k,v in zip(liste,l)])
            
            r=' '.join(rows[1:])
            #print(r,d)
            r=r.replace('_',' ')
            result.append((d,r))
            dataset['labels'].append(d)
            dataset['texts'].append( r)
            print(rows)
            
            
    return dataset


            


result=readFromDictionary(file_dict)
print(len(result['labels']))
result1=readFromCorpus(file_name)
dic={key:result[key]+result1[key]  for key in result1.keys()}

pickle.dump( dic, open( "datasetplutchik.pickle", "wb" ) )