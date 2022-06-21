# Function goes here

# Puts series of symbols at start and end of text (for emphasis)
def statement_generator(text, decoration):

    
   
    ends = decoration * 5

    # add decoration to start and end of statement
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""

# checks user choice is 'integer', 'text' or 'image'
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





# Main Routine goes here





# Heading
statement_generator("Bit Calculator for Integers, Texts and Images", "-")

# Display instructions if user has never used the program before

# Loop to allow multiple calculations per session
keep_going = ""
while keep_going == "":
    print()
