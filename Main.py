from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen , ScreenManager

class LoginPage(Screen):
    pass

class HomePage(Screen):
    pass

class Exercises(Screen):
    pass

class Progress(Screen):
    pass

class QuickConsult(Screen):
    pass

class Schedules(Screen):
    pass

class WindowManager(ScreenManager):
    pass
class AuraMain(MDApp):
    def build(self):
        return Builder.load_file('main.kv')
    
AuraMain().run()