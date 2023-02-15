# Corpus With Complex Emotion
## Corpus with Complex Emotion using Plutshik theory
We propose a new textual and social corpus, the labeled corpus that uses basic emotions according to Plutchik's theory. This corpus used in the framework of proposed a first study for the representation and interpretation of complex emotional interactions, using deep neural networks.

We propose a new textual and social corpus, the labeled corpus that uses basic emotions according to Plutchik's theory. This corpus was used in the framework of the first study for the representation and interpretation of complex emotional interactions, using deep neural networks.
The corpus is created by a mixture of several corpora, moreover, integrates several examples of WordNet annotated by manual, The examples of WordNet chosen according to their relation with the words of WordNetAffect.

## The corpus contains 

The corpus contains 4 dataset, each contains the example and is parceled by a fraction of plutshk or with its inverse or with the absence of both emotions.
For example: the dataset_anticipation_surprise.pickle dataset and Anticipation queries and its inverse Surprise or with the absense of both.

dataset_anticipation_surprise.pickle	: The dataset containt [anticipation,_surprise, Nan]

dataset_fear_anger.pickle		: The dataset containt [fear_, anger, Nan]

dataset_joy_sadness.pickle	: The dataset containt [joy, sadness, Nan]

dataset_trust_disgust.pickle	: The dataset containt [trust_, disgust, Nan]

### Dataset      Labels 

EmoTxt1        : joy, anger, sadness, love,surprise, fear

PsychExp       : joy, fear, anger, sadness,disgust, shame, guilt

DailyDialog    : no emotion, anger, dis-gust, fear, happiness, sad-ness, surprise

NRC_Emotion_Lexicon && emotion_proposition_store : joy, fear, disgust, anger,sadness,  surprise,  trustand anticipation

WordNetAffect : joy, fear, disgust, anger,sadness,  surprise,  trustand anticipation

# Read dataset:

To read the datasets you should use:

1- Install WordNet:

2- Execute the script: Python pickleToTxt.py

3- All word and affect of WordNetAffct exist in wnaffectlemmas.txt

## Citation
```
@inproceedings{belainine2020towards,
  title={Towards a multi-dataset for complex emotions learning based on deep neural networks},
  author={Belainine, Billal and Sadat, Fatiha and Boukadoum, Mounir and Lounis, Hakim},
  booktitle={Proceedings of the Second Workshop on Linguistic and Neurocognitive Resources},
  pages={50--58},
  year={2020}
}
```
