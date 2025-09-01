import sys
from ultralytics import YOLO

if len(sys.argv) < 3:
    print("Usage: python predict.py /path/to/model.pt /path/to/source")
    sys.exit(1)

model_path = sys.argv[1]
source_path = sys.argv[2]

model = YOLO(model_path)

results = model.predict(
    source=source_path,
    save=True,   # saves results in 'runs/detect'
    show=False   # set True to preview
)

print(f"Prediction done. Results saved in 'runs/detect'.")

