import os

import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

import subprocess
from subprocess import Popen, PIPE
import os

# import driver_drowsiness_new

kivy.require('1.9.0')

kv = Builder.load_file('sleepalert.kv')


# DriverDrow = driver_drowsiness

class MainWindow(Widget):
    def spinner_clicked(self, value):
        self.ids.click_label.text = f'{value}'

    def start_ride(self):
        # subprocess.call(" python script2.py 1", shell=True)
        with open("driver_drowsiness.py", "r") as rnf:
            exec(rnf.read())
            subprocess.run('driver_drowsiness.py')


class SleepAlert(App):
    def build(self):
        return MainWindow()


sleepAlert = SleepAlert()
SleepAlert().run()
