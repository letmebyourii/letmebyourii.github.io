# letmebyourii.github.io

Let Me Be Your Eyes demo uses computer vision to detect and label objects in uploaded images. It is built with Flask and powered by YOLOv8n, the nano variant of Ultralytics' YOLOv8 architecture. It is trained on the Open Images V7 dataset, which covers over 600 everyday object classes. When a user uploads an image, the model processes it through a forward pass and draws bounding boxes around detected objects. The model returns an annotated image directly in the browser. We chose the yolov8n-oiv7 model for its accuracy and speed, and it will be utilized in our long-term project of creating a real-time navigation website. 

