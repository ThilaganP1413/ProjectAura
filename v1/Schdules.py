from kivy.lang import Builder
from kivymd.app import MDApp

class Schedules(MDApp):

    def on_back_button(self):
        self.manager.current = 'HomePage'
        self.manager.transition.direction = 'right'
    
    def year_clicked(self,text):
        self.year = text

    def month_clicked(self,text):
        self.month = text

    def build(self):
        return Builder.load_file('schedules.kv')
    
Schedules().run()