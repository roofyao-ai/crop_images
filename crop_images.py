# coding=utf-8

import os
import sys
from PIL import Image

def on_error(msg) :
    print(msg, file=sys.stderr)
    print("example: python3 crop_images.py file test.png left 4 top 4 xs 8 ys 8 cropw 48 croph 48 outdir ./", file=sys.stderr)
    sys.exit(-1)

params = {}

def_keys = ["file", "left", "top", "xs", "ys", "cropw", "croph", "outdir"]
key = ""
for argv in sys.argv[1:] :
    if def_keys.count(argv) == 1 :
        key = argv
    else :
        params[key] = argv

def check_keys():
    for def_key in def_keys:
        if params.get(def_key) == None :
            on_error("param not found error: %s" % def_key)

check_keys()

file_path = params["file"]
left_space = int(params["left"])
top_space = int(params["top"])
x_space = int(params["xs"])
y_space = int(params["ys"])
crop_width = int(params["cropw"])
crop_height = int(params["croph"])
out_dir = params["outdir"]

if not os.path.isdir(out_dir) :
    on_error("%s directory does not exists." % out_dir)

image = Image.open(file_path)
file_name = os.path.basename(file_path)
ext_name = ""
dot_index = file_name.find(".")
if dot_index != -1 :
    ext_name = file_name[dot_index:]

y = top_space
row = 0
while y + crop_height <= image.height :
    x = left_space
    col = 0
    while x + crop_width <= image.width :
        image_crop = image.crop(box=(x, y, x+crop_width, y+crop_height))
        image_crop.save("%d_%d%s" % (col, row, ext_name))
        x += crop_width + x_space
        col += 1
    y += crop_height + y_space
    row += 1
