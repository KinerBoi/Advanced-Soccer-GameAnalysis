import cv2
import os


# Open the default camera
video_path = r"test_videos\WIN_20260721_22_44_52_Pro.mp4."  # Path to your video file
cam = cv2.VideoCapture(video_path)

# Verifying that the video file opened
if not cam.isOpened():
    print("Error: Could not open video file.")
    exit()



def extract_frames(cam, output_folder, frame_rate=1):
    # TODO: make sure output_folder exists before writing to it
    # (os module has a function for creating directories)
    os.makedirs(output_folder, exist_ok=True)

    currentFrame = 0
    frames = []
    while True:
        ret, frame = cam.read()
        if not ret:
            break

        if currentFrame % frame_rate == 0:

            name = f"frame_{currentFrame:04d}.jpg"
            path = os.path.join(output_folder, name)
            cv2.imwrite(path, frame)
            frames.append(frame)

        currentFrame += 1

    cam.release()
    return frames

frames_extracted = extract_frames(cam, "extracted_frames", frame_rate=10)
print(f"Extracted {len(frames_extracted)} frames")