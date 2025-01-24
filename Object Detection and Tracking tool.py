#import libraries

import torch
import cv2
import numpy as np



#Load YOLOv5 model

model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)



#Define a function to perform object detection and tracking

    def detect_and_track(video_source=0):
    
#Open video capture (0 for webcam or provide video file path)
    
    cap = cv2.VideoCapture(video_source)



if not cap.isOpened():
    print("Error: Could not open video source.")
    return

while True:
    ret, frame = cap.read()
    if not ret:
        print("End of video stream or error.")
        break



#Perform object detection
    results = model(frame)

#Extract detection results
    detections = results.xyxy[0].cpu().numpy()  #Bounding boxes and other data



for det in detections:
            x1, y1, x2, y2, conf, cls = det
            label = f"{model.names[int(cls)]} {conf:.2f}"



#Draw bounding boxes and labels on the frame

    cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
    cv2.putText(frame, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)



#Display the resulting frame

    cv2.imshow('Object Detection and Tracking', frame)

#Break the loop if 'q' is pressed

    if cv2.waitKey(1) & 0xFF == ord('q'):
    break


#Release resources

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    detect_and_track()

