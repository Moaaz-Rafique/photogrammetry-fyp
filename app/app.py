import glob
import numpy as np
import open3d as o3d
import open3d.visualization.gui as gui
import open3d.visualization.rendering as rendering
import os
import platform
import sys
import glob
from AppWindow import AppWindow

isMacOS = (platform.system() == "Darwin")


def main():
    gui.Application.instance.initialize()
    w = AppWindow(1024, 768)
    if len(sys.argv) > 1:
        path = sys.argv[1]
        if os.path.exists(path):
            w.load(path)
        else:
            w.window.show_message_box("Error",
                                      "Could not open file '" + path + "'")

    # Run the event loop. This will not return until the last window is closed.
    gui.Application.instance.run()
def check_and_create_directories(dir_list):
    for directory in dir_list:
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
                print(f"Directory '{directory}' created.")
            else:
                print(f"Directory '{directory}' already exists.")
        except Exception as e:
            print(e)
# Example usage

if __name__ == "__main__":
    cwd = os.getcwd()
    directories = [
        cwd+'/output_color',
        cwd + '/output_mesh',
        cwd + '/output_ply',
        cwd + '/output_depth',

    ]
    check_and_create_directories(directories)
    main()
