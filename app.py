import cv2
import keras
import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)


NB_IMGS_FROM_VID = 15
IMAGE_HEIGHT , IMAGE_WIDTH = 64, 64

dic = {0 : 'NonViolence', 1 : 'Violence'}

model = keras.models.load_model("models/CNN_LSTM_model.keras")
model2 = keras.models.load_model("models/mobilnet_LSTM_model.keras")

def predict_label(video_path , model_p):
 
    video_reader = cv2.VideoCapture(video_path)
    frames_count = int(video_reader.get(cv2.CAP_PROP_FRAME_COUNT))
    pas = max(int(frames_count/NB_IMGS_FROM_VID), 1)
    
    frames = []

    for i in range(NB_IMGS_FROM_VID):
        video_reader.set(cv2.CAP_PROP_POS_FRAMES, i * pas)
        success, frame = video_reader.read() 
        if not success:
            break
        resized_frame = cv2.resize(frame, (IMAGE_HEIGHT, IMAGE_WIDTH))
        
        #Normalisation
        normalized_frame = resized_frame / 255
        
        frames.append(normalized_frame)
    
    video_reader.release()
    frmvid = np.expand_dims(frames, axis = 0)
    p=model_p.predict(frmvid)
    predicted_label = np.argmax(p)
 
    # Get the class name using the retrieved index.
    predicted_class_name = dic[predicted_label]
    pr_val = p[0][predicted_label]
    return f'Predicted: {predicted_class_name}\n, Confidence: {"%.3f"}' % pr_val

# routes
@app.route("/", methods=['GET', 'POST'])
def main():
	return render_template("index.html")

@app.route("/submit", methods = ['GET', 'POST'])
def get_output():
	if request.method == 'POST':
		vid = request.files['video']

		vid_path = "uploaded_videos/" + vid.filename	
		vid.save(vid_path)
  
		p , p2= predict_label(vid_path, model), predict_label(vid_path, model2)
        
	return render_template("index.html", prediction = p,prediction2 = p2)


if __name__ =='__main__':
	app.run(debug = True)