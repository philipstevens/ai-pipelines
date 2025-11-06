# AI Pipelines

A unified framework for fine-tuning, evaluating, and deploying domain-optimized AI models.

This repository hosts modular pipelines for:

- LLM fine-tuning (LoRA, QLoRA, Axolotl)

- Vision model adaptation (CLIP, ViT) — planned

- RAG pipelines (retrieval + generation) — planned

- Governance audits (bias, fairness, explainability) — planned

The system is structured to support reproducible, composable, and auditable AI workflows.

## Structure

    ai-pipelines/
        pipelines/
          llm_finetuning/
              configs/
              scripts/
              serve/
              reports/
        common/  Shared utilities for data, models, evaluation, IO
        notebooks/ Example notebooks / Colab demos
        env.yml  Conda environment
        Dockerfile Reproducible runtime

## Quickstart

Create and activate the environment:

    conda env create -f env.yml
    conda activate ai-pipelines


Run LLM fine-tuning (example):

    python pipelines/llm_finetuning/scripts/run_finetune.py \
        --config pipelines/llm_finetuning/configs/example_config.yml


If you are running on Runpod with Axolotl, you can instead do:

    axolotl train pipelines/llm_finetuning/configs/example_config.yaml

    python pipelines/llm_finetuning/scripts/run_eval.py
    python pipelines/llm_finetuning/scripts/generate_client_report.py

## License

MIT License © 2025 Philip Stevens
