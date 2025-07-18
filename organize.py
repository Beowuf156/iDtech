import os
import shutil
import random

# Settings
input_dir = 'dataset'             # Where your raw images are
output_base = 'organized_dataset' # Output structure
split_ratios = (0.7, 0.15, 0.15)   # Train, val, test split

# Step 1: Group images by object name (everything before the last space in the filename)
object_images = {}

for filename in os.listdir(input_dir):
    if not filename.lower().endswith('.png'):
        continue

    # Remove file extension
    name = filename[:-4]

    # Object name is everything except the last space-part (image ID)
    parts = name.rsplit(' ', 1)
    if len(parts) != 2:
        print(f"Skipping file (unexpected format): {filename}")
        continue

    object_name_raw = parts[0]  # e.g., "2780 Peg with friction"
    # Clean name to make it folder-safe
    object_name = object_name_raw.replace(' ', '_')  # e.g., "2780_Peg_with_friction"

    object_images.setdefault(object_name, []).append(filename)

# Step 2: Create folders
for split in ['train', 'val', 'test']:
    for obj in object_images:
        os.makedirs(os.path.join(output_base, split, obj), exist_ok=True)

# Step 3: Shuffle and distribute
for object_name, images in object_images.items():
    random.shuffle(images)
    total = len(images)

    train_end = int(total * split_ratios[0])
    val_end = train_end + int(total * split_ratios[1])

    splits = {
        'train': images[:train_end],
        'val': images[train_end:val_end],
        'test': images[val_end:]
    }

    for split_name, image_list in splits.items():
        for img_file in image_list:
            src = os.path.join(input_dir, img_file)
            dst = os.path.join(output_base, split_name, object_name, img_file)
            shutil.copy(src, dst)  # Use shutil.move() to delete original files