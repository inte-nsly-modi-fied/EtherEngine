#Define a class named Calculator
class Calculator:
    # The __init__ method is the constructor. It initializes the attributes x and y. Gives them the values of 0.
    def __init__(self): # Self is used to represent itself and all throughout the class to use methods and variables
        self.x = 0
        self.y = 0

    #This method prompts the user to enter two numbers; One is called first and the other second
    def get_numbers(self):
        self.x = float(input('Enter the first number: '))
        self.y = float(input('Enter the second number: '))

#These methods simply return a value, which is enough for our desired outcome.
    #This method adds the attributes x and y and returns the result.
    def add(self):
        return self.x + self.y
    #This method substracts the attributes x and y and return the result.
    def subs(self):
        return self.x - self.y 
    #This method multiplies the attributes x and y and returns the result.
    def multiply(self):
        return self.x * self.y
    #This method divides the attributes x and y and returns the result.
    def divide(self):
        if self.y !=0:
            return self.x / self.y
        else: #This is a sort of error handling, we know that any variation is possible beisdes one. So it leaves us with two options, 0 and other numbers.
            return ' Error! Division by zero !! '

    def run(self): # Creating a run method; which will always run on a loop ( while True loop for a calculator )
        while True: # Infinite loop
            
            print(' Type in 1 for addition ')
            print(' Type in 2 for substraction ')
            print(' Type in 3 for multiplication ')
            print(' Type in 4 for division ')
            print(' Type in 5 to quit ')

            choice = input(' Select your weapon! ')
            
            if choice == '5': #5 will opt out of the loop and end the program
                break

            self.get_numbers() # Running the method we created earlier, so that when Run() is executed, we retrieve those numbers.
            
            if choice == '1':
                print(' Answer ', self.add()) # If choice '1' then print , then run the method we created
            elif choice == '2':
                print(' Answer ', self.subs()) # If choice '2' then print , then run the method we created
            elif choice == '3':
                print(' Answer ', self.multiply()) # If choice '3' then print , then run the method we created
            elif choice == '4':
                print(' Answer ', self.divide()) # If choice '4' then print , then run the method we created
            elif ValueError: 
                print(' That\'s not a number esse! ') # Value error handling when asking for a certain type of value.


bb = Calculator()
bb.run() 



    