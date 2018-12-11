Course_list = []


class School(object):

    def __init__(self, school_name):
        self.school_name = school_name
        self.students_list = []
        self.teachers_list = []

        global Course_list

    def hire(self, obj):
        self.teachers_list.append(obj.name)
        print("我们现在聘请了一个新老师{}".format(obj.name))

    def enroll(self, obj):
        self.students_list.append(obj.name)
        print("注册了一位新学员{}".format(obj.name))


class Grade(School):
    def __init__(self, school_name, grade_code, grade_course):
        super(Grade, self).__init__(school_name)
        self.code = grade_code
        self.course = grade_course
        self.members = []
        Course_list.append(self.course)

        print("我们现在有了 {0} 的第 {1} 期的 {2}".format(self.school_name, self.code, self.course))

    def course_info(self):
        print("课程大纲{0}是day01,day02,day03".format(self.course))


Python = Grade("BJ", 3, "Python")
Linux = Grade("CD", 1, "Linux")


class School_member(object):
    def __init__(self, name, age, sex, role):
        self.name = name
        self.age = age
        self.sex = sex
        self.role = role
        self.course_list = []

        print("我叫{},我是一个{}".format(self.name, self.role))


stu_num_id = 00


class Students(School_member):
    def __init__(self, name, age, sex, role, course):
        super(Students, self).__init__(name, age, sex, role)
        global stu_num_id
        stu_num_id += 1

        # zfill 填充，当只有一位数时，前面用0 填充，只能对str类型操作
        stu_id = course.school_name + "S" + str(course.code) + str(stu_num_id).zfill(2)

        self.id = stu_id
        self.mark_list = {}

        def study(self, course):
            print("我来这里学习{}课，我的学号是{}".format(course.course, self.id))

        def pay(self, course):
            print("我叫了1000块给{}".fromat(course.course))
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
        super(Teacher, self).__init__(name, age, sex, role)

        global tea_num_id

        tea_num_id += 1
        tea_id = course.school_name + "T" + str(course.code) + str(tea_num_id).zfill(2)

    def teach(self, course):
        print("我来这里讲{}门课了".format(coures.course, self.id))

    def record_mark(self, Date, course, obj, level):
        obj.mark_list['Date' + Date] = level


A = Students("小张", 18, "M", "student", "Python")
Python.enroll(A)

