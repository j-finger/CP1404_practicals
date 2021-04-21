from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.app import StringProperty


class ConvertMilesToKilometer(App):
    message = StringProperty()

    def build(self):
        Window.size = (300, 200)
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_increment(self, increment_number):
        if self.message.isdigit():
            self.message = str(int(self.message) + increment_number)
        elif self.message == '' or not self.message.isdigit():
            self.message = '0'

    def handle_convert(self):
        self.message = self.root.ids.input_number.text


ConvertMilesToKilometer().run()
