import open3d as o3d
import time

def custom_animation_callback(vis):
    progress = 0
    total_frames = 100

    while progress <= total_frames:
        print(f"Progress: {progress}/{total_frames}")

        # Update the progress bar (visualization)
        bar_length = 40
        filled_length = int(bar_length * progress / total_frames)
        bar = "[" + "#" * filled_length + "-" * (bar_length - filled_length) + "]"
        print(f"\r{bar} {progress}/{total_frames}", end="")

        # Simulate a time-consuming task
        time.sleep(0.1)

        progress += 1

        # Request a redraw of the Open3D window
        vis.update_geometry()

    print("\nProgress completed.")


if __name__ == "__main__":
    mesh = o3d.geometry.TriangleMesh.create_coordinate_frame(size=1.0)

    # Create an Open3D visualization window
    vis = o3d.visualization.VisualizerWithKeyCallback()
    vis.create_window(width=800, height=600)

    # Add the mesh to the visualization
    vis.add_geometry(mesh)

    # Set the custom animation callback function
    vis.register_animation_callback(custom_animation_callback)

    # Run the visualization
    vis.run()
    vis.destroy_window()