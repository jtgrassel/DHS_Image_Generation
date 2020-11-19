import json
from image_generator_fun import imageGen
from image_generator_fun import allFiles

jsonDir = "C:/Users/Joshua/Documents/DHS Project/JSON_Files/"
jsonFiles = allFiles(jsonDir)

count = 0
for jsonFile in jsonFiles:
    imageGen(jsonDir + jsonFile)
    count += 1
    status = 100*(count/len(jsonFiles))
    print("Status:" + str(status))

print("Complete")
