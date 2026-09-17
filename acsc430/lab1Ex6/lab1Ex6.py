def convert_distance(total_inches):
    INCHES_PER_FOOT = 12
    FEET_PER_YARD = 3
    YARDS_PER_FURLONG = 220
    FURLONGS_PER_MILE = 8
    MILES_PER_LEAGUE = 3

    #Inches --> Feet
    total_feet = total_inches // INCHES_PER_FOOT
    remaining_inches = total_inches % INCHES_PER_FOOT

    #Feet --> Yards
    total_yards = total_feet // FEET_PER_YARD
    remaining_feet = total_feet % FEET_PER_YARD

    #Yards --> Furlongs
    total_furlongs = total_yards // YARDS_PER_FURLONG
    remaining_yards = total_yards % YARDS_PER_FURLONG

    #Furlongs --> Miles
    total_miles = total_furlongs // FURLONGS_PER_MILE
    remaining_furlongs = total_furlongs % FURLONGS_PER_MILE

    #Miles --> Leagues
    total_leagues = total_miles // MILES_PER_LEAGUE
    remaining_miles = total_miles % MILES_PER_LEAGUE

    return (total_leagues, remaining_miles,
            remaining_furlongs, remaining_yards,
            remaining_feet, remaining_inches)

def print_results(results):
    leagues, miles, furlongs, yards, feet, inches = results

    print("\nLand Distance Breakdown:")
    print("-------------------------")
    print(f"Leagues : {leagues}")
    print(f"Miles   : {miles}")
    print(f"Furlongs: {furlongs}")
    print(f"Yards   : {yards}")
    print(f"Feet    : {feet}")
    print(f"Inches  : {inches}")

def main():
    total_inches = int(input("Enter the total distance in inches: "))

    results = convert_distance(total_inches)
    print_results(results)

main()