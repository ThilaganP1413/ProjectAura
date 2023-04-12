from kivy.lang import Builder
from kivymd.app import MDApp

class Progress(MDApp):
    def build(self):
        return Builder.load_file('progress.kv')
    
Progress().run()