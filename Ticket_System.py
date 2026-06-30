booking_dataset = {
    "Rohtak": {
        "Skytech Cinemas": [
            "Carry On Jatta 3",
            "Shadaa",
            "Singham Again",
            "Stree 2",
        ],
        "Deepak Cinema": [
            "Avengers: Secret Wars",
            "Spider-Man",
            "Pushpa 2",
            "Animal",
        ],
        "BMS Screens": ["Saunkan Saunkne", "Chal Mera Putt", "Gadar 2", "Jawan"],
        "Gold Digital": [
            "Deadpool & Wolverine",
            "Fantastic Four",
            "Fighter",
            "Dunki",
        ],
    },
    "Delhi": {
        "PVR Select CityWalk": [
            "Avengers: Secret Wars",
            "Blade",
            "Captain America",
            "Thor",
        ],
        "Cinepolis DLF Avenue": [
            "Jawan",
            "Pathaan",
            "Tiger 3",
            "Bhool Bhulaiyaa 3",
        ],
        "Miraj Cinemas": ["Saunkan Saunkne", "Chal Mera Putt", "Angrej", "Sufna"],
        "Delite Cinema": ["Gadar 2", "Animal", "Kalki 2898 AD", "Drishyam 2"],
    },
    "Karnal": {
        "Super Mall Multiplex": [
            "Deadpool & Wolverine",
            "Fantastic Four",
            "Iron Man",
            "Black Panther",
        ],
        "Movie Time Cinemas": ["Fighter", "Dunki", "Kabir Singh", "Shershaah"],
        "RP Multiplex": ["Arjan Dhillon Live", "Lahoriye", "Qismat", "Bambukat"],
        "Karnal Cinema Hall": [
            "Kalki 2898 AD",
            "Golmaal Again",
            "Chhava",
            "Baby John",
        ],
    },
    "Chandigarh": {
        "Elante PVR Multiplex": [
            "Avengers: Secret Wars",
            "Captain America",
            "Doctor Strange",
            "Ant-Man",
        ],
        "Piccadily Square": ["Sufna", "Qismat 2", "Muklawa", "Puaada"],
        "Wave Cinemas": ["Brahmastra", "Drishyam 2", "Chhichhore", "Uri"],
        "Fun Republic": [
            "Angrej",
            "Bambukat",
            "Vekh Baraatan Challiyan",
            "Rabb Da Radio",
        ],
    },
}

pricing_chart = {"Standard": 150, "Luxury": 250, "VIP": 400}


def book_ticket():
    print("WELCOME TO THE MOVIE BOOKING SYSTEM")

    cities = list(booking_dataset.keys())
    print("\nAvailable Cities:")
    index = 1
    for city in cities:
        print(index, city)
        index += 1
    city_choice = int(input("Select a city (Enter number): ")) - 1
    selected_city = cities[city_choice]

    theatres = list(booking_dataset[selected_city].keys())
    print("\nAvailable Theatres in", selected_city)
    index = 1
    for theatre in theatres:
        print(index, theatre)
        index += 1
    theatre_choice = int(input("Select a theatre (Enter number): ")) - 1
    selected_theatre = theatres[theatre_choice]

    movies = booking_dataset[selected_city][selected_theatre]
    print("\nShowing Movies at", selected_theatre)
    index = 1
    for movie in movies:
        print(index, movie)
        index += 1
    movie_choice = int(input("Select a movie (Enter number): ")) - 1
    selected_movie = movies[movie_choice]

    num_tickets = int(input("\nEnter number of tickets: "))

    suites = list(pricing_chart.keys())
    print("\nAvailable Suite Types:")
    index = 1
    for suite in suites:
        print(index, suite, "(Rs.", pricing_chart[suite], "each)")
        index += 1
    suite_choice = int(input("Select suite type (Enter number): ")) - 1
    selected_suite = suites[suite_choice]

    ticket_price = pricing_chart[selected_suite]
    total_price = ticket_price * num_tickets

    print("\n" + "=" * 40)
    print("               FINAL BILL               ")
    print("=" * 40)
    print("City:       ", selected_city)
    print("Theatre:    ", selected_theatre)
    print("Movie:      ", selected_movie)
    print("Suite Type: ", selected_suite)
    print("Quantity:   ", num_tickets)
    print("Price/Seat:  Rs.", ticket_price)
    print("-" * 40)
    print("TOTAL PRICE: Rs.", total_price)
    print("=" * 40)
    print("Enjoy your show!")

book_ticket()