""" Để lưu encodings và tên của các faces trong dataset vào file encodings.pickle"""
# USAGE
# python test.py --dataset dataset --encodings encodings.pickle

import imutils.paths as paths
import argparse
import pickle
import cv2
import os
import face_recognition

# lấy paths của images trong dataset
print("[INFO] quantifying faces...")
imagePaths = list(paths.list_images('dataset'))

# khởi tạo list chứa known encodings và known names (để các test images so sánh)
# chứa encodings và tên của các images trong dataset
knownEncodings = []
knownNames = []

# duyệt qua các image paths
for (i, imagePath) in enumerate(imagePaths):
    # lấy tên người từ imagepath
    print("[INFO] processing image {}/{}".format(i + 1, len(imagePaths)))
    name = imagePath.split(os.path.sep)[-2]

    # load image bằng OpenCV và chuyển từ BGR to RGB (dlib cần)
    image = cv2.imread(imagePath)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Đối với từng image phải thực hiện detect face, trích xuất face ROI và chuyển về encoding
    # trả về array of bboxes of faces, dùng dlib như bài face detection đó
    # model="cnn" chính xác hơn nhưng chậm hơn, "hog" nhanh hơn nhưng kém chính xác hơn
    boxes = face_recognition.face_locations(rgb, 1, 'cnn')

    # tính the facial embedding for the face
    # sẽ tính encodings cho mỗi face phát hiện được trong ảnh (có thể có nhiều faces)
    # Để lý tưởng trong ảnh nên chỉ có một mặt người của mình thôi
    encodings = face_recognition.face_encodings(rgb, boxes)

    # duyệt qua các encodings
    # Trong ảnh có thể có nhiều faces, mà ở đây chỉ có 1 tên
    # Nên chắc chắn trong dataset ban đầu ảnh chỉ có một mặt người thôi nhé
    # Lý tưởng nhất mỗi ảnh có 1 face và có 1 encoding thôi
    for encoding in encodings:
        # lưu encoding và name vào lists bên trên
        knownEncodings.append(encoding)
        knownNames.append(name)

    if i > 1:
        break

# dump (lưu) the facial encodings + names vào ổ cứng
print("[INFO] serializing encodings...")
data = {"encodings": knownEncodings, "names": knownNames}

with open('encodings.pickle', "wb") as f:
    f.write(pickle.dumps(data))









