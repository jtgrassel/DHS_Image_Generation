from numpy.core.fromnumeric import repeat
from image_generator_fun import allFiles
from image_generator_fun import imageGen
import multiprocessing as mp
from p_tqdm import p_map
from functools import partial
from itertools import repeat

# Location of the JSON file(s) that you wish to use to generate image(s) from
# JSON files should be formatted as the "template.json" file
jsonDir = "Input_JSON/"

# Location of the unedited MPEG7 images
# The MPEG7 dataset can be found at the following link: http://www.timeseriesclassification.com/description.php?Dataset=ShapesAll
mpeg7Dir = "MPEG7/"

jsonFiles = allFiles(jsonDir)  # Gets all the JSON files in the provided folder

# Generates an image for each JSON file provided

image_count = 5
# imageGen(jsonDir + jsonFiles[0], mpeg7Dir, 0)
args = {
    'json_dir': jsonDir + jsonFiles[0],
    'mpeg7Dir': mpeg7Dir,
}
pool = mp.Pool(2)
pool.starmap(imageGen, zip(repeat(args), range(image_count)))
# p_map(partial(imageGen, jsonDir + jsonFiles[0], mpeg7Dir), range(image_count))
pool.close()
# for jsonFile in jsonFiles:
#     imageGen(jsonDir + jsonFile, mpeg7Dir, save_index)
#     count += 1
#     status = round(count * progressMult, 2)
#     print("Status:" + str(status))

print("Complete")
