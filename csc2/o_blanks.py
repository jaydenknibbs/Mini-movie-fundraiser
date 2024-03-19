def not_blank (qestion):
    while True:
        response =input(qestion)

        if response == "":
            print ('sorry this cant be blank. please try again.')
        else:
            return response
        
#main routine goes here