import time

import cv2
import numpy as np

THRESHOLD = 25

prev_tick = cv2.getTickCount()
frame_number, prev_change_frame = 0, 0
is_dark = True

CAP = cv2.VideoCapture(0)

while(True):
    frame_number += 1

    ret, frame = CAP.read()
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    avg = np.average(img)

    is_now_dark = np.average(img) < THRESHOLD

    if is_dark != is_now_dark:
        is_dark = is_now_dark
        new = cv2.getTickCount()

        print("{:.3f} sec, {:.3f} frames".format(
            (new - prev_tick) / cv2.getTickFrequency(),
            frame_number - prev_change_frame
        ))
        prev_tick = new

        prev_change_frame = frame_number

        fill_color = 255 if is_dark else 0
        show = np.full(img.shape, fill_color, dtype=img.dtype)

        cv2.imshow('frame', show)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

CAP.release()
cv2.destroyAllWindows()