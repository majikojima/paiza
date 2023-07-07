print(1)
try:
    number = 1
    answer = 100 / number
    print(answer2)
except ZeroDivisionError as e:
    print("0では割り算できません")
    print(e)
except NameError as e:
    print("変数が定義されていません")
    print(e)
finally:
    print(2)

"""
1
変数が定義されていません
name 'answer2' is not defined
2
"""