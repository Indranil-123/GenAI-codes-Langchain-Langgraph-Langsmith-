from pydantic import BaseModel, Field
from typing import List, Optional

class Student(BaseModel):
    name: str
    age: Optional[int] = None
    
new_student = {'name': 'Bob'}
student = Student(**new_student)
print(type(student))
print(student)
    