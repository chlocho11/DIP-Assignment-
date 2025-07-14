# -*- coding: utf-8 -*-
"""
Created on Sun Jul 13 11:43:42 2025

@author: chloe
"""

import cv2

#open both videos
main_vid = cv2.VideoCapture(r"C:/Users/chloe/Downloads/Digital image/Assignent/CSC2014- Group Assignment_Aug-2025/street.mp4")
talk_vid = cv2.VideoCapture(r"C:/Users/chloe/Downloads/Digital image/Assignent/CSC2014- Group Assignment_Aug-2025/talking.mp4")
# enter video path

#check if vid opened successfully
if not main_vid.isOpened():
    print(" Failed to open main video.")
if not talk_vid.isOpened():
    print(" Failed to open talking video.")

#new vid
out = cv2.VideoWriter ("processed_video.avi",
                       cv2.VideoWriter_fourcc(*"MJPG"),
                       30.0,
                       (1280, 720))

# get total number of frame in main
total_no_frames = main_vid.get(cv2.CAP_PROP_FRAME_COUNT)
print(f" Total frames to process: {total_no_frames}")

for frame_count in range(0, int(total_no_frames)):
    success_main, frame = main_vid.read()
    success_talk, talk_frame = talk_vid.read()

    if not success_main:
        print(f"Failed to read frame {frame_count} from main video.")
        break

    if success_talk:
        #resize and overlay
        talk_frame = cv2.resize(talk_frame, (320, 180))
        frame[40:220, 40:360] = talk_frame

    else:
        print(f"No more talking at frame {frame_count}, showing main only.")


    #show
    cv2.imshow("Overlay Preview", frame)
    cv2.waitKey(1)

    out.write(frame)

print("Processing complete. Output saved as 'processed_video.avi'.")

main_vid.release()
talk_vid.release()
out.release()
cv2.destroyAllWindows()