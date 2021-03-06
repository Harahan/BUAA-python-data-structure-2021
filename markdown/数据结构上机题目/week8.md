# week8

**1**【问题描述】

上节课有同学反应二叉树的题目输入太不人性化......所以这次修改了输入格式。

这道题只是练习建树，如果不会的话可以参考下面的提示。



【输入形式】

二叉树仍然用一行字符串表示，空格分隔，包含数字或"None"。依然按照层序排序，但是**作为完全二叉树式的输入，每一层前面的None均不会省略。末尾连续的None可能被省略。**

例如：

![image.png](https://judge-buaa-edu-cn.vpn.buaa.edu.cn:8118/userfiles/image/2020/1604490016328044212.png)

上图所示的二叉树的输入格式为：1 None 2 None None 3，而非 1 None 2 3 None，第三层最前不存在的两个None没有被省略。



【输出形式】

输出**二叉树的最左下方节点**，即root.left.left.....left.val，如果不存在则输出None。


【样例输入】

1 None 2 None None 3

【样例输出】

1
【样例说明】

见上图，根节点（1）的左节点已经不存在，因此其本身即为所求。
【提示】

\1. 对于完全二叉树式的输入列表中，编号为 i 的节点，其左右节点的编号也可以用 i 表示出来。推导这个关系式以找到节点 i 的左右节点。

**2. 这个题目理论上不建树也可以，但是之后的题目可以复用这道题的建树流程。**



**2**【问题描述】

如上题，按照完全二叉树的格式，依次输入一个二叉树每一层的节点。请先建树之后，按照先序遍历输出全部节点的value。

空结点None不用输出。
【输入形式】

同上题，按照层次遍历二叉树的全部节点，空格分隔。
【输出形式】

先序遍历的二叉树节点，空格分隔。
【样例输入】

1 None 3 None None 4 5 None None None None 6 7 8 9
【样例输出】

1 3 4 6 7 5 8 9

【样例说明】

这应该很简单吧，白送分



**3**【问题描述】

给定一棵二叉树，一条路径的数值指的是从根节点到叶子节点的十进制数字表示。保证节点的数值不会超过10。

例如1 -> 3 -> 5 -> 2 这条路径的数值则为1352。请求出该二叉树全部路径的数值之和。
【输入形式】

同上题，二叉树的完全二叉树式的层次遍历。
【输出形式】

一个整数，代表路径数值之和。
【样例输入】

1 2 3 4 None 6 7
【样例输出】

397
【样例说明】

124 + 136 + 137 = 397