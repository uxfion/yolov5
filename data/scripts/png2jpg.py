import os
import cv2
import tqdm

path = "../../../datasets/mask/images"
# new_path = "../../datasets/mask/images"
new_path = path.replace("images", "images-jpg")

if not os.path.exists(new_path):
    os.makedirs(new_path)
    print("Created directory: ", new_path)

for file in tqdm.tqdm(os.listdir(path)):
    img = cv2.imread(os.path.join(path, file))
    cv2.imwrite(os.path.join(new_path, file.replace("png", "jpg")), img)

# rename images to images-png
os.rename(path, path.replace("images", "images-png"))
print("moved images to images-png")
os.rename(new_path, path)
print("moved images-jpg to images")

print("Done")
