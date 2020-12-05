class flight():
    def __init__(self, total_seats):
        self.total_seats=total_seats
        self.passangers=[]
    def add_passanger(self, name):
        if not self.remaining():
            return False
        self.passangers.append(name)
        return True

    def remaining(self):
        return self.total_seats - len(self.passangers)

light=flight(4)

people=["steve", "rock", "block", "kin", "modoc"]
for p in people:
    if light.add_passanger(p):
        print(f"we added {p} successfully in the flight")
    else:
        print(f"person {p} could not be added to the flight due to lack of seats")