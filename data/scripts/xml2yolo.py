import os
import tqdm
import xml.etree.ElementTree as ET

path = "../../../datasets/mask/annotations"
new_path = path.replace("annotations", "labels")

classes = ["with_mask", "without_mask"]


def convert(size, box):
    dw = 1.0 / size[0]
    dh = 1.0 / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


if not os.path.exists(new_path):
    os.makedirs(new_path)
    print("Created directory: ", new_path)


def convert_annotation(image_id):
    in_file = open(os.path.join(path, image_id + ".xml"))
    out_file = open(os.path.join(new_path, image_id + ".txt"), "w")
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find("size")
    w = int(size.find("width").text)
    h = int(size.find("height").text)

    for obj in root.iter("object"):
        cls = obj.find("name").text
        if cls not in classes:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find("bndbox")
        b = (float(xmlbox.find("xmin").text), float(xmlbox.find("xmax").text), float(xmlbox.find("ymin").text),
             float(xmlbox.find("ymax").text))
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + "\n")

    in_file.close()
    out_file.close()


for file in tqdm.tqdm(os.listdir(path)):
    image_id = file.split(".")[0]
    convert_annotation(image_id)

print("Done")
