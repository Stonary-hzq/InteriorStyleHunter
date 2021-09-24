from google.colab import files
import numpy as np 
from matplotlib import pyplot as plt 
from io import BytesIO
import cv2
import pickle
import os
import urllib.request
import random
import pandas as pd
from tensorflow import keras 

style_dict = {0:'romantic', 1:'morden',
              2:'natural', 3:'country', 4:'minimalist'}

#-*-coding:utf-8-*-
from datetime import datetime
hlist = [20, 40, 75, 155, 190, 270, 290, 316, 360]
svlist = [21, 178, 255]

def quantilize(h, s, v):
    '''hsv直方图量化'''
    # value : [21, 144, 23] h, s, v
    h = h * 2
    for i in range(len(hlist)):
        if h <= hlist[i]:
            h = i % 8
            break
    
    for i in range(len(svlist)):
        if s <= svlist[i]:
            s = i
            break
    for i in range(len(svlist)):
        if v <= svlist[i]:
            v = i
            break
    return 9 * h + 3 * s + v

quantilize_ufunc = np.frompyfunc(quantilize, 3, 1) # 自定义ufunc函数，即将quantilize函数转化为ufunc函数，其输入参数为３个，输出参数为１个。


def colors(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    nhsv = quantilize_ufunc(hsv[:,:,0], hsv[:,:,1], hsv[:,:,2]).astype(np.uint8) # 由于frompyfunc函数返回结果为对象，所以需要转换类型
    hist = cv2.calcHist([nhsv], [0], None, [72], [0,71]) # 40x faster than np.histogram
    cv2.normalize(hist, hist)
    hist.flatten()
    hist = hist.reshape(1,hist.shape[0])
    return hist

def styler(image, module_dir):
    _, image = list(image.items())[0]
    image = np.fromstring(image, np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    '''pkl_filename = os.path.join(module_dir,"models/SGD_HS_acc24_test35.pkl")
    with open(pkl_filename, 'rb') as file:
        clf2 = pickle.load(file)'''
    model = keras.models.load_model(module_dir+"models/simple_train44_val417_test50")
    feature = colors(image)
    #result = clf2.predict(feature)
    result = model.predict(feature)
    result = np.argmax(result[0])
    return style_dict[result]

def styler_url(url, module_dir):
    resp = urllib.request.urlopen(url).read()
    image = np.frombuffer(resp, np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    '''pkl_filename = os.path.join(module_dir,"models/SGD_HS_acc24_test35.pkl")
    with open(pkl_filename, 'rb') as file:
        clf2 = pickle.load(file)'''
    
    model = keras.models.load_model(module_dir+"models/simple_train44_val417_test50")
    feature = colors(image)
    #result = clf2.predict(feature)
    result = model.predict(feature)
    result = np.argmax(result[0])
    return style_dict[result]

def random_img(style, module_dir):
    img_dir = module_dir + 'display_img/'
    paths = pd.read_csv(img_dir+style + '.csv', usecols = ['Image'])
    paths = paths['Image'].to_numpy()
    path = random.choice(paths)
    return os.path.join(img_dir, path)