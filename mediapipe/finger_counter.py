import cv2
import mediapipe as mp
mp_hands=mp.solutions.hands
mp_draw=mp.solutions.drawing_utils
Hand=mp_hands.Hands(max_num_hands=1)
video=cv2.VideoCapture(0)
while True:
    success,image=video.read()
    image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    result=Hand.process(image)
    image=cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
    tipids=[4,8,12,16,20]
    lmlst=[]
    cv2.rectangle(image,(20,350),(80,450),(0,0,0),cv2.FILLED)
    cv2.rectangle(image,(20,350),(80,450),(32,22,234),2)
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:     # landmarks gives x,y,z values
            for id,lm in enumerate(hand_landmarks.landmark):    # enumerate -> gives the index and the value.  eg: lst=['apple','orange','grapes']. enumerate(lst) gives [(0, 'apple'), (1, 'orange'), (2, 'grapes')]
                # print(id,lm)           # id -> id of land marks ,   lm -> x,y,z values of land marks
                x=lm.x
                y=lm.y
                lmlst.append([id,x,y])
                # print(lmlst)
                if len(lmlst)!=0 and len(lmlst)==21:
                    fingerlst=[]

                    # thumb
                    if lmlst[0][1]<lmlst[1][1]:
                        if lmlst[4][1]<lmlst[3][1]:
                            fingerlst.append(0)
                        else:
                            fingerlst.append(1)
                    else:
                        if lmlst[4][1]>lmlst[3][1]:
                            fingerlst.append(0)
                        else:
                            fingerlst.append(1)    

                    # other fingers
                    for i in range(1,5):
                        if lmlst[tipids[i]][2]>lmlst[tipids[i]-2][2]:     # if y value of finger tip is large, finger is closed (in opencv y value increases from top to bottom)
                            fingerlst.append(0)  # finger closed
                        else:
                            fingerlst.append(1)  # finger opened

                    if len(fingerlst)!=0:
                        fingercount=fingerlst.count(1)
                        print(fingercount)
            cv2.putText(image,str(fingercount),(31,423),cv2.FONT_HERSHEY_DUPLEX,2,(255,255,255),2)
            mp_draw.draw_landmarks(image,hand_landmarks,mp_hands.HAND_CONNECTIONS,mp_draw.DrawingSpec(color=(0,0,0),thickness=2,circle_radius=3),mp_draw.DrawingSpec(color=(32,22,234),thickness=3))
                                                                                                    # giving 2 DrawingSpec - first one for land mark and second one for lines connecting the land marks
    cv2.imshow('Hand',image)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
video.release()
cv2.destroyAllWindows()  