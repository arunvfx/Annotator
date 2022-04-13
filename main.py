# -*- coding: utf-8 -*-

import os
import sys

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

from ui.ui_annotator import AnnotatorUi

import packages.pyperclip as pyperclip


class PaintWidget(QWidget):

    def __init__(self, parent, src_image, brush_size, color):
        """
        paint widget to process painting.
        :param QFrame parent: parent frame.
        :param src src_image: captured image file .
        :param  int brush_size: default brush size.
        :param str color: default color.
        """
        super(PaintWidget, self).__init__(parent)

        self.src_image = src_image
        self.brush_size = brush_size
        self.color = color
        self.btn_triggered = None
        self.font_size = None
        self.font_family = None
        self.painting = False
        self.text_pos = None
        self.origin = None
        self.destination = None
        self.strokes = []
        self.characters = []
        self.backup_strokes = []
        self.text_edit_size = QSize()

        self.load_grabbed_image()
        self.image = QImage(self.img.width(), self.img.height(), QImage.Format_RGB32)
        self.process_painting()
        self.text_editor()

    def load_grabbed_image(self):
        """
        load captured image to paint widget.
        :return: None
        """
        pixmap = QPixmap(self.src_image)
        if pixmap.width() < 1920 and pixmap.height() < 1080:
            self.img = pixmap.scaled(
                pixmap.width(), pixmap.height(), Qt.KeepAspectRatio, Qt.SmoothTransformation
            )
        else:
            self.img = pixmap.scaled(1920, 1080, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.setFixedSize(self.img.width() + 10, self.img.height() + 30)

    def paintEvent(self, event):
        """
        create empty canvas.
        """
        painter = QPainter(self)
        painter.drawImage(event.rect(), self.image, self.rect())

    def process_painting(self):
        """
        process painting shapes.
        :return: None.
        """
        painter = QPainter(self.image)
        painter.drawPixmap(QPoint(), self.img)
        painter.setRenderHint(QPainter.Antialiasing)

        if self.strokes:
            for stroke in self.strokes:
                if isinstance(stroke, list):
                    for line in stroke:
                        if len(line) == 3:
                            painter.setPen(
                                QPen(
                                    QColor(line[2]), line[1], Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin
                                )
                            )
                            painter.drawLine(line[0])

                        elif len(line) == 5:
                            painter.setPen(QPen(QColor(line[2])))
                            font = QFont(line[1])
                            font.setPixelSize(line[3] + (line[3]/3))
                            painter.setFont(font)
                            painter.drawText(line[0], line[4])

                else:
                    if not len(stroke) == 5:
                        painter.setPen(
                            QPen(
                                QColor(stroke[2]), stroke[1], Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin
                            )
                        )
                    if stroke[0].__class__.__name__ == 'QLine':
                        painter.drawLine(stroke[0])
                    elif stroke[0].__class__.__name__ == 'QRect':
                        painter.drawRect(stroke[0])
                    elif stroke[0].__class__.__name__ == 'QRectF' and len(stroke) == 3:
                        painter.drawEllipse(stroke[0])

        if self.destination:
            painter.setPen(
                QPen(
                    QColor(self.color),
                    self.brush_size.value(),
                    Qt.SolidLine,
                    Qt.RoundCap,
                    Qt.RoundJoin
                )
            )

            if self.btn_triggered == 'btn_line':
                line = (QLine(self.origin, self.destination), self.brush_size.value(), self.color)
                painter.drawLine(line[0])
            elif self.btn_triggered == 'btn_rectangle':
                rect = (QRect(self.origin, self.destination), self.brush_size.value(), self.color)
                painter.drawRect(rect[0].normalized())
            elif self.btn_triggered == 'btn_ellipse':
                ellipse = (
                    QRectF(self.origin, self.destination), self.brush_size.value(), self.color
                )
                painter.drawEllipse(ellipse[0])
            elif self.btn_triggered == 'btn_brush':
                line = (QLine(self.origin, self.destination), self.brush_size.value(), self.color)
                painter.drawLine(line[0])
            elif self.btn_triggered == 'btn_text':
                rect = QRectF(
                    self.text_pos.x() + 5,
                    self.text_pos.y() - 56,
                    self.text_edit_size.width() + 10,
                    self.text_edit_size.height() + 30
                )
                painter.drawText(rect, self.text_edit.toPlainText())
        self.update()

    def mousePressEvent(self, event):
        """
        mouse press operations.
        """
        if event.buttons() & Qt.LeftButton:
            self.origin = event.pos()
            self.text_pos = event.pos()
            self.destination = self.origin
            self.text_edit.hide()
            if self.characters:
                try:
                    self.strokes.append(self.characters.copy())
                except AttributeError:
                    self.strokes.append(list(self.characters))
            del self.characters[:]
            self.text_edit.clear()
            self.process_painting()
            if self.btn_triggered == 'btn_text':
                self.text_edit.show()
                self.text_edit.move(event.x(), event.y() - 60)
            self.update()

    def mouseReleaseEvent(self, event):
        """
        mouse release operations.
        """
        if event.button() & Qt.LeftButton and not self.btn_triggered == 'btn_brush':
            self.destination = event.pos()
            if self.btn_triggered == 'btn_line':
                self.strokes.append(
                    (QLine(self.origin, self.destination), self.brush_size.value(), self.color)
                )
            elif self.btn_triggered == 'btn_rectangle':
                self.strokes.append(
                    (QRect(self.origin, self.destination), self.brush_size.value(), self.color)
                )
            elif self.btn_triggered == 'btn_ellipse':
                self.strokes.append(
                    (QRectF(self.origin, self.destination), self.brush_size.value(), self.color)
                )

            self.origin, self.destination = QPoint(), QPoint()
            self.process_painting()
            self.update()

        if self.btn_triggered == 'btn_brush':
            self.painting = False

    def mouseMoveEvent(self, event):
        """
        mouse move operations.
        """
        if event.buttons() & Qt.LeftButton and not self.btn_triggered == 'btn_brush':
            self.destination = event.pos()
            self.process_painting()
            self.update()
        if event.buttons() & Qt.LeftButton and self.btn_triggered == 'btn_brush':
            self.destination = event.pos()
            if self.painting:
                self.strokes[-1].append(
                    (QLine(self.origin, self.destination), self.brush_size.value(), self.color)
                )
            elif not self.painting:
                self.strokes.append([])
                self.strokes[-1].append(
                    (QLine(self.origin, self.destination), self.brush_size.value(), self.color)
                )
            self.painting = True
            self.origin = event.pos()
            self.process_painting()
            self.update()

    def text_editor(self):
        """
        create QPlainTextEdit and call resize_text_edit function while typing.
        :return: None.
        """
        self.text_edit = QPlainTextEdit(self)
        self.text_edit.setObjectName('text_edit')
        self.text_edit.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.text_edit.hide()
        self.text_edit.textChanged.connect(self.resize_text_edit)

    def resize_text_edit(self):
        """
        update text while typing.
        :return:None
        """
        self.setStyleSheet(
            " background-color: rgba(0,0,0,0); border: None; color: {}".format(self.color)
        )
        self.text_edit.setFocus()
        font = QFont()
        font.setFamily(self.font_family)
        font.setPointSize(self.font_size)
        self.text_edit.setFont(font)
        font_metrics = QFontMetrics(font)
        self.text_edit_size = font_metrics.size(0, self.text_edit.toPlainText())
        self.text_edit.setMinimumSize(
            self.text_edit_size.width() + 60, self.text_edit_size.height() + 30
        )
        self.text_edit.resize(self.text_edit_size.width() + 60, self.text_edit_size.height() + 30)
        rect = QRectF(
            self.text_pos.x() + 4,
            self.text_pos.y() - 56,
            self.text_edit_size.width() + 100,
            self.text_edit_size.height() + 30
        )
        self.characters.append(
            (rect, self.font_family, self.color, self.font_size, self.text_edit.toPlainText())
        )
        if len(self.characters) > 1:
            self.characters.pop(0)

    def update_btn_triggered(self, btn_triggered):
        """
        update triggered button.
        :param str btn_triggered: button triggered.
        :return: None.
        """
        self.btn_triggered = btn_triggered
        self.text_edit.hide()
        if self.characters:
            try:
                self.strokes.append(self.characters.copy())
            except AttributeError:
                self.strokes.append(list(self.characters))

        del self.characters[:]
        self.process_painting()

    def undo_paint(self):
        """
        undo paint shapes.
        """
        if self.strokes:
            stroke = self.strokes.pop()
            self.backup_strokes.append(stroke)
            if self.strokes:
                stroke = self.strokes.pop()
                self.backup_strokes.append(stroke)
            self.process_painting()
            self.update()

    def redo_paint(self):
        """
        redo paint shapes.
        """
        if self.backup_strokes:
            stroke = self.backup_strokes.pop()
            self.strokes.append(stroke)
            if self.backup_strokes:
                stroke = self.backup_strokes.pop()
                self.strokes.append(stroke)
            self.process_painting()
            self.update()

    def update_color(self, color):
        """
        update selected color.
        :param str color: selected color.
        """
        self.color = color

    def update_font(self, font_size, font_family):
        """
        update font and font-size.
        :param str font_size: selected font size.
        :param str font_family: selected font-family.
        """
        self.font_family = font_family
        self.font_size = int(font_size)

    def clear_all_strokes(self):
        """
        clear all paint shapes.
        """
        del self.strokes[:]
        del self.backup_strokes[:]
        self.process_painting()

    def save_file(self, file):
        """
        save image file.
        :param str file: image file to be saved.
        """
        self.clipboard_image = file
        self.image.save(file, 'jpg', 100)
        self.copy_to_clipboard()

    def copy_to_clipboard(self):
        """
        copy image path to clipboard.
        :return: None.
        """
        if self.clipboard_image:
            if sys.platform == 'win32':
                pyperclip.copy(self.clipboard_image.replace('/', '\\'))
            else:
                pyperclip.copy(self.image_file)


# -------------------------------------- PAINT WIDGET -----------------------------------------

class Annotator(AnnotatorUi, QWidget):

    def __init__(self, src_image):
        super(Annotator, self).__init__()
        self.setupUi(self)

        self.buttons = [
            self.btn_brush, self.btn_text, self.btn_line, self.btn_rectangle, self.btn_ellipse
        ]
        self.color_buttons = [
            self.btn_color_red,
            self.btn_color_green,
            self.btn_color_blue,
            self.btn_color_white,
            self.btn_color_black
        ]

        self.layout_body = QHBoxLayout()
        self.execute_paint(src_image)
        self.update_font()
        self.layout_body.addWidget(self.paint_widget)
        self.frame_body.setLayout(self.layout_body)

        self.activate_tool()

    def execute_paint(self, src_image):
        """
        run paint operations widget.
        :param str src_image: image captured .
        :return: None
        """
        self.paint_widget = PaintWidget(
            self.frame_body,
            src_image,
            self.slider_brush_size,
            self.label_palette.palette().button().color().name()
        )

    def activate_tool(self):
        """
        trigger operations once button clicked.
        :return: None
        """
        self.btn_open.clicked.connect(self.open_image)
        self.btn_save.clicked.connect(self.execute_save_image)

        self.btn_brush.clicked.connect(self.toggle_buttons)
        self.btn_text.clicked.connect(self.toggle_buttons)
        self.btn_line.clicked.connect(self.toggle_buttons)
        self.btn_rectangle.clicked.connect(self.toggle_buttons)
        self.btn_ellipse.clicked.connect(self.toggle_buttons)
        self.btn_erase.clicked.connect(self.paint_widget.clear_all_strokes)
        self.btn_undo.clicked.connect(self.paint_widget.undo_paint)
        self.btn_redo.clicked.connect(self.paint_widget.redo_paint)

        self.btn_color_red.clicked.connect(self.toggle_color_buttons)
        self.btn_color_green.clicked.connect(self.toggle_color_buttons)
        self.btn_color_blue.clicked.connect(self.toggle_color_buttons)
        self.btn_color_white.clicked.connect(self.toggle_color_buttons)
        self.btn_color_black.clicked.connect(self.toggle_color_buttons)

        self.btn_color_palette.clicked.connect(self.color_picker)
        self.combo_font.currentIndexChanged.connect(self.update_font)
        self.combo_font_size.currentIndexChanged.connect(self.update_font)

        self.btn_copy_clipboard.clicked.connect(self.paint_widget.copy_to_clipboard)

    def color_picker(self):
        """
        open color picker popup.
        :return: None
        """
        color = QColorDialog.getColor()
        self.label_palette.setStyleSheet("QPushButton { background-color: %s} " % color.name())
        self.trigger_color_update()
        for button in self.color_buttons:
            button.setIcon(QIcon(''))
            button.setChecked(False)

    def toggle_buttons(self):
        """
        toggle shape buttons and update font, btn_triggered in paint widget.
        :return: None
        """
        for button in self.buttons:
            if button.objectName() == self.sender().objectName():
                button.setChecked(True)
                if self.sender().objectName() == 'btn_text':
                    self.combo_font.show()
                    self.combo_font_size.show()
                    self.update_font()
                else:
                    self.combo_font.hide()
                    self.combo_font_size.hide()
            else:
                button.setChecked(False)
        self.paint_widget.update_btn_triggered(self.sender().objectName())

    def toggle_color_buttons(self):
        """
        toggle color buttons.
        :return: None
        """
        for button in self.color_buttons:
            if button.objectName() == self.sender().objectName():
                button.setChecked(True)
                self.label_palette.setStyleSheet(
                    "background-color: {}".format(button.palette().button().color().name())
                )
                button.setIcon(QIcon('{}/icons/brush.png'.format(os.path.dirname(__file__))))
                self.trigger_color_update()
            else:
                button.setIcon(QIcon(''))
                button.setChecked(False)

    def trigger_color_update(self):
        """
        update selected color in paint widget.
        :return: None
        """
        self.paint_widget.update_color(self.label_palette.palette().button().color().name())

    def update_font(self):
        """
        update current font-family and font-size in paint widget.
        :return: None
        """
        self.paint_widget.update_font(
            self.combo_font_size.currentText(), self.combo_font.currentText()
        )

    def open_image(self):
        """
        open selected image and load in paint widget.
        :return: None.
        """
        file_selected = self.open_file_browser()
        if file_selected[0]:
            self.paint_widget.deleteLater()
            self.execute_paint(file_selected[0])
            self.layout_body.addWidget(self.paint_widget)

    def open_file_browser(self):
        """
        open file browser.
        :return tuple: file selected.
        """
        file_browser = QFileDialog()
        return file_browser.getOpenFileName(
            self, 'Open Image', 'C:/', 'Image Files (*.png *.jpg *.tiff)',
            options=QFileDialog.DontUseNativeDialog
        )

    def execute_save_image(self):
        """
        get filename to be saved and call save_file in paint widget.
        :return: None
        """
        self.paint_widget.update_btn_triggered(self.sender().objectName())
        file = self.save_image_browser()
        if file:
            self.paint_widget.save_file('{}.jpg'.format(os.path.splitext(file[0])[0]))
            self.btn_copy_clipboard.show()

    def save_image_browser(self):
        """
        save file browser.
        :return: None
        """
        file_browser = QFileDialog()
        return file_browser.getSaveFileName(
            self, 'Save Image', 'C:/', 'Image Files (*.jpg)',
            options=QFileDialog.DontUseNativeDialog
        )


# --------------------------------- CAPTURE SCREEN ---------------------------------------------

class GrabScreen(QWidget):
    """
    Widget to capture screen area
    """

    def __init__(self):
        super(GrabScreen, self).__init__()

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setGeometry(QRect(0, 0, 10000, 10000))
        self.setWindowOpacity(0.7)

        self.initial_pos, self.destination_pos = None, None
        self.bitmap_mask = QBitmap(50000, 30000)
        self.bitmap_mask.fill(Qt.black)
        self.mask = self.bitmap_mask.copy()
        self.dragArea = False

    def paintEvent(self, event):
        if self.dragArea:
            painter = QPainter(self.mask)
            brush = QBrush(Qt.white)
            painter.setBrush(brush)
            painter.drawRect(QRect(self.initial_pos, self.destination_pos))
            self.setMask(QBitmap(self.mask))

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.initial_pos = event.pos()
            self.dragArea = True

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.destination_pos = event.pos()
            try:
                window = QPixmap.grabWindow(
                    QApplication.desktop().winId(),
                    self.initial_pos.x(),
                    self.initial_pos.y() ,
                    self.destination_pos.x() - self.initial_pos.x(),
                    self.destination_pos.y() - self.initial_pos.y()
                )
            except ValueError:
                window = QPixmap.grabWindow(
                    long(QApplication.desktop().winId()),
                    self.initial_pos.x(),
                    self.initial_pos.y() ,
                    self.destination_pos.x() - self.initial_pos.x(),
                    self.destination_pos.y() - self.initial_pos.y()
                )
            image = '{}/Pictures/annotation_temp.jpg'.format(os.path.expanduser('~'))
            window.save(image, 'jpg', 100)
            self.close()
            popup_paint(image)

    def mouseMoveEvent(self, event):
        if self.dragArea:
            self.destination_pos = event.pos()
            self.update()


def popup_paint(img):
    """
    once captured, open paint ui widget.
    :param str img: Image captured
    :return: None
    """
    GrabScreen.t = Annotator(img)
    GrabScreen.t.show()


def main_annotator():
    main_annotator.ann = GrabScreen()
    main_annotator.ann.show()
