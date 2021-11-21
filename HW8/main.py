from datetime import datetime, timedelta

from models import User, Ticket, TicketType, Trip

print("METRO STATION MANAGER")
user_input = input("Enter your option\n1)Login\n2)Register\n")

if user_input == 2:
    pass

# TODO load user from pickle file
elif user_input == 1:
    user = {}
    if not user:
        print("User not found")
    user = User(**user)
    if user.is_admin:
        show_admin_manager = ""
    else:
        user_second_input = input("Enter option\n1)Bank account management\n2)Travel\n3)Buy Ticket\n")
        if user_second_input == 1:
            option = input("Enter option\n1)Deposit\n2)Withdraw\n")
            if option == 1:
                amount = int(input("Enter the amount to deposit"))
                user.deposit(amount)
            elif option == 2:
                amount = int(input("Enter the amount to withdraw"))
                user.withdraw(amount)
        elif user_second_input == 2:
            list_trips = [
                {
                    "destination": "a",
                    "cost": 12345,
                    "duration": 12345,
                    "origin_station": "b"
                },
                {
                    "destination": "a",
                    "cost": 4234125,
                    "duration": 12123345,
                    "origin_station": "b"
                },
                {
                    "destination": "a",
                    "cost": 23566,
                    "duration": 12313245,
                    "origin_station": "b"
                }
            ]
            for i, j in enumerate(list_trips):
                print(f"{i}) {j.get('origin_station')} -> {j.get('destination')} : {j.get('cost')}")
            travel_input = int(input("Select one of travels"))
            if travel_input > (len(list_trips)):
                raise ValueError
            trip = Trip(**list_trips[travel_input])
            tickets_list = [
                {
                    "id": 123,
                    "balance": 123,
                    "expire_date": None,
                    "cart_type": "tak_safare"
                },
                {
                    "id": 456,
                    "balance": 456,
                    "expire_date": None,
                    "cart_type": "credit"
                },
                {
                    "id": 789,
                    "balance": 789,
                    "expire_date": datetime.now() + timedelta(days=1),
                    "cart_type": "credit_date"
                },
            ]
            tickets_ids = list(map(lambda x: x.get("id"), tickets_list))
            if user.cart not in tickets_ids:
                raise ValueError
            user_ticket = Ticket(**list(filter(lambda x: x.get("id") == user.cart, tickets_list))[0])
            if user_ticket.cart_type == "tak_safare":
                # TODO log safar, remove ticket
                user.cart = None
            elif user_ticket.cart_type == "credit":
                user_ticket.trip_cost_calculation(trip.cost)
            elif user_ticket.cart_type == "credit_date":
                if user_ticket.expire_date < datetime.now():
                    raise ValueError
                user_ticket.trip_cost_calculation(trip.cost)
            # TODO update ticket
        elif user_second_input == 3:
            ticket_type = input("Enter ticket type\n1)tak_safare\n2)credit\n3)credit_date\n")
            ticket = Ticket()
            if ticket_type == 1:
                pass
            elif ticket_type == 2:
                amount = int(input("Enter the amount to charge your card"))
                ticket.cart_type = TicketType.CREDIT
                user.withdraw(amount)
                ticket.charge_cart(amount)
            elif ticket_type == 3:
                amount = int(input("Enter the amount to charge your card"))
                ticket.cart_type = TicketType.CREDIT_DATE
                user.withdraw(amount)
                ticket.charge_cart(amount)
                ticket.expire_date = datetime.now() + timedelta(days=90)
            user.cart = ticket.id
            # TODO save ticket as pickle
            # TODO update user