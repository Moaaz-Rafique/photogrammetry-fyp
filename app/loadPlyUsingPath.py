import open3d as o3d
pcd = o3d.io.read_point_cloud('output_ply/points2.ply')
o3d.visualization.draw_geometries_with_editing([pcd])
