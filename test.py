import open3d as o3d
import numpy as np

for i_no in range(1):#,72, 5):
  vertices = []
  color_raw = o3d.io.read_image(f'app/output_color/{i_no}_color.png')
  depth_raw = o3d.io.read_image(f'app/output_depth/{i_no}_depth.png')
  rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(
      color_raw, depth_raw)
  pcd = o3d.geometry.PointCloud.create_from_rgbd_image(
    rgbd_image,
    o3d.camera.PinholeCameraIntrinsic(o3d.camera.PinholeCameraIntrinsicParameters.PrimeSenseDefault),
    # depth_scale = 5
    )
# pcd.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])



pcd = o3d.io.read_point_cloud("points_test_1.ply")
# pcd = pcd.scale(1000, np.array([[.0],
#                          [.0],
#                          [.0]]))
# print(pcd)
# print(np.asarray(pcd.points))
# o3d.visualization.draw_geometries([pcd],
#                                   zoom=1,
#                                   front=[0.4257, -0.2125, -0.8795],
#                                   lookat=[0, 0, 0],
#                                   up=[-0.0694, -0.9768, 0.2024])
# mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_alpha_shape(dpcd, .03)
# mesh.compute_vertex_normals()
# # mesh.compute_uvatlas()
# o3d.visualization.draw_geometries([mesh], mesh_show_back_face=True)
# # o3d.io.write_point_cloud(f"points_test_1.ply", pcd)
# o3d.io.write_triangle_mesh('mesh2.gltf', mesh)
pcd.estimate_normals()

print('run Poisson surface reconstruction')
with o3d.utility.VerbosityContextManager(
        o3d.utility.VerbosityLevel.Debug) as cm:
    mesh, densities = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(
        pcd, depth=9)
print(mesh)
o3d.visualization.draw_geometries([mesh, pcd], mesh_show_back_face=False)

# keypoints = o3d.geometry.keypoint.compute_iss_keypoints(pcd)


# from PIL import Image, ImageFilter
#
# im = Image.open('img.png')
#
# im1 = im.filter(ImageFilter.UnsharpMask)
# im1 = im1.filter(ImageFilter.UnsharpMask)
# im1 = im1.filter(ImageFilter.UnsharpMask)
# im1 = im1.filter(ImageFilter.UnsharpMask)
# im1 = im1.filter(ImageFilter.UnsharpMask)
# im1 = im1.filter(ImageFilter.UnsharpMask)
# im1.show()
# im1.save('blur.png')
# im

