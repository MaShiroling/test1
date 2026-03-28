def selection_sort(arr):
    """
    选择排序算法实现
    
    原理：每次从未排序部分找到最小元素，放到已排序部分的末尾
    
    参数:
        arr: 待排序的列表
    返回:
        排序后的列表（原地修改）
    """
    n = len(arr)
    
    # 遍历所有元素
    for i in range(n):
        # 假设当前位置是最小值的位置
        min_idx = i
        
        # 在剩余未排序部分找到真正的最小值
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # 如果找到更小的元素，交换它们
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr


def selection_sort_stable(arr):
    """
    稳定的选择排序（通过插入代替交换）
    
    参数:
        arr: 待排序的列表
    返回:
        排序后的列表（原地修改）
    """
    n = len(arr)
    
    for i in range(n):
        # 找到最小元素
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # 将最小元素插入到正确位置（而不是交换）
        min_val = arr[min_idx]
        # 向后移动已排序部分的元素
        for j in range(min_idx, i, -1):
            arr[j] = arr[j - 1]
        arr[i] = min_val
    
    return arr


# 测试代码
if __name__ == "__main__":
    test_arrays = [
        [64, 34, 25, 12, 22, 11, 90],
        [3, -1, 0, 5, -2],
        [1],
        [],
        [5, 5, 5, 1],
        [88, 91, 72, 63, 55, 42],  # 逆序
    ]
    
    print("=" * 50)
    print("选择排序算法测试")
    print("=" * 50)
    
    for i, arr in enumerate(test_arrays, 1):
        print(f"\n测试 {i}:")
        print(f"原始数组: {arr}")
        
        # 标准选择排序
        arr_copy = arr.copy()
        selection_sort(arr_copy)
        print(f"排序结果: {arr_copy}")
        
        # 稳定版本
        arr_stable = arr.copy()
        selection_sort_stable(arr_stable)
        print(f"稳定版本: {arr_stable}")
        
        # 验证排序正确性
        assert arr_copy == sorted(arr), "标准版本不正确！"
        assert arr_stable == sorted(arr), "稳定版本不正确！"
    
    print("\n" + "=" * 50)
    print("所有测试通过！✓")
    print("=" * 50)