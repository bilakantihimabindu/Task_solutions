import copy
class Employee:
    def __init__(self, name, age, salary,email_id):
        self.name=name
        self.age=age
        self.salary=salary
        self.email_id=email_id
    def modify_content(self,name,email_id):
        self.name=name
        self.email_id=email_id
    def _str_(self):
        return 'Name:'+self.name+", age:"+str(self.age)+", salary:"+str(self.salary)+", email_id:"+self.email_id
    
E1=Employee("Ben",24,40000,"ben@gmail.com")

E2=copy.copy(E1)
E2.modify_content("TestName","Test.Name@emailid.com")

print("Employee details:\n "+E1._str_())
print("Modified Employee details:\n "+E2._str_())



   
