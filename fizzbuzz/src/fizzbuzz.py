class FizzBuzzWhizz:
    def __init__(self, number):
        self.number = number

    def game_num(self):
        if self.number % 3 == 0 and self.number % 7 == 0 and self.number % 5 == 0:
            return "FizzBuzzWhizz"
        if self.number % 3 == 0 and self.number % 5 == 0:
            return "FizzBuzz"
        if self.number % 3 == 0 and self.number % 7 == 0:
            return "FizzWhizz"
        if self.number % 5 == 0 and self.number % 7 ==0:
            return "BuzzWhizz"
        if self.number % 3 == 0:
            return "Fizz"
        if self.number % 3 != 0 and self.number % 7 != 0 and self.number % 5 == 0:
            return "Buzz"
        if self.number % 5 == 0:
            return "Buzz"
        if self.number % 7 == 0:
            return "Whizz"
        return  self.number
