import sys
sys.path.insert(0, "./deps")
from exif import Image
import yaml
import shutil


with open("input.yml", "r") as file:
    config = yaml.safe_load(file)
meta_data_attributes = config["Meta Data Attributes (attribute1, attribute2, ...)"].split(",")
meta_data_values = config["Meta Data Values (Value1,Value2, ... [At least as many as Meta Data Attributes])"].split(",")
flag_attr = config["Attribute With The Flag"]
image_name = config["Image Name"]
new_name = "/challenge/" + image_name
# Open an existing PNG file
with open("input/CP_wallpaper.jpg", "rb") as image_file:
    img = Image(image_file)


# Create a new PngInfo object to hold metadata

# Add new metadata
for i in range(len(meta_data_attributes)):
    attr = meta_data_attributes[i]
    val = meta_data_values[i]
    if(meta_data_attributes[i].strip() == flag_attr.strip()):
        #with open("/flag", "r") as f:
            val = "Bello"#f.readline()
    setattr(img, "Comment", val)

# Save the image with the new metadata
with open("./" + image_name, "wb") as updated_file:
    updated_file.write(img.get_file())

# Verify the metadata
for tag in img.list_all():
    print(f"{tag}: {getattr(img, tag)}")