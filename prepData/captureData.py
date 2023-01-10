import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

index = 1
while True:
    img = cap.read()[1]
    img = img[:,0:480]
    img = cv2.resize(img, [360, 360])
    cv2.imshow('Camera', img)

    # if cv2.waitKey(1) & 0xFF == ord("q"):
    #     break

    if cv2.waitKey(1) & 0xFF == ord("t"):
        directory = 'datasets/raw/'
        fileName = 'raw_{}.jpg'.format(index)

        cv2.imwrite(directory + fileName, img)
        print(index)
        index += 1
        continue
        