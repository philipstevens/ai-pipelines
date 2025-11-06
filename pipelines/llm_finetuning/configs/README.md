# Configuration Files

This directory contains **example configurations** for fine-tuning LLMs with Axolotl on Runpod.

| File | Description |
|------|--------------|
| `example_config.yaml` | Axolotl-compatible training configuration |
| `example_client_info.yml` | Template for delivery metadata |

Usage:
```bash
cp example_config.yaml config.yaml
axolotl train config.yaml
---

### **`notebooks/colab_notebook.ipynb`**
Add this key cell for training:
```python
!axolotl train pipelines/llm_finetuning/configs/example_config.yaml
Then reuse the same evaluation and report-generation cells.
