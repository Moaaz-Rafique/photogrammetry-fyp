
import numpy as np
import open3d as o3d

def load_point_clouds(voxel_size=0.0):
    pcds = []
    # for i in range(1):
    pcd = o3d.io.read_point_cloud("multiway_registration.pcd")
    # pcd_down = pcd.voxel_down_sample(voxel_size=voxel_size)
    # pcds.append(pcd_down)
    pcds.append(pcd)
    return pcds

if __name__ == "__main__":

    print("Load a ply point cloud, print it, and render it")
    pcds = load_point_clouds(voxel_size=0.1)
    o3d.visualization.draw_geometries(pcds)