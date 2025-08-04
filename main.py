# import libraries
import os
from transformers import DetrImageProcessor, DetrForObjectDetection
import torch
from PIL import Image
import requests
import numpy as np
import cv2 as cv
import discord
from dotenv import load_dotenv

# initialize keys for discord bot
load_dotenv()
token = os.getenv('DiscToken')
processor = DetrImageProcessor.from_pretrained("facebook/detr-resnet-50", revision="no_timm")
model = DetrForObjectDetection.from_pretrained("facebook/detr-resnet-50", revision="no_timm")


async def compvision():
    # start up cv
    cap = cv.VideoCapture(0)
    channel_id = int(os.getenv('channelid'))
    channel = client.get_channel(channel_id)

    if not cap.isOpened():
        print("Can't open the camera")
        exit()
        print(channel_id)
    while True:
        ret, frame = cap.read()
        if not ret:
            print("can't get the frame. exiting...")
            break
        img = frame
        # loops through frames, feeding each frame into the processor
        inputs = processor(images=img, return_tensors="pt") 
        outputs = model(**inputs)

        # img is a numpy array (shape: (height, width, channels)) so doing this returns a tuple of height and width that can be wrapped to a 2D tensor.
        height, width = img.shape[:2]
        target_sizes = torch.tensor([[height, width]])

        # convert outputs (bounding boxes and class logits) to COCO API
        #  only keep detections with score > 0.9
        results = processor.post_process_object_detection(outputs, target_sizes=target_sizes, threshold=0.9)[0]
        # detection code form model example on huggingface
        for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
            box = [round(i, 2) for i in box.tolist()]
            print(
                    f"Detected {model.config.id2label[label.item()]} with confidence "
                    f"{round(score.item(), 3)} at location {box}"
            )

            if model.config.id2label[label.item()] == "dog":
                await channel.send('Milo detected by the back door, make sure to take him out!' )


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    await compvision()
client.run(token)
