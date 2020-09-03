import glob
import os
current_dir = # PATH TO IMAGE DIRECTORY
# /dataset/baram
# /dataset/baram/obj.data
    # classes= 80
    # train  = data/train.txt
    # valid  = data/train.txt
    # names = data/obj.names
    # backup = backup/

# /dataset/baram/obj.names <- labelImg 
# /dataset/baram/data/quest
# /dataset/baram/data/hunter_book
# /dataset/baram/data/quest/1
# /dataset/baram/data/quest/1/1.jpg
# /dataset/baram/data/quest/1/1.txt
# /dataset/baram/data/quest/2
# /dataset/baram/data/quest/3
# /dataset/baram/data/quest/4


# Percentage of images to be used for the valid set
percentage_test = 10;
# Create train.txt and valid.txt
file_train = open('train.txt', 'w')  
file_test = open('valid.txt', 'w')
# Populate train.txt and valid.txt
counter = 1  
index_test = round(100 / percentage_test)  
for file in glob.iglob(os.path.join(current_dir, '*.jpg')):  
    title, ext = os.path.splitext(os.path.basename(file))
    if counter == index_test:
        counter = 1
        file_test.write(current_dir + "/" + title + '.jpg' + "\n")
    else:
        file_train.write(current_dir + "/" + title + '.jpg' + "\n")
        counter = counter + 1