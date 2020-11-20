import json

json_dir = "C:/Users/Joshua/Documents/DHS Project/JSON_Files/"
img_dir = "C:/Users/Joshua/Documents/DHS Project/temp/"
group_name = "turtle"

#make arrays for all the parameters
#save name?

backgroundA = [
    ("beige", 1080, 1080)
]

scaleA = [("T", .15, .2, .25)]

rotationA = [("U", 0, 365)]

colorA = [
    ("M", ((255, 0, 0, 100), (0, 255, 0, 100), (0, 0, 255, 100)))
]

centersA = [(100, 32)]

find_images = [
    {"name":"turtle-10.gif", "depth":0.5},
]

excluded_images = [
    {"name":"turtle-1.gif"},
    {"name":"turtle-2.gif"},
    {"name":"turtle-3.gif"},
    {"name":"turtle-4.gif"},
    {"name":"turtle-5.gif"},
    {"name":"turtle-6.gif"},
    {"name":"turtle-7.gif"},
    {"name":"turtle-8.gif"},
    {"name":"turtle-9.gif"},
    {"name":"turtle-10.gif"},
    {"name":"turtle-11.gif"},
    {"name":"turtle-12.gif"},
    {"name":"turtle-13.gif"},
    {"name":"turtle-14.gif"},
    {"name":"turtle-15.gif"},
    {"name":"turtle-16.gif"},
    {"name":"turtle-17.gif"},
    {"name":"turtle-18.gif"},
    {"name":"turtle-19.gif"},
    {"name":"turtle-20.gif"}
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
