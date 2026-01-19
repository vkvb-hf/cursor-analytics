#!/usr/bin/env python3
"""Test profile reference extraction from filenames."""

import re

# Sample filenames from the data
sample_filenames = [
    "CF_THLH73H2VSWDN842_Jade1314 2025-08-03T16_34_35Z.csv",
    "AU_TBDLJCJZX8LLWWF3_Jade1314 2025-10-31T13_25_16Z.csv",
    "FR_J2M3VKGZMHZNZ4Q9_Jade1314 2025-10-31T13_31_40Z.csv",
    "GB_QLKKNG4S2Q9428Q9_Jade1314 2025-09-14T17_43_53Z.csv",
    "NZ_ZDGX3H4S2Q9428Q9_Jade1314 2025-10-31T13_41_09Z.csv"
]

# Current regex pattern
pattern = r"_([A-Z0-9]{13})_"

print("Testing profile reference extraction:")
print("=" * 80)

for filename in sample_filenames:
    match = re.search(pattern, filename)
    if match:
        profile_ref = match.group(1)
        print(f"✅ {filename}")
        print(f"   → Profile Reference: {profile_ref}")
    else:
        print(f"❌ {filename}")
        print(f"   → No match found!")
        # Try alternative patterns
        alt1 = re.search(r"([A-Z0-9]{13})", filename)
        if alt1:
            print(f"   → Alternative match: {alt1.group(1)}")

