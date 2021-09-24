# InteriorStyleHunter
AI technology to infer a favorite interior style based on any colorful pictures

Contributor: Stonary-hzq, liukarlie

# Image Process
## Interior style image dataset
  1. Find interior images from Airbnb: USfilter.csv, London filter.csv
  2. Download and save parts of them in google drive
  3. Labeled around 2000 images as training dataset
## Painting image dataset
  1. download paintings from Painter By Number dataset in the Kaggle competition
  2. Labeled around 200 paintings as test dataset

# Model train and verify process
  1. literature review about pictures classifications (shown in reference)
  2. Chose efficient net, SVM, CNN to train and verify
  3. Extract common features in paintings and interior styles eg: hsv color
  4. SVM perform best, so further improve SVM

# Make user interface
  1. Download the zip file, final work, and unzip it.
  2. Open UserInterphase.ipynb.
     
     Before running the application, you should ensure that you installed the required package indicated in the third cell in UserInterphase.ipynb. If you don’t have it, please uncomment it.

     If you use Colab, uncomment the code in the first cell, then change the module_dir to your drive location.

     If you are running on Jupyter notebook, then change the module_dir to your file location. 

  3. Then click the “Run All” button, the application will run.

  4. During the application run, the users are required to input the image through image uploading or pasting URL, the input options are on the right hand side. 

  5. Final output will indicate your style and provide a recommended house design image.
