import torch
from PIL import Image
# import requests
import numpy as np
# import matplotlib.pyplot as plt
# from google.colab import files

from os import listdir
import open3d as o3d
import io


def loadImages(path):
    # return array of images

    imagesList = listdir(path)
    loadedImages = []
    for image in imagesList:
        img = Image.open(path + image)
        loadedImages.append(img)

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

selected_images = loadImages(path)
for i in range(len(selected_images[:1])):
  image = o3d.io.read_image(selected_images[i])
  output = estimate_depth(image)
  print(f"Output of image {i} generated")
  Image.fromarray(image.astype('uint8'), 'RGB').save(f'output_color/{i}_color.png')
  Image.fromarray(output.astype('uint8'), 'L').save(f'output_depth/{i}_depth.png')
