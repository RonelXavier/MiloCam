# 🐶 MiloCam

Real-time dog detection with DETR (facebook/detr-resnet-50) + Discord alerts.
---
<img width="651" height="72" alt="Screenshot 2025-07-24 at 10 11 23 PM" src="https://github.com/user-attachments/assets/fedf0f57-faed-44b8-89da-aed01ad48be9" />

![IMG_3710](https://github.com/user-attachments/assets/d07ab4df-cf7e-45c0-a45c-b9139acd3ba5|400)

### Overview

MiloCam is a lightweight computer vision tool that uses [facebook/detr-resnet-50](https://huggingface.co/facebook/detr-resnet-50) from Hugging Face to detect my dog (Milo) via webcam and send a Discord message when he's at the back door.

---

### Features

* Real-time object detection via webcam (OpenCV)
* DETR (DEtection TRansformer) model for dog detection
* Discord integration for instant alerts
* Runs locally with minimal setup

---

### Setup

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Create a `.env` file:

   ```
   DiscToken=your_discord_bot_token
   channelid=your_channel_id
   ```

3. Run the script:

   ```bash
   python your_script.py
   ```

---

### Requirements

See `requirements.txt` (generated via `pip freeze`) for exact versions.

---
