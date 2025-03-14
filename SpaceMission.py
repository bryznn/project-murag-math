import random

def display_intro():
    print("Welcome to Space Landing Challenge!")
    print("Your goal is to land the spaceship safely on the planet.")
    print("Control your thrust and angle to avoid crashing.")

def initialize_conditions():
    return {
        "speed": random.randint(50, 150),  # Random initial speed
        "fuel": 100,  # Fixed fuel amount
        "angle": random.randint(20, 60)  # Random starting angle
    }

def adjust_thrust(fuel):
    while True:
        try:
            thrust = int(input(f"Enter thrust amount (0-20) [Fuel: {fuel}]: "))
            if 0 <= thrust <= 20 and thrust <= fuel:
                return thrust
            else:
                print("Invalid input. Enter a value within the allowed range.")
        except ValueError:
            print("Please enter a number.")

def adjust_angle():
    while True:
        try:
            angle = int(input("Enter new angle (10-90 degrees): "))
            if 10 <= angle <= 90:
                return angle
            else:
                print("Invalid angle. Must be between 10 and 90 degrees.")
        except ValueError:
            print("Please enter a number.")

def check_landing_conditions(speed, angle):
    if speed > 30:
        print("Crash! You were going too fast.")
        return False
    elif angle < 20 or angle > 70:
        print("Crash! Your angle was incorrect.")
        return False
    else:
        print("Successful landing! Mission accomplished.")
        return True

def main():
    display_intro()
    game_state = initialize_conditions()
    
    while game_state["fuel"] > 0:
        print(f"\nCurrent Speed: {game_state['speed']} km/h")
        print(f"Current Angle: {game_state['angle']} degrees")
        print(f"Fuel Remaining: {game_state['fuel']}")
        
        thrust = adjust_thrust(game_state["fuel"])
        game_state["fuel"] -= thrust
        game_state["speed"] -= thrust  # Thrust reduces speed
        
        new_angle = adjust_angle()
        game_state["angle"] = new_angle
        
        if game_state["speed"] <= 30:
            if check_landing_conditions(game_state["speed"], game_state["angle"]):
                break
        
        if game_state["fuel"] == 0:
            print("Out of fuel! You drift into space forever...")
            break
    
    print("Game Over.")

if __name__ == "__main__":
    main()
