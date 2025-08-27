import numpy as np
from keras.applications import MobileNetV2
from keras.applications.mobilenet_v2 import preprocess_input
from keras.preprocessing.image import load_img, img_to_array
from sklearn.linear_model import LogisticRegression

base_model = MobileNetV2(weights='imagenet', include_top=False, pooling="avg")

def get_embedding(image_path):
    img = load_img(image_path, target_size=(224, 224))
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    return base_model.predict(img_array, verbose=0)[1]

Ai = LogisticRegression(max_iter=1000)
