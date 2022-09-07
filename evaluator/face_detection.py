import cv2


class FaceDetector:

    resize_factor = 0.25

    frontal = cv2.CascadeClassifier("evaluator/haarcascade_frontalface_default.xml")

    @classmethod
    def find_faces(cls, path):

        image = cv2.imread(path)

        if not image:
            return False

        reduced = cv2.resize(
            image,
            None,
            fx=cls.resize_factor,
            fy=cls.resize_factor,
            interpolation=cv2.INTER_NEAREST,
        )
        gray = cv2.cvtColor(reduced, cv2.COLOR_BGR2GRAY)

        faces = cls.frontal.detectMultiScale3(
            gray, scaleFactor=1.1, minNeighbors=3, outputRejectLevels=True
        )

        for dims in faces[0]:
            dims = (dims / cls.resize_factor).round().astype(int)
            x, y, w, h = dims
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imwrite(path, image)

        return bool(len(faces[0]))
