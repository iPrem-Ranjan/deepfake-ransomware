import cv2
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh
faceMesh = mp_face_mesh.FaceMesh()

cam=cv2.VideoCapture(0)

while True:
    check,frame = cam.read()
    height, width, _ = frame.shape
    result = faceMesh.process(frame)
    # print(result)
    try:
        for facial_landmarks in result.multi_face_landmarks:
            for i in range(0, 500):
                landmrk = facial_landmarks.landmark[i]
                locx = int(landmrk.x * width)
                locy = int(landmrk.y * height)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                cv2.circle(frame, (locx, locy), 1, (0, 200, 0), 0)
                cv2.imshow("Image", frame)
    except:
        cv2.imshow("Image",frame)
    key = cv2.waitKey(1)
    if key==ord('q'):
        break  

cam.release()
cv2.destroyAllWindows()


