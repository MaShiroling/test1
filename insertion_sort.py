def insertion_sort(arr):
    """
    插入排序算法实现
    
    参数:
        arr: 待排序的列表
    返回:
        排序后的列表（原地修改）
    """
    # 从第二个元素开始，逐个插入到已排序部分
    for i in range(1, len(arr)):
        # 当前要插入的元素
        key = arr[i]
        # 在已排序部分从后向前查找插入位置
        j = i - 1
        
        # 如果前一个元素大于当前元素，则后移
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # 将当前元素插入到正确位置
        arr[j + 1] = key
    
    return arr


def binary_insertion_sort(arr):
    """
    优化的插入排序（使用二分查找减少比较次数）
    
    参数:
        arr: 待排序的列表
    返回:
        排序后的列表（原地修改）
    """
    for i in range(1, len(arr)):
        key = arr[i]
        
        # 使用二分查找找到插入位置
        left, right = 0, i - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] < key:
                left = mid + 1
            else:
                right = mid - 1
        
        # 移动元素腾出位置
        for j in range(i - 1, left - 1, -1):
            arr[j + 1] = arr[j]
        
        arr[left] = key
    
    return arr


# 测试代码
if __name__ == "__main__":
    test_arrays = [
        [64, 34, 25, 12, 22, 11, 90],
        [3, -1, 0, 5, -2],
        [1],
        [],
        [5, 5, 5, 1],
        [2, 3, 4, 5, 1],  # 几乎有序
    ]
    
    print("=" * 50)
    print("插入排序算法测试")
    print("=" * 50)
    
    for i, arr in enumerate(test_arrays, 1):
        print(f"\n测试 {i}:")
        print(f"原始数组: {arr}")
        
        # 标准插入排序
        arr_copy = arr.copy()
        insertion_sort(arr_copy)
        print(f"排序结果: {arr_copy}")
        
        # 优化版本
        arr_opt = arr.copy()
        binary_insertion_sort(arr_opt)
        print(f"二分优化: {arr_opt}")
        
        # 验证
        assert arr_copy == sorted(arr), "标准版本不正确！"
        assert arr_opt == sorted(arr), "优化版本不正确！"
    
    print("\n" + "=" * 50)
    print("所有测试通过！✓")
    print("=" * 50)