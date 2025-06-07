# Airline Seat Booking System

## Overview
This Python script simulates an airline seat booking system. It allows users to view available seats, book specific seats, get seat suggestions, and find empty seat clusters. The program uses NumPy for efficient seat management and provides a user-friendly command-line interface.

## Features

- **Interactive Menu System**: Easy-to-use command-line interface
- **Seat Visualization**: Clear display of available (O) and booked (X) seats
- **Seat Booking**: Book specific seats with validation
- **Smart Suggestions**: Recommends the best available seat (centered in the row)
- **Cluster Finding**: Identifies adjacent empty seats for group bookings
- **Input Validation**: Handles invalid inputs gracefully

## Requirements

- Python 3.x
- NumPy library

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/tl5275/airline-seat-booking.git
   cd airline-seat-booking
2. Install the required dependencies:
   pip install numpy
   
## Usage
Run the program with Python:
python airline_seat_booking.py

## Menu Options:
1. Display Seating Chart: Shows current seat availability

2. Book a Seat: Book a specific seat by row and column

3. Suggest Best Available Seat: Get a recommended seat

4. Find Empty Seat Clusters: Find adjacent available seats (for groups)

5. Exit: Quit the program

## Example Usage
===== Airline Seat Booking Menu =====
1. Display Seating Chart
2. Book a Seat
3. Suggest Best Available Seat
4. Find Empty Seat Clusters (2 adjacent)
5. Exit
Enter your choice (1-5): 1

Seating Chart (O = available, X = booked):
   1 2 3 4 5 6
 1 O O O O O O
 2 O O O O O O
 ...

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License
This project is open-source and available under the MIT License.
