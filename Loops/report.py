def main():
    spacecraft = {
        "name" : "Voyager 1",
        "distance" : 163
    }
    spacecraft1 = {
        "name" : "James webb space telescope"
        # "distance" : 0.01
    }
    #spacecraft1["distance"] = 0.01
    spacecraft1.update({"distance": 0.01, "orbit": "Sun"})
    print(create_report(spacecraft))
    print(create_report(spacecraft1))

def create_report(spacecraft):
    return f"""
    =========Report=========

    Name: {spacecraft.get("name", "unknown")}
    Distance: {spacecraft.get("distance", "unknown")} AU
    Orbit: {spacecraft.get("orbit", "unknown")}
    
    ========================
    """

if __name__ == "__main__":
    main()

 # Distance: {spacecraft["distance"]} AU
#  Name: {spacecraft["name"]}