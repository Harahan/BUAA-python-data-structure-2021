# week1

**1**【问题描述】小O的期末考试成绩出来了，他想要整理出自己考得最好的科目，向小L炫耀一番，你能帮帮他吗？

【输入形式】一行若干个正整数，表示小W考试科目的成绩，中间用空格分隔。

【输出形式】一行若干个正整数，中间用空格分隔，表示小W成绩最高的科目是哪几科（编号），若有多门科目成绩并列最高，那么从小到大输出这些科目（编号）。

【样例输入】

100 99 98 97 100

【样例输出】

1 5

【样例说明】按照输入顺序，第1门和第5门同为100分，是最高分，故输出“1 5”
【评分标准】全部通过为满分





**2**【问题描述】在线性代数中，n阶单位矩阵，是一个n*n的方形矩阵，其主对角线元素为1，其余元素为0。

![鍥剧墖.png](https://judge-buaa-edu-cn.vpn.buaa.edu.cn:8118/userfiles/image/1536733971034061061.png)

现在请你打印一个n阶单位矩阵。

【输入形式】一行整数n (0 < n <= 10)

【输出形式】输出该n阶单位矩阵，每个元素之间用空格分隔

【样例输入】

3

【样例输出】

1 0 0

0 1 0

0 0 1

【样例说明】输出三阶单位矩阵
【评分标准】全部通过为满分 





**3**【问题描述】L老师觉得最近题目出的太简单了，于是表示自己想要出难题考大家。但是其他人有不同意见，L老师觉得干脆让大家举手表决好了。如果表示同意的人数占所有人数大于等于1/2，那么下一次上机题目将会出现真正手（wan）把（quan）手（zi）教（xue）的题目。每一行输入一个数，输入1表示支持，输入0则表示反对，输入-1则表示所有人都已投票。如果同意人数达到50%，则输出Yes表示票决通过，否则输出No表示未通过。(注意，并未规定人数)

【输入形式】每一行输入一个数（非0即1），输入1表示支持，输入0则表示反对，输入-1则表示所有人都已投票

【输出形式】Yes表示票决通过，否则输出No表示未通过

【样例输入】

1
0
1
0
1
0
1
0
1
-1

【样例输出】

Yes

【样例说明】5个1，4个0，故通过，输出Yes
【评分标准】全部通过即为满分





**4**【问题描述】小 f 听说莎士比亚的总词汇量在 15000 个至 21000个之间，在佩服之余，她也想要知道自己的词汇量如何。小 f 认为，对常用词汇的掌握相对来说更为重要，因此她想请你帮她统计一下，她平时最常使用的词汇是哪些。

【输入形式】

第一行一个正整数 *n*，表示输入的行数。

接下来 *n*行，每行一个字符串，只包含空格和大小写字母，一行内多个单词之间用空格分割。

【输出形式】

第一行一个正整数，表示出现最多次单词的次数。对于一个单词，不论其中字母的大小写如何变化，都视为同一个单词。如 `python`, `PYTHON`, `PyThOn` 只算作一个单词。

接下来若干行字符串，表示出现最多次的单词。如果出现最多次的单词不止一个，则需要根据输入时第一次出现的先后顺序逐行输出。请注意，输出的单词必须全为小写字母（即使输入中为大写）。

【样例输入】

3
use THAT two two
and THAT we should
hear and we speak

【样例输出】

2
that
two
and
we

【样例说明】

出现最多的单词有 4 个，均出现 2 次，因此首先输出2，再依次输出这4个单词 that, two, and, we。

【评分标准】全部通过为满分。





**5**【问题描述】如何判断一个数是否为素数？当输入数据小于等于2的时候，可以直接给出答案，当输入大于2的时候，其实可以用穷举法试出来的哦。依次用n除以2、3、4……直到n的一半（可直接取整），判断是否可以整除。如果期间的任意一个数可以整除n，则说明n不是素数，如果都不能整除，则n是素数。

【输入形式】每次输入一个自然数n，0≤n≤1000

【输出形式】一行，如果n是素数，则输出“Y”，否则输出“N”（注意不包含引号）

【样例输入】13
【样例输出】Y
【样例说明】13是素数，输出Y
【评分标准】全部通过得满分





**6**【问题描述】

给定一组无序整数，找出其中相邻数对中相差最大的数对（可以有多个）。

相邻数是指：在一组无序数据集中，对于其中一个数，比它小的数中与其相差最小的就是它的一个相邻数；比它大的数中与其相差最小的也是它的一个相邻数。

【输入形式】

先从标准输入读入整数的个数（大于等于2，小于等于100），然后在下一行输入这些无序整数（互不相同），各整数间以一个空格分隔。

【输出形式】

将相差最大的相邻数对输出到标准输出上，该数对中小的整数先输出，两整数间以一个空格分隔，第二个整数后跟回车。

若有多个相邻数对满足输出条件，则按照从小到大的顺序分行输出。

【样例输入】

11

137 -20 0 -93 262 27 82 -100 208 -75 158

【样例输出】

-75 -20

27 82

82 137

【样例说明】

输入了11个无序整数，其中-100最小，只有一个相邻数-93，两者相差7；262最大，也只有一个相邻数208，两者相差54；其它整数都有两个相邻数，例如：27的相邻数是0和82，分别相差27和55。所有相邻数对的最大差值为55，分别为-75和-20，27和82，82和137，按照从小到大的顺序分行输出到标准输出。

【评分标准】

该程序要求编程寻找相差最大的相邻数对。





**7**【问题描述】请使用循环结构读入一组整数并存入列表中（整数取值范围从 −100 至 +100，整数的个数不定，大于或等于 1，读入空字符串表示输入结束）。之后首先输出其中的最大值、最小值和输入的第 n/2（取整）个整数，其中 n 表示输入的行数（包括最后一个空字符串）。然后将列表排序，按从大到小的顺序拼接成字符串并输出（两个相邻的整数之间以空格分割）。提示：字符串拼接函数的输入列表只能由字符串构成。

【输入形式】第1行至第n-1行为一个整数（1≤n≤100），第n行为空字符

【输出形式】第一行为已输入整数的最大值；第二行为已输入整数的最小值；第三行为输入的第n/2个整数（直接保留整数，无需四舍五入）；第四行为一行字符串，为从大到小排序后的整数，两个整数之间以空格分割。
【样例输入】

75
-1
-33
99
42



【样例输出】

99
-33
-33
99 75 42 -1 -33

【样例说明】共输入6行（最后一行为空字符），其中最大值为99，最小值为-33，第n/2行取整为第3行，为-33，最后为倒序输出
【评分标准】共10个测试用例，全部通过为满分



