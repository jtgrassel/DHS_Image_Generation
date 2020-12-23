import json
from image_generator_fun import imageGen
from image_generator_fun import allFiles

#Location of the JSON file(s) that you wish to use to generate image(s) from
#JSON files should be formatted as the "template.json" file
jsonDir = "C:/Users/Joshua/Documents/DHS Project/JSON_Files/"

#Location of the unedited MPEG7 images
#The MPEG7 dataset can be found at the following link: http://www.timeseriesclassification.com/description.php?Dataset=ShapesAll
mpeg7Dir = "C:/Users/Joshua/Documents/DHS Project/MPEG7dataset/original/"

jsonFiles = allFiles(jsonDir) #Gets all the JSON files in the provided folder

#Generates an image for each JSON file provided
#Tracks the progress of the generation for use when many images are being generated
count = 0
progressMult = 100/len(jsonFiles)
for jsonFile in jsonFiles:
    imageGen(jsonDir + jsonFile, mpeg7Dir)
    count += 1
    status = round(count*progressMult, 2)
    print("Status:" + str(status))

print("Complete")