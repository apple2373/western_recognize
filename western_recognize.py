#!/usr/bin/python
# coding: UTF-8

import argparse
#parse arguments
parser = argparse.ArgumentParser()
parser.add_argument('--model', type=str,help='the trained model', default='./western_ResNet_stop142.h5')
parser.add_argument('--out', type=str,help='the output txt file',required=True)
parser.add_argument('--img', type=str,help='The directory that the images are stored',required=True)
parser.add_argument('--gpu', '-g', type=int, default=-1, help='GPU ID (negative value indicates CPU)')
args = parser.parse_args()

import os
from keras.models import Sequential, Model, load_model
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np

print("loading pre-trained models")
model = load_model(args.model)
print("%s is loaded"%args.model)

f = open(args.out,'w') 

image_directory=args.img
image_files = os.listdir(image_directory)
i=0
for path in image_files:
    name, ext = os.path.splitext(path)
    img = image.load_img(image_directory+'/'+path, target_size=(224, 224))
    x = image.img_to_array(img)/255.0
    x = np.expand_dims(x, axis=0)
    features = model.predict(x)
    print i,path,features[0][0]
    if features[0][0] >= 0.5:
        f.write(path+"\t"+str(features[0][0])+"\n")
    i+=1
f.close()