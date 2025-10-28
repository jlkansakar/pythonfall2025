class bank:
    def __init__(self, chain, location):
        self.chain = chain
        self.location = location
    class account:
        def __init__(self, name, id, balance=None):
            self.name = name
            self.id = id
            self.balance = balance
        class customer:
            def __init__(self, name, age, jobPosition, monthlySalary):
                self.name = name
                self.age = age
                self.jobPosition = jobPosition
                self.monthlySalary = monthlySalary
                
                
albank1 = bank("Arbejdernes Landsbank", "Copenhagen")


acc1 = bank.account("opsparing", 1, 25000)

customer1 = bank.account.customer("Jonathan", 24, "Intern", 10000)
print(albank1.__dict__)
print(acc1.__dict__)
print(customer1.__dict__)


class bankProper:
    def __init__(self, chain, location):
        self.chain = chain
        self.location = location
        self.account1 = accountProper()

class accountProper:
    def __init__(self, name, accid, balance):
        self.name = name
        self.id = accid
        self.balance = balance
        
class customerProper:
    def __init__(self, name, age, jobPosition, salary):
        self.name = name
        self.age = age
        self.position = jobPosition
        self.salary = salary
        