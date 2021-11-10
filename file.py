class customer:
    baknkname = 'SBI'
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    def deposite(self,amount):
        self.balance = self.balance+amount
        print('after deposite balance',self.balance)
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance = self.balance-amount
            print('amount withdwawn',self.balance) 
        else:
            print('insufficient balance')
    def display(self):
        print('available balance',self.balance)
    def store (self):    
        write1=open('demo.txt','a')
        write1.writelines(str(i))
        write1.writelines('\n')

x = open('demo.txt',mode='r')
for i in x.readlines():
    i = eval(i)
name = input('enter your name')
pass1 = input('enter your password')
if i['name'] in name and i['password'] in pass1:
    print('welcome to bank')
    c = customer('name')
    while True:
        s =input('press 1 for deposit/2 for withdraw/3 for check balance/4 for quit ==')
        if s == '1':
            amount = float(input('enter the amount to deposited'))
            c.deposite(amount)
        elif s == '2':
            amount = float(input('enter amount to withdwarl'))
            c.withdraw(amount)
        elif s == '3':
            c.display()
        elif s == '4':
            print('thanks for visit Bank')
            break
        else:
            print('plese choose correct key')
            continue 
else:
    print('You may enter wrong user_name or password','\n please try again')

   
