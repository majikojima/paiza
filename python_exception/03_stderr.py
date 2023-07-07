import traceback, sys

print(1)
try:
    number = 0
    answer = 100 / number
    print(answer)
except ZeroDivisionError as e:
    print("0では割り算できません")
    # print(traceback.format_exc())
    sys.stderr.write(traceback.format_exc())
finally:
    print(2)

"""
1
0では割り算できません
Traceback (most recent call last):
  line 6, in <module>
    answer = 100 / number
ZeroDivisionError: division by zero
2
"""