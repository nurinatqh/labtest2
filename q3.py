import streamlit as st
import torch
import torch.nn.functional as F
from torchvision import models, transforms
from PIL import Image
import requests

labels = requests.get("https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt").text.splitlines()
model = models.resnet18(weights='DEFAULT').eval()

preprocess = transforms.Compose([
    transforms.Resize(256), transforms.CenterCrop(224),
    transforms.ToTensor(), transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

img_file = st.camera_input("Take a photo")
if img_file:
    img = Image.open(img_file).convert("RGB")
    batch = preprocess(img).unsqueeze(0)
    with torch.no_grad():
        out = model(batch)
        prob = F.softmax(out[0], dim=0)
    top5_p, top5_i = torch.topk(prob, 5)
    for i in range(5):
        st.write(f"{labels[top5_i[i]]}: {top5_p[i].item():.4f}")