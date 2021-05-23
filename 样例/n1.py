import cv2 as cv
import numpy as np
import os
root_dir = "D:/projects/OIDv4_ToolKit-master/OID/Dataset"
# train_label_dir = "D:/football_train/data/labels/train"
valid_label_dir = "D:/fruit_train/data/labels/train"


def read_annotation(data_dype="train", clazz_type="Football"):
    current_dir = os.path.join(root_dir, data_dype, clazz_type)
    print(current_dir)
    files = os.listdir(current_dir)
    for f in files:
        if os.path.isfile(os.path.join(current_dir, f)):
            image = cv.imread(os.path.join(current_dir, f))
            label_file = os.path.join(current_dir, "label", f.replace(".jpg", ".txt"))
            yolo_label = f.replace(".jpg", ".txt")
            data_label_text_f = os.path.join(valid_label_dir, yolo_label)
            file_write_obj = open(data_label_text_f, 'w')

            with open(label_file) as f:
                boxes = [line.strip() for line in f.readlines()]
            clazz_index = -1
            # create new file
            for box in boxes:
                anno_info = box.split(" ")
                if anno_info[0] == "Tennis ball":
                    print("class name: ", anno_info[0])
                    x1 = float(anno_info[1])
                    y1 = float(anno_info[2])
                    x2 = float(anno_info[3])
                    y2 = float(anno_info[4])
                    clazz_index = 0
                else:
                    print("class name:", anno_info[0])
                    x1 = float(anno_info[1])
                    y1 = float(anno_info[2])
                    x2 = float(anno_info[3])
                    y2 = float(anno_info[4])
                    clazz_index = 1
                h, w, c = image.shape
                cx = (x1 + (x2 - x1) / 2) / w
                cy = (y1 + (y2 - y1) / 2) / h
                sw = (x2 - x1) / w
                sh = (y2 - y1) / h
                file_write_obj.write("%d %f %f %f %f\n"%(clazz_index, cx, cy, sw, sh))
                # cv.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)),(0, 0, 255), 2, 8)
            file_write_obj.close()
            # cv.imshow("image", image)
            # cv.waitKey(0)
    # cv.destroyAllWindows()


if __name__ == "__main__":
    read_annotation(data_dype="train", clazz_type="Tennis ball")