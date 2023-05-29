import glob
import numpy as np
import open3d as o3d
import open3d.visualization.gui as gui
import open3d.visualization.rendering as rendering
import os
import platform
import sys
import glob
from generateImagesForModel import generateImages


def show_message_dialog(self, title, message):
    # A Dialog is just a widget, so you make its child a layout just like
    # a Window.
    dlg = gui.Dialog(title)

    # Add the message text
    em = self.window.theme.font_size
    dlg_layout = gui.Vert(em, gui.Margins(em, em, em, em))
    dlg_layout.add_child(gui.Label(message))

    # Add the Ok button. We need to define a callback function to handle
    # the click.
    ok_button = gui.Button("Ok")
    ok_button.set_on_clicked(self._on_dialog_ok)

    # We want the Ok button to be an the right side, so we need to add
    # a stretch item to the layout, otherwise the button will be the size
    # of the entire row. A stretch item takes up as much space as it can,
    # which forces the button to be its minimum size.
    button_layout = gui.Horiz()
    button_layout.add_stretch()
    button_layout.add_child(ok_button)

    # Add the button layout,
    dlg_layout.add_child(button_layout)
    # ... then add the layout as the child of the Dialog
    dlg.add_child(dlg_layout)
    # ... and now we can show the dialog
    self.window.show_dialog(dlg)


def load_images(self, path):
    print(path)
    pcds = generateImages(path)
    try:
        self._scene.scene.clear_geometry()
        for i in range(len(pcds)):
            self._scene.scene.add_geometry(f"__model{i}__", pcds[i],
                                       self.settings.material)
    except Exception as e:
        print(e)


def export_image(self, path, width, height):
    def on_image(image):
        img = image

        quality = 9  # png
        if path.endswith(".jpg"):
            quality = 100
        o3d.io.write_image(path, img, quality)

    self._scene.scene.scene.render_to_image(on_image)
