import math
from ExperimentalData import ExperimentalData

from pathlib import Path
import json
import os

# gun = "MP9"
# caliber = "9x19mm Parabellum" 
# ammunition = "9x19mm RIP"
# velocity_ms = 381

# Building = 	"Coliseum Tower Residences"
# BuildingHeight = 259

# gravity_Ms = 9.81

#Covert your variables into parameters

def ProjectileFunction(experimentalData:ExperimentalData):

    time_s = math.sqrt((2 * experimentalData.BuildingHeight)/ experimentalData.gravity_Ms)

    distance = (experimentalData.velocity_ms * time_s)
    #distance = (experimentalData[velocity_ms] * time_s)

# def ProjectileFunction(gun:str, caliber:str, ammunition:str, velocity_ms: int, building, gravit:int): 
#     time = math.sqrt((2 * building_height) / gravity)
#     distance = (experimentalData[velocity]* gravity)




    print(f"The gun selcted was{experimentalData.gun}, the caliber used is {experimentalData.caliber}, the ammunition type.")

# experimentalData = {

# "gun": "MP9",
# "caliber": "9x19mm" , 
# "ammunition": "9x19mm RIP", 
# "velocity_ms": 381
# Building = "Coliseum Tower Residences
# BuildingHeight = 259
# gravity_Ms = 9.81

# }

experimentalData = ExperimentalData ("MP9", "9x19mm", "9x19mm RIP", 381, "Coliseum Tower Residences", 259, 9.81)


myDataSet = [

ExperimentalData ("MP9", "9x19mm", "9x19mm RIP", 381, "Coliseum Tower Residences", 259, 9.81),
ExperimentalData ("MP9-N", "9x19mm", "9x19mm Pst gzh", 381, "Coliseum Tower Residences", 259, 9.81),
ExperimentalData ("MPX", "9x19mm", "9x19mm Pst gzh", 381, "Coliseum Tower Residences", 259, 9.81),
ExperimentalData ("P90", "5.7x28mm FN", "5.7x28mm SS190", 381, "Coliseum Tower Residences", 259, 9.81)


]

for data in myDataSet:
    print("\n------------------------------------------------\n")
    ProjectileFunction(data)
myDataSet[0]
# ProjectileFunction(experimentalData)

#Serialization
myOutputPath = Path(__file__).parents[0]
myOutputFilePath = os.path.join(myOutputPath, "Projectile-Motion.json")

with open(myOutputFilePath, "w") as outfile:
    json.dump([data.__dict__ for data in myDataSet], outfile)
    json.dump(myDataSet[0].__dict__, outfile)

    # ProjectileFunction(experimentalData)