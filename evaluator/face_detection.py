import cv2


class FaceDetector:
    @classmethod
    def find_faces(cls, path):

        resize_factor = 0.25
        cascades = [
            "haarcascade_frontalface_default.xml",
            "haarcascade_profileface.xml",
            "haarcascade_frontalface_alt.xml",
            "haarcascade_frontalface_alt2.xml",
            "haarcascade_frontalface_alt_tree.xml",
            "haarcascade_eye.xml",
        ]
        for cascade in cascades:
            frontal = cv2.CascadeClassifier("evaluator/" + cascade)
            
            image = cv2.imread(path)

            if image is None:
                return False

            reduced = cv2.resize(
                image,
                None,
                fx=resize_factor,
                fy=resize_factor,
                interpolation=cv2.INTER_NEAREST,
            )
            gray = cv2.cvtColor(reduced, cv2.COLOR_BGR2GRAY)

            faces = frontal.detectMultiScale3(
                gray, scaleFactor=1.1, minNeighbors=3, outputRejectLevels=True
            )

            for dims in faces[0]:
                dims = (dims / resize_factor).round().astype(int)
                x, y, w, h = dims
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

            cv2.imwrite(path, image)
        
            if bool(len(faces[0])):
                return bool(len(faces[0]))
