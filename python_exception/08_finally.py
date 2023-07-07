def test_exception(number):
    print(2)
    try:
        print(3)
        answer = 100 / number
        print(4)
        return answer
    except ZeroDivisionError as e:
        print(5)
        raise e
    finally:
        print(6)

print(1)
try:
    answer = test_exception(0)
    print(7)
except ZeroDivisionError as e:
    print(8)
    print(e)

"""
1
2
3
5
6
8
division by zero
"""