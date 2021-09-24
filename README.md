# InteriorStyleHunter
AI technology to infer a favorite interior style based on any colorful pictures

Contributor: Stonary-hzq, liukarlie

# Image Process
## interior style image dataset
  1. Find interior images from Airbnb: USfilter.csv, London filter.csv
  2. Download and save parts of them in google drive
  3. Labeled around 2000 images as training dataset
## painting image dataset
  1. download paintings from Painter By Number dataset in the Kaggle competition
  2. Labeled around 200 paintings as test dataset

# model train and verify process
  1. literature review about pictures classifications (shown in reference)
  2. Chose efficient net, SVM, CNN to train and verify
  3. Extract common features in paintings and interior styles eg: hsv color
  4. SVM perform best, so further improve SVM

# make user interface
