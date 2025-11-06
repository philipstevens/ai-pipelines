import subprocess
import sys
import os

def main():
    config_path = sys.argv[1] if len(sys.argv) > 1 else "pipelines/llm_finetuning/configs/example_config.yaml"
    print(f"🚀 Starting fine-tuning with Axolotl using {config_path}")
    subprocess.run(["axolotl", "train", config_path], check=True)
    print("✅ Fine-tuning complete.")

if __name__ == "__main__":
    main()
