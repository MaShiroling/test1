def shell_sort(arr):
    """
    希尔排序算法实现
    
    原理：改进的插入排序，使用间隔（gap）对数据进行分组排序
    
    参数:
        arr: 待排序的列表
    返回:
        排序后的列表（原地修改）
    """
    n = len(arr)
    # 初始间隔从 n//2 开始，然后逐渐缩小
    gap = n // 2
    
    while gap > 0:
        # 对每个间隔组进行插入排序
        for i in range(gap, n):
            temp = arr[i]
            j = i
            
            # 插入排序的逻辑，但步长是 gap
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            
            arr[j] = temp
        
        # 缩小间隔
        gap //= 2
    
    return arr


def shell_sort_sedgewick(arr):
    """
    使用 Sedgewick 序列的希尔排序（更高效）
    
    参数:
        arr: 待排序的列表
    返回:
        排序后的列表（原地修改）
    """
    n = len(arr)
    # Sedgewick 序列
    gaps = []
    k = 0
    while True:
        gap = (4 ** k + 3 * (2 ** (k - 1)) + 12) if k > 0 else 1
        if gap > n:
            break
        gaps.insert(0, gap)
        k += 1
    
    # 对每个间隔进行排序
    for gap in gaps:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
    
    return arr


# 测试代码
if __name__ == "__main__":
    test_arrays = [
        [64, 34, 25, 12, 22, 11, 90],
        [3, -1, 0, 5, -2],
        [1],
        [],
        [5, 5, 5, 1],
        [99, 88, 77, 66, 55, 44, 33, 22, 11],
    ]
    
    print("=" * 50)
    print("希尔排序算法测试")
    print("=" * 50)
    
    for i, arr in enumerate(test_arrays, 1):
        print(f"\n测试 {i}:")
        print(f"原始数组: {arr}")
        
        # 标准希尔排序
        arr_copy = arr.copy()
        shell_sort(arr_copy)
        print(f"排序结果: {arr_copy}")
        
        # Sedgewick 优化版本
        arr_sedgewick = arr.copy()
        shell_sort_sedgewick(arr_sedgewick)
        print(f"Sedgewick: {arr_sedgewick}")
        
        # 验证
        assert arr_copy == sorted(arr), "标准版本不正确！"
        assert arr_sedgewick == sorted(arr), "Sedgewick 版本不正确！"
    
    print("\n" + "=" * 50)
    print("所有测试通过！✓")
    print("=" * 50)