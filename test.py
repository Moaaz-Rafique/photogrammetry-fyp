import open3d as o3d
import numpy as np
for i_no in range(1):#,72, 5):
  vertices = []
  color_raw = o3d.io.read_image(f'output_color/{i_no}_color.png')
  depth_raw = o3d.io.read_image(f'output_depth/{i_no}_depth.png')
  rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(
      color_raw, depth_raw)
  pcd = o3d.geometry.PointCloud.create_from_rgbd_image(
    rgbd_image,
    o3d.camera.PinholeCameraIntrinsic(o3d.camera.PinholeCameraIntrinsicParameters.PrimeSenseDefault),
    # depth_scale = 5
    )
#   pcd.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])

  print(pcd.has_points())
  print(np.asarray(pcd.points))
  o3d.visualization.draw_geometries([pcd])

#   o3d.io.write_point_cloud(f"points{i_no}.pcd", pcd)
  
  