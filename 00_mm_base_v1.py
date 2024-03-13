# Set max ticket amount
max_tickets = 3

# Initialize tickets_sold outside the loop
tickets_sold = 0
# Function to prompt for yes/no responses
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
    instructions = yes_no('Do you want to read the instructions? ')

    if instructions == 'yes':
        print('instrutctions here')
        break
    elif instructions == 'no':
        print('Proceeding without reading the instructions.')
        break
    else:
        print('Please enter yes or no.')



# Loop for ticket sales
while tickets_sold < max_tickets:
    name = input("Please enter your name or type 'XXX' here to quit: ")

    if name == 'xxx':
        break

    tickets_sold += 1

# Output number of tickets sold
remaining_tickets = max_tickets - tickets_sold
if tickets_sold == max_tickets:
    print('Congratulations, you have sold all the tickets!')
else:
    print('You have sold {} ticket/s. There are {} ticket/s left.'.format(tickets_sold, remaining_tickets))
