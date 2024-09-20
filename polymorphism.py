class User:
    name = "Kris"
    email = "kriszha@gmail.com"
    password = "admin123"

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if entry_email == self.email and entry_password == self.password:
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The password or email is incorrect.")

class Employee(User):
    base_pay = 4.00
    department = "Division 4"
    pin_number = "0421"

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_pin = input("Enter your pin: ")
        if entry_email == self.email and entry_pin == self.pin_number:
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The pin or email is incorrect")

customer = User()
customer.getLoginInfo()

manager = Employee()
manager.getLoginInfo()
