import os, yaml, re, datetime
import pypandoc

TEMPLATE_PATH = "pipelines/llm_finetuning/reports/client_delivery_template.md"
OUTPUT_DIR = "pipelines/llm_finetuning/reports/"
CONFIG_PATH = "pipelines/llm_finetuning/configs/client_info.yml"

def render_template(template_str, data):
    """Replace {{PLACEHOLDERS}} with YAML data."""
    def repl(match):
        key = match.group(1)
        return str(data.get(key, f"{{{{{key}}}}}"))
    return re.sub(r"{{\s*([^}]+)\s*}}", repl, template_str)

def main():
    with open(CONFIG_PATH) as f:
        config = yaml.safe_load(f)

    config.setdefault("DATE", datetime.date.today().strftime("%Y-%m-%d"))
    config.setdefault("CLIENT_SLUG", config["CLIENT_NAME"].lower().replace(" ", "_"))

    with open(TEMPLATE_PATH) as f:
        template = f.read()

    rendered = render_template(template, config)

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    md_out = os.path.join(OUTPUT_DIR, f"{config['CLIENT_SLUG']}_delivery.md")

    with open(md_out, "w") as f:
        f.write(rendered)
    print(f"✅ Markdown report saved to {md_out}")

    try:
        pdf_out = md_out.replace(".md", ".pdf")
        pypandoc.convert_text(rendered, "pdf", format="md", outputfile=pdf_out, extra_args=["--standalone"])
        print(f"📄 PDF report generated: {pdf_out}")
    except Exception as e:
        print(f"⚠️ Skipped PDF export: {e}")

if __name__ == "__main__":
    main()
