"""Refactoring the travel loops code using a function and enumerate where applicable."""
from travel_loops import travel_cities

if __name__ == "__main__":

    # Declare lists
    cities = ["Rome", "Nairobi", "Phnom Penh", "Santiago", "Toronto", "Rotorua"]
    cities_daily_cost = [150, 70, 60, 80, 110, 125]

    # Call the function
    travel_cities(cities, cities_daily_cost)