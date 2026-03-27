def quick_sort(arr):
    """
    快速排序算法实现
    
    参数:
        arr: 待排序的列表
    返回:
        排序后的新列表
    """
    # 基本情况：如果列表长度小于等于1，直接返回
    if len(arr) <= 1:
        return arr
    
    # 选择基准值（这里选择中间元素）
    pivot = arr[len(arr) // 2]
    
    # 将列表分为三部分
    left = [x for x in arr if x < pivot]      # 小于基准值的元素
    middle = [x for x in arr if x == pivot]   # 等于基准值的元素
    right = [x for x in arr if x > pivot]     # 大于基准值的元素
    
    # 递归排序并合并结果
    return quick_sort(left) + middle + quick_sort(right)


def quick_sort_inplace(arr, low=0, high=None):
    """
    原地快速排序实现（不创建新列表，节省内存）
    
    参数:
        arr: 待排序的列表
        low: 起始索引
        high: 结束索引
    """
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        # 分区操作，获取基准值的最终位置
        pivot_index = partition(arr, low, high)
        
        # 递归排序左右两部分
        quick_sort_inplace(arr, low, pivot_index - 1)
        quick_sort_inplace(arr, pivot_index + 1, high)
    
    return arr


def partition(arr, low, high):
    """
    分区函数：将数组分为两部分，左边小于基准值，右边大于基准值
    
    参数:
        arr: 待分区的列表
        low: 起始索引
        high: 结束索引
    返回:
        基准值的最终位置
    """
    # 选择最右边的元素作为基准值
    pivot = arr[high]
    
    # i 指向小于基准值的区域的最后一个元素
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # 将基准值放到正确的位置
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    
    return i + 1


# 测试代码
if __name__ == "__main__":
    # 测试数据
    test_arrays = [
        [64, 34, 25, 12, 22, 11, 90],
        [3, -1, 0, 5, -2],
        [1],
        [],
        [5, 5, 5, 1],
    ]
    
    print("=" * 50)
    print("快速排序算法测试")
    print("=" * 50)
    
    for i, arr in enumerate(test_arrays, 1):
        print(f"\n测试 {i}:")
        print(f"原始数组: {arr}")
        
        # 使用非原地排序
        sorted_arr = quick_sort(arr.copy())
        print(f"排序结果: {sorted_arr}")
        
        # 使用原地排序
        arr_inplace = arr.copy()
        quick_sort_inplace(arr_inplace)
        print(f"原地排序: {arr_inplace}")
        
        # 验证排序正确性
        assert sorted_arr == sorted(arr), "排序结果不正确！"
        assert arr_inplace == sorted(arr), "原地排序结果不正确！"
    
    print("\n" + "=" * 50)
    print("所有测试通过！✓")
    print("=" * 50)
