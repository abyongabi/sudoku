class Number:
    def __init__(self, num: int | None = None):
        self.num = num
        self.probability = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def set_value(self, num: int):
        self.num = num
        self.probability = []

    def remove_probability(self, num: int):
        if num in self.probability:
            self.probability.remove(num)

    def __repr__(self):
        return str(self.num)