# 深入流程控制

和大多数语言一样，if else, for,  while。    continue 和  break 也有 作用不变
只不过
if 
else if 
else 

变成了,  条件后面要加冒号了
if xx: 
elif xx: 
else :

for 和  while   后面可以接 else   

while xx:
	xxx
else:
	xxx

for i in range(1,2):
	xxx
else:
	xxx

range倒是和go差不多  只不过  go  不能直接range(1,5)这样使用


`然后 再是 关键字参数，说白了就是 忘记了函数定义时  忘记了形参的顺序了可以在任意位置传入形参的值（PS:如果我忘了函数定义时形参的名字可咋办）`


然后再是参数列表什么的 。。  后面具体用到在看吧。。。  



# 数据结构

`终于到数据结构了`

有其他语言的基础看起来确实不怎么费劲～～   但是  方法太多看完一遍  啥也没记住啊

# 手动抄一遍吧

元组：`元组同字串都是不可变的: 无法对元组指定项进行赋值 (尽管可通过切片和连接来模拟这个操作). 元组中可以包含可变的对象, 如列表.`

列表：
append, 
extend， 连接两个列表
insert(pos,value),pos = 0 时，代表列表的开头插入，而a.insert(len(a),value), 代表在最末段插入
remove(val),`移除列表中第一个值为 x 的项. 没有符合要求的项时, 会产生一个错误.`
```
def outputlist(ls):
	for l in ls:
		print(l)
	print()


ll = [11, 22, 'cc', [11, 22, 33, 44], [22, 11, 33, 44]]

outputlist(ll)
ll.remove(22)
outputlist(ll)

ll.remove(11)
outputlist(ll)

ll.remove(33)
outputlist(ll)

```

这句话居然理解错了，移除列表中第一个值为x的项，我本以为ll.remove(11),会将`11`和`[11, 22, 33, 44]`都移除出去的，然后结果确是这样的
```
11
22
cc
[11, 22, 33, 44]
[22, 11, 33, 44]

11
cc
[11, 22, 33, 44]
[22, 11, 33, 44]

cc
[11, 22, 33, 44]
[22, 11, 33, 44]

Traceback (most recent call last):
  File "3thlistremove.py", line 16, in <module>
    ll.remove(33)
ValueError: list.remove(x): x not in list

```
### 照这样说remove 是移除不掉 列表里面的列表咯？

pop([i]),`删除列表给定位置的项, 并返回它. 如果没有指定索引, a.pop 移除并返回列表的最后一项. (函式原型的 i 在中方括号中 意味着它是一个可选参数, 而不是你应当在那里键入一个方括号. 你将会在 Python 库参考中经常见到这种表示法.)`



del ll[index]  `这有一种通过给定索引而不是值, 来删除列表中项的方法`


