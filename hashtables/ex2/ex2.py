from typing import List
# First ticket is None, Something
# Last ticket is Something, None 

class Ticket:
    def __init__(self, source: str, destination: str):
        self.source = source
        self.destination = destination

def reconstruct_trip(tickets: List[Ticket], length: int) -> List[str]:
    route_dict = {}
    for i in tickets:
    	route_dict[i.source] = i.destination
    curr_stop = route_dict['NONE']
    route_list = [curr_stop]
    while curr_stop != 'NONE':
    	curr_stop = route_dict[curr_stop]
    	route_list.append(curr_stop)
    return(route_list)
    
ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")
tickets = [ticket_1, ticket_2, ticket_3]
print(reconstruct_trip(tickets, 3))
expected = ["PDX", "DCA", "NONE"]
