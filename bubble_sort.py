def bubble_sort(arr):
    """
    冒泡排序算法实现
    
    参数:
        arr: 待排序的列表
    返回:
        排序后的新列表（原地修改）
    """
    n = len(arr)
    
    # 外层循环控制排序轮数
    for i in range(n):
        # 优化：如果某一轮没有发生交换，说明已经有序
        swapped = False
        
        # 内层循环进行相邻元素比较和交换
        # 每次循环后，最大的元素会"冒泡"到末尾
        for j in range(0, n - i - 1):
            # 如果前一个元素大于后一个元素，交换它们
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # 如果没有发生交换，提前结束排序
        if not swapped:
            break
    
    return arr


def bubble_sort_optimized(arr):
    """
    优化的冒泡排序（每次记录最后一次交换位置）
    
    参数:
        arr: 待排序的列表
    返回:
        排序后的新列表（原地修改）
    """
    n = len(arr)
    last_swap_index = n - 1
    
    for i in range(n):
        swapped = False
        current_swap_index = 0
        
        # 只需遍历到最后一次交换的位置
        for j in range(0, last_swap_index):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                current_swap_index = j
        
        last_swap_index = current_swap_index
        
        if not swapped:
            break
    
    return arr


# 测试代码
if __name__ == "__main__":
    # 测试数据
    test_arrays = [
        [64, 34, 25, 12, 22, 11, 90],
        [3, -1, 0, 5, -2],
        [1],
        [],
        [5, 5, 5, 1],
        [9, 8, 7, 6, 5, 4, 3, 2, 1],  # 逆序数组
    ]
    
    print("=" * 50)
    print("冒泡排序算法测试")
    print("=" * 50)
    
    for i, arr in enumerate(test_arrays, 1):
        print(f"\n测试 {i}:")
        print(f"原始数组: {arr}")
        
        # 使用标准冒泡排序
        arr_copy = arr.copy()
        sorted_arr = bubble_sort(arr_copy)
        print(f"排序结果: {sorted_arr}")
        
        # 使用优化版本
        arr_opt = arr.copy()
        bubble_sort_optimized(arr_opt)
        print(f"优化版本: {arr_opt}")
        
        # 验证排序正确性
        assert sorted_arr == sorted(arr), "排序结果不正确！"
        assert arr_opt == sorted(arr), "优化版本结果不正确！"
    
    print("\n" + "=" * 50)
    print("所有测试通过！✓")
    print("=" * 50)