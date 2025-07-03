class Employee:

  company="ITC"
  salary=1200000
  def show(self):
    print(f"The name of the employee is {self.company} and the salary  is {self.salary}")

class coder:
  language="python"
  def printlang(self):
    print(f"The name of the language is {self.language}")


class programmer(Employee,coder):
  company="ITC infotech"

  def showlang(self):
    
    print(f"The name is {self.company} and the langage is    {self.language}")



a=Employee()
b=programmer()
b.show()
b.printlang()
b.showlang()


