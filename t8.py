class Employee:
    def __init__(self, firstName, lastName, salary):
        self.firstName = firstName
        self.lastName = lastName
        self.salary = salary

    def calTax(self):
        if self.salary <= 3000000:
            return 0
        elif 3000000 < self.salary < 5000000:
            return 10 * 3000000 / 100
        else:
            return 20 * 3000000 / 100

    def calInsurance(self):
        return 10 * self.salary / 100
        
    def Pay(self):
        ans = self.salary - (self.calInsurance() + self.calTax())
        print(ans)
        
emp1 = Employee('firstName',' fookin lastName', 3100000)
        
emp1.Pay()
