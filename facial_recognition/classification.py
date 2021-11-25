import cv2
from PIL import Image
import numpy as np
from base_selfies.database import get_name_by_id

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('./classificadorBPH.yml')

image_test = './base_selfies/files/image_name.jpg'

image = Image.open(image_test).convert('L')
image_np = np.array(image, 'uint8')

id, per = recognizer.predict(image_np)

name = get_name_by_id(id)
print(per)
print(name)
