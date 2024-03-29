#!/usr/env python3
import os
import os.path as op
import sys
from pathlib import Path

import flywheel
from PyQt5 import QtGui, QtWidgets, uic

from management.analysis_management import AnalysisManagement
from management.app_management import AppManagement
from management.tree_management import TreeManagement


class AppLauncher(QtWidgets.QMainWindow):
    "Main window for the application."

    def __init__(self):
        """
        Initialize application.
        """
        super(AppLauncher, self).__init__()
        self.CacheDir = Path(os.path.expanduser("~") + "/flywheelIO/")

        # TODO: allow them to change what they are logged into
        self.fw_client = flywheel.Client()

        self.source_dir = Path(op.dirname(os.path.realpath(__file__)))

        Form, _ = uic.loadUiType(self.source_dir / "resources/app_launcher.ui")
        self.ui = Form()
        self.ui.setupUi(self)

        # Initialize related component subsets
        self.tree_management = TreeManagement(self)
        self.app_management = AppManagement(self)
        self.analysis_management = AnalysisManagement(self)


if __name__ == "__main__":
    source_dir = Path(os.path.dirname(os.path.realpath(__file__)))
    app = QtWidgets.QApplication([])
    app.setWindowIcon(QtGui.QIcon(str(source_dir / "resources/flywheel.png")))
    application = AppLauncher()
    application.show()
    sys.exit(app.exec())
