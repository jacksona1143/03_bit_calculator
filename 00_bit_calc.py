# Function goes here

# Statement Generator function puts series of symbols at start and end of text (for emphasis)
def statement_generator(text, decoration):

    
   
    ends = decoration * 5

    # add decoration to start and end of statement
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""

# User Choice function checks user choice is 'integer', 'text' or 'image'
def user_choice():

    text_ok = ["text" , "t" , "txt"]
    integer_ok = ["integer" , "int" , "#" , "number"]
    image_ok = [ "image" , "img" , "pix" , "picture" , "pic" , "p"]

    valid = False
    while not valid:

        # Ask user for file type
        response = input("File type (integer / text / image): ").lower()

        # for integer, ask for an integer       
        # (must be a  integer more than/ equal to 0)
        if response in text_ok:
            return "text"

        elif response in integer_ok:
              return "integer"

        elif response in image_ok:
              return "image"
        
        elif response == "i":
            want_integer = input("Press <enter> for an integer or any key for image: ")
            if want_integer == "":
                return "integer"
            else:
                return "image"

        else:
                print("Please choose a valid file type!")
                print()

#Num Check Function - checks whether integer is greater than low number from parameter
def num_check (question, low):
    valid = False
    while not valid: 
        
        #error = "Please enter a value more than 0"
        error = "Please enter an integer that is more than ""(or equal to) {}".format(low)

        try:
            #ask user to enter a number
            response = int(input(question))

            #check if the integer entered is greater or equal to the low number we have provided
            if response >= low:
                return response

            else:
                #output my error message if the integer is not valid
                print(error)
                print()

        except ValueError:
                print("Please enter a number")
                print()
          

               




# Main Routine goes here


#Heading
statement_generator("Bit Calculator for Integers, Texts and Images", "-")




# Display instructions if user has never used the program before



# Loop to allow multiple calculations per session
keep_going = ""
while keep_going == "":

    #Ask the user for the file type by calling 'User Choice Function'
    data_type = user_choice()
    print("You chose", data_type)
   