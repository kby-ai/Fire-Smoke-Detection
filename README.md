<p align="center">
  <a href="https://play.google.com/store/apps/dev?id=7086930298279250852" target="_blank">
    <img alt="" src="https://github-production-user-asset-6210df.s3.amazonaws.com/125717930/246971879-8ce757c3-90dc-438d-807f-3f3d29ddc064.png" width=500/>
  </a>  
</p>

### Our facial recognition algorithm is globally top-ranked by NIST in the FRVT 1:1 leaderboards. <span><img src="https://github.com/kby-ai/.github/assets/125717930/bcf351c5-8b7a-496e-a8f9-c236eb8ad59e" alt="badge" width="36" height="20"></span>  
[Latest NIST FRVT evaluation report 2024-12-20](https://pages.nist.gov/frvt/html/frvt11.html)  

![FRVT Sheet](https://github.com/user-attachments/assets/16b4cee2-3a91-453f-94e0-9e81262393d7)

#### 🆔 ID Document Liveness Detection - Linux - [Here](https://web.kby-ai.com)  <span><img src="https://github.com/kby-ai/.github/assets/125717930/bcf351c5-8b7a-496e-a8f9-c236eb8ad59e" alt="badge" width="36" height="20"></span>
#### 🤗 Hugging Face - [Here](https://huggingface.co/kby-ai)
#### 📚 Product & Resources - [Here](https://github.com/kby-ai/Product)
#### 🛟 Help Center - [Here](https://docs.kby-ai.com)
#### 💼 KYC Verification Demo - [Here](https://github.com/kby-ai/KYC-Verification-Demo-Android)
#### 🙋‍♀️ Docker Hub - [Here](https://hub.docker.com/r/kbyai/fire-smoke-detection)
```bash
sudo docker pull kbyai/fire-smoke-detection:latest
sudo docker run -v ./license.txt:/home/openvino/kby-ai-fire/license.txt -p 8081:8080 -p 9001:9000 kbyai/fire-smoke-detection:latest
```
# Fire-Smoke-Detection

## Overview

This repository demonstrates  `Fire/Smoke Detection` SDK with high accuracy by applying artificial intelligence and machine learning techniques. </br>
Fire and smoke are common hazards that can cause severe damage to life and property. Early detection of fire and smoke can help in preventing or mitigating the consequences of such disasters. However, traditional fire and smoke detection methods, such as sensors and alarms, may not be effective in some scenarios, such as outdoor environments, large areas, or complex scenes. Therefore, there is a need for a system that can use the power of computer vision and deep learning to analyze visual data and identify fire and smoke events in real time.
`KBY-AI`'s `LPR` solutions utilizes artificial intelligence and machine learning to greatly surpass legacy solutions. Now, in real-time, users can receive a vehicle's plate number through `API`.
> We can customize the `SDK` to align with customer's specific requirements.

The `ALPR` system works in these strides, the initial step is the location of the vehicle and capturing a vehicle image of front or back perspective of the vehicle, the second step is the localization of Number Plate and then extraction of vehicle Number Plate is an image. The final stride uses image segmentation strategy, for the segmentation a few techniques neural network, mathematical morphology, color analysis and histogram analysis. Segmentation is for individual character recognition. Optical Character Recognition (OCR) is one of the strategies to perceive the every character with the assistance of database stored for separate alphanumeric character.
