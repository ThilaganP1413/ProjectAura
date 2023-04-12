from kivy.lang import Builder
from kivymd.app import MDApp

class Exercise(MDApp):
    def build(self):
        return Builder.load_file('exercise.kv')
    
Exercise().run()