# LLM Fine-Tuning Pipeline

This module fine-tunes and evaluates large language models using LoRA / QLoRA methods.

### Steps

1. **Prepare Data**
   ```bash
   python scripts/run_data_pipeline.py --input_dir data/raw
   ```

2. **Fine-tune**
   ```bash
   python scripts/run_finetune.py --config configs/example_config.yml
   ```

3. **Evaluate**
   ```bash
   python scripts/run_eval.py --model_before meta-llama/Llama-3-8B-Instruct --model_after models/finetuned-llama3/
   ```

4. **Quantize**
   ```bash
   python scripts/quantize.py --model_dir models/finetuned-llama3/ --out_dir models/quantized/
   ```

5. **Serve**
   ```bash
   docker build -t llm-runtime .
   docker run --gpus all -p 8000:8000 llm-runtime
   ```

---

Output:
- Fine-tuned adapter / model
- Evaluation report
- Lightweight inference container
