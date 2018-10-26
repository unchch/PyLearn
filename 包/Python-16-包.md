# 1. 模块
- 一个模块就是一个包含python代码的文件，后缀名是.py，模块就是个python文件
- 为什么要用模块
  - 程序太大，编写维护不方便，需要拆分
  - 模块可以增加代码重复利用的方式
  - 当做命名空间使用，避免命名冲突
- 如何定义模块
  - 模块就是一个普通文件，所以任何代码可以直接写
  - 不过根据模块的规范，最好在模块中编写以下内容：
    - 函数（单一功能）
    - 类（相似功能的组合，或者类似业务模块）
    - 测试代码
- 如何使用模块
  - 直接导入模块
  - 加入模块名称直接以数字开头，需要借助importlib帮助
  - 语法：
 
        import module_name
        module_name.function_name
        module_name.class_name
        
  - import 模块 as 别名
    - 导入的同时给模块起了一个别名
    - 其余用法跟第一种相同
   
  - from 模块 import func_name, class_name
    - 按上述方法有选择性的导入
    - 使用的售后直接使用，不需要前缀
   
  - from 模块 import *
    - 导入模块所有内容
   
- `if __name__ == "main"`  的使用
  - 可以有效避免模块在被导入时被动执行的问题
  - 建议所有的模块以此代码为入口
  
# 2.  模块的搜索路径和目录
- 什么是模块的搜索路径
  - 加载模块的时候，系统会在哪些地方寻找此模块
- 系统默认的模块搜索路径

         import sys
         sys.path 属性可以获取搜索路径
         
- 添加自定义搜索路径

        sys.path.append(dir)
        
- 模块的加载顺序
  1. 搜索内存中已经加载好的
  2. 所有 python 的内置模块
  3. 所有 sys.path 路径  
  
# 3. 包
- 包是一种组织管理代码的方式，包里面存放的是模块
- 用于将模块包含在一起的文件夹就是包
- 自定义包的结构

        |--包
        |--|-- __init__.py 包的标志文件
        |--|-- 模块1
        |--|-- 模块2
        |--|-- 子包（子文件夹）
        |--|--|-- __init___ 包的标志文件
        |--|--|-- 模块1
        |--|--|-- 模块2
        
- 包的导入操作
  - import 包名
    - 直接导入一个包，可以使用__init__.py 中的内容
    - 使用方式是：
    
            包名.func_name
            包名.class_name.func_name()            
    - 此种方式访问的内容是
    
  - import package_name as 别名
    - 具体用法和作用，跟上述一致
    - 注意的是此种方法是默认对 __init__py 内容的导入
    
  - import package.module
    - 规避了对 __init__.py 的导入
    - 导入包中某一个具体的模块
    - 使用方法
    
            package.module.func()
            package.module.class.func()
            package.module.class.var
            
    - import package.module as pm
    
- from ... import 导入
  - from package import module1, module2, ...
  - 此种方法不执行 `__init__.py` 的内容
 
        from pkg01 import p01
        p01.sayHello()
        
   - from package import *
     - 导入当前包 `__init__.py` 文件中所有的函数和类
     - 使用方法
   
        func_name()
        class_name.func()
        class_name.var
        
     - 注意此种方法导入的具体内容
   
- from package.module import *
  - 导入包中指定模块的所有内容
  - 使用方法：
 
         func_name()
         class_name.func_name()
         
  - 在开发环境中经常会用到其他模块，可以在当前包中直接导入其他模块中的内容
  - import 完整的包或者模块的路径
  
- `__all__` 的用法
  - 在使用from package import * 的时候， * 可以导入的内容
  - `__init__.py` 中如果为空，或者没有 `__all__`,那么可以只把`__init__.py` 中的内容导入
  - `__init__.py` 中如果设置了 `__all__`, 那么则按照 `__all__` 中设置的子包或者模块进行导入，不会在载入`__init__.py` 中的其他内容了
  
        __all__=['module01', 'module02', ...]
        
# 4. 命名空间
  - 用于区分不同位置不同功能，单名称相同的函数或者变量的一个特定前缀
  - 作用是防止命名冲突
        
            
 
 
   