class Luhn:
    def __init__(self, card_num):
        self.v = None

        try:
            self.arr = [int(a) for a in str(card_num) if a != " "]
        except ValueError:
            self.v = False

    def valid(self):
        if self.v is not None:
            return self.v
        if len(self.arr) < 2:
            return False
        for i in range(len(self.arr) - 2, -1, -2):
            self.arr[i] = self.arr[i] * 2
            if self.arr[i] > 9:
                self.arr[i] -= 9
        self.v = sum(self.arr) % 10 == 0
        return self.v
