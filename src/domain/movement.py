class Movement:
    def __init__(self, id, date, time, from_currency,from_quantity,to_currency,to_quantity):
        self.id = id
        self.date= date
        self.time= time
        self.from_currency=from_currency
        self.from_quantity=from_quantity
        self.to_currency=to_currency
        self.to_quantity=to_quantity

    def unitary_price(self):
        return float(self.from_quantity)/float(self.to_quantity)