from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen , ScreenManager
from kivymd.uix.pickers import MDDatePicker
from kivy.properties import ListProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import OneLineIconListItem,IconLeftWidget
from kivymd.uix.card import MDCard
from kivy.uix.scrollview import ScrollView
from kivymd.uix.label import MDIcon, MDLabel


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


class MyLayout(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.spacing = "10dp"
        self.padding = "10dp"
        self.pos_hint ={'top':0.8}
        
        # create first card
        card1 = MDCard(
            size_hint_y=None,
            height="100dp",
            orientation="horizontal",
            spacing="10dp",
            padding="10dp",
            elevation = 2,
            radius=[15, 15, 0, 0],
            md_bg_color=(1, 1, 1, 1),
        )
        icon1 = MDIcon(icon='clock', pos_hint={'center_y':0.5})
        text = MDLabel(text="Total Duration is 1hr", halign='left', valign='center')
        card1.add_widget(icon1)
        card1.add_widget(text)
        
        # create second card
        card2 = MDCard(
            size_hint_y=None,
            height="50dp",
            orientation="horizontal",
            spacing="10dp",
            padding="10dp",
            radius=[15, 15, 0, 0],
            md_bg_color=(1, 1, 1, 1),
        )
        text = MDLabel(text="Exercises Done", halign='left', valign='center')
        card2.add_widget(text)
        
        
        # create scrollview with a list of items
        scrollview = ScrollView()
        list_items = MDBoxLayout(
            orientation="vertical",
            spacing="10dp",
            padding="10dp",
            size_hint_y=None,
        )
        list_items.bind(minimum_height=list_items.setter("height"))
        item1 = OneLineIconListItem(IconLeftWidget(icon='Assets/squat 256x256 image.png'),text=f"Squats")
        list_items.add_widget(item1)
        item2 = OneLineIconListItem(IconLeftWidget(icon='Assets/legraise 256x256 image.png'),text=f"Leg Raise")
        list_items.add_widget(item2)
        item3 = OneLineIconListItem(IconLeftWidget(icon='Assets/handraise 256x256 image.png'),text=f"Hand Raise")
        list_items.add_widget(item3)
        item4 = OneLineIconListItem(IconLeftWidget(icon='Assets/situps 256x256 image.png'),text=f"Sit Ups")
        list_items.add_widget(item4)

        scrollview.add_widget(list_items)
        
        # add cards and scrollview to the layout
        self.add_widget(card1)
        self.add_widget(card2)
        self.add_widget(scrollview)

class RecordsScreen(Screen):
    def on_back_button(self):
        self.manager.current = 'HomeScreen'
        self.manager.transition.direction = 'right'

    def on_save(self, instance, value, date_range):
        self.ids.date_label.text = str(value)
        layout = MyLayout()
        self.add_widget(layout)


    def show_date_picker(self):
        date_dialog = MDDatePicker(min_year=2022,max_year=2024)
        date_dialog.bind(on_save=self.on_save)
        date_dialog.open()

    def LayoutToSpawn(self):
        pass


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