class Calculator:
    def __init__(self): 
        self.x = 0
        self.y = 0

    def get_numbers(self):
        self.x = float(input('Enter the first number please: '))
        self.y = float(input('Now, the second number: '))

    def add(self):
        return self.x + self.y
    def subs(self):
        return self.x - self.y 
    def multiply(self):
        return self.x * self.y
    def divide(self):
        if self.y !=0:
            return self.x / self.y
        else: 
            return ' Error! Division by zero !! '

    def run(self): 
        while True: 
            print(' Type in 1 for addition ')
            print(' Type in 2 for substraction ')
            print(' Type in 3 for multi plication ')
            print(' Type in 4 for division ')
            print(' Type in 5 to quit ')

            choice = input(' Select your option. ')
            
            if choice == '5': 
                break

            self.get_numbers() 
            
            if choice == '1':
                print(' Answer ', self.add()) 
            elif choice == '2':
                print(' Answer ', self.subs()) 
            elif choice == '3':
                print(' Answer ', self.multiply()) 
            elif choice == '4':
                print(' Answer ', self.divide()) 
            elif ValueError: 
                print(' That\'s not a number esse! ') 


bb = Calculator()
bb.run() 



    
