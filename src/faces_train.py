import os

BASE_DOR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DOR, "images")

X_train = []
Y_label = []

for root, dirs, files in os.walk(image_dir):
    for file in files:
        if file.endswith("png") or file.endswith("jpg"):
            path = os.path.join(root, file)
            label = os.path.basename(os.path.dirname(path)).replace(" ", "-").lower()
            print(label, path)
            Y_label.append(label)  # Some number
            X_train.append(path)  # Verify this image, turn into a NUMPY array & gray conversion
