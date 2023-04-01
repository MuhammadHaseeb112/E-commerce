from keras.models import load_model
# from keras.preprocessing.image import load_img
# from keras.preprocessing.image import img_to_array
from keras_preprocessing.image import img_to_array, load_img
# from tensorflow.keras.utils import img_to_array
import numpy as np

import matplotlib.pyplot as plt


model1 = load_model("home\\static\\ClassificationModel.h5",compile=False)  


from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)

train_directory="home\\static\\train"
training_set = train_datagen.flow_from_directory(train_directory,
                                                 target_size = (200, 200),
                                                 batch_size = 32,
                                                 class_mode = 'categorical')

lab = training_set.class_indices
lab={k:v for v,k in lab.items()}

def output(location):
    img=load_img(location,target_size=(200,200,3))
    img=img_to_array(img)
    img=img/255
    img=np.expand_dims(img,[0])
    answer=model1.predict(img)
    y_class = answer.argmax(axis=-1)
    y = " ".join(str(x) for x in y_class)
    y = int(y)
    res = lab[y]
    print("Clasifications:  ",res)
    return res

# "C:\Users\Admin\Pictures\8.png"

img="C:\\Users\\Admin\\Pictures\\8.png"
pic=load_img(img,target_size=(200,200,3))
plt.imshow(pic)
result_final = output(img)

# plt.imshow(result_final) 