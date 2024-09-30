"""
Exercise: Restaurant Table Reservation System

The goal of this exercise is to create a linked list system that handles restaurant reservations.
Each reservation contains information about the customer, the number of people in the party,
and the reservation time. The system should be able to add reservations, display all reservations,
and delete a reservation based on the customer's name.

Author: Larose IKITAMA
"""


class ReservationNode:
    """
    Node class for storing individual reservation data in the linked list.

    Attributes:
        data : dict
            A dictionary containing the customer's reservation information (full_name, number_of_people, hour).
        next : ReservationNode
             Pointer to the next node in the linked list
    """
    def __init__(self, data):
        self.data = data
        self.next = None


class ReservationList:
    """
    A class to represent a linked list for handling restaurant reservations.

    Methods:
        add(data):
            Adds a new reservation to the list.
        reservations():
            Displays all the current reservations.
        delete_by_name(customer_name):
            Deletes a reservation from the list based on the customer's name.
    """
    def __init__(self):
        self.head = None

    def add(self, data):
        new_reservation = ReservationNode(data)
        if self.head is None:
            self.head = new_reservation
        else:
            current_reservation = self.head
            while current_reservation.next:
                current_reservation = current_reservation.next
            current_reservation.next = new_reservation

    def reservations(self):
        current_reservation = self.head
        while current_reservation:
            customer = current_reservation.data
            print(f"""
            Full name : {customer['full_name']}
            Number of peoples : {customer['number_of_people']}
            Hour : {customer['hour']}
""")
            print("-" * 30)
            current_reservation = current_reservation.next

    def delete_by_name(self, customer_name):
        if self.head is None:
            print("No reservation to delete")
            return

        if self.head.data['full_name'].lower() == customer_name.lower():
            self.head = self.head.next
            print(f"Reservation for the customer {customer_name} has been deleted")
            return

        current_reservation = self.head
        while current_reservation.next:
            if current_reservation.next.data['full_name'].lower() == customer_name.lower():
                current_reservation.next = current_reservation.next.next
                return
            current_reservation = current_reservation.next


def main():
    """
    Main function to execute the restaurant reservation system. It creates a lst of sample reservations, adds them to
    the system, displays the reservations, deletes a reservation by name, and shows the updated list.
    """
    customers = [
        {"full_name": "Jaden Smart",
         "number_of_people": 2,
         "hour": "7pm"
         },
        {"full_name": "Margo Robine",
         "number_of_people": 1,
         "hour": "6pm"
         },
        {"full_name": "Snow Fall",
         "number_of_people": 5,
         "hour": "7pm"
         },
        {"full_name": "Perry White",
         "number_of_people": 2,
         "hour": "7am"
         },
    ]

    llist = ReservationList()

    for customer in customers:
        llist.add(customer)

    print("List of reservation")
    llist.reservations()

    customer_name = "snow Fall"
    llist.delete_by_name(customer_name)
    print(f"List after cancellation of {customer_name.title()} customer's reservation")
    llist.reservations()


if __name__ == "__main__":
    main()
