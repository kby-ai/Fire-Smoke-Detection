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

This repository demonstrates  `Fire/Smoke Detection SDK` with high accuracy by applying artificial intelligence and machine learning techniques. </br>
Fire and smoke are common hazards that can cause severe damage to life and property. Early detection of fire and smoke can help in preventing or mitigating the consequences of such disasters. However, traditional fire and smoke detection methods, such as sensors and alarms, may not be effective in some scenarios, such as outdoor environments, large areas, or complex scenes. Therefore, there is a need for a system that can use the power of computer vision and deep learning to analyze visual data and identify fire and smoke events in real time.
> We can customize the `SDK` to align with customer's specific requirements.

## Try the API
## Online Demo
To try `KBY-AI`'s `Fire/Smoke Detection SDK` online, please visit [here](https://huggingface.co/spaces/kby-ai/FireSmokeDetection)
 ![image](https://github.com/user-attachments/assets/28f04d35-090b-4d34-864d-100b6a9374da)
 
### Postman
  The `API` can be evaluated through `Postman` tool. Here are the endpoints for testing:
  - Test with an image file: Send a `POST` request to `http://127.0.0.1:8081/fire`.
  - Test with a `base64-encoded` image: Send a `POST` request to `http://127.0.0.1:8081/fire_base64`.
  ![image](https://github.com/user-attachments/assets/8518eb28-23a6-451c-8610-79a5ad560f28)

## SDK License
This project demonstrates `KBY-AI`'s `Fire/Smoke Detection SDK`, which requires a license per machine.</br>
- The code below shows how to use the license: https://github.com/kby-ai/Fire-Smoke-Detection-Docker/blob/e2f68c88839d0c21a77d8b54d58802bcca01df5b/app.py#L17-L28
- To request the license, please provide us with the `machine code` obtained from the `getMachineCode` function.</br>
#### Please contact us:</br>
🧙`Email:` contact@kby-ai.com</br>
🧙`Telegram:` [@kbyai](https://t.me/kbyai)</br>
🧙`WhatsApp:` [+19092802609](https://wa.me/+19092802609)</br>
🧙`Discord:` [KBY-AI](https://discord.gg/CgHtWQ3k9T)</br>
🧙`Teams:` [KBY-AI](https://teams.live.com/l/invite/FBAYGB1-IlXkuQM3AY)</br>

## How to run

### 1. System Requirements
  - `CPU`: 2 cores or more (Recommended: 2 cores)
  - `RAM`: 4 GB or more (Recommended: 8 GB)
  - `HDD`: 4 GB or more (Recommended: 8 GB)
  - `OS`: `Ubuntu 20.04` or later
  - Dependency: `ncnn` (Version: 2024.12.26)

### 2. Setup and Test
  - Clone the project:
    ```bash
    git clone https://github.com/kby-ai/Fire-Smoke-Detection-Docker.git
    ```
    ```bash
    cd Fire-Smoke-Detection-Docker
    ```
  - Build the `Docker` image:
    ```bash
    sudo docker build --pull --rm -f Dockerfile -t kby-ai-fire:latest .
    ```
  - Read `machine code`
    ```
    sudo docker run -e LICENSE="xxxxx" kby-ai-fire:latest
    ```
  - Send us `machine code` obtained.
    ![image](https://github.com/user-attachments/assets/a6ca197d-43a7-4177-952b-9ebdbaeb0164)
  - Update the `license.txt` file by overwriting the `license key` that you received from `KBY-AI` team.
  - Run the `Docker` container:
    ```bash
    sudo docker run -v ./license.txt:/home/openvino/kby-ai-fire/license.txt -p 8081:8080 -p 9001:9000 kby-ai-fire:latest
    ```
    ![image](https://github.com/user-attachments/assets/f241d982-48f8-4a71-b4b3-cfac8778388e)

  - Here are the endpoints to test the `API` through `Postman`:
    Test with an image file: Send a `POST` request to `http://{xx.xx.xx.xx}:8081/fire`.</br>
    Test with a `base64-encoded` image: Send a `POST` request to `http://{xx.xx.xx.xx}:8081/fire_base64`.</br>

### 3. Execute the Gradio demo
  - Setup `Gradio`
    Ensure that the necessary dependencies are installed. </br>
    `Gradio` requires `Python 3.7` or above. </br>
    Install `Gradio` using `pip` by running the following command:
    ```bash
    pip install -r requirements.txt
    ```
  - Run the demo with the following command:
    ```bash
    cd gradio
    python demo.py
    ```
  - `SDK` can be tested on the following URL: `http://127.0.0.1:9000`



