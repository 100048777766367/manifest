# ==============================================================================
# 📋 MANIFEST ENGINE: QUẢN LÝ ĐỊNH MỨC 10 TỆP BẮT BUỘC (10-FILE BOM)
# ==============================================================================
MANDATORY_10_BOM = [
    ".github/workflows/node.yml",
    "Dockerfile",
    ".github/dependabot.yml",
    "contract.json",
    "engine.py",
    "synapse_forward.json",
    "synapses/bio_passport.json",
    "synapses/state.json",
    ".gitignore",
    "README.md"
]

def verify_bom_integrity(file_list):
    missing = []
    for item in MANDATORY_10_BOM:
        matched = False
        for f in file_list:
            if item == f or (item.endswith("engine.py") and ("engine.py" in f or "kernel.py" in f)):
                matched = True; break
        if not matched: missing.append(item)
    return len(missing) == 0, missing

print("📋 [MANIFEST ENGINE] Đã nạp Định Mức 10 Tệp BOM Chuẩn Quốc Tế.")
