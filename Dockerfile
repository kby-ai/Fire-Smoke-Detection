FROM openvino/ubuntu20_runtime:2024.5.0

USER root
RUN rm -rf /var/lib/apt/lists/* && apt update && apt install -y unzip \
    libjpeg8 \
    libwebp6 \
    libpng16-16 \
    libtbb2 \
    libtiff5 \
    libtbb-dev \
    libopenexr-dev \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libgomp1

# Set up working directory
RUN mkdir -p /home/openvino/kby-ai-fire
WORKDIR /home/openvino/kby-ai-fire

# Copy shared libraries and application files
COPY ./libopencv.zip .
RUN unzip libopencv.zip
RUN cp -f libopencv/* /usr/local/lib/ 
RUN ldconfig

# Copy Python and application files
COPY ./libfire.so .
COPY ./app.py .
COPY ./firesdk.py .
COPY ./requirements.txt .
COPY ./license.txt .
COPY ./run.sh .
COPY ./ncnn.zip .
RUN unzip ncnn.zip

# Install Python dependencies

RUN pip3 install --no-cache-dir -r requirements.txt
# RUN chmod +x ./run.sh
# USER openvino
# Set up entrypoint
CMD ["bash", "./run.sh"]

# Expose ports
EXPOSE 8080 9000
