train_seat = input(("Enter the seat you want to book (e.g., sleeper, luxury, general, Ac): ")).lower()

match train_seat:
    case "sleeper":
        print("You have booked a Sleeper class seat.")
    case "luxury":
        print("You have booked a Luxury class seat.")
    case "general":
        print("You have booked a General class seat.")
    case "ac":
        print("You have booked an AC class seat.")
    case _:
        print("Invalid seat type selected. Please choose from sleeper, luxury, general, or AC.")
        