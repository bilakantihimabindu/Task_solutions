from read_write_Employee_records import *
ename="Nord"
edept="Windows"

print("\n*******************************List of employee*******************************\n")
read_employee_details()
print("\n*******************************Adding employee*******************************\n")
write_employee_details(ename,edept)
print("\n*******************************Updated employee list*******************************\n")
read_employee_details()
