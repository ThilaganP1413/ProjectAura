from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt1

class plot(FloatLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        x1 = [1,2,3,4]
        y1= [2,4,6,8]
        plt1.plot(x1,y1)
        box =self.ids.box
        box.add_widget(FigureCanvasKivyAgg(plt1.gcf()))

class Progress(MDApp):

    def build(self):
        Builder.load_file('progress.kv')
        return plot()
    
Progress().run()