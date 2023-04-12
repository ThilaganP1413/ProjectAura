from kivy.lang import Builder
from kivymd.app import MDApp

class Schedules(MDApp):
    def build(self):
        return Builder.load_file('schedules.kv')
    
Schedules().run()