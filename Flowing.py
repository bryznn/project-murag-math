from graphviz import Digraph

def generate_flowchart():
    dot = Digraph("Space Mission Flowchart")
    
    # Nodes
    dot.node("Start", "Start")
    dot.node("Briefing", "Display Mission Briefing")
    dot.node("Init", "Set Initial Conditions\n(Speed, Fuel, Angle)")
    dot.node("PlayerInput", "Player Input: Adjust Thrust & Angle")
    dot.node("Update", "Update Speed & Position")
    dot.node("CheckSpeed", "Speed > 30?")
    dot.node("Crash", "Crash! Too Fast 💥")
    dot.node("CheckAngle", "Angle Correct?")
    dot.node("AngleCrash", "Crash! Bad Angle 💥")
    dot.node("FuelCheck", "Fuel Remaining?")
    dot.node("SafeSpeed", "Speed < 15?")
    dot.node("Drift", "Out of Fuel! Drifting in Space 🚀")
    dot.node("Success", "Successful Landing! 🎯")
    dot.node("End", "End")
    
    # Edges
    dot.edge("Start", "Briefing")
    dot.edge("Briefing", "Init")
    dot.edge("Init", "PlayerInput")
    dot.edge("PlayerInput", "Update")
    dot.edge("Update", "CheckSpeed")
    dot.edge("CheckSpeed", "Crash", label="Yes")
    dot.edge("CheckSpeed", "CheckAngle", label="No")
    dot.edge("CheckAngle", "AngleCrash", label="No")
    dot.edge("CheckAngle", "FuelCheck", label="Yes")
    dot.edge("FuelCheck", "Drift", label="No")
    dot.edge("FuelCheck", "SafeSpeed", label="Yes")
    dot.edge("SafeSpeed", "Success", label="Yes")
    dot.edge("SafeSpeed", "Crash", label="No")
    dot.edge("Crash", "End")
    dot.edge("AngleCrash", "End")
    dot.edge("Drift", "End")
    dot.edge("Success", "End")
    
    # Output DOT source instead of rendering with UTF-8 encoding
    with open("space_mission_flowchart.dot", "w", encoding="utf-8") as file:
        file.write(dot.source)
    print("DOT source saved as 'space_mission_flowchart.dot'. Render it locally using Graphviz.")

if __name__ == "__main__":
    generate_flowchart()
