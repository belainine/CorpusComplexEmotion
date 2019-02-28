

'joy,fear,anger,sadness,disgust,shame,guilt,surprise,trust,anticipation'
dialogues_text = "ijcnlp_dailydialog/dialogues_text.txt" 
dialogues_emotion = "ijcnlp_dailydialog/dialogues_emotion.txt" 
def readdialydialog(dialogues_text,dialogues_emotion):
    dicEmotion={0: 'no', 1: 'anger', 2: 'disgust', 3: 'fear', 4: 'joy', 5: 'sadness', 6: 'surprise',7:'shame',8:'guilt',9:'trust',10:'anticipation'}
    dataset={'labels':list(),'texts':list()}
    with open(dialogues_text,'r',encoding='utf-8') as file:
        with open(dialogues_emotion,'r',encoding='utf-8') as filelabel:
            for label , line in zip(filelabel,file):
                labels=label.strip('\n').strip('\s').split(' ')[:-1]
                #print(label.strip('\n').strip('\s'))
                lines=line.split('__eou__')[:-1]
                for i in range(-len(labels)+1,0):
                    if len(lines[i].split(' '))<6:
                        
                        del(labels[i])
                        del(lines[i])
                        
                        #print(labels,len(lines),len(line.split('__eou__')[:-1]) )             
                #print( labels.split(' ')[:-1],line.split('__eou__')[:-1])
                labelstemp= [dict([(v,0) if v!=dicEmotion[int(i)] else (v,1) for k,v in dicEmotion.items() ]) for i in labels]
                [  d.pop('no') for d in labelstemp]

                dataset['labels']+=labelstemp
                dataset['texts']+=line.split('__eou__')[:-1]
                #print( [(l,text) for l,text in zip(labelstemp,line.split('__eou__')[:-1])])
    return dataset


dataset=  readdialydialog(dialogues_text,dialogues_emotion)
