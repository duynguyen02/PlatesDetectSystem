import cv2
import torch

import function.utils_rotate as utils_rotate
import function.helper as helper

from app_utils import *
from app_utils.threading_video_capture import ThreadingVideoCapture
from service.database import get_approved_plate_by_id
from service.mqtt import door, jetson


def run():
    # load model
    yolo_LP_detect = torch.hub.load('yolov5', 'custom', path='model/LP_detector_nano_61.pt', force_reload=True,
                                    source='local')
    yolo_license_plate = torch.hub.load('yolov5', 'custom', path='model/LP_ocr_nano_62.pt', force_reload=True,
                                        source='local')
    yolo_license_plate.conf = 0.60

    prev_frame_time = 0
    new_frame_time = 0

    cap = ThreadingVideoCapture(0)

    # door state manager
    checked_plates = []
    open_at = None
    open_remain = 0

    while True:

        frame = cap.read()

        plates = yolo_LP_detect(frame, size=640)
        list_plates = plates.pandas().xyxy[0].values.tolist()
        list_read_plates = set()
        for plate in list_plates:
            flag = 0
            x = int(plate[0])  # xmin
            y = int(plate[1])  # ymin
            w = int(plate[2] - plate[0])  # xmax - xmin
            h = int(plate[3] - plate[1])  # ymax - ymin
            crop_img = frame[y:y + h, x:x + w]
            cv2.rectangle(frame, (int(plate[0]), int(plate[1])), (int(plate[2]), int(plate[3])), color=(0, 0, 225),
                          thickness=2)
            # cv2.imwrite("crop.jpg", crop_img)
            # rc_image = cv2.imread("crop.jpg")
            lp = ""
            for cc in range(0, 2):
                for ct in range(0, 2):
                    lp = helper.read_plate(yolo_license_plate, utils_rotate.deskew(crop_img, cc, ct))
                    if lp != "unknown":
                        list_read_plates.add(lp)

                        if get_approved_plate_by_id(lp):

                            if lp not in checked_plates:
                                checked_plates.append(lp)
                                open_remain += int(OPEN_TIME) * 1000

                            cv2.putText(frame, f"{lp} : Approved", (int(plate[0]), int(plate[1] - 10)),
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.9,
                                        (36, 255, 12), 2)
                        else:
                            cv2.putText(frame, f"{lp} : Denied", (int(plate[0]), int(plate[1] - 10)),
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.9,
                                        (255, 0, 0), 2)

                        flag = 1
                        break
                if flag == 1:
                    break
        new_frame_time = time.time()
        fps = 1 / (new_frame_time - prev_frame_time)
        prev_frame_time = new_frame_time
        fps = int(fps)
        # cv2.putText(frame, str(fps), (7, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (100, 255, 0), 3, cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        if open_at is not None:
            time_open = open_at + open_remain
            remain = time_open - current_milli_time()
            print(remain)
            if remain <= 0:
                open_at = None
                open_remain = 0
                checked_plates.clear()
                print("Closing...")
                # door.close_the_door()
                jetson.open()

        else:
            if len(checked_plates) > 0:
                open_at = current_milli_time()
                print("Opening...")
                # door.open_the_door()
                jetson.close()

    cap.release()
    cv2.destroyAllWindows()
