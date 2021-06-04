"""CP1404 Practical 07 - Jacob Finger - Convert Miles to Km GUI Program"""
from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty
from kivy.core.window import Window
KILOMETERS_PER_MILE = 1.609


class ConvertMilesToKilometer(App):
    message = StringProperty()

    def build(self):
        """Build Program GUI from file convert_miles_km.kv"""
        Window.size = (300, 175)
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_increment(self, user_input, increment):
        """Increments given input with given increment"""
        number_to_increment = self.string_to_float(user_input)
        number_to_increment += increment
        self.root.ids.input_number.text = str(number_to_increment)
        self.handle_convert(user_input)

    def handle_convert(self, user_input):
        """Converts given input from kilometers to miles"""
        user_input = self.string_to_float(user_input)
        self.message = str(user_input * KILOMETERS_PER_MILE)

    @staticmethod
    def string_to_float(text):
        """Converts text to a float or resets input to 0.0 for a non-numerical input"""
        try:
            number = float(text)
        except ValueError:
            number = 0.0
        return number


ConvertMilesToKilometer().run()
