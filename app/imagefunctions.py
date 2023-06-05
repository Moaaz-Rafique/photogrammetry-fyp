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
            pcd = pcds[point_id]

            _points = np.asarray(pcd.points)
            colors = np.asarray(pcd.colors)

            # Calculate the grayscale intensity of each color (assuming RGB colors)
            intensities = np.mean(colors, axis=1)

            # Filter out points with black color (intensity close to 0)
            black_filter = intensities > 0.1  # Adjust the threshold as needed

            # Apply the color filter to the point cloud
            filtered_points = _points[black_filter]
            filtered_colors = colors[black_filter]

            # Create a new point cloud with the filtered points and colors
            filtered_pcd = o3d.geometry.PointCloud()
            filtered_pcd.points = o3d.utility.Vector3dVector(filtered_points)
            filtered_pcd.colors = o3d.utility.Vector3dVector(filtered_colors)
            # Visualize the filtered point cloud
            uni_down_pcd = filtered_pcd.voxel_down_sample(.001
                                                          ).uniform_down_sample(every_k_points=15)
            # print("Statistical outlier removal")
            cl2, ind2 = uni_down_pcd.remove_radius_outlier(nb_points=16, radius=0.5)
            cl, ind = cl2.remove_statistical_outlier(nb_neighbors=16,
                                                     std_ratio=2.0)

            points = np.concatenate((points, cl.points))
            pcd_combined.points = o3d.utility.Vector3dVector(points)
            o3d.io.write_point_cloud(f"{cwd}/output_ply/point{point_id}_filtered.ply", cl)
            print(f'filtered points{point_id}')

            self._scene.scene.add_geometry(f"__model_{point_id}__", cl,
                                           self.settings.material)

        pcd_combined_down = pcd_combined.voxel_down_sample(voxel_size=0.01)
        s_points = np.asarray(pcd_combined.points)

        # Scale the z-axis coordinates
        scale_factor = 10  # Adjust the scale factor as needed
        scaled_points = np.copy(s_points)
        scaled_points[:, 2] *= scale_factor

        # Create a new point cloud with the scaled points
        scaled_pcd = o3d.geometry.PointCloud()
        scaled_pcd.points = o3d.utility.Vector3dVector(scaled_points)

        self._scene.scene.add_geometry(f"__model_combined__", scaled_pcd,
                                       self.settings.material)
        try:
            print(pcd_combined)
            print(f"{cwd}/output_ply/points_combined.ply")
            o3d.io.write_point_cloud(f"{cwd}/output_ply/points_combined.ply", pcd_combined)
        except Exception as e:
            print(e)
        o3d.io.write_point_cloud(f"{cwd}/output_ply/points_combined_down.ply", scaled_points)
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
