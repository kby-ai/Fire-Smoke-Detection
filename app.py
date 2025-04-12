import sys
sys.path.append('.')

import os
import base64
import json
from ctypes import *
from firesdk import *
import cv2
import numpy as np
from flask import Flask, request, jsonify


licensePath = "license.txt"
license = ""

machineCode = getMachineCode()
print("\nmachineCode: ", machineCode.decode('utf-8'))

try:
    with open(licensePath, 'r') as file:
        license = file.read().strip()
except IOError as exc:
    print("failed to open license.txt: ", exc.errno)

print("\nlicense: ", license)

ret = setActivation(license.encode('utf-8'))
print("\nactivation: ", ret)

ret = initSDK()
print("init: ", ret)

app = Flask(__name__) 

def mat_to_bytes(mat):
    """
    Convert cv::Mat image data (NumPy array in Python) to raw bytes.
    """
    # Encode cv::Mat as PNG bytes
    is_success, buffer = cv2.imencode(".png", mat)
    if not is_success:
        raise ValueError("Failed to encode cv::Mat image")
    return buffer.tobytes()

@app.route('/fire', methods=['POST'])
def fire():
    result = "None"
    object_name = {}
    box = {}
    pro = {}
    
    file = request.files['file']
    
    try:
        image = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
        # image = cv2.resize(image, (1024, 640))
    except:
        result = "Failed to open file"
        response = jsonify({"result": result, "class": object_name, "coordinate": box, "score": pro})

        response.status_code = 200
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response

    img_byte = mat_to_bytes(image)
    
    box_array = (c_int * 1024)()  # Assuming a maximum of 256 rectangles
    score_array = (c_float * 1024)()  # Assuming a maximum of 256 rectangles
    label_array = (c_int * 1024)()
    
    cnt = getFireDetection(img_byte, len(img_byte), label_array, box_array, score_array)

    rectangles = [
    (box_array[i * 4], box_array[i * 4 + 1], box_array[i * 4 + 2], box_array[i * 4 + 3])
    for i in range(cnt)]
    scores = [score_array[i] for i in range(cnt)]
    labels = [label_array[i] for i in range(cnt)]

    # print(f"detection number: {cnt}, box: {rectangles}, labels: {labels}, scores: {scores} \n")

    if cnt == 0:
        result = "Nothing Detected !"
        response = jsonify({"result": result, "class": object_name, "coordinate": box, "score": pro})

        response.status_code = 200
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response
    
    result = "Fire or Smoke Detected !"
    for i in range(cnt):
        if labels[i] == 0:
            object_name[f"id {i + 1}"] = "fire"
        else:
            object_name[f"id {i + 1}"] = "smoke"
        box[f"id {i + 1}"] = rectangles[i]
        pro[f"id {i + 1}"] = scores[i]
    
    response = jsonify({"result": result, "class": object_name, "coordinate": box, "score": pro})

    response.status_code = 200
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    return response

@app.route('/fire_base64', methods=['POST'])
def fire_base64():

    result = "None"
    object_name = {}
    box = {}
    pro = {}
    
    content = request.get_json()

    try:
        imageBase64 = content['base64']
        image_data = base64.b64decode(imageBase64) 
        np_array = np.frombuffer(image_data, np.uint8)
        image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)  
        # image = cv2.resize(image, (1024, 640)) 
    except:
        result = "Failed to open file1"
        response = jsonify({"result": result, "class": object_name, "coordinate": box, "score": pro})

        response.status_code = 200
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response
    

    img_byte = mat_to_bytes(image)
    
    box_array = (c_int * 1024)()  # Assuming a maximum of 256 rectangles
    score_array = (c_float * 1024)()  # Assuming a maximum of 256 rectangles
    label_array = (c_int * 1024)()
    
    cnt = getFireDetection(img_byte, len(img_byte), label_array, box_array, score_array)

    rectangles = [
    (box_array[i * 4], box_array[i * 4 + 1], box_array[i * 4 + 2], box_array[i * 4 + 3])
    for i in range(cnt)]
    scores = [score_array[i] for i in range(cnt)]
    labels = [label_array[i] for i in range(cnt)]

    # print(f"detection number: {cnt}, box: {rectangles}, labels: {labels}, scores: {scores} \n")

    if cnt == 0:
        result = "Nothing Detected !"
        response = jsonify({"result": result, "class": object_name, "coordinate": box, "score": pro})

        response.status_code = 200
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response
    
    result = "Fire or Smoke Detected !"
    for i in range(cnt):
        if labels[i] == 0:
            object_name[f"id {i + 1}"] = "fire"
        else:
            object_name[f"id {i + 1}"] = "smoke"
        box[f"id {i + 1}"] = rectangles[i]
        pro[f"id {i + 1}"] = scores[i]
    
    response = jsonify({"result": result, "class": object_name, "coordinate": box, "score": pro})

    response.status_code = 200
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    return response

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)