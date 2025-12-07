import os
from ultralytics import YOLO

# --- Configuration ---
# 1. Define the path to your custom YAML data configuration file.
# Make sure this path is correct relative to where you run this script.
DATA_YAML_PATH = 'custom_dataset.yaml'

# 2. Choose the base model to use. 'yolov8s.pt' is the small, pre-trained model.
MODEL_WEIGHTS = 'yolov8s.pt' 

# 3. Define training parameters.
PROJECT_NAME = 'YOLOv8_Custom_Training' # Folder to save results (runs/detect/...)
EXPERIMENT_NAME = 'vehicles_badguys_run' # Subfolder for this specific training run
EPOCHS = 50                          # Number of training cycles (start with a smaller number for testing)
IMG_SIZE = 640                       # Image size 
BATCH_SIZE = 16                      # Number of images per batch (adjust based on your GPU VRAM)

# --- Script Execution ---

def train_yolov8_model():
    """Initializes and trains a YOLOv8 model."""
    print(f"Loading model: {MODEL_WEIGHTS}")
    try:
        # Load the model
        model = YOLO(MODEL_WEIGHTS)

        print("\nStarting training...")
        # Train the model
        results = model.train(
            data=DATA_YAML_PATH,  # Path to the dataset configuration file
            epochs=EPOCHS,        # Number of epochs
            imgsz=IMG_SIZE,       # Input image size
            batch=BATCH_SIZE,     # Batch size
            name=EXPERIMENT_NAME, # Experiment name for saving results
            project=PROJECT_NAME, # Project folder name
            # device=0,           # Optional: Specify GPU 0
        )

        print("\nTraining completed!")
        print(f"Results saved in: {PROJECT_NAME}/{EXPERIMENT_NAME}")

    except FileNotFoundError:
        print(f"Error: Data YAML file not found at {DATA_YAML_PATH}. Ensure it's in the same directory or the path is correct.")
    except Exception as e:
        print(f"An unexpected error occurred during training: {e}")

if __name__ == '__main__':
    train_yolov8_model()