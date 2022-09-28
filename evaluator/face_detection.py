import cv2


class FaceDetector:
    @classmethod
    def find_faces(cls, path):

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


            faces, _, confidence = frontal.detectMultiScale3(
                image, scaleFactor=1.1, minNeighbors=5, outputRejectLevels=True
            )

            if bool(len(faces)):

                x, y, w, h = faces[confidence.argmax()]
                
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.imwrite(path, image)
                return bool(len(faces))

        return False
