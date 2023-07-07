import sys

print(1)
try:
    print(2)
    raise Exception("エラーです")
    print(3)
except Exception as e:
    print("予期せぬエラーが発生しました")
    print(e)
    print("huhuhu")
    sys.stderr.write("eeeeerror")
finally:
    print(4)

"""
1
2
予期せぬエラーが発生しました
エラーです
huhuhu
4
"""