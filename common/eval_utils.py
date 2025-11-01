def compare_metrics(before, after):
    return {k: after[k] - before[k] for k in after}
