import cv2
import sys

try:
    fs = cv2.FileStorage("/ORB_SLAM3/data/mav0_all_sensor.yaml", cv2.FILE_STORAGE_READ)
    if not fs.isOpened():
        print("Failed to open file")
        sys.exit(-1)
    print("File opened successfully")
    
    # Try to read a value
    version = fs.getNode("File.version").string()
    print(f"File version: {version}")
    
    fs.release()
except Exception as e:
    print(f"Error: {e}")
    sys.exit(-1)