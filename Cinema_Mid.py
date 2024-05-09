class Star_Cinema:
    def __init__(self):
        self._hall_list = []

    def entry_hall(self, hall):
        self._hall_list.append(hall)


class Hall:
    def __init__(self, rows, cols, hall_no):
        self._seats = {}
        self._show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no

        Star_Cinema().entry_hall(self)

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self._show_list.append(show_info)

        seats = []
        for i in range(self._rows):
            col = []
            for j in range(self._cols):
                col.append(0)
            seats.append(col)

        self._seats[id] = seats

    def _valid_seat(self, row, col):
        return 0 <= row < self._rows and 0 <= col < self._cols

    def _seat_available(self, id, row, col):
        return self._seats[id][row][col] == 0

    def book_seats(self, id, seats_to_book):
        if id not in self._seats:
            raise ValueError("Invalid show ID")

        for row, col in seats_to_book:
            if not self._valid_seat(row, col):
                raise ValueError("Invalid seat")
            if not self._seat_available(id, row, col):
                raise ValueError("Seat already booked")
            self._seats[id][row][col] = 1

    def view_show_list(self):
        i = 0
        while i < len(self._show_list):
            print(self._show_list[i])
            i = i + 1


    def view_available_seats(self, id):
        if id not in self._seats:
            raise ValueError("Invalid show ID")

        return [[(r, c) for c, seat in enumerate(row) if seat == 0] for r, row in enumerate(self._seats[id])]


cinema = Star_Cinema()
hall1 = Hall(rows=5, cols=10, hall_no=1)
hall1.entry_show(id="100", movie_name="Avengers", time="12:00 PM")
hall1.entry_show(id="101", movie_name="Inception", time="2:00 PM")
hall1.entry_show(id="102", movie_name="Zindagi na milegi Dobara", time="54:00 PM")
hall1.entry_show(id="103", movie_name="Money Heist", time="6:00 PM")
hall1.entry_show(id="104", movie_name="Breaking Bad", time="8:00 PM")
hall1.entry_show(id="105", movie_name="Spider Man", time="10:00 PM")
hall1.entry_show(id="106", movie_name="Cost Way", time="10:00 AM")
hall1.entry_show(id="107", movie_name="Spider Man", time="12:00 PM")

while True:
    print('1. View all show')
    print('2. View available seats')
    print('3. Book your Ticket')
    print('4. Exit')

    option = int(input("Enter your choice: "))
    print('\n')

    if option == 1:
        hall1.view_show_list()
    
    elif option == 2:
        show_id = input("Enter ID of the show: ")
        try:
            print(hall1.view_available_seats(show_id))
        except ValueError as e:
            print(e)
    
    elif option == 3:
        try:
            show_id = input("Enter ID of the show: ")
            seats_to_book = []
            
            while True:
                try:
                    seats = int(input("Enter the number of seat do you want to book: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid choice.")

            available_seats = hall1.view_available_seats(show_id)
            print("Available Seats:", available_seats)
            
            for i in range(seats):
                while True:
                    try:
                        row = int(input(f"Enter row number for seat {i + 1}: "))
                        col = int(input(f"Enter column number for seat {i + 1}: "))
                        if (row, col) in available_seats[row]:
                            seats_to_book.append((row, col))
                            break
                        else:
                            print("Seat not available. Please select another seat.")
                    except ValueError:
                        print("Invalid input. Please enter a valid choice.")
            
            hall1.book_seats(show_id, seats_to_book)
            print("Tickets booked successfully, Thank You!")
        except ValueError as e:
            print(e)
    
    elif option == 4:
        break
    else:
        print("Invalid Choice! Please choose a valid option.")
