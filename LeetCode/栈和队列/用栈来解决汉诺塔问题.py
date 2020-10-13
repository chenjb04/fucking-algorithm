"""
题目描述
有一个整型数组arr和一个大小为w的窗口从数组的最左边滑到最右边，窗口每次向右边滑一个位置，求每一种窗口状态下的最大值。（如果数组长度为n，窗口大小为w，则一共产生n-w+1个窗口的最大值）
输入描述:
第一行输入n和w，分别代表数组长度和窗口大小
第二行输入n个整数X_iX 
i
​   
 ，表示数组中的各个元素
输出描述:
输出一个长度为n-w+1的数组res，res[i]表示每一种窗口状态下的最大值
示例1
输入
复制
8 3
4 3 5 4 3 3 6 7
输出
复制
5 5 5 4 6 7
说明
例如，数组为[4，3，5，4，3，3，6，7]，窗口大小为3时：

[4 3 5] 4 3 3 6 7        窗口中最大值为5

4 [3 5 4] 3 3 6 7        窗口中最大值为5

4 3 [5 4 3] 3 6 7        窗口中最大值为5

4 3 5 [4 3 3] 6 7        窗口中最大值为4

4 3 5 4 [3 3 6] 7        窗口中最大值为6

4 3 5 4 3 [3 6 7]        窗口中最大值为7

输出的结果为{5 5 5 4 6 7}
"""


"""
解题思路：
    使用双端队列，双端队列中存放数组的下标
    遍历数组，放入规则：
        如果deque为空，直接把i放入deque
        如果deque不为空，取出队尾元素记为j
            如果arr[j] > arr[i],把i添加到deque的队尾
            如果arr[i] >= arr[j],把j弹出，继续deque放入
    弹出规则：
        如果deque队头的下标等于i-w，说明deque的队头下标过期，弹出队头下标
        
"""
class GetMaxWindow:
    def __init__(self, nums, size):
        self.nums = nums
        self.size = size
        self.deque = []
        
    def get_max_window(self):
        if self.nums == None or len(self.nums) < 1 or len(self.nums) < self.size:
            return

        res = []
        # 如果队列为空或者队尾所对应的元素大于arr[i] 压入队列，否则pop
        for i in range(len(self.nums)):

            while len(self.deque) != 0 and self.nums[self.deque[-1]] <= self.nums[i]:
                self.deque.pop()
            self.deque.append(i)
            # 判断队头元素是否等于i - w，如果是的话说明此时队头已经不在当前窗口的范围内，删去
            if self.deque[0] == i - self.size:
                self.deque.pop(0)
            if i >= self.size - 1:
                res.append(self.nums[self.deque[0]])
        return res

    
if __name__ == '__main__':
    nums = [4,3, 5, 4, 3, 3, 6, 7]
    size = 3
    get_max = GetMaxWindow(nums, size)
    print(get_max.get_max_window())