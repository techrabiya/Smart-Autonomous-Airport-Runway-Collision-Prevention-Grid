print("--- Challenge 1 Initialized: Airport Runway Collision Grid ✈️ ---")

def airport_runway_safety_engine(aircraft_speed_knots, distance_to_preceding_plane_m, visibility_meters):
    print(f"Airport runway safety engine starting with visibility: {visibility_meters}m")
    
    if visibility_meters < 800.0:
        print("Alert Message: Low visibility warning detected")
        return "emergency diversion activated"
    elif distance_to_preceding_plane_m < 2000.0:
        if aircraft_speed_knots > 160.0:
            print("that was high speed proximity alert")
            return "immediate go-around maneuver required"
        else:
            print("that was cautionary spacing log")
            return "slow approach recommended"
    else:
        print("clear runway log was normal")
        return "normal landing clearance approved"

# Testing the Runway Safety Engine
print("\nRunning status Airport Runway Collision Grid")
print(airport_runway_safety_engine(165.0, 1500.0, 1000.0))
print("-" * 35)
print(airport_runway_safety_engine(140.0, 2500.0, 900.0))
