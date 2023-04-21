from kivy.lang import Builder
from kivymd.app import MDApp

class HomePage(MDApp):
    def build(self):
        return Builder.load_file('homepage.kv')
    
HomePage().run()