import random

# Q: 找到一个长度为 N 的乱序数组中第 K 大元素的
# 使用快速选择算法,最优时间复杂度是 O(N)
def quickSelect(nums, k):
    def partition(left, right, pivotIndex):
        pivotValue = nums[pivotIndex]
        nums[pivotIndex], nums[right] = nums[right], nums[pivotIndex]  # 将枢轴移动到末尾
        storeIndex = left
        for i in range(left, right):
            if nums[i] < pivotValue:
                nums[storeIndex], nums[i] = nums[i], nums[storeIndex]
                storeIndex += 1
                print(nums)
        nums[right], nums[storeIndex] = nums[storeIndex], nums[right]  # 将枢轴移动到正确的位置
        print()
        return storeIndex

    # 递归选择函数
    def select(left, right, k_smallest):
        if left == right:  # 如果只剩下一个元素
            return nums[left]

        pivotIndex = random.randint(left, right)     # 选择随机枢轴
        pivotIndex = partition(left, right, pivotIndex)

        if k_smallest == pivotIndex:
            print('found')
            return nums[k_smallest]
        elif k_smallest < pivotIndex:
            print('<')
            return select(left, pivotIndex - 1, k_smallest)
        else:
            print('>')
            return select(pivotIndex + 1, right, k_smallest)

    n = len(nums)
    print(n)
    return select(0, n - 1, n - k)  # tips： n-k+1 小的元素等价于第 k 大的元素,n-k 是index

# 示例
nums = [3, 2, 1, 5, 6, 4]
k = 2
kth_largest = quickSelect(nums, k)
print(f"第 {k} 大的元素是: {kth_largest}")  # 输出: 第 2 大的元素是: 5