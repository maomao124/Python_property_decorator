"""
 * Project name(项目名称)：Python_property装饰器
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/26 
 * Time(创建时间)： 22:07
 * Version(版本): 1.0
 * Description(描述)：
 既要保护类的封装特性，又要让开发者可以使用“对象.属性”的方式操作操作类属性，
 除了使用 property() 函数，Python 还提供了 @property 装饰器。通过 @property 装饰器，
 可以直接通过方法名来访问方法，不需要在方法名后添加一对“（）”小括号。
 @property
def 方法名(self)
    代码块

 """


class Rect:
    def __init__(self, area):
        self.__area = area

    @property
    def area(self):
        print("@property")
        return self.__area


if __name__ == '__main__':
    rect = Rect(45)
    # 直接通过方法名来访问 area 方法
    print("矩形的面积是：", rect.area)
    # 不允许
    # rect.area = 38
    # print("修改后的面积：", rect.area)
