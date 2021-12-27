# -*- coding: utf-8 -*-
import os

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class AnnotatorUi(object):
    def setupUi(self, AnnotaorUi):
        if not AnnotaorUi.objectName():
            AnnotaorUi.setObjectName("AnnotaorUi")
        AnnotaorUi.resize(1553, 881)
        self.verticalLayout = QVBoxLayout(AnnotaorUi)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(3, 6, 3, 6)
        self.frame_header = QFrame(AnnotaorUi)
        self.frame_header.setObjectName("frame_header")
        self.frame_header.setMaximumSize(QSize(16777215, 30))
        self.frame_header.setFrameShape(QFrame.NoFrame)
        self.frame_header.setFrameShadow(QFrame.Plain)
        self.horizontalLayout = QHBoxLayout(self.frame_header)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(6, 0, 6, 0)
        self.btn_open = QPushButton(self.frame_header)
        self.btn_open.setObjectName("btn_open")
        self.btn_open.setMaximumSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.btn_open)

        self.btn_save = QPushButton(self.frame_header)
        self.btn_save.setObjectName("btn_save")
        self.btn_save.setMaximumSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.btn_save)

        self.frame_dummy1 = QFrame(self.frame_header)
        self.frame_dummy1.setObjectName("frame_dummy1")
        self.frame_dummy1.setMinimumSize(QSize(250, 0))
        self.frame_dummy1.setMaximumSize(QSize(16777215, 16777215))
        self.frame_dummy1.setFrameShape(QFrame.NoFrame)
        self.frame_dummy1.setFrameShadow(QFrame.Plain)

        self.horizontalLayout.addWidget(self.frame_dummy1)

        self.btn_undo = QPushButton(self.frame_header)
        self.btn_undo.setObjectName("btn_undo")
        self.btn_undo.setMaximumSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.btn_undo)

        self.btn_redo = QPushButton(self.frame_header)
        self.btn_redo.setObjectName("btn_redo")
        self.btn_redo.setMaximumSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.btn_redo)

        self.frame_6 = QFrame(self.frame_header)
        self.frame_6.setObjectName("frame_6")
        self.frame_6.setMinimumSize(QSize(15, 0))
        self.frame_6.setMaximumSize(QSize(15, 16777215))
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Plain)

        self.horizontalLayout.addWidget(self.frame_6)

        self.btn_erase = QPushButton(self.frame_header)
        self.btn_erase.setObjectName("btn_erase")
        self.btn_erase.setMaximumSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.btn_erase)

        self.frame_dummy2 = QFrame(self.frame_header)
        self.frame_dummy2.setObjectName("frame_dummy2")
        self.frame_dummy2.setMinimumSize(QSize(60, 0))
        self.frame_dummy2.setMaximumSize(QSize(60, 16777215))
        self.frame_dummy2.setFrameShape(QFrame.NoFrame)
        self.frame_dummy2.setFrameShadow(QFrame.Plain)

        self.horizontalLayout.addWidget(self.frame_dummy2)

        self.btn_text = QPushButton(self.frame_header)
        self.btn_text.setObjectName("btn_text")
        self.btn_text.setMaximumSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.btn_text)

        self.combo_font_size = QComboBox(self.frame_header)
        self.combo_font_size.setMinimumSize(50, 24)
        self.combo_font_size.setMaximumSize(50, 24)
        self.horizontalLayout.addWidget(self.combo_font_size)

        # self.combo_font = QComboBox(self.frame_header)

        # self.horizontalLayout.addWidget(self.combo_font)

        self.combo_font = QFontComboBox(self.frame_header)
        self.combo_font.setMinimumSize(120, 24)
        self.combo_font.setMaximumSize(180, 24)
        self.horizontalLayout.addWidget(self.combo_font)

        self.btn_line = QPushButton(self.frame_header)
        self.btn_line.setObjectName("btn_line")
        self.btn_line.setMaximumSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.btn_line)

        self.btn_rectangle = QPushButton(self.frame_header)
        self.btn_rectangle.setObjectName("btn_rectangle")
        self.btn_rectangle.setMaximumSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.btn_rectangle)

        self.btn_ellipse = QPushButton(self.frame_header)
        self.btn_ellipse.setObjectName("btn_ellipse")
        self.btn_ellipse.setMaximumSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.btn_ellipse)

        self.btn_brush = QPushButton(self.frame_header)
        self.btn_brush.setObjectName("btn_brush")
        self.btn_brush.setMaximumSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.btn_brush)

        self.frame_dummy3 = QFrame(self.frame_header)
        self.frame_dummy3.setObjectName("frame_dummy3")
        self.frame_dummy3.setMinimumSize(QSize(20, 0))
        self.frame_dummy3.setMaximumSize(QSize(20, 16777215))
        self.frame_dummy3.setFrameShape(QFrame.NoFrame)
        self.frame_dummy3.setFrameShadow(QFrame.Plain)

        self.horizontalLayout.addWidget(self.frame_dummy3)

        self.slider_brush_size = QSlider(self.frame_header)
        self.slider_brush_size.setObjectName("slider_brush_size")
        self.slider_brush_size.setMinimumSize(QSize(70, 0))
        self.slider_brush_size.setMaximumSize(QSize(100, 16777215))
        self.slider_brush_size.setFocusPolicy(Qt.NoFocus)
        self.slider_brush_size.setMaximum(20)
        self.slider_brush_size.setValue(5)
        self.slider_brush_size.setOrientation(Qt.Horizontal)

        self.horizontalLayout.addWidget(self.slider_brush_size)

        self.frame_dummy6 = QFrame(self.frame_header)
        self.frame_dummy6.setObjectName("frame_dummy3")
        self.frame_dummy6.setMinimumSize(QSize(20, 0))
        self.frame_dummy6.setMaximumSize(QSize(20, 16777215))
        self.frame_dummy6.setFrameShape(QFrame.NoFrame)
        self.frame_dummy6.setFrameShadow(QFrame.Plain)

        self.horizontalLayout.addWidget(self.frame_dummy6)

        self.btn_color_palette = QPushButton(self.frame_header)
        self.btn_color_palette.setObjectName("btn_color_palette")
        self.btn_color_palette.setMaximumSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.btn_color_palette)

        self.label_palette = QPushButton(self.frame_header)
        self.label_palette.setObjectName("label_palette")
        self.label_palette.setMinimumSize(QSize(30, 30))
        self.label_palette.setMaximumSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.label_palette)

        self.frame_dummy4 = QFrame(self.frame_header)
        self.frame_dummy4.setObjectName("frame_dummy4")
        self.frame_dummy4.setMinimumSize(QSize(15, 0))
        self.frame_dummy4.setMaximumSize(QSize(15, 16777215))
        self.frame_dummy4.setFrameShape(QFrame.NoFrame)
        self.frame_dummy4.setFrameShadow(QFrame.Plain)

        self.horizontalLayout.addWidget(self.frame_dummy4)

        self.btn_color_red = QPushButton(self.frame_header)
        self.btn_color_red.setObjectName("btn_color_red")
        self.btn_color_red.setMaximumSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_color_red)

        self.btn_color_green = QPushButton(self.frame_header)
        self.btn_color_green.setObjectName("btn_color_green")
        self.btn_color_green.setMaximumSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_color_green)

        self.btn_color_blue = QPushButton(self.frame_header)
        self.btn_color_blue.setObjectName("btn_color_blue")
        self.btn_color_blue.setMaximumSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_color_blue)

        self.btn_color_white = QPushButton(self.frame_header)
        self.btn_color_white.setObjectName("btn_color_white")
        self.btn_color_white.setMaximumSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_color_white)

        self.btn_color_black = QPushButton(self.frame_header)
        self.btn_color_black.setObjectName("btn_color_black")
        self.btn_color_black.setMaximumSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_color_black)

        self.frame_dummy5 = QFrame(self.frame_header)
        self.frame_dummy5.setObjectName("frame_dummy5")
        self.frame_dummy5.setMinimumSize(QSize(250, 0))
        self.frame_dummy5.setFrameShape(QFrame.NoFrame)
        self.frame_dummy5.setFrameShadow(QFrame.Plain)

        self.horizontalLayout.addWidget(self.frame_dummy5)


        self.verticalLayout.addWidget(self.frame_header)

        self.frame_body = QFrame(AnnotaorUi)
        self.frame_body.setObjectName("frame_body")
        self.frame_body.setFrameShape(QFrame.NoFrame)
        self.frame_body.setFrameShadow(QFrame.Plain)

        self.verticalLayout.addWidget(self.frame_body)

        self.setWindowTitle("Annotator")
        self.btn_save.setFocusPolicy(Qt.NoFocus)
        self.btn_open.setFocusPolicy(Qt.NoFocus)
        self.btn_erase.setFocusPolicy(Qt.NoFocus)
        self.btn_line.setFocusPolicy(Qt.NoFocus)
        self.btn_ellipse.setFocusPolicy(Qt.NoFocus)
        self.btn_rectangle.setFocusPolicy(Qt.NoFocus)
        self.btn_color_palette.setFocusPolicy(Qt.NoFocus)
        self.label_palette.setFocusPolicy(Qt.NoFocus)
        self.btn_text.setFocusPolicy(Qt.NoFocus)
        self.btn_redo.setFocusPolicy(Qt.NoFocus)
        self.btn_undo.setFocusPolicy(Qt.NoFocus)
        self.btn_brush.setFocusPolicy(Qt.NoFocus)
        self.btn_color_red.setFocusPolicy(Qt.NoFocus)
        self.btn_color_green.setFocusPolicy(Qt.NoFocus)
        self.btn_color_black.setFocusPolicy(Qt.NoFocus)
        self.btn_color_blue.setFocusPolicy(Qt.NoFocus)
        self.btn_color_white.setFocusPolicy(Qt.NoFocus)

        self.setStyleSheet(
            "QPushButton{border: None; margin:0px; padding:0px; background-color: None; }"
            "QPushButton:pressed{background-color: #212121; "
            "border-radius: 4px;}"
            "QPushButton:checked{background-color: #212121; "
            "border-radius: 4px;}"
        )

        src_path = os.path.dirname(os.path.dirname(__file__))
        self.btn_open.setIcon(QIcon('{}/icons/open_lite.png'.format(src_path)))
        self.btn_save.setIcon(QIcon('{}/icons/save_lite.png'.format(src_path)))
        self.btn_undo.setIcon(QIcon('{}/icons/undo_lite.png'.format(src_path)))
        self.btn_redo.setIcon(QIcon('{}/icons/redo_lite.png'.format(src_path)))
        self.btn_erase.setIcon(QIcon('{}/icons/delete_lite.png'.format(src_path)))
        self.btn_text.setIcon(QIcon('{}/icons/text_lite.png'.format(src_path)))
        self.btn_rectangle.setIcon(QIcon('{}/icons/rectangle_lite.png'.format(src_path)))
        self.btn_line.setIcon(QIcon('{}/icons/line_lite.png'.format(src_path)))
        self.btn_ellipse.setIcon(QIcon('{}/icons/ellipse_lite.png'.format(src_path)))
        self.btn_brush.setIcon(QIcon('{}/icons/brush_lite.png'.format(src_path)))
        self.btn_color_palette.setIcon(QIcon('{}/icons/color_palette.png'.format(src_path)))
        self.btn_color_white.setStyleSheet('QPushButton{background-color: #FFFFFF; border-radius: 5px;}')
        self.btn_color_black.setStyleSheet('QPushButton{background-color: #000000; border-radius: 5px;}')
        self.btn_color_red.setStyleSheet('QPushButton{background-color: #FF0000; border-radius: 5px;}')
        self.btn_color_green.setStyleSheet('QPushButton{background-color: #00FF00; border-radius: 5px;}')
        self.btn_color_blue.setStyleSheet('QPushButton{background-color: #0000FF; border-radius: 5px;}')
        self.label_palette.setStyleSheet('QPushButton{background-color: #FF0000; }')

        self.btn_open.setIconSize(QSize(20, 20))
        self.btn_save.setIconSize(QSize(20, 20))
        self.btn_undo.setIconSize(QSize(20, 20))
        self.btn_redo.setIconSize(QSize(20, 20))
        self.btn_erase.setIconSize(QSize(20, 20))
        self.btn_text.setIconSize(QSize(20, 20))
        self.btn_line.setIconSize(QSize(20, 20))
        self.btn_rectangle.setIconSize(QSize(20, 20))
        self.btn_ellipse.setIconSize(QSize(20, 20))
        self.btn_brush.setIconSize(QSize(20, 20))
        self.btn_color_palette.setIconSize(QSize(22, 22))
        self.btn_color_red.setIconSize(QSize(20, 20))
        self.btn_color_green.setIconSize(QSize(20, 20))
        self.btn_color_blue.setIconSize(QSize(20, 20))
        self.btn_color_white.setIconSize(QSize(20, 20))
        self.btn_color_black.setIconSize(QSize(20, 20))

        for size in range(10, 120, 4):
            self.combo_font_size.addItem(str(size))
        self.combo_font_size.setCurrentText(str(30))

        self.combo_font_size.hide()
        self.combo_font.hide()
        # self.btn_erase.setCheckable(True)
        self.btn_text.setCheckable(True)
        self.btn_line.setCheckable(True)
        self.btn_rectangle.setCheckable(True)
        self.btn_ellipse.setCheckable(True)
        self.btn_brush.setCheckable(True)
        self.btn_color_red.setCheckable(True)
        self.btn_color_green.setCheckable(True)
        self.btn_color_blue.setCheckable(True)
        self.btn_color_white.setCheckable(True)
        self.btn_color_black.setCheckable(True)
        self.label_palette.setCheckable(False)

        self.btn_undo.setToolTip('Undo')
        self.btn_redo.setToolTip('Redo')
        self.btn_line.setToolTip('Line')
        self.btn_rectangle.setToolTip('Rectangle')
        self.btn_brush.setToolTip('Brush')
        self.btn_ellipse.setToolTip('Ellipse')
        self.btn_erase.setToolTip('Clear All')
        self.btn_open.setToolTip('Open')
        self.btn_save.setToolTip('Save')
        self.btn_color_palette.setToolTip('Color Palette')
        self.btn_text.setToolTip('Text')





