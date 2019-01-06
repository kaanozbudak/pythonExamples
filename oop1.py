# python oop examples
# class Employee:
#    pass
# emp_1 = Employee()
# emp_2 = Employee()
#
# print(emp_1)
# print(emp_2)  # you will see they are different 2 objects
#
# emp_1.firstName = "Kaan"
# emp_1.lastName = "Ozbudak"
# emp_1.email = "kaanozbudak@hotmail.com"
# emp_1.pay = 50000
#
# e#mp_2.firstName = "Melih"
# emp_2.lastName = "Can"
# emp_2.email = "kadirmelihcan@hotmail.com"
# emp_2.pay = 40000
#
# print(emp_1.email)
# print(emp_2.pay)

# it was not good way because just imagine you need to add 1000 employee to your system

class Employee:
    raise_amount = 1.05
    num_of_emp = 00

    def __init__(self, first_name, last_name, price):
        self.first_name = first_name
        self.last_name = last_name
        self.price = price
        Employee.num_of_emp += 1

    @property
    def email(self):
        if self.first_name is not None and self.last_name is not  None:
            return '{}.{}@company.com'.format(self.first_name.lower(), self.last_name.lower())
        else:
            return 'full name deleted'

    @property
    def full_name(self):
        if self.first_name != None and self.last_name != None:
            return '{} {}'.format(self.first_name, self.last_name)
        else:
            return 'full name deleted'

    @full_name.setter
    def full_name(self, name):
        first_name, last_name = name.split(' ')
        self.first_name = first_name
        self.last_name = last_name

    @full_name.deleter
    def full_name(self):
        print('Delete Name !')
        self.first_name = None
        self.last_name = None

    def apply_raise(self):
        self.price = int(self.price * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first_name, last_name, price = emp_str.split('-')
        return cls(first_name, last_name, int(price))

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first_name, self.last_name, self.price)

    def __str__(self):
        return '{} --> {}'.format(self.full_name, self.email)

    def __add__(self, other):
        return self.price + other.price

    def __len__(self):
        return len(self.full_name)


emp_1 = Employee("Kaan", "Ozbudak", 50000)  # we give values to object when we created
emp_2 = Employee("Samet", "Adilak", 60000)
emp_3_str = 'John-Doe-70000'
first_name, last_name, price = emp_3_str.split('-')
emp_3 = Employee(first_name, last_name, price)

# print(emp_1.last_name)
# print(emp_1.email)
# #  change the price with using methods
# print(emp_1.price)
# emp_1.apply_raise()
# print(emp_1.price)
#
# #  get full name
# # print('{} {}'.format(emp_1.first_name, emp_1.last_name))
# print(emp_1.full_name())      # we don't have to pass argue because it takes by self
# print(Employee.full_name(emp_1))  # we need to give value
#
# print(emp_1.__dict__)
#
# print(type((emp_1.__dict__)))
#
# print(Employee.__dict__)
# emp_1.raise_amount = 1.5
# print(emp_1.raise_amount)
# print(Employee.raise_amount)
# print(emp_1.price)
# emp_1.apply_raise()
# print(emp_1.price)
# print(Employee.num_of_emps)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
#
# emp_1.set_raise_amt(1.5)
# print("-------------------")
#
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# print(emp_3.__dict__)
# emp_3.apply_raise()
# print(emp_3.price)
#
# emp_3 = Employee.from_string(emp_3_str)
#
# print(emp_3.__dict__)

class Developer(Employee):
    def __init__(self, first_name, last_name, price, soft_lang):
        super().__init__(first_name, last_name, price)
        self.soft_lang = soft_lang

class Manager(Employee):
    def __init__(self, first_name, last_name, price, employees_list=None):
        super().__init__(first_name,last_name,price)
        if employees_list is None:
            self.employees_list = []
        else:
            self.employees_list = employees_list

    def add_emp(self, emp):
        if emp not in self.employees_list:
            self.employees_list.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees_list:
            self.employees_list.remove(emp)

    def print_employees(self):
        for emp in self.employees_list:
            print('-->', emp.full_name())


dev_1 = Developer('Kaan', 'Ozbudak', 90000, 'Python')
dev_2 = Developer('Eray', 'Surmeli', 80000, 'Java')

# print(dev_1.__dict__)
#
# print(help(Developer))

# print(dev_1.price)
dev_1.set_raise_amt(2.0)
dev_1.apply_raise()
# print(dev_1.price)
#
# print(dev_2.soft_lang)

mng_1 = Manager('Kaan', 'Ozbudak', 150000)

mng_1.add_emp(dev_1)
mng_1.add_emp(dev_2)
mng_1.add_emp(emp_1)
mng_1.remove_emp(emp_1)
# mng_1.print_employees()

# print(isinstance(mng_1, Developer))
# print(isinstance(mng_1, Employee))
# print(issubclass(Developer, Employee))
# print(issubclass(Developer, Manager))

# print(dev_1 + dev_2)

print(len(mng_1))
emp_1.first_name = 'Yunus'
print(emp_1.full_name)
print(emp_1.email)


emp_1.full_name = 'Eto Acar'
print(emp_1.full_name)
print(emp_1.email)

del emp_1.full_name

print(emp_1.full_name)
print(emp_1.email)