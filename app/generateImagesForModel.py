import torch
from PIL import Image, ImageFilter
import numpy as np
from generetePlyFromPath import generatePlyFromIndex
from os import listdir
import open3d as o3d
import io
import os
import time
import cv2


cwd = os.getcwd()


# print(cwd)
def loadImages(path):
    # return array of images
    imagesList = listdir(path)
    loadedImages = []
    for image in imagesList:
        print('loading images', path + '/' + image)
        try:
            img = Image.open(path + '/' + image)
            img = cv2.imread(path + '/' + image)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            loadedImages.append(img)
        except Exception as e:
            print(e)

    return loadedImages

# model_type = "DPT_Large"     # MiDaS v3 - Large     (highest accuracy, slowest inference speed)
# #model_type = "DPT_Hybrid"   # MiDaS v3 - Hybrid    (medium accuracy, medium inference speed)
# #model_type = "MiDaS_small"  # MiDaS v2.1 - Small   (lowest accuracy, highest inference speed)
#
# model = torch.hub.load("intel-isl/MiDaS", model_type)
# gpu_device = torch.device('cpu')
# model.to(gpu_device)
# model.eval()
#
# transform = torch.hub.load('intel-isl/MiDaS', 'transforms').dpt_transform


# def estimate_depth(image):
    # transformed_image = transform(image).to(gpu_device)
    # with torch.no_grad():
    #     prediction = model(transformed_image)
    #
    #     prediction = torch.nn.functional.interpolate(
    #         prediction.unsqueeze(1),
    #         size=image.shape[:2],
    #         mode="bicubic",
    #         align_corners=False,
    #     ).squeeze()
    #
    # output = prediction.cpu().numpy()
    # return output




def generateImages(path):
    print(path)
    # selected_images = loadImages(path)
    # print(f'loaded {len(selected_images)} in the current directory.')
    pcds = []
    for i in range(2):
    #     # time.sleep(1)
        try:
    #         image = np.array(selected_images[i])
    #         output = estimate_depth(image)
    #         # selected_images[i].save()
    #         cv2.imwrite(f'{cwd}/output_color/{i}_color.png', cv2.cvtColor(selected_images[i], cv2.COLOR_RGB2BGR))
    #         cv2.imwrite(f'{cwd}/output_depth/{i}_depth.png',cv2.cvtColor(output, cv2.COLOR_RGB2BGR))
            # out_img = Image.fromarray(output.astype('uint8'), 'L')
            # out_img.save(f'{cwd}/output_depth/{i}_depth.png')
            print(f"Output of image {i} generated")
            pcds.append(generatePlyFromIndex(i, cwd))

        except Exception as e:
            print(e)
        # o3d.visualization.draw_geometries_with_vertex_selection(pcds)
    return pcds


# path = "D:\\fyp\\pdfs\\hammerPics\\maskedImages"
# pcds = generateImages(path)
# o3d.visualization.draw_geometries(pcds)