import glob
import numpy as np
import open3d as o3d
import open3d.visualization.gui as gui
import open3d.visualization.rendering as rendering
import os
import platform
import sys
import glob
from generateImagesFromModel import generateImages
import app1
from Settings import Settings


def _set_mouse_mode_rotate(self):
    self._scene.set_view_controls(gui.SceneWidget.Controls.ROTATE_CAMERA)

def _set_mouse_mode_fly(self):
    self._scene.set_view_controls(gui.SceneWidget.Controls.FLY)

def _set_mouse_mode_sun(self):
    self._scene.set_view_controls(gui.SceneWidget.Controls.ROTATE_SUN)

def _set_mouse_mode_ibl(self):
    self._scene.set_view_controls(gui.SceneWidget.Controls.ROTATE_IBL)

def _set_mouse_mode_model(self):
    self._scene.set_view_controls(gui.SceneWidget.Controls.ROTATE_MODEL)

