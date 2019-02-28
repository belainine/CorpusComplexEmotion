# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 21:26:32 2019

@author: belainine
"""

from nltk.corpus import wordnet
from nltk.corpus import wordnet as wn
import nltk
from nltk.tokenize import MWETokenizer,word_tokenize,TweetTokenizer
import json
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('brown')
nltk.download('universal_tagset')
wn.synsets('dog') # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
'''
wn.synsets('ashamed', pos=wn.VERB)

wn.synsets('love', pos=wn.VERB)[2].examples()

wn.synsets('love', pos=wn.VERB)[0].hypernyms()

wn.synsets('love', pos=wn.VERB)[0].hyponyms()

wn.synsets('love', pos=wn.VERB)[0].member_holonyms()

wn.synset('good.a.01').lemmas()[0].antonyms()


synonyms = []= []
antonyms = []= []

for syn in wordnet.synsets("love"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

print(set(synonyms))
print(set(antonyms))
'''
tokenizer = MWETokenizer([("i'am", "d'oeuvre")], separator='_')
str='In a little or a little bit or a lot in spite of'.replace('â€™',"'").replace('``'," ")
tokenizer.tokenize(str.split())
#print(tokenizer)
with open('vocabulary.json', encoding='utf-8') as data_file:
    data = json.loads(data_file.read())
    
def getNewSentenses(string):
    tokenizer = TweetTokenizer()
    text = tokenizer.tokenize ( string)
    #print(text)
    
    listofresult=set()
    listofresult.add(string)
    words_pos=nltk.pos_tag (text,tagset='universal')
    
    for i in range(len(words_pos)):
        w,p=words_pos[i]
        pos=wn.NOUN
        if p[0]=='V' or p=='CONJ':
            pos=wn.VERB
        elif p=='ADJ':
            pos=wn.ADJ
        elif p=='ADV':
            pos=wn.ADV
        elif p[0]=='N':
            pos=wn.NOUN
        else:
            pos=None
        Synsets=set()
        setNeg={}
        if(w[-3:] =='n\'t'):
            if w!='can':
                Synsets={w,w[:-3]+' not'}
            else :
                Synsets={w,w[:-2]+' not'}
            setNeg=Synsets
        listsynsets=wn.synsets(w, pos=pos)
        
        if len(listsynsets) > 0  and (pos!=wn.NOUN and  pos!=None) :
            
            Synset1=listsynsets[0]
            
            Synsets=Synsets|{lemma   for lemma in Synset1.lemma_names()}
            
        elif pos!=None:
            k=0
            for Synset1 in wn.synsets(w, pos=pos):
                
                if k> 3 :
                    Synsets=Synsets|{lemma   for lemma in Synset1.lemma_names()}  
                k+=1
                
        else:

            for Synset1 in wn.synsets(w):
              Synsets=Synsets|{lemma   for lemma in Synset1.lemma_names()} 
        
        for  term in Synsets:

            if  term in data.keys() or term in setNeg:
                result=words_pos[0:i]+[(term.replace('_',' '),p)]+words_pos[i+1:]
                #print(term,'####',' '.join(wr for wr,ps in result))
                listofresult.add(' '.join(wr for wr,ps in result))
                
    print(len(listofresult))
    return listofresult
getNewSentenses("your doesn't love is a lot" )

for Synset1 in wn.synsets('optimistic', pos=wn.ADJ)[0].hyponyms():
            
            
            Synsets={i   for i in Synset1.lemma_names()}
            print(Synsets)
file_wnaffect='annotation/wordnetaffect/wnaffectlemmas.txt'
'''
'''
file_wn_text='annotation/wordnetaffect/wnaffectlemmasexample_vrb.txt'
def wordnetExampls(file_wn_text,pos=wn.VERB):
    dataset={'labels':list(),'texts':list()}
    liste=['', 'trust', 'sadness', 'surprise', 'anticipation', 'joy', 'fear', 'disgust', 'anger']

    with open(file_wn_text,'w',encoding='utf-8') as filew:
        with open('annotation/wordnetaffect/new_wnaffectlemmas.txt','r',encoding='utf-8') as file:
            
            for i, row in enumerate(file):
                row=row.replace('\t'," ")
                rows=row.strip().split('#')
                
                lab=rows[0].split(',')
                l=[1 if e in lab else 0  for e in liste]
                
                d=dict([(k,v) for k,v in zip(liste,l)])
                
                for r in rows[1:]:
                    r=r.strip().replace('_',' ')
                    if r in data.keys() or ' ' in r:
                        for synset in wn.synsets(r, pos=pos):
                            for example in synset.examples():
                                if example not in dataset['texts']:
                                    print(lab,example,'##',r)
                                    filew.write(','.join(lab)+'## '+example+'   ##'+r+'\n')
                                    dataset['labels'].append(d)   
                                    dataset['texts'].append(example)
                                else:
                                     index=dataset['texts'].index(example)   
                                     for k,v in d.items():
                                         dataset['labels'][index][k]=1 if v==1 else dataset['labels'][index][k]

    return dataset
def wordnetAllExampls():
    dataset={'labels':list(),'texts':list()}
    dataset1=wordnetExampls('annotation/wordnetaffect/wnaffectlemmasexample_vrb.txt',pos=wn.VERB)
    dataset2=wordnetExampls('annotation/wordnetaffect/wnaffectlemmasexample_adj.txt',pos=wn.ADJ)
    dataset3=wordnetExampls('annotation/wordnetaffect/wnaffectlemmasexample_non.txt',pos=wn.NOUN)
    dataset4=wordnetExampls('annotation/wordnetaffect/wnaffectlemmasexample_adv.txt',pos=wn.ADV)

    dataset['labels']+=dataset1['labels']+dataset2['labels']+dataset3['labels']+dataset4['labels']
    dataset['texts']+=dataset1['texts']+dataset2['texts']+dataset3['texts']+dataset4['texts']
    return dataset
#print(wordnetAllExampls())