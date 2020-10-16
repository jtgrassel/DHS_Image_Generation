import json

json_dir = "JSON_Files"

#make arrays for all the parameters
#save name?

backgroundA = [("white, black")]
widthA = [(1920)]
heightA = [(1080)]

scaleA = [("U", 0.3, 0.4)]

rotationA = [("U", 0, 365)]

colorA = [
    ("U", (10, 255), (10, 255), (10, 255), (150, 180))
]

centersA = [(150, 32)]

findImgA = [("bat-7.gif", 0.5)]

excBat = []
for i in range(1,21):
    excBat.append("bat-" + str(i) + ".gif")

excImgA = [excBat]

save_num = 0





# for backItem in backgroundA:
#     for widthItem in widthA:
#         for scaleItem in scaleA:
#             for rotationItem in rotationA:
#                 for colorItem in colorA:
#                     for centersItem in centersA:
#                         for findImgItem in findImgA:
#                             for excImgItem in excImgA:
#                                 #make a dictionary for each combination with some variable name?
#                                 #maybe just write the json file here?
#                                 save_name = "img" + str(save_num) + ".json"
#                                 json_dict = {
#                                     "save_dir":json_dir,
#                                     "save_name":save_name,
#                                     "params":{
#                                         "background":
#                                     },
#                                     "find_images":find_images,
#                                     "excluded_images":excluded_images,
#                                 }

