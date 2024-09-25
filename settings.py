from pathlib import Path
import sys

# Get the absolute path of the current file
file_path = Path(__file__).resolve()

# Get the parent directory of the current file
root_path = file_path.parent

# Add the root path to the sys.path list if it is not already there
if root_path not in sys.path:
    sys.path.append(str(root_path))

# Get the relative path of the root directory with respect to the current working directory
ROOT = root_path.relative_to(Path.cwd())

# Sources
IMAGE = 'Image'
VIDEO = 'Video'
YOUTUBE = 'YouTube'

SOURCES_LIST = [IMAGE, VIDEO, YOUTUBE]

# Images config
IMAGES_DIR = ROOT / 'images'

IMAGES_DICT = {
    'image_1': IMAGES_DIR / "image1.png",
    'image_2': IMAGES_DIR / "image2.png",
    'image_3': IMAGES_DIR / "image3.png",
    'image_4': IMAGES_DIR / "image4.png",
    'image_5': IMAGES_DIR / "image5.png",
    'image_6': IMAGES_DIR / "image6.png",
    'image_7': IMAGES_DIR / "image7.png",
    'image_8': IMAGES_DIR / "image8.png",
    'image_9': IMAGES_DIR / "image9.jpg",
    'image_10': IMAGES_DIR / "image10.jpg",
    'image_11': IMAGES_DIR / "image11.jpg",
    'image_12': IMAGES_DIR / "image12.jpg",
    'image_13': IMAGES_DIR / "image13.jpg",
}
DEFAULT_IMAGE = IMAGES_DIR / 'image1.png'
DEFAULT_DETECT_IMAGE = IMAGES_DIR / '2621908_1699590107725534.png'

# Videos config
VIDEO_DIR = ROOT / 'videos'
VIDEO_1_PATH = VIDEO_DIR / 'video_1.mp4'
VIDEOS_DICT = {
    'video_1': VIDEO_1_PATH
}

# ML Model config
MODEL_DIR = ROOT / 'weights'
DETECTION_MODEL = MODEL_DIR / 'best_FP16.onnx'


