import tensorflow as tf
import cv2
import numpy as np
import time
import os


yolo_model = tf.lite.Interpreter("/Users/cheruichang/Desktop/checkpoints/fitting_yolov5s_v12.tflite")
yolo_model.allocate_tensors()
input_details = yolo_model.get_input_details()
output_details = yolo_model.get_output_details()
input = input_details[0]
box_colors = {0: (0, 255, 0),
              1: (0, 255, 255),
              2: (255, 255, 0),
              3: (255, 0, 255),
              4: (200, 0, 200),
              5: (200, 200, 0),
              6: (0, 200, 200),
              7: (200, 200, 200),
              8: (170, 170, 0),
              9: (170, 0, 170),
              10: (0, 170, 170)
              }


def run_model(im):  # returns yolov5 output tensor
    yolo_model.set_tensor(input['index'], im)
    yolo_model.invoke()
    y = []
    for output in output_details:
        x = yolo_model.get_tensor(output['index'])
        y.append(x)
    y = [x if isinstance(x, np.ndarray) else x.numpy() for x in y]
    return y


def plot_boxes(image, results, preds):
    # Gets the image shape
    W, H, C = image.shape
    # Plots all the bboxes out on to the image
    for i, index in enumerate(results):
        pred = preds[0][0][index]
        xc, yc, w, h = pred[:4]

        label = '{}'.format(i)
        b_color = box_colors[i]
        # Computes the bbox in xyxy form
        xmin, ymin, xmax, ymax = int((xc - w / 2) * W), int((yc - h / 2) * H), int((xc + w / 2) * W), int((yc + h / 2) * H)

        # Draws the bbox
        cv2.rectangle(image, (xmin, ymin), (xmax, ymax), b_color, 2)

        # # put text above rectangle
        # cv2.putText(image, label, (xmin, ymin - 4), cv2.FONT_HERSHEY_COMPLEX_SMALL,
        #             2, b_color, 2, lineType=cv2.LINE_AA)
    return image


def iou_filter(image, preds, thres=0.5, iou_thres=0.25):
    results = []
    for i, pred in enumerate(preds[0][0]):
        if pred[4] >= thres:
            if len(results) == 0:
                results.append(i)
            else:
                redundant = False
                for bbox in results:
                    iou = iou_calculate(image, pred[:4], preds[0][0][bbox][:4])
                    if iou > iou_thres:
                        redundant = True
                if not redundant:
                    results.append(i)
    return results


def iou_calculate(image, rect1, rect2):
    inter = overlap(image, rect1, rect2)
    if inter:
        return inter / (area(image, rect1) + area(image, rect2) - inter)
    else:
        return 0


def area(image, rect):
    W, H, C = image.shape
    # Computes the bbox in xyxy form
    xmin, ymin = int((rect[0] - rect[2] / 2) * W), int((rect[1] - rect[3] / 2) * H)
    xmax, ymax = int((rect[0] + rect[2] / 2) * W), int((rect[1] + rect[3] / 2) * H)
    return (xmax - xmin) * (ymax - ymin)


def overlap(image, rect1, rect2):  # returns None if rectangles don't intersect
    W, H, C = image.shape

    # Computes the bbox in xyxy form
    xmin1, ymin1 = int((rect1[0] - rect1[2] / 2) * W), int((rect1[1] - rect1[3] / 2) * H)
    xmax1, ymax1 = int((rect1[0] + rect1[2] / 2) * W), int((rect1[1] + rect1[3] / 2) * H)
    xmin2, ymin2 = int((rect2[0] - rect2[2] / 2) * W), int((rect2[1] - rect2[3] / 2) * H)
    xmax2, ymax2 = int((rect2[0] + rect2[2] / 2) * W), int((rect2[1] + rect2[3] / 2) * H)

    dx = min(xmax1, xmax2) - max(xmin1, xmin2)
    dy = min(ymax1, ymax2) - max(ymin1, ymin2)

    if (dx >= 0) and (dy >= 0):
        return dx*dy


def bbox_dist_filter(preds, thres=0.5):
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
                        redundant = True
                if not redundant:
                    results.append(i)
    return results


def xywh2xyxy(image, indices, preds):
    W, H, C = image.shape
    result = []
    # Plots all the bboxes out on to the image
    for index in indices:
        pred = preds[0][0][index]
        xc, yc, w, h = pred[:4]

        # Computes the bbox in xyxy form
        xmin, ymin, xmax, ymax = int((xc - w / 2) * W), int((yc - h / 2) * H), int((xc + w / 2) * W), int((yc + h / 2) * H)

        result.append([xmin, ymin, xmax, ymax])

    return result


def xywh(indices, preds):
    results = []
    for index in indices:
        pred = preds[0][0][index]
        results.append(pred[:4])
    return results


def ann_image(image):
    try:
        im = cv2.resize(image, (320, 320))
        im = [im.astype(np.float32) / 255]
        # Inference
        preds = run_model(im)

        # Gets the bboxes
        indices = iou_filter(image, preds, 0.5)

        # Plot the bboxes out on the image
        pred_img = plot_boxes(image, indices, preds)

        bboxes = xywh(indices, preds)

        return pred_img, bboxes
    except Exception as e:
        print(e)
