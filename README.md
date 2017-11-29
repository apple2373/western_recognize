Western Blot Recognizer
================
This is the developed classifier in a paper ["A case study of viziometrics: What's the role of western blots in Alzheimer's Disease literature?"](link). 

If you find it useful, please consider to cite: 
```
@inproceedings{western-recognize,
  title={{A Data Driven Approach for Compound Figure Separation Using Convolutional Neural Networks}},
  author={Satoshi Tsutsui etal},
  booktitle={{iConference}},
  year={2018}
}
```

Tested environment
------------------
-  Keras version 2.1.1
-  Tensorflow version 1.4.0

Download the pretrained model
------------------
Let's donwload the pretrained model. I uploaded onto multiple places.  
Google Drive: [https://drive.google.com/open?id=15TPl88ewLutI98Vak1qutcuIsyn47Uch](https://drive.google.com/open?id=15TPl88ewLutI98Vak1qutcuIsyn47Uch)  
Dropbox: [https://www.dropbox.com/s/bnayluu65hxz8tn/western_ResNet_stop142.h5?dl=0](https://www.dropbox.com/s/bnayluu65hxz8tn/western_ResNet_stop142.h5?dl=0)

How to use
-----------------
See help
```
python western_recognize.py --help #see help

usage: western_recognize.py [-h] [--model MODEL] --out OUT --img IMG
                            [--gpu GPU]

optional arguments:
  -h, --help         show this help message and exit
  --model MODEL      the trained model
  --out OUT          the output txt file
  --img IMG          The directory that the images are stored
  --gpu GPU, -g GPU  GPU ID (negative value indicates CPU)
```
An example is 
```
python western_recognize.py --img imgs/ --out western-blot-images.txt
```
then  `western-blot-images.txt` will have the file names of western blot images. 


### samlple image source
The sample images are cropped from [PMC4076561](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4076561/figure/fig5/). 
