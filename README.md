# DHS_Image_Generation

# Setting the Image Parameters
The code generates an image based on the parameters set in the JSON files.
In the home folder of this project there is a "template.json" that is an example of a working set of parameters used to generate an image.

The following sections will be used to explain how to change the parameters used in a JSON file.

1. `save_dir`
    This is input will dictate where the generated image will be saved. This can be either an absolute or relative path. See two examples below.

   ```json
        "save_dir": "C:/Users/Joshua/Documents/DHS Project/Image_Output/"
   ```
    ```json
        "save_dir": "/Image_Ouput/"
   ```
2. `save_name`
    This input will be the text that is used to name the output files.
    When run three files will be generated.

    1. The image using the input parameters named "<save_name>.png"
    2. Another version of the image that makes the specified find image white named "<save_name>-find.png"
    3. A .json file that contains the input parameters and additional metadata named "<save_name>.json"

3. `background`
    This section includes 3 inputs. The color, length, and height of the background image. A valid entry will be formatted as follows:

    ```json
        "background": {
            "color": "beige",
            "width": 1080,
            "height": 1080
    ```