import collections
import bisect

Student = collections.namedtuple('Student', ('name', 'grade_point_average'))

def comp_gpa(student):
    return (-student.grade_point_average, student.name)

def search_student(students, target, comp_gpa):
    i = bisect.bisect_left([comp_gpa(s) for s in students], comp_gpa(target))
    return (0<=i<len(students)) and (students[i]==target)

Bob = Student(name='Bob', grade_point_average=3.91)
Jane = Student(name='Jane', grade_point_average=3.4)
Jean = Student(name='Jean', grade_point_average=3.4)
Mary = Student(name='Mary', grade_point_average=3.62)
Rose = Student(name='Rose', grade_point_average=3.13)

s = [Bob, Mary, Jean, Jane, Rose]
print(search_student(s, Bob, comp_gpa))
print(comp_gpa(Bob))
print(search_student(s, Jean, comp_gpa))
print(comp_gpa(Jean))
print(search_student(s, Jane, comp_gpa))
print(comp_gpa(Jane))
print(search_student(s, Mary, comp_gpa))
print(comp_gpa(Mary))
print(search_student(s, Rose, comp_gpa))
print(comp_gpa(Rose))