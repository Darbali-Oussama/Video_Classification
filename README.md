# Violent_Videos_Classification

This project focuses on classifying violent and non-violent videos by extracting frames using the OpenCV library. Two different models are developed:

1. A CNN-RNN architecture.
2. A model combining a pretrained Mobilenet with LSTM, enhanced by YOLOv8 and YOLO-NAS for object detection.

The Mobilenet-LSTM architecture achieved up to 94% accuracy during training. The model is deployed with Flask and containerized using Docker for easy deployment.

### Technologies Used:
- TensorFlow, Keras
- CNN, LSTM
- Mobilenet, YOLOv8, YOLO-NAS
- OpenCV, Flask, Docker
- Fine-tuning and Transfer Learning

### How to Build and Run

1. **Build the Docker image:**
   ```bash
   docker build -t vid_class .

2. **Run the container (choose a port):**
   ```bash
   docker run -it -p 4000:5000 vid_class

3. **Access the web application: Open your browser and visit:**
   ```bash
   http://localhost:4000/
