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

def show_message_dialog(self, title, message):
        dlg = gui.Dialog(title)
        em = self.window.theme.font_size
        dlg_layout = gui.Vert(em, gui.Margins(em, em, em, em))
        dlg_layout.add_child(gui.Label(message))
        ok_button = gui.Button("Ok")
        ok_button.set_on_clicked(self._on_dialog_ok)
        button_layout = gui.Horiz()
        button_layout.add_stretch()
        value = 0.0        
        progress_bar = gui.ProgressBar()
        progress_bar.value = value
        dlg = gui.Dialog('killme')
        button_layout.add_child(progress_bar)
        button_layout.add_stretch()
        button_layout.add_child(ok_button)
        dlg_layout.add_child(button_layout)
        dlg.add_child(dlg_layout)
        self.window.show_dialog(dlg)


def load_images(self, path):
        # try:
        #     show_message_dialog(self, "kilme", "pls")
        # except Exception as e:
        #       print(e)
        generateImages(path)
        print(path)       
    
def export_image(self, path, width, height):

        def on_image(image):
            img = image

            quality = 9  # png
            if path.endswith(".jpg"):
                quality = 100
            o3d.io.write_image(path, img, quality)

        self._scene.scene.scene.render_to_image(on_image)

