# Write a program that asks the user to enter the width and length of a room.

width = input("Insert the width of the room: ")
length = input("Insert the length of the room: ")

# Once these values have been read, your program should compute and display the area of the room. 
# The length and the width will be entered as **floating-point numbers**.  

area = float(width) * float(length) 

# Include units in your prompt and output message; either feet or meters, depending on which
# unit you are more comfortable working with.

print(f"The area of the room is: {float(area)} mq")

print("Thanks for use")


