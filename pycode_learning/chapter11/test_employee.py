import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """针对Employee类的测试"""

    def setUp(self):
        """创建一个Employee实例，供使用的测试方法使用"""
        self.employee = Employee("Jack", 10000)

    def test_give_default_raise(self):
        """测试默认年薪增加"""
        self.employee.raise_salary()
        self.assertEqual(self.employee.get_salary(), 15000)

    def test_give_custom_raise(self):
        """测试自定义年薪增加"""
        self.employee.raise_salary(1000)
        self.assertEqual(self.employee.get_salary(), 11000)

unittest.main()