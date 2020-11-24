import json

json_dir = "C:/Users/Joshua/Documents/DHS Project/JSON_Files/"
img_dir = "C:/Users/Joshua/Documents/DHS Project/temp/"
group_name = "No_BatHoneyPot"

#make arrays for all the parameters
#save name?

backgroundA = [
    ("beige", 1080, 1080)
]

scaleA = [("T", .15, .2, .25)]

rotationA = [("U", 0, 365)]

colorA = [
    ("U", ((10, 255), (10, 255), (10, 255), (140, 170)))
]

centersA = [(150, 32)]

find_image_name = "bat"
find_image_number = "-5"

find_images = [
    {"name":find_image_name + find_image_number + ".gif", "depth":0.5},
]

excluded_images = [
    {"name":find_image_name + "-1.gif"},
    {"name":find_image_name + "-2.gif"},
    {"name":find_image_name + "-3.gif"},
    {"name":find_image_name + "-4.gif"},
    {"name":find_image_name + "-5.gif"},
    {"name":find_image_name + "-6.gif"},
    {"name":find_image_name + "-7.gif"},
    {"name":find_image_name + "-8.gif"},
    {"name":find_image_name + "-9.gif"},
    {"name":find_image_name + "-10.gif"},
    {"name":find_image_name + "-11.gif"},
    {"name":find_image_name + "-12.gif"},
    {"name":find_image_name + "-13.gif"},
    {"name":find_image_name + "-14.gif"},
    {"name":find_image_name + "-15.gif"},
    {"name":find_image_name + "-16.gif"},
    {"name":find_image_name + "-17.gif"},
    {"name":find_image_name + "-18.gif"},
    {"name":find_image_name + "-19.gif"},
    {"name":find_image_name + "-20.gif"}
]

save_num = 0

for backItem in backgroundA:
    for scaleItem in scaleA:
        for rotationItem in rotationA:
            for colorItem in colorA:
                for centersItem in centersA:
                    #make a dictionary for each combination with some variable name?
                    #maybe just write the json file here?
                    save_num += 1
                    save_name = group_name + "_img" + str(save_num)
                    json_dict = {
                        "save_dir":img_dir,
                        "save_name":save_name,
                        "params":{
                            "background": {
                                "color": backItem[0],
                                "width": backItem[1],
                                "height": backItem[2]
                            },
                            "scale": {
                                "dist": scaleItem[0],
                                "params": scaleItem[1:]
                            },
                            "rotation": {
                                "dist": rotationItem[0],
                                "params": rotationItem[1:]
                            },
                            "color": {
                                "dist": colorItem[0],
                                "args": colorItem[1]
                            },
                            "centers": {
                                "r": centersItem[0],
                                "k": centersItem[1]
                            }
                        },
                        "find_images":find_images,
                        "excluded_images":excluded_images,
                    }
                    with open(json_dir + save_name + ".json", 'w') as json_file:
                        json.dump(json_dict, json_file, indent=4)
