import unittest
import ticketViewer
allTickets = 1
singleTicket = 2
url = 'https://zcctickets0823.zendesk.com/api/v2/tickets?page[size]=25'
class TestAllTickets(unittest.TestCase):
    def testSingleTicket(self):
        print("Program Output: ")
        getTicketData(singleTicket, 3, url, user, pwd)
        print("Expected Output:)
        print("---------------------------------------------------------------------------")
        print("Ticket ID:  3"
        print("Subject:  Test ticket #6")
        print("Descripton:  This is test ticket #6")
        print("Status:  open")
        print("Submitted by  1903605410607  on  2021-11-25T20:22:58Z")
        print("---------------------------------------------------------------------------")
    def testSingleTicketFrontEdge(self):
        print("Program Output: ")
        getTicketData(singleTicket, 1, url, user, pwd)
        print("Expected Output:)
        print("---------------------------------------------------------------------------")
        print("Ticket ID:  1"
        print("Subject:  Sample ticket: Meet the ticket")
        print("Descripton:  I知 sending an email because I知 having a problem setting up your new product. Can you help me troubleshoot?
        print("Thanks,")
        print("The Customer")
        print("Status:  open")
        print("Submitted by  1903605410607  on  2021-11-25T01:26:37Z")
        print("---------------------------------------------------------------------------")
    def testSingleTicketBackEdge(self):
        print("Program Output: ")
        getTicketData(singleTicket, 21, url, user, pwd)
        print("Expected Output:)
        print("---------------------------------------------------------------------------")
        print("Ticket ID:  21"
        print("Subject:  Test ticket #0")
        print("Descripton:  This is test ticket #0")
        print("Status:  open")
        print("Submitted by  1903605410607  on  2021-11-25T20:22:58Z")
        print("---------------------------------------------------------------------------")
    def testAllLess25(self):
        print("Program Output: ")
        getTicketData(allTickets, -1, url, user, pwd)
        print("Expected Output:)
        print("---------------------------------------------------------------------------")
        print("Ticket ID:  1"
        print("Subject:  Sample ticket: Meet the ticket")
        print("Descripton:  I知 sending an email because I知 having a problem setting up your new product. Can you help me troubleshoot?
        print("Thanks,")
        print("The Customer")
        print("Status:  open")
        print("Submitted by  1903605410607  on  2021-11-25T01:26:37Z")
        print("---------------------------------------------------------------------------")
        print("Ticket ID:  2"
        print("Subject:  Test ticket #17")
        print("Descripton:  This is test ticket #17")
        print("Status:  open")
        print("Submitted by  1903605410607  on  2021-11-25T20:22:58Z")
        print("---------------------------------------------------------------------------")
        print("Ticket ID:  3"
        print("Subject:  Test ticket #6")
        print("Descripton:  This is test ticket #6")
        print("Status:  open")
        print("Submitted by  1903605410607  on  2021-11-25T20:22:58Z")
        print("---------------------------------------------------------------------------")
        print("Ticket ID:  4"
        print("Subject:  Test ticket #10")
        print("Descripton:  This is test ticket #10")
        print("Status:  open")
        print("Submitted by  1903605410607  on  2021-11-25T20:22:58Z")
        print("---------------------------------------------------------------------------")
        print("Ticket ID:  5"
        print("Subject:  Test ticket #2")
        print("Descripton:  This is test ticket #2")
        print("Status:  open")
        print("Submitted by  1903605410607  on  2021-11-25T20:22:58Z")
        print("---------------------------------------------------------------------------")