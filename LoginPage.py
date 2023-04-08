from kivy.lang import Builder
from kivymd.app import MDApp

class LoginPage(MDApp):
    def build(self):
        #self.theme_cls.theme_style = "Light"
        #self.theme_cls.primary_palette = "White"
        return Builder.load_file('loginpage.kv')
    
LoginPage().run()