from PIL import Image
import cv2
import numpy as np
from base_selfies.database import get_db_images

def processing_image(dir: str):
    image = Image.open(dir).convert('L')
    image_np = np.array(image, 'uint8')

    return image_np


ids, face_images = get_db_images()
ids = np.array(ids)
face_images = list(map(processing_image, face_images))

""" Training ... """
lbph = cv2.face.LBPHFaceRecognizer_create()
lbph.train(face_images, ids)
lbph.write('classificadorBPH.yml')

