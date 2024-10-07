# Violent_Videos_Classification

Extracting frames from violent and non-violent videos using OpenCV library. 
Building two models one using CNN-RNN architecture and the other one using pretrained Mobilnet model and LSTM and the integration of YOLOv8 and YOLO-NAS for detection. 
Training the model and getting up to 94% accuracy using Mobilnet-LSTM architecture. Deploying the model using Flask and containerizing it using Docker.

Technologies: TensorFlow, Keras, CNN, LSTM, Mobilnet, YOLO, Fine-tuning, OpenCV, Flask, Docker.


Build the Docker image:
docker build -t vid_class .

Run the container on a port of your choice:
docker container run -it -p 4000:5000 vid_class

Access the page in a browser: Open your browser and go to:
http://localhost:4000/
