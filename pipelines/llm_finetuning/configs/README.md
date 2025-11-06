# LLM Fine-Tuning Configs

## Purpose

This folder contains example configuration files for the LLM fine-tuning pipeline.  
There are two different kinds of configs:

- **Training config** (Axolotl-style)  
- **Client / delivery info** (used to fill the client report template)

---

## Files

    example_config.yaml  
    example_client_info.yml

---

## File Descriptions

### example_config.yaml

This is an **Axolotl-compatible training configuration**.  
It tells Axolotl which base model to use, which dataset to pull (for example `tatsu-lab/alpaca`), where to write outputs, and what training hyperparameters to use.

You pass it to Axolotl like this:

    axolotl train pipelines/llm_finetuning/configs/example_config.yaml

---

### example_client_info.yml

This is an example of the **metadata** you would fill in for a specific client (client name, use case, metrics).  
The report generator script will read this file and produce a Markdown delivery document.

---

## Suggested Workflow

1. **Copy the example Axolotl config to a real config**

        cp pipelines/llm_finetuning/configs/example_config.yaml pipelines/llm_finetuning/configs/config.yaml

2. **Edit `config.yaml`** to match the model and dataset you selected in Runpod.

3. *(Optional)* **Copy the client info example**

        cp pipelines/llm_finetuning/configs/example_client_info.yml pipelines/llm_finetuning/configs/client_info.yml

   Then edit `client_info.yml` with the actual client data.

4. **Run training**

        axolotl train pipelines/llm_finetuning/configs/config.yaml

5. **Generate a delivery report**

        python pipelines/llm_finetuning/scripts/generate_client_report.py

---

## Notes

- Keep **training configs** and **client configs** separate.  
- Do **not commit** real `client_info.yml` files to GitHub — only the example one.  
- This folder is **LLM-only**. Future pipelines (e.g. `vision_finetuning`, `rag_pipeline`, `governance_audit`) will have their own `configs/` folders.
