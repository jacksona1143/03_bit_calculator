#functions

#check if number is greater than zero
def num_check_image (question, low):
    valid = False
    while not valid: 
        
        #error = "Please enter a value more than 0"
        error = "Please enter a pixel value that is more than ""(or equal to) {}".format(low)

        try:
            #ask user to enter a number
            response = int(input(question))

            #check if the value entered is greater or equal to the low number we have provided
            if response >= low:
                return response

            else:
                #output my error message if the value is not valid
                print(error)
                print()

        except ValueError:
                print("Please enter a number")
                print()
           
                

#code runs here

keep_going = ""
while keep_going == "":


    width = num_check_image ( "Enter the image width in pixels? ", 1)
    height = num_check_image ( "Enter the image height in pixels? ", 1)
    print("Image Width",width)
    print("Image Height",height)
    bitSize = width * height * 24
    bitSizeShow = "{:,}".format(int(format("{:.0f}".format(bitSize))))



    #print("Image Size in Bits: ",bitSize)
    print("Image Size in Bits: ",bitSizeShow)
    #perimeter = (width + height)
    #print()
    #print()
    #print("Perimeter: {:.2f} units" .format(perimeter))
    #print("Area: {:.2f} square units".format(area))

    keep_going = input("Press <enter> to keep going or any key to quit")

    

   

    
#print()
#print("Thanks for using area/perimeter calculator")   