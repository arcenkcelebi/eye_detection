import cv2

kamera = cv2.VideoCapture(0)

while True:
    ret, kare = kamera.read()

    goz_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

    gri_ton = cv2.cvtColor(kare, cv2.COLOR_BGR2GRAY)

    gozler = goz_cascade.detectMultiScale(gri_ton, 1.1, 4)

    for (x, y, w, h) in gozler:
        cv2.rectangle(kare, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('ekran', kare)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

kamera.release()

cv2.destroyAllWindows()
