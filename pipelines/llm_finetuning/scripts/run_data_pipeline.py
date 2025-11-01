import os, json, random, argparse
from tqdm import tqdm

def clean_text(t):
    return t.replace("\n", " ").strip()

def main(args):
    os.makedirs("data/processed", exist_ok=True)
    files = [f for f in os.listdir(args.input_dir) if f.endswith(".txt") or f.endswith(".jsonl")]
    dataset = []

    for f in files:
        path = os.path.join(args.input_dir, f)
        if f.endswith(".txt"):
            with open(path) as fh:
                for line in fh:
                    if line.strip():
                        dataset.append({"instruction": line.strip(), "response": ""})
        else:
            with open(path) as fh:
                for l in fh:
                    try:
                        dataset.append(json.loads(l))
                    except:
                        pass

    random.shuffle(dataset)
    split = int(len(dataset) * 0.9)
    train, val = dataset[:split], dataset[split:]

    with open("data/processed/train.jsonl", "w") as out:
        for r in train:
            json.dump(r, out); out.write("\n")

    with open("data/processed/val.jsonl", "w") as out:
        for r in val:
            json.dump(r, out); out.write("\n")

    print(f"Processed {len(dataset)} samples → train={len(train)} val={len(val)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_dir", default="data/raw")
    args = parser.parse_args()
    main(args)
