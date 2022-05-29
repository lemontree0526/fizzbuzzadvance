class FizzBuzzWhizz:
    def __init__(self, number):
        self.number = number

    def game_num(self):
        if self.number % 3 == 0:
            return "Fizz"
        if self.number % 5 == 0:
            return "Buzz"
        return  self.number
