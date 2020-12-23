# DHS_Image_Generation

##Setting the Image Parameters
The code generates an image based on the parameters set in the JSON files.
In the home folder of this project there is a "template.json" that is an example of a working set of parameters used to generate an image.

The following sections will be used to explain how to change the parameters used in a JSON file.

1. `size-limit` section in `package.json`:

   ```json
     "size-limit": [
       {
         "path": "index.js",
         "import": "{ createStore }",
         "limit": "500 ms"
       }
     ]
   ```
