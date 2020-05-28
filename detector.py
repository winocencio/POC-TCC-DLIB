import os
import dlib
import cv2
import glob
import resources as rs

detectorOvo = dlib.simple_object_detector(rs.svmFilePath)
for imagem in glob.glob(os.path.join(rs.imagesPath,"*")):
    img = cv2.imread(imagem)

    objetosDetectados = detectorOvo(img,2)
    print(len(objetosDetectados))
    for d in objetosDetectados:
        e, t, d, b = (int(d.left()), int(d.top()),int(d.right()),int(d.bottom()))
        cv2.rectangle(img,(e,t),(d,b),(0,0,255),2)

    cv2.imshow("Imagens" +str(len(objetosDetectados)),img)
    cv2.waitKey(0)

cv2.destroyAllWindows()