FROM nvidia/cuda:12.2.0-runtime-ubuntu22.04

WORKDIR /app

RUN apt-get update && apt-get install -y python3 python3-pip git && \
    pip install --upgrade pip

COPY env.yml /tmp/env.yml
RUN pip install torch transformers peft bitsandbytes accelerate fastapi uvicorn pyyaml datasets evaluate

COPY . /app
EXPOSE 8000

CMD ["python3", "pipelines/llm_finetuning/serve/app.py"]
