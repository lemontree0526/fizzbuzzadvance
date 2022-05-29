class FizzBuzzWhizz:
    def __init__(self, number):
        self.number = number

    def game_num(self):
        if self.number % 3 == 0:
            return "Fizz"
        return  self.number
