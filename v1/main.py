from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen , ScreenManager

class LoginPage(Screen):
    pass

class HomePage(Screen):
    pass

class Exercises(Screen):
    def on_back_button(self):
        self.manager.current = 'HomePage'
        self.manager.transition.direction = 'right'

class Progress(Screen):
    def on_back_button(self):
        self.manager.current = 'HomePage'
        self.manager.transition.direction = 'right'

class QuickConsult(Screen):
    def on_back_button(self):
        self.manager.current = 'HomePage'
        self.manager.transition.direction = 'right'


class Schedules(Screen):
    def on_back_button(self):
        self.manager.current = 'HomePage'
        self.manager.transition.direction = 'right'

    def spinner_clicked(self,value):
        pass

class WindowManager(ScreenManager):
    pass
class AuraMain(MDApp):
    def build(self):
        return Builder.load_file('main.kv')
    
AuraMain().run()