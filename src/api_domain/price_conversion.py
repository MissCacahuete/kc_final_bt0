class PriceConversion:
    def __init__(self, id, symbol, name, amount,last_updated,symbol_to, price):
        self.id = id
        self.symbol= symbol
        self.name= name
        self.amount=amount
        self.last_updated=last_updated
        self.symbol_to=symbol_to
        self.price=price

    def calculate_amount(self):
        print(self.amount)
        print(self.price)
        return self.amount * self.price