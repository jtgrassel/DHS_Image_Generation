import random

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
    if dist == "M":
        newColor = (
            
        )
    return newColor

with open(json_dir) as f:
    json_data = json.load(f)

params = json_data['params']

"color":colorRandomizer(
    params["color"]["dist"], 
    params["color"]["channels"]["red"], 
    params["color"]["channels"]["green"],
    params["color"]["channels"]["blue"],
    params["color"]["channels"]["alpha"]
)