import numpy as np
import cv2

def predict_from_model(image,model,labels):
    image = cv2.resize(image,(80,80))
    image = np.stack((image,)*3, axis=-1)
    prediction = labels.inverse_transform([np.argmax(model.predict(image[np.newaxis,:]))])
    return prediction

def string_LP(list_image, model, labels):
	final_string=''
	for i in list_image:
		title = np.array2string(predict_from_model(i,model,labels))
		final_string+=title.strip("'[]")
	return final_string
