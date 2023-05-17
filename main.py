import cv2
import time
from local_settings import scale, colour, cam_num, pause_key, quit_key, screenshot_key


# video capture device ID, may require some trail and error
webcam = cv2.VideoCapture(cam_num)
pos1 = (0,0)
pos2 = (0,0)
setpos1 = True
take_input = True


def onMouse(event, x, y, flags, param):
    global pos1, pos2, setpos1
    if event == cv2.EVENT_LBUTTONDOWN:
        if setpos1:
            pos1 = (x,y)
            setpos1 = False
        else:
            pos2 = (x,y)
            setpos1 = True
            print(f'length: {(cv2.norm(pos1,pos2)/scale):.2f} micron, pixels: {(cv2.norm(pos1,pos2))}')
        #print('x = %d, y = %d'%(x, y))
    if event == cv2.EVENT_RBUTTONDOWN:
        pos1 = (0,0)
        pos2 = (0,0)

while(True):
    cv2.namedWindow('frame')
    
    if take_input:
        ret, frame = webcam.read()
   
    k = cv2.waitKey(20)
    if k == ord(quit_key):
        break
    if k == ord(pause_key):
        take_input = not take_input
    if k == ord(screenshot_key):
        path = f'{time.time()}.png'
        cv2.imwrite(path,frame)
    cv2.setMouseCallback('frame',onMouse)
    cv2.putText(frame,f'{(cv2.norm(pos1,pos2)/scale):.2f} micron',pos2,cv2.FONT_HERSHEY_SIMPLEX,1,colour)
    cv2.line(frame,pos1,pos2,colour,2)
    cv2.imshow('frame', frame)


webcam.release()
cv2.destroyAllWindows()