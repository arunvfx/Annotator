
import nuke
from main import *
# from nukescripts import panels


menu = nuke.menu('Nuke').addMenu('thEdge')
menu.addCommand('Annotator', 'main_annotator()')
