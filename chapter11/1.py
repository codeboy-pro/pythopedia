class Employee:
  name="Pradip"
  lang="njqdj"
  company="ITC"
  def show(self):
    print(f"The name of the employee is {self.company} and the salary  is {self.salary}")



class programmer(Employee):
  def showlang(self):
    
    print(f"The name is {self.name} and the langage is{self.lang}")



a=Employee()
b=programmer()
print(a.company,b.showlang())

