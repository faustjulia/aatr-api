from examply import my_function


def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"


def test_my_function():
    assert my_function(arg2=5, arg1=1) == 6, 'Should be 6'


if __name__ == "__main__":
    test_sum()
    test_my_function()
    print("Everything passed")
