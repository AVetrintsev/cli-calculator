"""Render documentation previews from the shared translation fragments."""

import json
from pathlib import Path


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def main():
    help_dir = Path(__file__).resolve().parent
    locale_dir = help_dir.parent / "localization"
    index = read_json(help_dir / "operator-help.json")
    messages = read_json(locale_dir / "catalog.json")["messages"]
    keys = index["fragments"]
    if len(keys) != len(set(keys)):
        raise ValueError("Duplicate help fragment")

    for language in ("en", "ru"):
        values = read_json(locale_dir / f"{language}.json")
        parts = []
        previous_table = False
        for key in keys:
            is_table = messages[key]["elementType"] == "help_table_row"
            value = values[key]
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"Empty fragment: {language}/{key}")
            if language == "en" and value != messages[key]["text"]:
                raise ValueError(f"English source mismatch: {key}")
            if parts:
                parts.append("\n" if is_table and previous_table else "\n\n")
            parts.append(value)
            previous_table = is_table
        (help_dir / f"operators.{language}.md").write_text(
            "".join(parts) + "\n", encoding="utf-8"
        )


if __name__ == "__main__":
    main()
