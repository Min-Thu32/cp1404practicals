from taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.price_per_km *= fanciness

    def get_fare(self):
        fare = super().get_fare() + self.flagfall
        return round(fare, 1)  # rounding to the nearest 10 cents

    def __str__(self):
        return f"{super().__str__()} plus flagfall of ${self.flagfall}"