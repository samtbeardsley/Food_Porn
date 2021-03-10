import numpy as np
import tensorflow as tf
from tensorflow.keras.models import model_from_json
from keras.models import load_model
from tensorflow import keras
import gradio as gr


#load model
json_file = open('Model/model.json','r')
model_json = json_file.read()
json_file.close()
model = model_from_json(model_json)
model.load_weights('Model/model.h5')
model.compile(loss='categorical_crossentropy',optimizer='adam', metrics=['accuracy'])


# define predict functionality
def gradio_predict(image):
    '''resize image and predict'''

    image = np.resize(image, (224, 224, 3))

    # predict results
    result = model.predict(image[None])
    result = result[0][0]
    result = np.around(result*100,2)

    if result < 25:
        prediction = f"Congrats it's #foodporn! I'm {100-result}% sure."
    elif (result <= 25) and (result < 50):
        prediction = f"Could use some more work, but I think its {100-result}% #foodporn"
    elif (result >= 50) and (result < 75):
        prediction = f"I'm {(result)}% sure this is not #foodporn."
    else:
        prediction = f"Are you sure this is food? I'm {(result)}% sure this is #gross. Try again!"    
    return prediction



# customize interface
title = 'The Food Pornographer'

description = 'Upload your food photos to see what the model thinks. Are they #foodporn or #gross?'

article = '<p>The Food Pornographer is a convolutional neural network made using transfer learning with the ResNet50 architecture. If you would like to learn more about this project you can visit my github <a href="https://github.com/samtbeardsley/Food_Porn">here</a> or drop me a line at <a href="mailto: samtbeardsley@gmail.com">samtbeardsley@gmail.com</a>! <br /><br />Need some examples? Try these:</p> <ul type="square"> <li><a href="https://github.com/samtbeardsley/Food_Porn/blob/master/Gradio/Sample%20Images/Sample%201.jpg"> sample 1 </a></li> <li><a href="https://github.com/samtbeardsley/Food_Porn/blob/master/Gradio/Sample%20Images/Sample%202.jpg"> sample 2 </a></li> <li><a href="https://github.com/samtbeardsley/Food_Porn/blob/master/Gradio/Sample%20Images/Sample%203.jpg"> sample 3 </a></li> </ul>'
iface = gr.Interface(gradio_predict, gr.inputs.Image(), "text", title=title, description=description, article=article)
iface.launch()
