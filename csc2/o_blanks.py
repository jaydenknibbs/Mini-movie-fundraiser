def not_blank (qestion):
    while True:
        response =input(qestion)

        if response == "":
            print ('sorry this cant be blank. please try again.')
        else:
            return response
  
        while True:
            response = input(qestion)
            if response == "":
                print ('sorry this cant be blank')
            else:
                return response

while True:
    name = not_blank (" enter name or type xxx to quite ")
    if name == 'xxx':
        break
print ('we are done')