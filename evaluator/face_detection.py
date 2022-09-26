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


            faces = frontal.detectMultiScale3(
                image, scaleFactor=1.1, minNeighbors=3, outputRejectLevels=True
            )

            for x, y, w, h in faces[0]:
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

            cv2.imwrite(path, image)

            if bool(len(faces[0])):
                return bool(len(faces[0]))

        return False
