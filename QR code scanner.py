import cv2
from pyzbar.pyzbar import decode
import webbrowser

def scan_qr_code():
    # Open the device's camera
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture image.")
            break

        # Decode the QR code in the frame
        decoded_objects = decode(frame)

        for obj in decoded_objects:
            # Draw the bounding box
            points = obj.polygon
            if len(points) > 4:
                hull = cv2.convexHull(points)
                points = hull.reshape((-1, 2))
            for j in range(len(points)):
                cv2.line(frame, tuple(points[j]), tuple(points[(j + 1) % len(points)]), (0, 255, 0), 3)

            # Extract the data from the QR code
            qr_data = obj.data.decode("utf-8")
            cv2.putText(frame, qr_data, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
            print(f"QR Code data: {qr_data}")

            # Option to open links or perform actions
            if qr_data.startswith("http://") or qr_data.startswith("https://"):
                webbrowser.open(qr_data)
                print(f"Opened {qr_data} in web browser.")

        # Display the resulting frame
        cv2.imshow('QR Code Scanner', frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture and destroy all windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    scan_qr_code()
