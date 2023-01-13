import cv2

WIDTH = 1280
HEIGHT = 720

TARGET_SIZE = 32 * 8

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)

index = 1
while True:
    img = cap.read()[1]
    img = img[:,int((WIDTH - HEIGHT) / 2):int((WIDTH + HEIGHT) / 2)]
    cv2.imshow('Camera', img)

    if cv2.waitKey(1) & 0xFF == ord("c"):
        directory = 'datasets/newData/'
        fileName = 'img_{}.jpg'.format(index)
        
        img = cv2.resize(img, [TARGET_SIZE, TARGET_SIZE])
        cv2.imwrite(directory + fileName, img)
        print(index)
        index += 1
        continue
        