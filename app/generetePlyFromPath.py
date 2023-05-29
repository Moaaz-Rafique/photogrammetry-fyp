import open3d as o3d
import numpy as np
# pcds=[]
def generatePlyFromIndex(i_no=0, cwd=''):
    # ,72, 5):
    try:
        color_raw = o3d.io.read_image(f'{cwd}/output_color/{i_no}_color.png')
        depth_raw = o3d.io.read_image(f'{cwd}/output_depth/{i_no}_depth.png')

        rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(
            color_raw, depth_raw)
        pcd = o3d.geometry.PointCloud.create_from_rgbd_image(
            rgbd_image,
            o3d.camera.PinholeCameraIntrinsic(
                o3d.camera.PinholeCameraIntrinsicParameters.PrimeSenseDefault))
        # Flip it, otherwise the pointcloud will be upside down
        pcd.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
        # o3d.visualization.draw_geometries([pcd])
        pcd.scale(10000.0, np.array([[.0],
                                 [.0],
                                 [.0]]))

        # pcd = pcd.scale(1000, np.array([[.0],
        #                          [.0],
        #                          [.0]]))
        o3d.io.write_point_cloud(f"{cwd}/output_ply/points{i_no}.ply", pcd)
        print(f'{i_no} points were generated')
        # pcds.append(pcd)
        return pcd
    except Exception as e:
        print(e)
    # print(np.array(vertices)[:10], np.array(colors)[:10])
# o3d.visualization.draw_geometries(pcds)
