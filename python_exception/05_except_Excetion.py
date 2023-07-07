print(1)
try:
    number = "a"
    answer = 100 / number
    print(answer2)
# except TypeError as e:
#     print("文字列と数値は足し算できません")
#     print(e)
except ZeroDivisionError as e:
    print("0では割り算できません")
    print(e)
except NameError as e:
    print("変数が定義されていません")
    print(e)
except Exception as e:
    print("何らかの例外が発生しました")
    print(e)
finally:
    print(2)

"""
1
何らかの例外が発生しました
unsupported operand type(s) for /: 'int' and 'str'
2
"""