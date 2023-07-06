```
题目描述
给定一个由纯数字组成以字符串表示的数值，现要求字符串中的每个数字最多只能出现2次，超过的需要进行删除；

删除某个重复的数字后，其它数字相对位置保持不变。

如”34533″，数字3重复超过2次，需要删除其中一个3，删除第一个3后获得最大数值”4533″

请返回经过删除操作后的最大的数值，以字符串表示。

输入描述
第一行为一个纯数字组成的字符串，长度范围：[1,100000]

输出描述
输出经过删除操作后的最大的数值

用例
输入
34533
输出
4533
```
# memo
- according to question, we need to remove digits which frequency is bigger than 2, so removing current digit when later digit is bigger than it, which can make number becomes bigger.
- keeping digits which frequency is smaller or equal to 2, because this way will make the value of number at least 10 times than the value of number removed any digit.
