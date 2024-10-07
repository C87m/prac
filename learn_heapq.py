# heapqの使い方

import heapq

"""
heapq.heapify()....リストを優先度付きキューに変換する
heapq.heappop()....優先度付きキューから最小値を取り出す
heapq.heappush()...優先度付きキューに要素を挿入
"""

# ソートされる前のリスト
list_heap = [3, 5, 2, 6, 8, 0, 1]
print(f"ソート前: {list_heap}")

# 優先度付けされたリスト
heapq.heapify(list_heap)
print(f"優先度付きキュー: {list_heap}")

# 最小値を取り出す
print(f"1つ取り出す: {heapq.heappop(list_heap)}")
print(f"優先度付きキュー: {list_heap}")

# 要素を挿入する
heapq.heappush(list_heap, -4)
print(f"-4を挿入: {list_heap}")

print("\n")

# 最大値を取り出す場合-1をかける
list_minus = [3, 5, 2, 6, 8, 0, 1]
print(f"ソート前のリスト: {list_heap}")
list_minus = list(map(lambda x: x*(-1), list_minus))
heapq.heapify(list_minus)
print(f"優先度付きキュー: {list_minus}")

print(f"最大値を取り出す: {heapq.heappop(list_minus)*(-1)}")
print(f"優先度付きキュー: {list_minus}")