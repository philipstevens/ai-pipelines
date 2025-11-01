from transformers import AutoModelForCausalLM, AutoTokenizer
import argparse, os

def quantize(model_dir, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    model = AutoModelForCausalLM.from_pretrained(model_dir, load_in_8bit=True, device_map="auto")
    tokenizer = AutoTokenizer.from_pretrained(model_dir)
    model.save_pretrained(out_dir)
    tokenizer.save_pretrained(out_dir)
    print(f"Quantized model saved to {out_dir}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_dir", required=True)
    parser.add_argument("--out_dir", default="models/quantized")
    args = parser.parse_args()
    quantize(args.model_dir, args.out_dir)
