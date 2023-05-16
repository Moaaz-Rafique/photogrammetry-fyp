import glob
import numpy as np
import open3d as o3d
import open3d.visualization.gui as gui
import open3d.visualization.rendering as rendering
import os
import platform
import sys
import glob
from generateImagesFromModel import generateImages
import app1
from Settings import Settings

def load_images(self, path):
        # self._scene.scene.clear_geometry()
        print(path)
        # depth_raw = o3d.io.read_image(path)
        # depth = o3d.geometry.Image(depth_raw)
        # print(depth)
        
        image_list = []       
        generateImages(path)
    
def export_image(self, path, width, height):

        def on_image(image):
            img = image

            quality = 9  # png
            if path.endswith(".jpg"):
                quality = 100
            o3d.io.write_image(path, img, quality)

        self._scene.scene.scene.render_to_image(on_image)

