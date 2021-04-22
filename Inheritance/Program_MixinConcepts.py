"""You apply the mixin to the Address class to support the feature. Now, you can write a small program to test it:"""
import json
from Employee_Composition import EmployeeDatabase


def print_dict(d):
    print(json.dumps(d, indent=2))


for employee in EmployeeDatabase().employees:
    print_dict(employee.to_dict())

