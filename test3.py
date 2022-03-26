"""
 * Project name(项目名称)：Python_property装饰器
 * Package(包名): 
 * File(文件名): test3
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/26 
 * Time(创建时间)： 22:13
 * Version(版本): 1.0
 * Description(描述)： 还可以使用 deleter 装饰器来删除指定属性
 @方法名.deleter
def 方法名(self):
    代码块
 """


class Rect:
    def __init__(self, area):
        self.__area = area

    @property
    def area(self):
        print("@property")
        return self.__area

    @area.setter
    def area(self, value):
        print("@area.setter")
        self.__area = value

    # @area.deleter
    # def area(self):
    #     print("@area.deleter")
    #     del self.__area

    @area.deleter
    def area(self):
        print("@area.deleter")
        # del self.__area
        self.__area = -1


if __name__ == '__main__':
    rect = Rect(45)
    # 直接通过方法名来访问 area 方法
    print("矩形的面积是：", rect.area)
    rect.area = 38
    print("修改后的面积：", rect.area)
    del rect.area
    print(rect.area)
