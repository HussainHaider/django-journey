courses = ['history', 'math', 'physics']
courses_2 = ['MM', 'SQA']
courses.append('Arts')

courses.insert(0, 'SPM')
courses.extend(courses_2)

courses.remove('math')

popped = courses.pop()
print(popped)

print(courses)
print(len(courses))
print(courses[0])
print(courses[-1])
print(courses[0:2])

courses.sort()
print(courses)

courses.reverse()
print(courses)

#following function don't change the original array.
sorted_courses = sorted(courses)
print(sorted_courses)

print(min(courses))
print(max(courses))

print(courses.index('Arts'))

print('math' in courses)

for item in courses:
    print(item)

letters = ["a", "b", "c", "d"]     
first, second, *other = letters 
print(first, second, other)

tuple_1 = ('history', 'math', 'physics')
tuple_2 = tuple_1

print(tuple_1, tuple_2)

cs_courses = {'history', 'math', 'physics', 'math'}
arts_courses = {'history', 'math', 'Art', 'Design'}

print('math' in cs_courses)
print(cs_courses.intersection(arts_courses))
print(cs_courses.difference(arts_courses))
print(cs_courses.union(arts_courses))