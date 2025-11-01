def load_jsonl(path):
    with open(path) as f:
        return [json.loads(l) for l in f]
