# checks input is  a number more than a given value
def num_check (question):
    valid = False
    while not valid: 
        
        error = "Please enter a value more than 0"

        try:
            response = float(input(question))

            if response > 0:
                return response

            else:
                print(error)
                

        except ValueError:
                print("Please enter a number")
                print()
                        