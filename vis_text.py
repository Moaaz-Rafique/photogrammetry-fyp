import open3d as o3d
import numpy as np
import pymesh
import copy


w, h = 10, 10
corners = np.array([
    [0, 0, 0],
    [w, 0, 0],
    [w, h, 0],
])

triangles = np.array([[2, 1, 0]])
mesh_o3d = o3d.t.io.read_triangle_mesh('mesh.obj')
mesh_o3d.compute_uvatlas()
o3d
# faces = mesh_o3d.triangles
# mesh_pymesh = pymesh.form_mesh(mesh_o3d.vertices, mesh_o3d.triangles)
#
# # Perform UV unwrapping using PyMesh
# mesh_pymesh.add_attribute("vertex_uv")
# pymesh.unwrap_uv(mesh_pymesh)
#
# # Access the UV coordinates
# uvs = mesh_pymesh.get_attribute("vertex_uv")
#
# mesh_o3d.triangle_uvs = o3d.utility.Vector2dVector(uvs)
# # #
# mesh_o3d.compute_vertex_normals()
# # #
mat = o3d.visualization.rendering.MaterialRecord()
# # mesh.compute_triangle_uvs()
#
#
mat.albedo_img = o3d.io.read_image("checkers.png")

o3d.visualization.draw({'name': 'test_mesh', 'geometry': mesh_o3d, 'material': mat})
o3d.visualization.draw_geometries([mesh_o3d])
