from flask import Flask, request, jsonify, json
from dbconnection import connection
import base64
import time
import datetime
import gc

import cv2
import numpy as np
import pytesseract
from PIL import Image
import os


def analyze_name(textt):

    imgdata = base64.b64decode(textt)

    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H-%M-%S')

    filename = st+'.jpg'

    with open(filename, 'wb') as f:
        f.write(imgdata)

    # Read image with opencv
    img = cv2.imread(filename)

    # Convert to gray
    # if img.all() != None:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    # Write image after removed noise
    cv2.imwrite("noise.png", img)

    #  Apply threshold to get image with only black and white
    img = cv2.adaptiveThreshold(
        img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

    # Write the image after apply opencv
    cv2.imwrite("thres.png", img)

    # Recognize text with tesseract for python
    image_result = pytesseract.image_to_string(Image.open("noise.png"))

    # Remove template file
    # os.remove("noise.png")
    # os.remove("thres.png")
    # os.remove(filename)

    print(image_result)
    try:
        print("db_result")
        c, conn = connection()
        c.execute("SELECT * FROM structures where element ='"+textt+"'")
        db_result = c.fetchall()

        lwis = str(db_result).split("', '")
        lenth = len(lwis)
        xxx = ""

        for i in range(lenth):
            if i == 0:
                lwis[0] = lwis[0][3:]
            elif i == lenth-1:
                size = len(lwis[i])
                lwis[i] = lwis[i][:size-4]

        final_answer = ",".join(lwis)

        c.close()
        conn.close()
        gc.collect()
    except Exception as e:
        return (str(e))
    return final_answer


def lewis_t(text):
    try:
        print("db_result")
        c, conn = connection()
        c.execute("SELECT * FROM structures where element ='"+text+"'")
        db_result = c.fetchall()

        lwis = str(db_result).split("', '")
        lenth = len(lwis)
        xxx = ""

        for i in range(lenth):
            if i == 0:
                lwis[0] = lwis[0][3:]
            elif i == lenth-1:
                size = len(lwis[i])
                lwis[i] = lwis[i][:size-4]

        final_answer = ",".join(lwis)

        c.close()
        conn.close()
        gc.collect()
    except Exception as e:
        return (str(e))
    return final_answer


def analyze_struc(textt):
    print(textt)
    imgdata = base64.b64decode(textt)

    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H-%M-%S')

    filename = st+'.jpg'

    with open(filename, 'wb') as f:
        f.write(imgdata)

    # Read image with opencv
    img = cv2.imread(filename)

    # Convert to gray
    # if img.all() != None:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    # Write image after removed noise
    cv2.imwrite("noise.png", img)

    #  Apply threshold to get image with only black and white
    img = cv2.adaptiveThreshold(
        img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

    # Write the image after apply opencv
    cv2.imwrite("thres.png", img)

    # Recognize text with tesseract for python
    image_result = pytesseract.image_to_string(Image.open("thres.png"))

    # Remove template file
    os.remove("noise.png")
    os.remove("thres.png")
    # os.remove(filename)

    print(image_result)

    identified_element = []
    identified_count = []
    final_r = []

    elements = str(textt).split("-")
    len_eli = len(elements)

    C_count = 0
    H_count = 0
    N_count = 0

    for i in range(len_eli):
        if i == 0:
            # if any("C" in s for s in elements):
                        #C_count += 1
                        # print(C_count)
            C_count = elements.count("C")
            if C_count != 0:
                identified_element.append("C")
                identified_element.append(C_count)

            H_count = elements.count("H")
            if H_count != 0:
                identified_element.append("H")
                identified_element.append(H_count)

            N_count = elements.count("N")
            if N_count != 0:
                identified_element.append("N")
                identified_element.append(N_count)

    answer = "".join(map(str, identified_element))

    print(answer)
    answer2 = "CO2"

    c, conn = connection()
    c.execute("SELECT * FROM structures where element ='"+answer2+"'")
    db_result = c.fetchall()

    lwis = str(db_result).split("', '")
    lenth = len(lwis)
    xxx = ""

    for i in range(lenth):
        if i == 0:
            lwis[0] = lwis[0][3:]
        elif i == lenth-1:
            size = len(lwis[i])
            lwis[i] = lwis[i][:size-4]

    final_answer = ",".join(lwis)

    c.close()
    conn.close()
    gc.collect()

    return final_answer
