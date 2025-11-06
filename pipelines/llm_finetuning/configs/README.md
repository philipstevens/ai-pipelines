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
