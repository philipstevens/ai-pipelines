FROM runpod/worker:latest

RUN apt-get update && apt-get install -y git
RUN pip install --upgrade pip wheel
RUN pip install axolotl[flash-attn] pypandoc pandas matplotlib

WORKDIR /workspace/fine-tuning
COPY . .

CMD ["bash"]
