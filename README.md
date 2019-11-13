# Corpus With Complex Emotion
# Corpus with Complex Emotion using Plutshik theory
We propose a new textual and social corpus, the labeled corpus that uses basic emotions according to Plutchik's theory. This corpus used in the framework of proposed a first study for the representation and interpretation of complex emotional interactions, using deep neural networks.

We propose a new textual and social corpus, the labeled corpus that uses basic emotions according to Plutchik's theory. This corpus was used in the framework of the first study for the representation and interpretation of complex emotional interactions, using deep neural networks.
The corpus is created by a mixture of several corpora, moreover, integrates several examples of WordNet annotated by manual, The examples of WordNet chosen according to their relation with the words of WordNetAffect.

## The corpus contains 

the corpus contains 4 dataset, each contains the example and is parceled by a fraction of plutshk or with its inverse or with the absence of both emotions.
For example: the dataset_anticipation_surprise.pickle dataset and Anticipation queries and its inverse Surprise or with the absense of both.

dataset_anticipation_surprise.pickle	
dataset_fear_anger.pickle	
dataset_joy_sadness.pickle
dataset_trust_disgust.pickle

The mixed corpora are:

### Dataset      Labels 

EmoTxt1        : joy, anger, sadness, love,surprise, fear

PsychExp       : joy, fear, anger, sadness,disgust, shame, guilt

DailyDialog    : no emotion, anger, dis-gust, fear, happiness, sad-ness, surprise

NRC_Emotion_Lexicon && emotion_proposition_store : joy, fear, disgust, anger,sadness,  surprise,  trustand anticipation

WordNetAffect : joy, fear, disgust, anger,sadness,  surprise,  trustand anticipation
