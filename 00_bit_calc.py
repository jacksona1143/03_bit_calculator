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




statement_generator("Bit Calculator for Integers, Texts and Images", "-")

# Main routine goes here
statement_generator("look , stars", "*")
