import cv2
import subprocess

url = "https://www.youtube.com/live/u7GyFcQJs98?si=qu81p7fGHo7NDFWk"

stream = subprocess.check_output(
    ["yt-dlp", "-g", url]
).decode("utf-8").strip()

cap = cv2.VideoCapture(stream)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("Live Stream", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()