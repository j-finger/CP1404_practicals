from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty


class ConvertMilesToKilometer(App):
    message = StringProperty()

    def build(self):
        """Build Program GUI from file convert_miles_km.kv"""
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_increment(self, user_input, increment):
        number_to_increment = self.string_to_float(user_input)
        number_to_increment += increment
        self.root.ids.input_number.text = str(number_to_increment)
        self.handle_convert(user_input)

    def handle_convert(self, user_input):
        user_input = self.string_to_float(user_input)
        self.message = str(user_input * 1.609)

    @staticmethod
    def string_to_float(text):
        try:
            number = float(text)
        except ValueError:
            number = 0.0
        return number


ConvertMilesToKilometer().run()
