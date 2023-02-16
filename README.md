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



## Installation

We assume that you're using [Python 3.5](https://www.python.org/downloads/) with [pip](https://pip.pypa.io/en/stable/installing/) installed.

First you need to install [pyTorch (version 0.2+)](http://pytorch.org/), currently by:
```bash
conda install pytorch -c pytorch
```
When pyTorch is installed, unzip the file of complexemotions.zip, after that, run the following in the root directory to install the remaining dependencies:

```bash
pip install -e .
```
This will install the following dependencies:
* [scikit-learn](https://github.com/scikit-learn/scikit-learn)
* [text-unidecode](https://github.com/kmike/text-unidecode)
* [emoji](https://github.com/carpedm20/emoji)

Then, run the download script to downloads the pretrained torchMoji weights (~85MB) from [here](https://www.dropbox.com/s/q8lax9ary32c7t9/pytorch_model.bin?dl=0) and put them in the model/ directory:

```bash
python scripts/download_weights.py
```
## Trining
To run trining, 
```bash
python complexemotions\scripts\finetune_dataset_moji.py
```
## Testing
To run the tests, install [nose](http://nose.readthedocs.io/en/latest/). After installing, navigate to the [tests/](tests) directory and run:

```bash
cd tests
nosetests -v
```
By default, this will also run finetuning tests. These tests train the model for one epoch and then check the resulting accuracy, which may take several minutes to finish. If you'd prefer to exclude those, run the following instead:

```bash
cd tests
nosetests -v -a '!slow'
```
 

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
