"""
输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

 

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7
 

限制：

0 <= 节点个数 <= 5000
"""


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
前序遍历：根 左 右  [3,9,20,15,7]
中序遍历：左 根 右  [9,3,15,20,7]
由此特点可知：
	1.前序遍历第一个节点一定是root根节点  即 3 为根节点
	2.中序遍历根据根节点可以划分左右子树 [左子树(9) 3 右子树(15,20,7)]
	3.前序遍历划分为 [3 左子树(9) 右子树(20,15,7)]
可以确定3个关系 根节点 左子树根节点 右子树根节点 
递归的处理左子树和右子树

递归分析：
递归参数：根节点索引 pre_root 中序遍历左边界 in_left,中序遍历右边界 in_right
递归终止条件：当in_left > in_right,子树中序遍历为空，说明已经越过叶子节点
递归：
	建立根节点root： 值为前序遍历中索引为pre_root的节点值
	搜索根节点root在中序遍历的索引i： 为了提升搜索效率，使用哈希表 dic 预存储中序遍历的值与索引的映射关系，每次搜索的时间复杂度为 O(1)。
	构建根节点root的左子树和右子树： 通过调用 recur() 方法开启下一层递归。
左子树： 根节点索引为 pre_root + 1 ，中序遍历的左右边界分别为 in_left 和 i - 1。
右子树： 根节点索引为 i - in_left + pre_root + 1（即：根节点索引 + 左子树长度 + 1），中序遍历的左右边界分别为 i + 1 和 in_right。
返回值： 返回 root，含义是当前递归层级建立的根节点 root 为上一递归层级的根节点的左或右子节点


"""
def buildTree(preorder: List[int], inorder: List[int]) -> TreeNode:
	self.dic = {}
    self.po = preorder
    for i in range(len(inorder)):
        self.dic[inorder[i]] = i
    return self.recur(0, 0, len(inorder) - 1)

def recur(self, pre_root, in_left, in_right):
	# 递归终止条件 中序遍历为空
	if in_left > in_right:
		return
	# 根节点
	root = TreeNode(self.po[pre_root])
	# 搜索根节点在中序遍历的索引，划分左右子树
	in_root = self.dic[self.po[pre_root]]
	# 递归左子树
	root.left = self.recur(pre_root + 1, in_left, in_root - 1)
	# 递归右子树
	root.right = self.recur(in_root - in_left + pre_root + 1, in_root + 1, in_right)
	# 返回根节点
	return root