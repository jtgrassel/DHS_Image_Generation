from PIL import Image
from os import listdir
from os.path import isfile, join
import math
import random
from poisson_disc_fun import poissonDisc
from image_funs import advPaste
import json

def allFiles(path): #Gets a list of all the files in a folder
    files = [f for f in listdir(path) if isfile(join(path, f))]
    return files

def getKeysByValue(dictOfElements, valueToFind, index):
    listOfKeys = list()
    listOfItems = dictOfElements.items()
    for item  in listOfItems:
        if item[index] == valueToFind:
            listOfKeys.append(item[0])
    return  listOfKeys

def colorRandomizer(dist, red, green, blue, alpha):
    if dist == "U":
        newColor = (
            int(round(random.uniform(red[0], red[1]))),
            int(round(random.uniform(green[0], green[1]))),
            int(round(random.uniform(blue[0], blue[1]))),
            int(round(random.uniform(alpha[0], alpha[1])))
        )
    if dist == "T":
        newColor = (
            int(round(random.triangular(red[0], red[1], red[2]))),
            int(round(random.triangular(green[0], green[1], green[2]))),
            int(round(random.triangular(blue[0], blue[1], blue[2]))),
            int(round(random.triangular(alpha[0], alpha[1], alpha[2])))
        )
    return newColor

def genRandomizer(dist, params):
    if dist == "U":
        rand_num = random.uniform(params[0], params[1])
    elif dist == "T":
        rand_num = random.triangular(params[0], params[1], params[2])
    return rand_num

mpeg7_dir = "C:/Users/Joshua/Documents/DHS Project/MPEG7dataset/original/"
save_dir = "Temp/"
save_name = "no-bat-7"

params =  {
    "background": {
        "color" : "black",
        "width" : 1920,
        "height" : 1080
    },
    "scale" : {
        "dist" : "U",
        "params" : (0.3, 0.4)
    },
    "rotation" : {
        "dist" : "U",
        "params" : (0, 365)
    },
    "color" : {
        "dist" : "U",
        "channels" : {
            "red" : (10, 255),
            "green" : (10, 255),
            "blue" : (10, 255),
            "alpha" : (150, 180)
        }
    },
    "centers" : {
        "r" : 150,
        "k" : 32
    }
}

find_images = [
    #{"name":"bat-7.gif", "depth":0.5},
]

excluded_images = [
    {"name":"bat-1.gif"},
    {"name":"bat-2.gif"},
    {"name":"bat-3.gif"},
    {"name":"bat-4.gif"},
    {"name":"bat-5.gif"},
    {"name":"bat-6.gif"},
    {"name":"bat-7.gif"},
    {"name":"bat-8.gif"},
    {"name":"bat-9.gif"},
    {"name":"bat-10.gif"},
    {"name":"bat-11.gif"},
    {"name":"bat-12.gif"},
    {"name":"bat-13.gif"},
    {"name":"bat-14.gif"},
    {"name":"bat-15.gif"},
    {"name":"bat-16.gif"},
    {"name":"bat-17.gif"},
    {"name":"bat-18.gif"},
    {"name":"bat-19.gif"},
    {"name":"bat-20.gif"}
]

fileList = allFiles(mpeg7_dir)

#remove excluded images
for item in excluded_images:
    fileList.remove(item["name"])

#make an empty dictionary to keep track of the images
imageDic = {}

#make the background
composite = Image.new('RGBA', (params["background"]["width"], params["background"]["height"]), color=params["background"]["color"])

#pre-generate all the image center points
centerPoints = poissonDisc(params["background"]["width"], params["background"]["height"], params["centers"]["r"], params["centers"]["k"])

#palce all the random images
num = 0
for newCenter in centerPoints:
    new_entry = {
        num: {
            "imageDir":fileList[random.randint(0, len(fileList)-1)],
            #"imageDir":"device3-1.gif",
            "center":newCenter,
            "scale":genRandomizer(params["scale"]["dist"], params["scale"]["params"]),
            "rotation":genRandomizer(params["rotation"]["dist"], params["rotation"]["params"]),
            "color":colorRandomizer(
                params["color"]["dist"], 
                params["color"]["channels"]["red"], 
                params["color"]["channels"]["green"],
                params["color"]["channels"]["blue"],
                params["color"]["channels"]["alpha"]
            )
        }
    }
    imageDic.update(new_entry)
    num += 1

#update the find images
findIndices = []
for item in find_images:
    imageNum = int(round((1-item["depth"])*len(centerPoints), 0))
    imageDic[imageNum]["imageDir"] = item["name"]
    findIndices.append(imageNum)


#start pasting images
for key in imageDic:
    newImageDir = imageDic[key]["imageDir"]
    newImage = Image.open(mpeg7_dir + newImageDir)
    composite = advPaste(
        newImage,
        composite,
        imageDic[key]["center"],
        imageDic[key]["scale"],
        imageDic[key]["rotation"],
        imageDic[key]["color"]
    )

#save the final image
composite.save(save_dir + save_name + ".png", 'PNG')

#make the easy find image
for i in findIndices:
    findImageDir = imageDic[i]["imageDir"]
    newImage = Image.open(mpeg7_dir + findImageDir)
    composite = advPaste(
        newImage,
        composite,
        imageDic[i]["center"],
        imageDic[i]["scale"],
        imageDic[i]["rotation"],
        (255, 255, 255, 255)
    )

#save the easy find image
composite.save(save_dir + save_name + "-find.png", 'PNG')

#make json file
json_dic = {
    "params":params,
    "find_images":find_images,
    "excluded_images":excluded_images,
    "results":imageDic
}

with open(save_dir + save_name + ".txt", 'w') as json_file:
    json.dump(json_dic, json_file, indent=4)