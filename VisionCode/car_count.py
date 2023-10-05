import cv2

def count_cars(image_path):
    image = cv2.imread(image_path)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    car_cascade = cv2.CascadeClassifier('cars.xml')

    cars = car_cascade.detectMultiScale(gray, 1.1, 2)

    for (x, y, w, h) in cars:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('Detected Cars', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return len(cars)