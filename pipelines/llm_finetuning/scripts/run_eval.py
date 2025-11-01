import argparse, json, time
from transformers import AutoModelForCausalLM, AutoTokenizer
from tqdm import tqdm
import numpy as np

def evaluate(model_name, eval_file):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto")

    data = [json.loads(l) for l in open(eval_file)]
    latencies = []
    for item in tqdm(data):
        inp = item["instruction"]
        inputs = tokenizer(inp, return_tensors="pt").to("cuda")
        t0 = time.time()
        _ = model.generate(**inputs, max_new_tokens=128)
        latencies.append(time.time() - t0)
    return np.mean(latencies)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_before")
    parser.add_argument("--model_after")
    parser.add_argument("--eval_file", default="data/processed/val.jsonl")
    args = parser.parse_args()

    before = evaluate(args.model_before, args.eval_file)
    after = evaluate(args.model_after, args.eval_file)
    improvement = (before - after) / before * 100
    print(f"Latency improvement: {improvement:.2f}%")
