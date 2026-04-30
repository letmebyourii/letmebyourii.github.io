import os 
import io 
import base64 
from flask import Flask, render_template, request 
from ultralytics import YOLO
from PIL import Image


app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

model = YOLO("./models/yolov8n-oiv7")

def process_imgs(imgs): 
  results = model(imgs)

  processed = []
  for r in results: 
    im_bgr = r.plot()
    im_rgb = Image.fromarray(im_bgr[..., ::-1])
    processed.append(im_rgb)
  
  return processed

def pil_to_base64(img: Image.Image) -> str:
    """Convert a PIL image to a base64 string for embedding in HTML."""
    buffer = io.BytesIO()
    img.save(buffer, format="JPEG")
    return base64.b64encode(buffer.getvalue()).decode("utf-8")

  

@app.route('/')
def index():
  return render_template('lmbye.html')

@app.route('/img-demo/', methods=['POST'])
def img_demo():
    file = request.files.get('image_uploads')
    if not file or file.filename == '':
        return render_template('lmbye.html', error="No file uploaded.")

    # Save temporarily so YOLO can read it
    save_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(save_path)

    processed_images = process_imgs([save_path])

    # Convert results to base64 so they can be rendered in the template
    images_b64 = [pil_to_base64(img) for img in processed_images]

    return render_template('lmbye.html', images_b64=images_b64)

if __name__ == '__main__':
  port = int(os.environ.get("PORT", 10000))
  app.run(host="0.0.0.0", port=port) #debug=True)