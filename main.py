import sys

from ui import Ui_MainWindow
from PyQt6 import QtCore, QtMultimedia
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import Qt


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self._player = QtMultimedia.QMediaPlayer()
        self._audio_output = QtMultimedia.QAudioOutput()
        self._player.setAudioOutput(self._audio_output)
        self._audio_output.setVolume(100)

        self.all_buttons = {Qt.Key.Key_Q: [self.q, 'guitar_As2_very-long_forte_normal.mp3'],
                            Qt.Key.Key_W: [self.w, 'guitar_B2_very-long_forte_normal.mp3'],
                            Qt.Key.Key_E: [self.e, 'guitar_C3_very-long_forte_normal.mp3'],
                            Qt.Key.Key_R: [self.r, 'guitar_Cs3_very-long_forte_normal.mp3'],
                            Qt.Key.Key_T: [self.t, 'guitar_D3_very-long_forte_normal.mp3'],
                            Qt.Key.Key_Y: [self.y, 'guitar_Ds3_very-long_forte_normal.mp3'],
                            Qt.Key.Key_U: [self.u, 'guitar_E3_very-long_forte_normal.mp3'],
                            Qt.Key.Key_I: [self.i, 'guitar_F3_very-long_forte_normal.mp3'],
                            Qt.Key.Key_O: [self.o, 'guitar_Fs3_very-long_forte_normal.mp3'],
                            Qt.Key.Key_P: [self.p, 'guitar_G3_very-long_forte_normal.mp3'],
                            Qt.Key.Key_A: [self.a, 'guitar_Gs3_very-long_forte_normal.mp3']}

        self.q.clicked.connect(lambda x: self.sound('guitar_As2_very-long_forte_normal.mp3'))
        self.w.clicked.connect(lambda x: self.sound('guitar_B2_very-long_forte_normal.mp3'))
        self.e.clicked.connect(lambda x: self.sound('guitar_C3_very-long_forte_normal.mp3'))
        self.r.clicked.connect(lambda x: self.sound('guitar_Cs3_very-long_forte_normal.mp3'))
        self.t.clicked.connect(lambda x: self.sound('guitar_D3_very-long_forte_normal.mp3'))
        self.y.clicked.connect(lambda x: self.sound('guitar_Ds3_very-long_forte_normal.mp3'))
        self.u.clicked.connect(lambda x: self.sound('guitar_E3_very-long_forte_normal.mp3'))
        self.i.clicked.connect(lambda x: self.sound('guitar_F3_very-long_forte_normal.mp3'))
        self.o.clicked.connect(lambda x: self.sound('guitar_Fs3_very-long_forte_normal.mp3'))
        self.p.clicked.connect(lambda x: self.sound('guitar_G3_very-long_forte_normal.mp3'))
        self.a.clicked.connect(lambda x: self.sound('guitar_Gs3_very-long_forte_normal.mp3'))

    def keyPressEvent(self, event):
        if event.key() in self.all_buttons.keys():
            self.sound(self.all_buttons[event.key()][1])

    def sound(self, file):
        self.load_mp3(file)
        self._player.play()

    def load_mp3(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        self._player.setSource(media)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
