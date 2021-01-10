from determine_LP import * 
from binary_image import *
from get_characters import * 
from predict_character import *
import time

from sklearn import preprocessing, model_selection
import numpy as np

# load model
wpod_net = load_model("wpod-net.json")

json_file = open('MobileNets_character_recognition.json', 'r')
loaded_model_json = json_file.read()
json_file.close()

model = model_from_json(loaded_model_json)
model.load_weights("License_character_recognition_weight.h5")

labels = preprocessing.LabelEncoder()
labels.classes_ = np.load('license_character_classes.npy')
#end load


start = time.time()
image_plate = cv2.imread("bs5.jpg")
img2 = plate_image(image_plate, wpod_net)

im2 = binary_image(img2)

list_top, list_bot = get_characters(im2)

string_top = string_LP(list_top, model, labels)
string_bot = string_LP(list_bot, model, labels)


print(string_top)
print(string_bot)

end = time.time()

print('time ', end - start)

