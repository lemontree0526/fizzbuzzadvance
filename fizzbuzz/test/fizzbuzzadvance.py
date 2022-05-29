import pytest
from fizzbuzz.src.fizzbuzz import FizzBuzzWhizz
def test_should_return_original_number_when_playing_game_given_number_is_not_mod_by_3_5_7_and_not_container_3_5_7():
    fbw = FizzBuzzWhizz(int(1))
    assert fbw.game_num() == 1

def test_should_return_Fizz_when_playing_game_given_number_is_only_mod_by_3_and_not_container_3_5_7():
    fbw = FizzBuzzWhizz(int(6))
    assert fbw.game_num() == "Fizz"


def test_should_return_Fizz_when_playing_game_given_number_is_only_mod_by_5_and_not_container_3_5_7():
    fbw = FizzBuzzWhizz(int(10))
    assert fbw.game_num() == "Buzz"


def test_should_return_FizzBuzz_when_playing_game_given_number_is_only_mod_by_3_5_and_not_container_3_5_7():
    fbw = FizzBuzzWhizz(int(60))
    assert fbw.game_num() == "FizzBuzz"

def test_should_return_FizzWhizz_when_playing_game_given_number_is_only_mod_by_3_7_and_not_container_3_5_7():
    fbw = FizzBuzzWhizz(int(21))
    assert fbw.game_num() == "FizzWhizz"

def test_should_return_BuzzWhizz_when_playing_game_given_number_is_only_mod_by_5_7_and_not_container_3_5_7():
    fbw = FizzBuzzWhizz(int(140))
    assert fbw.game_num() == "BuzzWhizz"

def test_should_return_FizzBuzzWhizz_when_playing_game_given_number_is_mod_by_3_5_7_and_not_container_3_5_7():
    fbw = FizzBuzzWhizz(int(210))
    assert fbw.game_num() == "FizzBuzzWhizz"
