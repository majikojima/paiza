import sys

def test_exception(number):
    print(2)
    try:
        print(3)
        answer = 100 / number
    except Exception as e:
        print("何らかの例外が発生しました")
        print(e)
        sys.stderr.write("eeeeerror")
        answer = 0
    return answer

print(1)
try:
    answer = test_exception(0)
    print("answer:" , answer)
except ZeroDivisionError as e:
    print("0では割り算できません")
    print(e)
print("end")

"""
1
2
3
何らかの例外が発生しました
division by zero
answer: 0
end
"""