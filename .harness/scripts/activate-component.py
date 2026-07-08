#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


PLACEHOLDER_MARKER = "Activation status: inactive."


COMPONENT_VARIANTS = {
    "reference": ["source-library"],
    "code": ["ml-python"],
    "paper": ["latex-generic"],
    "reviewer": ["minimal"],
    "rebuttal": ["minimal"],
    "artifact": ["minimal"],
}


def is_generated_noise(path: Path) -> bool:
    return "__pycache__" in path.parts or path.suffix in {".pyc", ".pyo"}


def load_mapping(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        try:
            import yaml  # type: ignore
        except Exception as exc:
            raise SystemExit(f"{path}: expected JSON-compatible YAML or install PyYAML") from exc
        data = yaml.safe_load(text)
    if not isinstance(data, dict):
        raise SystemExit(f"{path}: expected mapping")
    return data


def dump_mapping(path: Path, data: dict[str, Any]) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def copy_blueprint(src: Path, dest: Path, *, force: bool) -> list[str]:
    conflicts: list[str] = []
    for item in src.rglob("*"):
        rel = item.relative_to(src)
        if is_generated_noise(rel):
            continue
        target = dest / rel
        if item.is_dir():
            continue
        if target.exists() and not force:
            existing = target.read_text(encoding="utf-8", errors="ignore")
            incoming = item.read_text(encoding="utf-8", errors="ignore")
            if existing == incoming:
                continue
            if target.name == "README.md" and PLACEHOLDER_MARKER in existing:
                continue
            conflicts.append(str(target))

    if conflicts:
        return conflicts

    for item in src.rglob("*"):
        rel = item.relative_to(src)
        if is_generated_noise(rel):
            continue
        target = dest / rel
        if item.is_dir():
            target.mkdir(parents=True, exist_ok=True)
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        if target.exists() and not force:
            existing = target.read_text(encoding="utf-8", errors="ignore")
            incoming = item.read_text(encoding="utf-8", errors="ignore")
            if existing == incoming:
                continue
            if not (target.name == "README.md" and PLACEHOLDER_MARKER in existing):
                continue
        shutil.copyfile(item, target)
    return []


def update_component_state(root: Path, component: str, variant: str) -> None:
    activated_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()

    manifest_path = root / ".harness" / "manifest.yaml"
    manifest = load_mapping(manifest_path)
    components = manifest.setdefault("components", {})
    if not isinstance(components, dict):
        raise SystemExit(".harness/manifest.yaml: `components` must be a mapping")
    component_state = components.setdefault(component, {})
    if not isinstance(component_state, dict):
        raise SystemExit(f".harness/manifest.yaml: component `{component}` must be a mapping")
    component_state["status"] = "active"
    component_state["active_variant"] = variant
    component_state["activated_at"] = activated_at
    dump_mapping(manifest_path, manifest)

    harness_path = root / "harness.yaml"
    harness = load_mapping(harness_path)
    harness_components = harness.setdefault("components", {})
    if not isinstance(harness_components, dict):
        raise SystemExit("harness.yaml: `components` must be a mapping")
    harness_components[component] = {
        "path": component_state.get("path", component),
        "status": "active",
        "variant": variant,
        "activated_at": activated_at,
    }
    dump_mapping(harness_path, harness)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Activate a project harness component from a local blueprint.")
    parser.add_argument("component", choices=sorted(COMPONENT_VARIANTS))
    parser.add_argument("--variant", help="blueprint variant to activate")
    parser.add_argument("--force", action="store_true", help="overwrite existing non-placeholder files")
    args = parser.parse_args(argv)

    root = Path.cwd()
    harness_dir = root / ".harness"
    if not (harness_dir / "manifest.yaml").exists():
        print("ERROR: run this script from the project root", file=sys.stderr)
        return 2

    variants = COMPONENT_VARIANTS[args.component]
    variant = args.variant or variants[0]
    if variant not in variants:
        print(f"ERROR: unknown variant {variant!r} for {args.component}; expected one of {variants}", file=sys.stderr)
        return 2

    blueprint = harness_dir / "blueprints" / args.component / variant
    if not blueprint.exists():
        print(f"ERROR: missing blueprint: {blueprint}", file=sys.stderr)
        return 2

    target = root / args.component
    conflicts = copy_blueprint(blueprint, target, force=args.force)
    if conflicts:
        print("ERROR: refusing to overwrite existing files without --force:", file=sys.stderr)
        for conflict in conflicts:
            print(f"  {conflict}", file=sys.stderr)
        return 2

    update_component_state(root, args.component, variant)
    print(f"OK: activated {args.component} component using {variant} blueprint")
    print("Next: update memory/current-status.md and run `rph validate .`.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
