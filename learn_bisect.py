# bisectの練習

import bisect

"""
bisect.bisect_left(a, x)....二分探索して、左側の挿入点を返す
bisect.bisect_right(a, x)...二分探索して、右側の挿入点を返す
bisect.bisect(a, x).........bisect_right(a, x)と同様
bisect.insort_left(a, x)....ソートされた順序に保ちつつ左側に挿入する
bisect.insort_right(a, x)...ソートされた順序に保ちつつ右側に挿入する
bisect.insort(a, x).........bisect.insort_right(a, x)と同様
"""

list_bisect = [0, 3, 5, 6, 8, 11, 15, 20]
print(f"ソート済みリスト: {list_bisect}")

# 二分探索
print(f"左側の挿入点を見つける: {bisect.bisect_left(list_bisect, 8)}")
print(f"右側の挿入点を見つける: {bisect.bisect_right(list_bisect, 8)}")

# 挿入
bisect.insort_left(list_bisect, 8)
print(f"ソートを保ったまま8を挿入: {list_bisect}")
bisect.insort_right(list_bisect, 11)
print(f"ソートを保ったまま11を挿入: {list_bisect}")

