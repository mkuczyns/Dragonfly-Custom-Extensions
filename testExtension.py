#-------------------------------------------#
# Test Custom Extension for ORS Dragonfly   #
# Using Python 3.6                          #
#                                           #
# Created By:   Michael T. Kuczynski        #
# Created On:   05/10/2018                  #
# Version:      1.0                         #
#-------------------------------------------#

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLineEdit

class myLineEdit(QLineEdit) :
    def enterEvent(self, e) :
        self.setCursor(Qt.PointingHandCursor)