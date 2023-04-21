from kivy.lang import Builder
from kivymd.app import MDApp

class QuickConsult(MDApp):
    def build(self):
        return Builder.load_file('quickconsult.kv')
    
QuickConsult().run()