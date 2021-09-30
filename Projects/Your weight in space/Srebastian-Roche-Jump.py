planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
rel_gravity = [2.65, 1.11, 1, 2.64, 0.40, 0.94, 1.13, 0.88]

print("What is your jump length on Earth (meters)?")

myJumps = int(input("How long was your jump?"))
myPlanets = input(f"Select a planet from the list: {planets}")

print(("Your jump length on Earth is: ") + str(myJumps))

planet_index = planets.index(myPlanets)

print(f"The length of your jump in {planets[planet_index]} is {((myJumps) * (rel_gravity[planet_index]))} meters ")
