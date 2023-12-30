import os ,sys
from os.path import dirname , join, abspath

print("*"*50)
print(dirname(__file__))
print("*"*50)

sys.path.insert(0, abspath(join(dirname(__file__) , '..')))

from course import course_details

def payment():
    print("this is my payment file")
    
print("*"*50)
course_details.course()
print("*"*50)

print("*"*50)
for i in sys.path:
    print(i)
print("*"*50)