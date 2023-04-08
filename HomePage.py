import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class MyLayout(Widget):
    pass

class HomePage(App):
    def build(self):
        return MyLayout()
    
if __name__ == "__main__":
    HomePage().run()