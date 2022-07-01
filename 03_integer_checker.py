# functions go here

# checks input is  a number more than a given value
def num_check (question):
    valid = False
    while not valid: 
        
        error = "Please enter a value more than 0"

        try:

            # asks user to enter a question
            response = float(input(question))

            # checks number is more than zero
            if response > 0:
                return response

            # outputs error if input is invalid
            else:
                print(error)
                print()

        except ValueError:
                print("Please enter a number")
                print()
                        