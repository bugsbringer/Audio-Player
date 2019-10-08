# -*- coding: utf-8 -*-
import os
from PyQt5 import QtWidgets
from PyQt5.QtCore import QDir, Qt, QUrl, QAbstractListModel, QPoint
from PyQt5.QtWidgets import QStyle, QFileDialog, QStatusBar
from PyQt5.QtGui import QIcon, QPalette, QColor
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer, QMediaPlaylist
from player_ui import Ui_MainWindow
import web_music

def time_converter(mcs):
    return ("%02d:%02d" % divmod(mcs // 1000, 60))


def upload_data(path, instance):
    '''create dict from files in dir(path):
    { 'filename': instance('filepath')}'''
    data = {}

    for item in os.listdir(path):
        name = os.path.splitext(item)[0]
        data.update({name: instance(f"{path}/{item}")})

    return data


class PlaylistModel(QAbstractListModel):
    def __init__(self, playlist, names, *args, **kwargs):
        super(PlaylistModel, self).__init__(*args, **kwargs)
        self.playlist = playlist
        self.names = names

    def data(self, index, role):
        if role == Qt.DisplayRole:
            i = index.row()
            if self.names and i < len(self.names):
                return self.names[i]

            else:
                media = self.playlist.media(i)
                return media.canonicalUrl().fileName()



    def rowCount(self, index):
        return self.playlist.mediaCount()


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.oldPos = self.pos()
        self.mousePressEvent = lambda event: setattr(self, 'oldPos', event.globalPos())
        self.icons = upload_data("data/icons", QIcon)

        #window buttons
        self.ui.minimizeButton.setIcon(self.icons['minimize'])
        self.ui.minimizeButton.released.connect(lambda: (self.showMinimized(), setattr(self, 'oldPos', self.pos())))

        self.ui.maximizeButton.setIcon(self.icons['maximize'])
        self.ui.maximizeButton.released.connect(self.resizing)

        self.ui.closeButton.setIcon(self.icons['close'])
        self.ui.closeButton.released.connect(self.close)

        #playlist
        self.playlist = QMediaPlaylist()
        self.playlist_modes = {
            "normal": QMediaPlaylist.Loop,
            "repeat": QMediaPlaylist.CurrentItemInLoop,
            "shuffle": QMediaPlaylist.Random
        }
        self.playlist.currentIndexChanged.connect(self.playlist_position_changed)
        self.playlist.loadFailed.connect(lambda error: print(error))

        #player
        self.player = QMediaPlayer()
        self.player.error.connect(lambda *args: print(args))
        self.player.setPlaylist(self.playlist)
        self.player.durationChanged.connect(self.update_duration)
        self.player.stateChanged.connect(self.player_state)
        self.player.positionChanged.connect(self.update_position)
        self.player.mediaStatusChanged.connect(self.media_control)

        #buttons
        self.ui.playButton.pressed.connect(self.play_control)
        self.ui.prevButton.pressed.connect(self.playlist.previous)
        self.ui.nextButton.pressed.connect(self.playlist.next)
        self.ui.shuffleButton.toggled.connect(self.mode_control)
        self.ui.repeatButton.toggled.connect(self.mode_control)
        self.ui.volumeButton.pressed.connect(self.mute_control)
        self.ui.searchButton.pressed.connect(self.search_music)
        self.ui.clearListButton.pressed.connect(self.clear_playlist)

        #sliders
        self.ui.volumeSlider.valueChanged.connect(self.volume_control)
        self.timeSliderPressed = False
        self.ui.timeSlider.sliderPressed.connect(lambda: setattr(self, 'timeSliderPressed', True))
        self.ui.timeSlider.sliderMoved.connect(lambda pos: self.ui.currentTime.setText(time_converter(pos)))
        self.ui.timeSlider.sliderReleased.connect(self.time_slider_release)

        #model
        self.playlist_names = []
        self.model = PlaylistModel(self.playlist, self.playlist_names)
        self.ui.playlistView.setModel(self.model)

        selection_model = self.ui.playlistView.selectionModel()
        selection_model.selectionChanged.connect(self.playlist_selection_changed)

        #icons
        self.ui.prevButton.setIcon(self.icons['prev'])
        self.ui.playButton.setIcon(self.icons['play'])
        self.ui.nextButton.setIcon(self.icons['next'])
        self.ui.repeatButton.setIcon(self.icons['repeat'])
        self.ui.shuffleButton.setIcon(self.icons['shuffle'])
        self.ui.searchButton.setIcon(self.icons['search'])
        self.ui.clearListButton.setIcon(self.icons['clear-list'])

        #some settings
        self.activate(False)
        self.setAcceptDrops(True)
        self.ui.volumeSlider.setValue(25)
        self.mode_control()

    def activate(self, state):
        state = not state
        self.ui.prevButton.setDisabled(state)
        self.ui.playButton.setDisabled(state)
        self.ui.nextButton.setDisabled(state)
        self.ui.repeatButton.setDisabled(state)
        self.ui.shuffleButton.setDisabled(state)
        self.ui.timeSlider.setDisabled(state)


    def clear_playlist(self):
        self.playlist.clear()
        self.playlist_names.clear()
        self.model.layoutChanged.emit()
        self.activate(False)

    def update_playlist(self):
        self.model.layoutChanged.emit()
        self.activate(bool(self.playlist.mediaCount()))

    def search_music(self):
        query = self.ui.searchInput.text()
        if not query:
            return

        self.ui.searchButton.setDisabled(True)
        self.clear_playlist()

        for item in web_music.search(query):
            self.playlist_names.append(f"{item['author']} - {item['title']}")
            self.playlist.addMedia(QMediaContent(QUrl(item['url'])))

        self.update_playlist()
        self.ui.searchButton.setDisabled(False)
        self.player.play()

    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls():
            e.acceptProposedAction()

    def dropEvent(self, item):
        for url in item.mimeData().urls():
            path = url.path()[1:]
            if os.path.isdir(path):
                for file in os.listdir(path):
                    if os.path.splitext(file)[1] == '.mp3':
                        self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile(path + '\\' + file)))
            else:
                self.playlist.addMedia(QMediaContent(url))

        self.update_playlist()

    def update_duration(self, duration):
        self.ui.timeSlider.setMaximum(duration)
        self.ui.totalTime.setText(time_converter(duration))

    def update_position(self, position):
        if not self.timeSliderPressed:
            self.ui.currentTime.setText(time_converter(position))
            self.ui.timeSlider.setValue(position)

    def player_state(self, state):
        if state == QMediaPlayer.PlayingState:
            self.ui.playButton.setIcon(self.icons['pause'])

        else:
            self.ui.playButton.setIcon(self.icons['play'])

    def play_control(self):
        if self.player.state() == QMediaPlayer.PlayingState:
            self.player.pause()
        else:
            self.player.play()

    def media_control(self, status):
        if status == self.player.BufferedMedia:
            if not self.player.duration():
                self.playlist.next()

    def mode_control(self):
        if self.ui.repeatButton.isChecked():
            self.playlist.setPlaybackMode(self.playlist_modes['repeat'])

        elif self.ui.shuffleButton.isChecked():
            self.playlist.setPlaybackMode(self.playlist_modes['shuffle'])

        else:
            self.playlist.setPlaybackMode(self.playlist_modes['normal'])

    def volume_control(self, volume):
        if volume:
            if volume < 33:
                self.ui.volumeButton.setIcon(self.icons['low-volume'])
            elif volume < 67:
                self.ui.volumeButton.setIcon(self.icons['medium-volume'])
            else:
                self.ui.volumeButton.setIcon(self.icons['high-volume'])
        else:
            if self.ui.volumeSlider.underMouse():
                self.prevVolumeValue = 50
            self.ui.volumeButton.setIcon(self.icons['mute'])

        self.player.setVolume(volume)

    def mute_control(self):
        if self.ui.volumeSlider.value():
            self.prevVolumeValue = self.ui.volumeSlider.value()
            self.ui.volumeSlider.setValue(0)
        else:
            self.ui.volumeSlider.setValue(self.prevVolumeValue)

    def time_slider_release(self):
        self.timeSliderPressed = False
        self.player.setPosition(self.ui.timeSlider.value())

    def playlist_selection_changed(self, index):
        i = index.indexes()[0].row()
        self.playlist.setCurrentIndex(i)
        self.player.play()

    def playlist_position_changed(self, i):
        if i > -1:
            ix = self.model.index(i)
            self.ui.playlistView.setCurrentIndex(ix)
            if self.model.names and i < len(self.model.names):
                self.ui.mediaName.setText(self.model.names[i])
            else:
                name = self.playlist.media(ix.row()).canonicalUrl().fileName()
                self.ui.mediaName.setText(os.path.splitext(name)[0])

    def mouseMoveEvent(self, event):
        if not self.isMaximized():
            delta = QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())

        self.oldPos = event.globalPos()

    def resizing(self):
        if self.isMaximized():
            self.showNormal()
            self.ui.maximizeButton.setIcon(self.icons['maximize'])
        else:
            self.showMaximized()
            self.ui.maximizeButton.setIcon(self.icons['restore-window'])


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    app.setStyle(QtWidgets.QStyleFactory.create('Fusion'))

    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.white)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.black)

    app.setPalette(palette)
    app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")

    window = Window()
    window.show()

    SystemExit(app.exec())
