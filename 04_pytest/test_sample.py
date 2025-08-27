# content of test_sample.py

def func(x: int) -> int:
    return x + 1

def func1(x: int) -> int:
    return x + 1

# break

def test_answer():

    assert func(3) == 5

def test_answer1():

    assert func(3) == 4
    