import cv2



def main():
    # load the photograph
    image = cv2.imread('IMG_1531.jpg')
    image = ResizeWithAspectRatio(image, width=640)
    # load the pre-trained model
    classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    # perform face detection
    bboxes = classifier.detectMultiScale(image)
    # print bounding box for each detected face
    for box in bboxes:
        # extract
        x, y, width, height = box
        x2, y2 = x + width, y + height
        # draw a rectangle over the pixels
        cv2.rectangle(image, (x, y), (x2, y2), (0,0,255), 1)
    # show the image
    cv2.imshow('face detection', image)
    # keep the window open until we press a key
    cv2.waitKey(0)
    # close the window
    cv2.destroyAllWindows()

def ResizeWithAspectRatio(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    return cv2.resize(image, dim, interpolation=inter)


if __name__ == "__main__":
    main()