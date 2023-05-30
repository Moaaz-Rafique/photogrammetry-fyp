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

cwd = os.getcwd()


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
        pcd_combined = o3d.geometry.PointCloud()
        points = pcd_combined.points

        for point_id in range(len(pcds)):
            # pcds[point_id].transform(pose_graph.nodes[point_id].pose)
            # pcd_combined.__add__(pcds[point_id])
            points = np.concatenate((points, pcds[point_id].points))
            pcd_combined.points = o3d.utility.Vector3dVector(points)
            self._scene.scene.add_geometry(f"__model_{point_id}__", pcds[point_id],
                                           self.settings.material)

        pcd_combined_down = pcd_combined.voxel_down_sample(voxel_size=0.01)
        # for i in range(len(pcds)):
        self._scene.scene.add_geometry(f"__model_combined__", pcd_combined_down,
                                       self.settings.material)
        try:
            print(pcd_combined)

            print(f"{cwd}/output_ply/points_combined.ply")
            o3d.io.write_point_cloud(f"{cwd}/output_ply/points_combined.ply", pcd_combined)
        except Exception as e:
            print(e)
        o3d.io.write_point_cloud(f"{cwd}/output_ply/points_combined_down.ply", pcd_combined_down)
        # o3d.io.write_point_cloud(os.getcwd()+f"/output_ply/combinedDownSamplePoints{len(pcds)}.ply", pcd_combined_down)
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
