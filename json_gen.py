import json

json_dir = "JSON_Files/"
img_dir = "temp/DOEtest/"
group_name = "no_bat"

#make arrays for all the parameters
#save name?

backgroundA = [
    ("beige", 1080, 1080)
]

scaleA = [("T", .15, .2, .25), ("T", .25, .3, .35), ("T", .35, .4, .45)]

rotationA = [("U", 0, 365), ("T", -15, 0, 15)]

colorA = [
    ("U", (10, 255), (10, 255), (10, 255), (140, 170)), 
    ("U", (10, 255), (10, 255), (10, 255), (100, 200)), 
    ("T", (202, 212, 222), (77, 87, 97), (227, 237, 247), (130, 155, 180)),
    ("T", (0, 30, 60), (120, 150, 180), (137, 167, 197), (130, 155, 180))
]

centersA = [(100, 32), (125, 32), (150, 32)]

find_images = [
    # {"name":"butterfly-14.gif", "depth":0.5},
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
                                "channels": {
                                    "red": colorItem[1],
                                    "green": colorItem[2],
                                    "blue": colorItem[3],
                                    "alpha": colorItem[4]
                                }
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
