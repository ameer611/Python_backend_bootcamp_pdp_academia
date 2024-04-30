import bisect

grades = [20, 40, 65, 85, 100]
grade = int(input("Enter a grade: "))
numbers = "12345"
test = bisect.bisect_left(grades, grade)
print(numbers[test])