# model.py
import tensorflow as tf
import numpy as np
import cv2

def load_model(model_path):
    return tf.saved_model.load(model_path)

def apply_ghibli_style(model, image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (512, 512))
    image = image.astype(np.float32) / 127.5 - 1
    input_image = np.expand_dims(image, axis=0)
    stylized_image = model(input_image)
    stylized_image = (stylized_image.numpy()[0] + 1) * 127.5
    stylized_image = np.clip(stylized_image, 0, 255).astype(np.uint8)
    return cv2.cvtColor(stylized_image, cv2.COLOR_RGB2BGR)
