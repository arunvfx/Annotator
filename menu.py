
import nuke
from main import *


menu = nuke.menu('Nuke').addMenu('thEdge')
menu.addCommand('Annotator', 'main_annotator()')
