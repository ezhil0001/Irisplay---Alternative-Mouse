import cv2
import mediapipe as mp
import pyautogui
cam=cv2.VideoCapture(0)
face_mesh=mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w,screen_h=pyautogui.size()

while True:
    _, frame=cam.read()
    frame=cv2.flip(frame,1)
    rgb_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    output=face_mesh.process(rgb_frame)
    landmark_points=output.multi_face_landmarks
    frame_h,frame_w, _ =frame.shape

    if landmark_points:
        landmarks=landmark_points[0].landmark
        for id, landmark in enumerate(landmarks[474:478]):
            X=int(landmark.x*frame_w)
            Y=int(landmark.y*frame_h)
            cv2.circle(frame,(X,Y),3,(0,255,0))
            if id==1:
                screen_X =screen_w/frame_w*X
                screen_Y=screen_h/frame_h*Y
                pyautogui.moveTo(screen_X,screen_Y)
    left=[landmarks[145],landmarks[159]]
    for landmark in left:
        X = int(landmark.x * frame_w)
        Y = int(landmark.y * frame_h)
        cv2.circle(frame, (X, Y), 3, (0, 255, 255))
    if(left[0].y-left[1].y)<0.004:
        pyautogui.click()
        pyautogui.sleep(1)
    cv2.imshow('Eye controlled',frame)
    cv2.waitKey(1)