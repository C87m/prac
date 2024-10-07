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

print("\n")

# 最小値を取り出す
print(f"1つ取り出す: {heapq.heappop(list_heap)}")
print(f"優先度付きキュー: {list_heap}")

print("\n")

# 要素を挿入する
heapq.heappush(list_heap, -4)
print(f"-4を挿入: {list_heap}")
