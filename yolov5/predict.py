import torch
import cv2
import time

model = torch.hub.load('C:\\Users\\Martin Zhu\\PycharmProjects\\ObjectDetection\\yolov5', 'custom', 'runs/train/exp4/weights/best.pt', source='local')
model.conf = 0.6

pTime = 0
cTime = 0

print()
print('====== Moded loading is comleted ======')
print()

cap = cv2.VideoCapture(0)

while True:
    img = cap.read()[1]
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    results = model(img, size=160)
    data = results.pandas().xyxy[0]

    nums = len(data)
    for i in range(nums):
        obj = data.iloc[i]
        xmin = int(obj['xmin'])
        ymin = int(obj['ymin'])
        xmax = int(obj['xmax'])
        ymax = int(obj['ymax'])
        conf = obj['confidence']
        name = obj['name']

        textSize = cv2.getTextSize("{:.2f}".format(conf), cv2.FONT_HERSHEY_PLAIN, 1.2, 2)
        textWidth = textSize[0][0]
        textHeight = textSize[0][1]

        cv2.rectangle(img, (xmin, ymin - textHeight - 10), (xmin + textWidth + 10, ymin), (0, 255, 0), -1)
        cv2.putText(img, "{:.2f}".format(conf), (xmin + 5, ymin - 5), cv2.FONT_HERSHEY_PLAIN, 1.2, (255, 255, 255), 2)
        
        cv2.rectangle(img, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)


    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, "FPS: " + str(int(fps)), (5, 40), cv2.FONT_HERSHEY_PLAIN, 1.8, (0, 255, 0), 2)
    cv2.putText(img, "Detected: " + str(nums), (5, 70), cv2.FONT_HERSHEY_PLAIN, 1.8, (0, 255, 0), 2)

    cv2.imshow('camera', img)



    if cv2.waitKey(1) & 0xFF == ord("q"):
        break