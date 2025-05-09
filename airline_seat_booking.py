import numpy as np

# Initialize seating chart
rows, cols = 10, 6
seats = np.zeros((rows, cols), dtype=bool)

def display_seats(seats):
    print("\nSeating Chart (O = available, X = booked):")
    print("   " + " ".join(f"{i+1}" for i in range(cols)))
    for idx, row in enumerate(seats):
        print(f"{idx+1:2} " + " ".join('X' if seat else 'O' for seat in row))

def book_seat(row, col):
    if 0 <= row < rows and 0 <= col < cols:
        if not seats[row, col]:
            seats[row, col] = True
            print(f"✅ Seat ({row+1},{col+1}) booked.")
        else:
            print(f"❌ Seat ({row+1},{col+1}) is already booked.")
    else:
        print("❌ Invalid seat coordinates.")

def find_empty_clusters(seats, cluster_size=2):
    clusters = []
    for i in range(seats.shape[0]):
        for j in range(seats.shape[1] - cluster_size + 1):
            if not seats[i, j:j+cluster_size].any():
                clusters.append(((i, j), (i, j+cluster_size-1)))
    return clusters

def suggest_best_seat(seats):
    center_col = seats.shape[1] // 2
    for i in range(seats.shape[0]):
        available_indices = np.where(seats[i] == False)[0]
        if len(available_indices) > 0:
            best_col = min(available_indices, key=lambda x: abs(x - center_col))
            return (i, best_col)
    return None

# --- Main loop ---
while True:
    print("\n===== Airline Seat Booking Menu =====")
    print("1. Display Seating Chart")
    print("2. Book a Seat")
    print("3. Suggest Best Available Seat")
    print("4. Find Empty Seat Clusters (2 adjacent)")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == '1':
        display_seats(seats)

    elif choice == '2':
        try:
            r = int(input("Enter row number (1-10): ")) - 1
            c = int(input("Enter column number (1-6): ")) - 1
            book_seat(r, c)
        except ValueError:
            print("❌ Invalid input. Please enter numbers.")

    elif choice == '3':
        seat = suggest_best_seat(seats)
        if seat:
            print(f"🎯 Suggested Seat: Row {seat[0]+1}, Column {seat[1]+1}")
        else:
            print("🚫 No available seats found.")

    elif choice == '4':
        clusters = find_empty_clusters(seats)
        if clusters:
            print(f"🔍 Found {len(clusters)} empty seat clusters of size 2:")
            for c in clusters:
                print(f"Row {c[0][0]+1}, Col {c[0][1]+1} to Col {c[1][1]+1}")
        else:
            print("🚫 No empty clusters found.")

    elif choice == '5':
        print("👋 Exiting the simulation. Goodbye!")
        break

    else:
        print("❌ Invalid choice. Please select a number from 1 to 5.")
