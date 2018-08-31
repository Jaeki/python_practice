import re

#1
string = 'Earch is the third planet from the Sun'
rs = re.findall(r'\b\w{2}', string)
print(rs)

#2
string = 'abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhd.com, first.test@rest.biz'
rs = re.findall(r'@\w+[.]com', string)
print(rs)

#3
string = 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009'
rs = re.findall(r'\d{2}-\d{2}-\d{4}', string)
print(rs)

#4
string = "Earth's gravity interacts with other objects in space, especially the Sun and the Moon"
rs = re.findall(r'\b[aeiou]\w+', string, re.I)
print(rs)

#5
lst = ['010-256-1354', '010-1234-5576', '070-642-0384', '010-290*-4858', '0105734123']
for num in lst:
    if(re.match(r'010-\d{3,4}-\d{4}', num)):
        print(num, 'YES')
    else:
        print(num, 'NO')