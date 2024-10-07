# dequeの練習

import collections
from collections import deque

str = "abcdefg"

# deque化
d = deque(str)
print(d)

# 要素追加
d.append("h")
print(f"右側に要素を追加: {d}")
d.appendleft("z")
print(f"左側に要素を追加: {d}")

# イテラブルなオブジェクトを追加
d.extend("ijk")
print(f"右側に配列を追加: {d}")
d.extendleft("yx")
print(f"左側に配列を追加: {d}")

# 要素の削除
print(f"右側の要素を削除: {d.pop()}")
print(f"削除後のデキュー: {d}")
print(f"右側の要素を削除: {d.popleft()}")
print(f"削除後のデック: {d}")

# スクロール
d.rotate()
print(f"1つスクロール: {d}")
d.rotate(3)
print(f"3つスクロール: {d}")
d.rotate(-4)
print(f"-4つスクロール: {d}")

print("\n")

# 最大要素数を指定
e = deque("abc", 3)
print(e)
e.append("d")
print(f"最大要素数を超える時: {e}")
# maxlenは変更不可