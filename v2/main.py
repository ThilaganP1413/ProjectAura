from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen , ScreenManager

class HomeScreen(Screen):

    def leave_tab(self,nav_item):
        if nav_item.name == 'Home':
            nav_item.icon = 'home-outline'
        if nav_item.name == 'Consult':
            nav_item.icon = 'message-outline'
        if nav_item.name == 'Communiy':
            nav_item.icon = 'account-group-outline'
        if nav_item.name == 'Account':
            nav_item.icon = 'account-cog-outline'

    def enter_tab(self, nav_item):
        if nav_item.name == 'Home':
            nav_item.icon = 'home'
        if nav_item.name == 'Consult':
            nav_item.icon = 'message'
        if nav_item.name == 'Communiy':
            nav_item.icon = 'account-group'
        if nav_item.name == 'Account':
            nav_item.icon = 'account-cog'

class ProgressScreen(Screen):
    def on_back_button(self):
        self.manager.current = 'HomeScreen'
        self.manager.transition.direction = 'right'

class RecordsScreen(Screen):
    def on_back_button(self):
        self.manager.current = 'HomeScreen'
        self.manager.transition.direction = 'right'

class SessionScreen(Screen):
    def on_back_button(self):
        self.manager.current = 'HomeScreen'
        self.manager.transition.direction = 'right'
        
class WindowManager(ScreenManager):
    pass


class Aura(MDApp):
    
    def build(self):
        return Builder.load_file('main.kv')
    

Aura().run()