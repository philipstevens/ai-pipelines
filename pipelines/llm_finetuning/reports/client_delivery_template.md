# Delivery Package – {{CLIENT_NAME}}

**Project:** Domain-Tuned, Optimized LLM  
**Date:** {{DATE}}  
**Consultant:** {{YOUR_NAME}}  

---

## 1. Summary

You now have a **fine-tuned and optimized LLM** (adapter-based) for your use case: **{{USE_CASE}}**.

### What You Get
1. Fine-tuned model or adapter artifacts  
2. Evaluation report (before vs. after)  
3. Reference runtime (FastAPI + Dockerfile)  
4. Deployment guidance for your infrastructure  
5. Monitoring recommendations  

---

## 2. What We Tuned

- **Base model:** `{{BASE_MODEL}}`  
- **Tuning method:** PEFT (LoRA / QLoRA)  
- **Data used:** {{DATA_DESC}} (≈{{N_SAMPLES}} samples / {{N_TOKENS}} tokens)  
- **Target behavior:** {{TARGET_BEHAVIOR}}  
- **Scope limits:** One use case, one model family, up to ~50k tokens  

---

## 3. Files Delivered

| File / Folder | Description |
|----------------|-------------|
| `models/{{CLIENT_SLUG}}/` | Fine-tuned adapter / model weights |
| `serve/` | FastAPI reference runtime |
| `Dockerfile` | Build + run container on your infrastructure |
| `reports/{{CLIENT_SLUG}}_benchmark.md` | Evaluation metrics |
| `configs/{{CLIENT_SLUG}}.yml` | Training and evaluation config |

> **Note:** Raw training data is *not included* unless explicitly approved by you.

---

## 4. Evaluation (Before vs. After)

**Test set size:** {{EVAL_SIZE}}  
**Methodology:** Fixed prompts, deterministic decoding, rule-based or semantic scoring  

| Metric | Before | After | Δ |
|--------|---------|--------|--|
| Quality / Task Success | {{BEFORE_QUALITY}} | {{AFTER_QUALITY}} | {{DELTA_QUALITY}} |
| Factuality / Hallucination | {{BEFORE_FACTUALITY}} | {{AFTER_FACTUALITY}} | {{DELTA_FACTUALITY}} |
| Consistency | {{BEFORE_CONSISTENCY}} | {{AFTER_CONSISTENCY}} | {{DELTA_CONSISTENCY}} |
| Latency (p50) | {{BEFORE_LAT}} ms | {{AFTER_LAT}} ms | {{DELTA_LAT}} |
| Est. Cost / 1K Tokens | {{BEFORE_COST}} | {{AFTER_COST}} | {{DELTA_COST}} |

---

## 5. How to Run It

```bash
docker build -t {{CLIENT_SLUG}}-llm .
docker run --gpus all -p 8000:8000 {{CLIENT_SLUG}}-llm
curl -X POST http://localhost:8000/generate \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Explain deductible"}'
```

This runtime is **for reference**.  
Your team can adapt it for Kubernetes, ECS, or on-prem clusters.

---

## 6. Deployment Options

- vLLM / Triton / Azure: Load adapter or merged weights  
- On-prem GPU: Use provided Dockerfile  
- Hybrid (RAG): Integrate with vector DB (Pinecone, Weaviate, pgvector)  

---

## 7. Monitoring & Operations

- Log prompt, model version, latency, tokens, and errors  
- Track latency and OOM errors (Prometheus / Grafana)  
- Optional: Content violation / jailbreak logs  
- Suggested: Model version dashboard (MLflow / DVC)

---

## 8. Next Steps

- Add more examples → incremental re-train  
- Add **RAG** for higher factuality  
- Expand to **multi-behavior** (support + triage + compliance)  
- Add **bias / explainability audit**  
- Integrate compliance filters ({{COMPLIANCE}}: HIPAA / SOC2 / FINRA)  

---

**Thank you.**  
{{YOUR_NAME}}  
{{CONTACT_EMAIL}} • {{WEBSITE}} • {{GITHUB_LINK}}
