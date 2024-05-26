from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.toolbar import MDTopAppBar

KV = '''
MDScreen:
    orientation: "vertical"
    spacing: "10dp"

    MDBoxLayout:
        id: box
        orientation: "vertical"
        spacing: "12dp"
        pos_hint: {"top": 1}
        adaptive_height: True

    ScrollView:
        pos_hint: {"top": 0.89}
        size_hint_y: 0.89
        MDList:
            id: list
            size_hint_y: None
            height: self.minimum_height

    MDLabel:
        text: "Hello, World!"
        halign: "center"
'''

class App(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        self.theme_cls.material_style = "M3"
        return Builder.load_string(KV)

    def on_start(self):
        type_height = "small"
        
        self.root.ids.box.add_widget(
            MDTopAppBar(
                type_height=type_height,
                headline_text=f"Headline {type_height.lower()}",
                md_bg_color="#9e0000",
                title="CygenAndroid" if type_height == "small" else "",
                pos_hint={"top": 1}
            )
        )

App = App()

App.run()