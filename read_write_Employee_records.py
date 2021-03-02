def read_employee_details():
    with open(r".\Employee_details.txt", encoding="utf-8") as f:
        lines = f.read().splitlines()
        print(lines)
    f.close()

def write_employee_details(empname,dept):
    with open(r".\Employee_details.txt",'a') as f:
        f.write('\n'+empname+','+dept)
        print("Employee entry added successfully")
    f.close()






