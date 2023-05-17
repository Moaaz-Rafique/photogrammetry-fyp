import open3d.visualization.gui as gui


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

