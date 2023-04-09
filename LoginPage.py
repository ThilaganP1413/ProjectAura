from kivy.lang import Builder
from kivymd.app import MDApp

class LoginPage(MDApp):
    def build(self):
        return Builder.load_file('loginpage.kv')
    
LoginPage().run()