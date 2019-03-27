#  学习Python的第二天

看官方的中文文档啊， 英语菜鸡  哎～～


###看到这定制模块的时候很有意思啊
`Python 为你提供两个钩子 (hook) 来定制交互环境: sitecustomize 和 usercustomize. 要知道它如何工作, 你需要先找到你的 user site-package 目录的位置. 打开 Python 并运行这段代码:`
```
>>> import site
>>> 
>>> 
>>> site.getusersitepackages()
'/home/bo/.local/lib/python3.6/site-packages'
>>> 
```
`现在你可以在那个目录下创建一个名为 usercustomize.py 的文件, 并在里面放置任何你想放的东西. 它将影响到每一次 Python 的调用, 除非使用了 -s 选项来禁用了自动导入功能.
sitecustomize 以同样的方式工作, 但通常由该计算机的管理员在全局 site-packages 目录下创建, 并且在 usercustomize 之前被导入. 参看 site 模块的文档获取更多细节.`

这是我的 usercustomize.py 文件

```
bo@bo-PC:~/.local/lib/python3.6/site-packages$ cat usercustomize.py 
#!/usr/bin/python3

print('i am first import')
bo@bo-PC:~/.local/lib/python3.6/site-packages$ 
```

然后在自己写一个test.py   运行一下
```
bo@bo-PC:~/python3_test$ vi test.py 
bo@bo-PC:~/python3_test$ 
bo@bo-PC:~/python3_test$ 
bo@bo-PC:~/python3_test$ 
bo@bo-PC:~/python3_test$ cat test.py 
#!/usr/bin/python3


print('i am test py')
bo@bo-PC:~/python3_test$ python3 test.py 
i am first import
i am test py
bo@bo-PC:~/python3_test$ 

```


#简直是惊喜啊


接着看了 ～～




## 3. 非正式介绍Python

这部分确实是非正式介绍了，随便介绍了python的数值，变量，简单的字符串操作什么的，然后切片，列表啥的。。。学过go的来说 还是能理解的

#### 唯一记得的是   
# Python居然可以对小数取余

```
>>> 
>>> 
>>> 25.5 % 2.25
0.75
>>> -1.5 % 2.25
0.75
>>> 15 % 2.25
1.5
>>> 

```

`那么对小数取余  使用在哪的？`




不行   这样学习太慢了。。   之后还是看到亮点怕忘了的时候。在记录下来吧

#### 或者记录下自己看到哪里了    好好激励自己  懒得不行啊