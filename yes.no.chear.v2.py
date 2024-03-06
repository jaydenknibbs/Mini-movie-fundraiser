# Function goes here
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == 'yes' or response == 'y':
            return "yes"

        elif response == 'no' or response == 'n':
            return "no"

        else:
            print("Please enter yes or no")

# Main stuff goes here
while True:
    Instructions = yes_no('Did you want to read the instructions? ')

    if Instructions == 'yes':
        print('Show instructions')

    else:
        print ('done')
