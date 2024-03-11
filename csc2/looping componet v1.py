# Set max ticket amount
max_tickets = 3

# Initialize tickets_sold outside the loop
tickets_sold = 0

# Loop here
while tickets_sold < max_tickets:
    name = input("Please enter your name or type 'XXX' here to quit: ")

    if name == 'XXX':
        break

    tickets_sold += 1
# Output number of tickets sold
remaining_tickets = max_tickets - tickets_sold
if tickets_sold == max_tickets:
    print('Congratulations, you have sold all the tickets!')
else:
    print ('you have sold {} ticket/s. there are {} ticket/s left'.format(tickets_sold, max_tickets - tickets_sold ))