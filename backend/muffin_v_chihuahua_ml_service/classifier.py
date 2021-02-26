from os.path import abspath, dirname, join

import numpy as np
from tensorflow.keras.applications.inception_v3 import InceptionV3
from tensorflow.keras.applications.inception_v3 import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image


def an_object_detection_model():
    return InceptionV3(weights=join(dirname(abspath(__file__)), 'inception_v3_weights_tf_dim_ordering_tf_kernels.h5'))


def predict_class_for(img: bytes, model=an_object_detection_model()):
    x = image.img_to_array(img)  # a (299, 299) image is expected by the model
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    predictions = model.predict(x)
    return decode_predictions(predictions, top=3)[0]
