import cv2

key = cv2.waitKey(1)
webcam = cv2.VideoCapture(0)
safeguard = 'start'
safeguard_password = input("Enter your safeguard password:")
while safeguard == safeguard_password:

    try:
        check, frame = webcam.read()
        print(check)  # prints true as long as the webcam is running
        print(frame)  # prints matrix values of each framecd 
        cv2.imshow("Capturing", frame)
        key = cv2.waitKey(1)


        def capture(args=True):
            cv2.imwrite(filename='saved_img.jpg', img=frame)
            webcam.release()
            img_new = cv2.imread('saved_img.jpg', cv2.IMREAD_GRAYSCALE)
            img_new = cv2.imshow("Captured Image", img_new)
            cv2.waitKey(1650)
            cv2.destroyAllWindows()
            print("Renderering real-time image...")
            img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
            print("Converting RGB image to grayscale...")
            gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
            print("RGB to Grayscale successfully converted.")
            print("Pixeling of image to 350x350 scale...")
            img_ = cv2.resize(gray, (350, 350))
            print("Resized successfully.")
            img_resized = cv2.imwrite(filename='saved_img-final.jpg', img=img_)
            print("Image saved to database successfully.")


        if key == ord('q'):
            # if key==ord('q'):
            capture()
            print("Turning Camera off...")
            webcam.release()
            print("Camera off.")
            print("Welcome, your credentials has been successfully.")
            cv2.destroyAllWindows()
            break

    except(KeyboardInterrupt):
        print("Turning off camera.")
        webcam.release()
        print("Camera off.")
        print("Program ended.")
        cv2.destroyAllWindows()
        break
