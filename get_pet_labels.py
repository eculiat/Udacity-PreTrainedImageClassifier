#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Esteban R. Culiat 
# DATE CREATED: 1 Dec 2018                                 
# REVISED DATE: 1 Dec 2018
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Replace None with the results_dic dictionary that you created with this
    # function
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Esteban R. Culiat 
# DATE CREATED: 1 Dec 2018                                 
# REVISED DATE: 1 Dec 2018
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Replace None with the results_dic dictionary that you created with this
    # function

    # get list of filenames in the image directory
    filename_list = listdir(image_dir)
    results_dic = dict()
    pet_labels = []
    
    # make a list of pet labels
    def make_pet_labels(list):   
        # loop through each item or filename in the list of filenames
        for item in list:
            if item[0] != "." :
                print("true file<<<<<<<<<<<<<<<")
                lcase_item = item.lower()                # lower case
                lcase_item_list = lcase_item.split("_")  # split "_"
                temp_item = ""
                # since the filename was split from "_" go through the list
                for sub_item in lcase_item_list:
                    # disregard sub_item with "." ie 03750.jpg
                    if sub_item.find(".") == -1:
                        temp_item += " " + sub_item
                temp_item = temp_item.strip()
                print(temp_item)
                pet_labels.append(temp_item)
                #print(temp_item)
            else:
                print("file begins with . <<<<<<<<<<<<")
       
        return pet_labels
                    
    # process each file name in the list
    make_pet_labels(filename_list)
   
    for i in range(0, len(filename_list), 1):
        filename = filename_list[i]
        if filename in results_dic:
            print("Warning: Key already exists in results_dic")
        else:
            results_dic[filename] = [pet_labels[i]]
            
        #print(results_dic)
    return results_dic