bitbucket.org
github.com
launchpad.net
koders.com

### Installing Python Packages
1. pip from http://pypi.python.org/pypi/pip
2. distribute from http://pypi.python.org/pypi/distribute
3. nose from http://pypi.python.org/pypi/nose/
4. virtualenv from http://pypi.python.org/pypi/virtualenv

[python_liaoxuefeng](http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000)

ANACONDA  OPEN DATA SCIENCE PLATFORM ACCELERATE. CONNECT. EMPOWER.  https://www.continuum.io/
pip	      The PyPA recommended tool for installing Python packages. https://pypi.python.org/pypi/pip	

- [python2 standard library](https://docs.python.org/2/library/) 	
- [python3 standard library](https://docs.python.org/3/library/)
- [pypi](https://pypi.python.org/pypi)
- [3rd-party library](https://pypi.python.org/pypi?%3Aaction=browse)

1. __all__
2. __all__.extend()
3. __all__.append()
2. from xxx import xxx
3. import xxx as xxx
4. xxx.module[]

```
x = [1, 2, 3]
x.append([4, 5])
print (x)
gives you: [1, 2, 3, [4, 5]]

extend: Extends list by appending elements from the iterable.

x = [1, 2, 3]
x.extend([4, 5])
print (x)
gives you: [1, 2, 3, 4, 5]
```

更多的是一种规范吧，如下（摘自http://www.cnblogs.com/yaksea/archive/2011/08/30/2159416.html）：
1. _单下划线开头：弱“内部使用”标识，如：”from M import *”，将不导入所有以下划线开头的对象，包括包、模块、成员

2. 单下划线结尾_：只是为了避免与python关键字的命名冲突

3. __双下划线开头：模块内的成员，表示私有成员，外部无法直接调用

4. 双下划线开头双下划线结尾：指那些包含在用户无法控制的命名空间中的“魔术”对象或属性，如类成员的name 、doc、init、import、file、等。推荐永远不要将这样的命名方式应用于自己的变量或函数。

- classmethod：类方法
- staticmethod：静态方法
在python中，静态方法和类方法都是可以通过类对象和类对象实例访问。但是区别是：
  - @classmethod
    是一个函数修饰符，它表示接下来的是一个类方法，而对于平常我们见到的则叫做实例方法。 类方法的第一个参数cls，而实例方法的第一个参数是self，表示该类的一个实例。 
    普通对象方法至少需要一个self参数，代表类对象实例
    类方法有类变量cls传入，从而可以用cls做一些相关的处理。并且有子类继承时，调用该类方法时，传入的类变量cls是子类，而非父类。 对于类方法，可以通过类来调用，就像C.f()，有点类似C＋＋中的静态方法, 也可以通过类的一个实例来调用，就像C().f()，这里C()，写成这样之后它就是类的一个实例了。 
  - 静态方法则没有，它基本上跟一个全局函数相同，一般来说用的很少

__future__模块，让你在旧的版本中试验新版本的一些特性

当函数的参数不确定时，可以使用*args 和**kwargs，*args 没有key值，**kwargs有key值。

