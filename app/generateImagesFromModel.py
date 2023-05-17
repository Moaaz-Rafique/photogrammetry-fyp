import torch
from PIL import Image
# import requests
import numpy as np
# import matplotlib.pyplot as plt
# from google.colab import files

from os import listdir
# import open3d as o3d
import io
import os
import time

cwd = os.getcwd()

# print(cwd)
def loadImages(path):
    # return array of images

    imagesList = listdir(path)
    loadedImages = []
    for image in imagesList:
        print('loading images', path +'/'+ image)
        try:
            img = Image.open(path +'/'+ image)
            loadedImages.append(img)
        except Exception as e:
            print(e)



    return loadedImages




midas_type = "DPT_Large"

model = torch.hub.load("intel-isl/MiDaS", midas_type)
gpu_device = torch.device('cpu')
model.to(gpu_device)
model.eval()

transform = torch.hub.load('intel-isl/MiDaS', 'transforms').dpt_transform

def estimate_depth(image):
    transformed_image = transform(image).to(gpu_device)
    with torch.no_grad():
        prediction = model(transformed_image)
        
        prediction = torch.nn.functional.interpolate(
            prediction.unsqueeze(1),
            size=image.shape[:2],
            mode="bicubic",
            align_corners=False,
        ).squeeze()
    
    output = prediction.cpu().numpy()
    return output

path = "test_images/"
def generateImages(path):
    print(path)
    selected_images = loadImages(path)
    print(f'loaded {len(selected_images)} in the current directory.')
    for i in range(len(selected_images[:1])):
        time.sleep(1)
        try:
            image = np.array(selected_images[i])
            output = estimate_depth(image)
            Image.fromarray(image.astype('uint8'), 'RGB').save(f'{cwd}/output_color/{i}_color.png')
            Image.fromarray(output.astype('uint8'), 'L').save(f'{cwd}./output_depth/{i}_depth.png')
            print(f"Output of image {i} generated")
        except Exception as e:
            print(e)

# generateImages(path)