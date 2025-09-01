# Russian Armor Detection
Object detection model using YOLOv8 to identify Russian armored vehicles (MBTs and IFVs/APCs) from open-source imagery gathered from the Russo-Ukrainian War and the Syrian Civil War.

## Demo
Watch a short video of the model in action:


[![Watch the video](https://img.youtube.com/vi/bkcUh47aMxM/hqdefault.jpg)](https://www.youtube.com/embed/bkcUh47aMxM)

## Installation
Clone the repository and install dependencies:

PLACEHOLDER
```bash
git clone https://github.com/yankeeFulcrum/rus-armor-detection.git
cd rus-armor-detection
pip install ultralytics opencv-python torch torchvision
wget https://github.com/yankeeFulcrum/rus-armor-detection/releases/download/v1.0/yolov8_armor.pt
```
## Usage
To detect armored vehicles in a folder of images:

```bash
python detect.py --weights yolov8_armor.pt --source ./your_images/
```
To run detection on a video:

```bash
python detect.py --weights yolov8_armor.pt --source ./demo_video.mp4
```
Results will be saved in runs/detect/exp by default.
## Dataset
Training and test images were collected from open-source intelligence (OSINT) sources.  

This project uses data from the [Vehicle Dataset for YOLO](https://www.kaggle.com/datasets/nadinpethiyagoda/vehicle-dataset-for-yolo) by Nadin Pethiyagoda, available under the [Open Database License (ODbL)](https://opendatacommons.org/licenses/odbl/1-0/).  

This project uses data from the [Background](https://www.kaggle.com/datasets/nuidelirina/background) by Nuidel Irina, available under the [Open Database License (ODbL)](https://opendatacommons.org/licenses/odbl/1-0/).  
## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details
