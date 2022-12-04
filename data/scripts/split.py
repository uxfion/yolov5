import os
import random
import tqdm

path = "../../../datasets/mask/images"

percentage = "9:1:0"

train = int(percentage.split(":")[0])
val = int(percentage.split(":")[1])
test = int(percentage.split(":")[2])

print("train: ", train)
print("val: ", val)
print("test: ", test)

train_percent = train / (train + val + test)
val_percent = val / (train + val + test)
test_percent = test / (train + val + test)

print("train_percent: ", train_percent)
print("val_percent: ", val_percent)
print("test_percent: ", test_percent)

total = len(os.listdir(path))
print("total: ", total)

# clean files
if os.path.exists(os.path.join(path, "../train.txt")):
    os.remove(os.path.join(path, "../train.txt"))
    print("removed train.txt")
if os.path.exists(os.path.join(path, "../val.txt")):
    os.remove(os.path.join(path, "../val.txt"))
    print("removed val.txt")
if os.path.exists(os.path.join(path, "../test.txt")):
    os.remove(os.path.join(path, "../test.txt"))
    print("removed test.txt")

# create train.txt at father directory
train_file = open(os.path.join(path, "../train.txt"), "w")
val_file = open(os.path.join(path, "../val.txt"), "w")
test_file = open(os.path.join(path, "../test.txt"), "w")

for file in tqdm.tqdm(os.listdir(path)):
    if random.random() < train_percent:
        train_file.write("./images/" + file + "\n")
    elif random.random() < val_percent:
        val_file.write("./images/" + file + "\n")
    elif random.random() < test_percent:
        test_file.write("./images/" + file + "\n")

train_file.close()
print("train.txt created")
val_file.close()
print("val.txt created")
test_file.close()
print("test.txt created")

print("Done")
