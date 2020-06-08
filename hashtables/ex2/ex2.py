from typing import List

#  Hint:  You may not need all of these.  Remove the unused functions.


class Ticket:
    def __init__(self, source: str, destination: str):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets: List[Ticket], length: int) -> List[str]:
    route_dict = {}

    for i in tickets:
    	route_dict[i.source] = i.destination

    print(route_dict)
    return None



ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")
tickets = [ticket_1, ticket_2, ticket_3]
reconstruct_trip(tickets, 3)
expected = ["PDX", "DCA", "NONE"]
