import argparse, os, yaml
from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForCausalLM, TrainingArguments, Trainer
from peft import LoraConfig, get_peft_model

def main(cfg):
    tokenizer = AutoTokenizer.from_pretrained(cfg["base_model"], use_fast=True)
    tokenizer.pad_token = tokenizer.eos_token

    dataset = load_dataset("json", data_files={"train": cfg["train_path"], "validation": cfg["val_path"]})
    def tokenize(batch):
        text = batch["instruction"] + "\n" + batch.get("response", "")
        return tokenizer(text, truncation=True, padding="max_length", max_length=cfg["max_seq_length"])
    tokenized = dataset.map(tokenize, batched=True)

    model = AutoModelForCausalLM.from_pretrained(
        cfg["base_model"],
        load_in_4bit=cfg.get("load_in_4bit", True),
        device_map="auto",
    )

    lora_config = LoraConfig(
        r=cfg["lora_r"],
        lora_alpha=cfg["lora_alpha"],
        target_modules=["q_proj", "v_proj"],
        lora_dropout=cfg["lora_dropout"],
        bias="none",
        task_type="CAUSAL_LM",
    )
    model = get_peft_model(model, lora_config)

    args = TrainingArguments(
        output_dir=cfg["output_dir"],
        num_train_epochs=cfg["num_train_epochs"],
        per_device_train_batch_size=cfg["per_device_train_batch_size"],
        learning_rate=cfg["learning_rate"],
        bf16=cfg.get("bf16", True),
        evaluation_strategy="epoch",
        save_strategy="epoch",
        logging_steps=20,
    )

    trainer = Trainer(
        model=model,
        args=args,
        train_dataset=tokenized["train"],
        eval_dataset=tokenized["validation"],
    )

    trainer.train()
    model.save_pretrained(cfg["output_dir"])
    print(f"✅ Model saved to {cfg['output_dir']}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="pipelines/llm_finetuning/configs/example_config.yml")
    args = parser.parse_args()
    with open(args.config) as f:
        cfg = yaml.safe_load(f)
    main(cfg)
