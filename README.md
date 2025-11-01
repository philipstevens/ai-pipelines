# AI Pipelines

A unified framework for fine-tuning, evaluating, and deploying domain-optimized AI models.

This repository hosts modular **pipelines** for:
- LLM fine-tuning (LoRA, QLoRA)
- Vision model adaptation (CLIP, ViT)
- RAG pipelines (retrieval + generation)
- Governance audits (bias, fairness, explainability)

The system is structured to support reproducible, composable, and auditable AI workflows.

---

## Structure

```
pipelines/       # Distinct workflows (LLM, Vision, etc.)
common/          # Shared utils for data, models, eval, IO
env.yml          # Conda environment
Dockerfile       # Reproducible runtime
```

---

## Quickstart

```bash
conda env create -f env.yml
conda activate ai-pipelines

# Example: run LLM fine-tuning
python pipelines/llm_finetuning/scripts/run_finetune.py \
  --config pipelines/llm_finetuning/configs/example_config.yml
```

---

## License

MIT License © 2025 Philip Stevens
