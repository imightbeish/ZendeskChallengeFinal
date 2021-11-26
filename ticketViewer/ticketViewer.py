import pip._vendor.requests

def getTicketData(option, ticket):
    #divider
    print("---------------------------------------------------------------------------")
    # set the request parameters
    url = 'https://zcctickets0823.zendesk.com/api/v2/tickets' + '?page[size]=25'
    user = 'ishaan.shah823@gmail.com'
    pwd = 'isatus4Fun'

    # do the http get request
    response = pip._vendor.requests.get(url, auth=(user, pwd))

    # error connecting
    if response.status_code != 200:
        print('status:', response.status_code, 'error with the request, exiting.')
        exit()

    data = response.json()

    # print the given ticket
    if option == "2":
        print( 'Given Ticket = ', data['tickets'][ticket]['raw_subject'] )
    else:
        while url:
            response = pip._vendor.requests.get(url, auth=(user, pwd))
            data = response.json()
            for ticket in data['tickets']:
                print(ticket['id'])
            if data['meta']['has_more']:
                url = data['links']['next']
            else:
                url = None
    #divider
    print("---------------------------------------------------------------------------")

userInput = " "
while userInput != "q":
    print("Press 1 to view all tickets")
    print("Press 2 to view individual tickets")
    print("Press q to quit")
    userInput = input("Enter an option: ")

    if userInput == "1":
        print("All tickets")
        getTicketData(userInput, -1)
    elif userInput == "2":
        ticketNum = input("Which ticket would you like to view: ")
        ticketNum = int(ticketNum)
        getTicketData(userInput, ticketNum)
        #print that ticket
    elif userInput == "q":
        continue
    else:
        print("Invalid Command! Please type one of the commands shown above.")

