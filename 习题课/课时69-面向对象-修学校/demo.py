Course_list = []

class School(object):
    def __init__(self, school_name):
        self.school_name = school_name
        self.students_list = []
        self.teachers_list = []

        global Course_list

    def hire(self, obj):
        self.teachers_list.append(obj.name)
        print("聘请了一个新老师: {}".format(obj.name))

    def enroll(self, obj):
        self.students_list.append(obj.name)
        print("注册了一位新学员: {}".format(obj.name))

class Grade(School):
    def __init__(self, school_name, grade_code, grade_course):
        super().__init__(school_name)
        self.code = grade_code
        self.course = grade_course
        self.members = []
        Course_list.append(self.course)

        print("我们现在有了 {0} 校区第 {1} 期的 {2} 课程".format(self.school_name, self.code, self.course))

    def course_info(self):
        print("课程大纲{0}是day01,day02,day03".format(self.course))


class School_member(object):
    def __init__(self, name, age, sex, role):
        self.name = name
        self.age = age
        self.sex = sex
        self.role = role
        self.course_list = []

        print("我叫{},我今年{}岁,我是{}生,我是一名{}".format(self.name, self.age, self.sex, self.role))


stu_num_id = 00


class Students(School_member):
    def __init__(self, name, age, sex, role, course):
        super().__init__(name, age, sex, role)
        global stu_num_id
        stu_num_id += 1

        # zfill 填充，当只有一位数时，前面用0 填充，只能对str类型操作
        stu_id = course.school_name + "S" + str(course.code) + str(stu_num_id).zfill(2)

        self.id = stu_id
        self.mark_list = {}

    def study(self, course):
        print("我来这里学习{}课，我的学号是{}".format(course.course, self.id))

    def pay(self, course):
        print("我交了1000块给{}".format(course.course))
        self.course_list.append(course.course)

    def zan(self, obj):
        print("{}觉得{}真棒".format(self.name, obj.name))

    def mark_check(self):
        for i in self.mark_list.items():
            print(i)

    def out(self):
        print("我离开了")


tea_num_id = 00


class Teachers(School_member):
    def __init__(self, name, age, sex, role, course):
        super().__init__(name, age, sex, role)
        global tea_num_id
        tea_num_id += 1
        tea_id = course.school_name + "T" + str(course.code) + str(tea_num_id).zfill(2)
        self.id = tea_id

    def teach(self, course):
        print("我来这里讲{}门课了，我的id是{}".format(course.course, self.id))

    def record_mark(self, Date, course, obj, level):
        obj.mark_list['Date' + Date] = level

print("定义校区,年级和课程: ")
Python = Grade("BJ", 3, "Python")
Linux = Grade("CD", 1, "Linux")
print("=" * 30)

print("注册一个学生: ")
a = Students("小张", 18, "M", "student", Python)
Python.enroll(a)
a.study(Python)
a.pay(Python)
print("=" * 30)

print("注册一个学生2: ")
b = Students("小王", 22, "F", "student", Python)
Python.enroll(b)
b.study(Python)
b.pay(Python)

print("=" * 30)

print("注册一个老师: ")
t = Teachers("小周", 30, "M", "teacher", Python)
Python.hire(t)
t.teach(Python)

t.record_mark("1", Python, a, "A")
t.record_mark("1", Python, b, "B")
t.record_mark("2", Python, a, "A")
t.record_mark("2", Python, b, "A")

print(b.course_list)
b.mark_check()
b.out()

print("=" * 30)

print("给好评")
a.zan(t)