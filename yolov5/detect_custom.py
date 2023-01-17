import tensorflow as tf
import cv2
import numpy as np

cam = cv2.VideoCapture(0)
yolo_model = tf.lite.Interpreter("/Users/cheruichang/Desktop/checkpoints/yolov5s_v1.tflite")
yolo_model.allocate_tensors()
input_details = yolo_model.get_input_details()
output_details = yolo_model.get_output_details()
input = input_details[0]


def run_model(im):  # returns yolov5 output tensor

    yolo_model.set_tensor(input['index'], im)
    yolo_model.invoke()
    y = []
    for output in output_details:
        x = yolo_model.get_tensor(output['index'])

        y.append(x)
    y = [x if isinstance(x, np.ndarray) else x.numpy() for x in y]
    return y


def process_preds(preds, thres=0.5):
    results = []
    for i, pred in enumerate(preds[0][0]):
        if pred[4] >= thres:
            if len(results) == 0:
                results.append(i)
            else:
                # Compute the distance between the centers of bboxes to see if it is redundant
                redundant = False
                for bbox in results:
                    dist = ((pred[0] - preds[0][0][bbox][0])**2 + (pred[1] - preds[0][0][bbox][1])**2) ** (1/2)
                    if dist < 0.01:
                        print("this box is redundant, not plotted")
                        redundant = True
                if not redundant:
                    results.append(i)
    return results


def plot_boxes(image, results, preds):
    # Gets the image shape
    W, H, C = image.shape
    # Plots all the bboxes out on to the image
    for index in results:
        pred = preds[0][0][index]
        xc, yc, w, h = pred[:4]

        # Computes the bbox in xyxy form
        xmin = int((xc - w / 2) * W)
        ymin = int((yc - h / 2) * H)
        xmax = int((xc + w / 2) * W)
        ymax = int((yc + h / 2) * H)

        # Draws the bbox
        cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (0, 255, 0), 1)

        score_str = " {:.2f}".format(pred[4])
        label = 'fitting' + score_str
        # get text size
        (text_width, text_height), baseline = cv2.getTextSize(label, cv2.FONT_HERSHEY_COMPLEX_SMALL,
                                                              1.5, thickness=2)
        # put filled text rectangle
        cv2.rectangle(image, (xmin, ymin), (xmin + text_width, ymin - text_height - baseline), (0, 255, 0), thickness=cv2.FILLED)

        # put text above rectangle
        cv2.putText(image, label, (xmin, ymin - 4), cv2.FONT_HERSHEY_COMPLEX_SMALL,
                    1.5, (255, 0, 0), 2, lineType=cv2.LINE_AA)
    return image


def main():
    while True:
        _, image = cam.read()

        # Image preprocess
        image = image[:, 280:1001]
        im = cv2.resize(image, (320, 320))
        im = im.astype(np.float32)
        im /= 255
        im = im[None]

        # Inference
        preds = run_model(im)

        # Gets the bboxes
        bboxes = process_preds(preds, 0.5)

        # Plot the bboxes out on the image
        pred_img = plot_boxes(image, bboxes, preds)

        # Display the image
        cv2.imshow("img", pred_img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
