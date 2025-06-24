import os
import pandas as pd

# Paths (relative to Notebooks directory)
base_data_dir = os.path.join('..', 'Data')
splits = ['train', 'valid', 'test']

# Output directories for YOLO format
yolo_base = os.path.join('..', 'yolo_dataset')
for split in splits:
    os.makedirs(os.path.join(yolo_base, 'images', split), exist_ok=True)
    os.makedirs(os.path.join(yolo_base, 'labels', split), exist_ok=True)

def convert_bbox(row, img_w, img_h):
    x_center = (row['xmin'] + row['xmax']) / 2.0 / img_w
    y_center = (row['ymin'] + row['ymax']) / 2.0 / img_h
    width = (row['xmax'] - row['xmin']) / img_w
    height = (row['ymax'] - row['ymin']) / img_h
    return x_center, y_center, width, height

# Collect all classes
all_classes = set()
for split in splits:
    csv_path = os.path.join(base_data_dir, split, '_annotations.csv')
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
        all_classes.update(df['class'].unique())
classes = sorted(list(all_classes))
class_to_id = {cls: idx for idx, cls in enumerate(classes)}

# Save class list for YOLOv8 data.yaml
with open(os.path.join(yolo_base, 'classes.txt'), 'w') as f:
    for cls in classes:
        f.write(f"{cls}\n")

# Convert each split
def process_split(split):
    csv_path = os.path.join(base_data_dir, split, '_annotations.csv')
    images_dir = os.path.join(base_data_dir, split)
    labels_dir = os.path.join(yolo_base, 'labels', split)
    images_out_dir = os.path.join(yolo_base, 'images', split)
    if not os.path.exists(csv_path):
        print(f"No CSV for {split}, skipping.")
        return
    df = pd.read_csv(csv_path)
    grouped = df.groupby('filename')
    for filename, group in grouped:
        img_w = group.iloc[0]['width']
        img_h = group.iloc[0]['height']
        label_path = os.path.join(labels_dir, os.path.splitext(filename)[0] + '.txt')
        with open(label_path, 'w') as f:
            for _, row in group.iterrows():
                class_id = class_to_id[row['class']]
                x_center, y_center, width, height = convert_bbox(row, img_w, img_h)
                f.write(f"{class_id} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}\n")
        # Copy image to YOLO images directory
        src_img = os.path.join(images_dir, filename)
        dst_img = os.path.join(images_out_dir, filename)
        if os.path.exists(src_img):
            if not os.path.exists(dst_img):
                try:
                    import shutil
                    shutil.copy2(src_img, dst_img)
                except Exception as e:
                    print(f"Error copying {src_img} to {dst_img}: {e}")
        else:
            print(f"Image file {src_img} not found.")

for split in splits:
    process_split(split)

print("Conversion to YOLO format complete! Check the yolo_dataset directory.") 