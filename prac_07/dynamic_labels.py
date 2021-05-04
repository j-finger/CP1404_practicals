"""Practical 07 - Jacob Finger - Dynamic Label Maker"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label


class DynamicLabelsApp(App):

    def __init__(self, **kwargs):
        """Constructs the main app"""
        super().__init__(**kwargs)
        self.name_to_phone = {"Bob Brown": "0414144411", "Cat Cyan": "0441411211", "Oren Ochre": "0432123456"}

    def build(self):
        """Build the Kivy Label GUI"""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Iterates through the list of numbers and creates a label for each"""
        for name in self.name_to_phone:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()
