from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM_FACTOR = 1.60934  # Conversion factor


class MilesToKmConverterApp(App):
    def build(self):
        self.title = 'Miles to Kilometers Converter'
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_increment(self, value):
        try:
            miles = float(self.root.ids.miles_input.text) + value
            self.root.ids.miles_input.text = str(miles)
            self.calculate_conversion()
        except ValueError:
            self.root.ids.output_label.text = '0.0 km'

    def calculate_conversion(self):
        try:
            miles = float(self.root.ids.miles_input.text)
            kilometers = miles * MILES_TO_KM_FACTOR
            self.root.ids.output_label.text = f'{kilometers:.2f} km'
        except ValueError:
            self.root.ids.output_label.text = '0.0 km'


if __name__ == '__main__':
    MilesToKmConverterApp().run()