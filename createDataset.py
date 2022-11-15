import shutil
import os
import pandas as pd

df = pd.read_csv('kid_f_train.csv', names=['Filename', 'Class'])
labels = df.sort_values('Class')

class_names = list(labels.Class.unique())

# create set of subfolders
for i in class_names:
    os.makedirs(os.path.join('dataset', i))

for c in class_names:
    for i in list(labels[labels['Class'] == c]['Filename']):

        #create path to the image
        get_image = os.path.join('train', i)

        #If image has not already exist in the new folder create one
        if not os.path.exists('dataset/'+c+i):
            # move the image
            # move_image_to_cat = shutil.move(get_image,'test_/'+c)
            copy_image_to_cat = shutil.copy(get_image, 'dataset/'+c)
