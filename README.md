# 🧠 Jetson Image Classifier & Dataset Organizer

This project contains two Python scripts designed for Jetson devices using NVIDIA’s Jetson Inference framework:

* `main.py` — Classifies an image using a pre-trained or custom Jetson model.
* `organize.py` — Organizes a dataset of PNG images into train/val/test splits based on object names parsed from filenames.

---

## 📁 Project Structure

```
.
├── main.py            # Image classification using Jetson Inference
├── organize.py        # Dataset organizer and train/val/test splitter
├── labels.txt         # Class label file used for inference
├── resnet18.onnx      # (Optional) ONNX model file
├── dataset/           # Input folder for raw images (for organize.py)
└── organized_dataset/ # Output folder for structured dataset
```

---

## 🚀 Requirements

* NVIDIA Jetson device (e.g., Nano, Xavier, TX2)
* Jetson Inference library
* Python 3

Install dependencies (on Jetson):

```bash
sudo apt-get install python3-pip
sudo pip3 install numpy
# Jetson Inference should already be installed if you're using a JetPack image
```

---

## 🖼️ Image Classification (`main.py`)

### Usage

```bash
python3 main.py image.png --model=resnet18.onnx --labels=labels.txt
```

### Arguments

* `filename`: Path to the image to classify (PNG, JPG, etc.)
* `--model`: ONNX model to use (default: `resnet18.onnx`)
* `--labels`: Text file with class labels (default: `labels.txt`)

### Output

Prints something like:

```
image is recognized as Screwdriver (class #2) with 94.56% confidence
```

---

## 📂 Dataset Organizer (`organize.py`)

This script splits a folder of PNG images into `train`, `val`, and `test` sets based on object names derived from filenames.

### Filename Format

Images must be named with the object name followed by an ID, separated by a space:

```
2780 Peg with friction 001.png
2780 Peg with friction 002.png
```

Becomes:

```
organized_dataset/
├── train/
│   └── 2780_Peg_with_friction/
├── val/
│   └── 2780_Peg_with_friction/
└── test/
    └── 2780_Peg_with_friction/
```

### Settings

Adjust these variables in `organize.py` as needed:

```python
input_dir = 'dataset'
output_base = 'organized_dataset'
split_ratios = (0.7, 0.15, 0.15)
```

---

## 📝 License

Include your license here (MIT, GPL, etc.)

---

## 🙋‍♀️ Contribution

Feel free to fork this repo and submit pull requests!
