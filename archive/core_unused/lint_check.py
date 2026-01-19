#!/usr/bin/env python3
"""
Run flake8 linting on ddi-pays-pipelines files

Usage:
    python core/lint_check.py <file_path> [file_path2 ...]
    python core/lint_check.py ddi_pays_pipelines/generic_etls/ascs_decision_service_simulation.py
    python core/lint_check.py ddi_pays_pipelines/generic_etls/*.py
"""
import subprocess
import sys
import os


def run_flake8(file_paths):
    """
    Run flake8 on specified files using ddi-pays-pipelines .flake8 config

    Args:
        file_paths: List of file paths to lint

    Returns:
        int: Exit code (0 if success, 1 if issues found)
    """
    # Path to ddi-pays-pipelines repo (adjust if needed)
    ddi_pays_pipelines_path = os.path.expanduser(
        "~/Documents/GitHub/ddi-pays-pipelines"
    )

    if not os.path.exists(ddi_pays_pipelines_path):
        print(f"❌ Error: ddi-pays-pipelines not found at {ddi_pays_pipelines_path}")
        print("   Update the path in this script if needed")
        return 1

    # Path to flake8 (try common locations)
    flake8_paths = [
        os.path.expanduser("~/Library/Python/3.9/bin/flake8"),
        "/usr/local/bin/flake8",
        "flake8"  # System PATH
    ]

    flake8_cmd = None
    for path in flake8_paths:
        if os.path.exists(path) or path == "flake8":
            flake8_cmd = path
            break

    if not flake8_cmd:
        print("❌ Error: flake8 not found. Install with: pip3 install flake8")
        return 1

    print("=" * 80)
    print("Running flake8 linter")
    print("=" * 80)
    print(f"Workspace: {ddi_pays_pipelines_path}")
    print(f"Files: {', '.join(file_paths)}")
    print()

    # Build full paths
    full_paths = []
    for file_path in file_paths:
        if os.path.isabs(file_path):
            full_paths.append(file_path)
        else:
            full_paths.append(os.path.join(ddi_pays_pipelines_path, file_path))

    # Run flake8
    try:
        result = subprocess.run(
            [flake8_cmd] + full_paths,
            cwd=ddi_pays_pipelines_path,
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            print("✅ No linting issues found!")
            return 0
        else:
            print("❌ Linting issues found:\n")
            print(result.stdout)
            if result.stderr:
                print("Errors:")
                print(result.stderr)
            return 1

    except FileNotFoundError:
        print(f"❌ Error: Could not run flake8 at {flake8_cmd}")
        print("   Install with: pip3 install flake8")
        return 1
    except Exception as e:
        print(f"❌ Error running flake8: {e}")
        return 1


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python lint_check.py <file_path> [file_path2 ...]")
        print()
        print("Examples:")
        print("  python core/lint_check.py ddi_pays_pipelines/generic_etls/ascs_decision_service_simulation.py")
        print("  python core/lint_check.py ddi_pays_pipelines/generic_etls/*.py")
        print("  python core/lint_check.py ddi_pays_pipelines/generic_etl_runner/etls.py")
        sys.exit(1)

    file_paths = sys.argv[1:]
    exit_code = run_flake8(file_paths)
    sys.exit(exit_code)






