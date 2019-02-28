

import pickle

def getData():
    file_txt = "./AffectiveText/affectivetext_trial.txt" 
    file_labels = "./AffectiveText/affectivetext_trial.emotions.gold" 
    labels=['anger', 'disgust', 'fear', 'joy', 'sadness', 'surprise']
    # Open and read the pickle file 
    dic={'trust': 0, 'sadness': 0, 'surprise': 0, 'love': 0, 'anger': 0, 'disgust': 0, 'guilt': 0, 'joy': 1, 'anticipation': 0, 'shame': 0, 'fear': 0}
    dic={'trust': 0, 'sadness': 0, 'surprise': 0, 'love': 0, 'anger': 0, 'disgust': 0, 'guilt': 0, 'joy': 1, 'anticipation': 0, 'shame': 0, 'fear': 0}
    dataset1={'labels':list(),'texts':list()}
    with open(file_txt, "r") as fd,open(file_labels, "r") as fl:
        for txt,lab in zip(fd.readlines(),fl.readlines()):
        
            dataset1['texts'].append(txt.strip())
            lbs=lab.split()
            temp={'trust': 0,  'love': 0,  'guilt': 0,  'anticipation': 0, 'shame': 0}
            temp2={labels[i]: (1 if int(lbs[i])> 30 else 0)  for i in range(len(labels))}
            for k,v in temp.items():
                temp2[k]=0
            dataset1['labels'].append(temp2)
            #print(temp2,txt.strip())
    return dataset1

#getData()