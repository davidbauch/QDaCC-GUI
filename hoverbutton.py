
from PySide6.QtCore import QAbstractAnimation, QPropertyAnimation, Property, QEasingCurve
from PySide6.QtWidgets import QPushButton
from PySide6 import QtGui

class HoverButton(QPushButton):
    def __init__(self, *args):
        super().__init__(*args)
        self._value = 150
        self._color_from_1 = 243, 244, 246
        self._color_to_1 = 230, 232, 236
        self._color_from_2 = 230, 232, 236
        self._color_to_2 = 243, 244, 246 #197, 206, 222
        self.__initUi()

    def __initUi(self):
        self.__animation = QPropertyAnimation(self, b"value")
        self.__animation.valueChanged.connect(self.__setvalue)
        self.__animation.setStartValue(0)
        self.__animation.setEndValue(1)
        self.__animation.setDuration(200)
        self.__animation.setEasingCurve(QEasingCurve.InOutQuad)
        self.__styleInit(0.0)

    def lerp(self,a,b,t):
        return a + (b-a)*t

    def __styleInit(self, value: float):
        c1 = tuple( self.lerp(a,b,value) for a,b in zip(self._color_from_1, self._color_from_2) )
        c2 = tuple( self.lerp(a,b,value) for a,b in zip(self._color_to_1, self._color_to_2) )
        style = f'background-color: qlineargradient(spread:pad, x1:0, y1:{value}, x2:1, y2:{1-value}, stop:0 rgba({c1[0]}, {c1[1]}, {c1[2]}, 255), stop:1 rgba({c2[0]}, {c2[1]} ,{c2[2]}, 255)); border-radius: {5*value}px;'
        self.setStyleSheet(style)

    def enterEvent(self, e):
        self.__animation.setDirection(QAbstractAnimation.Forward)
        self.__animation.start()
        return super().enterEvent(e)

    def leaveEvent(self, e):
        self.__animation.setDirection(QAbstractAnimation.Backward)
        self.__animation.start()
        return super().leaveEvent(e)

    def __setvalue(self, value):
        self.__styleInit(value)

    @Property(float)
    def value(self):
        return self._value
    @value.setter
    def value(self, value):
        self._value = value