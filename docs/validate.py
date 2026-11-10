#!/usr/bin/env python3
"""
Dictionary-IAC Schema & Integrity Validator
Runs automated checks across all JSON datasets in Dictionary-IAC to ensure:
1. Valid JSON syntax.
2. Unique IDs across all entries.
3. Required schema fields present.
4. Metadata counts match actual item counts.
5. Consolidated seed_data.json is in sync with modular files.
"""

import json
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_json(rel_path):
    full_path = os.path.join(BASE_DIR, rel_path)
    if not os.path.exists(full_path):
        print(f"❌ Missing file: {rel_path}")
        sys.exit(1)
    with open(full_path, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except Exception as e:
            print(f"❌ JSON Syntax error in {rel_path}: {e}")
            sys.exit(1)


def validate_words(words):
    required_fields = ["id", "hanzi", "pinyin", "zhuyin", "tr", "en", "level_id", "difficulty"]
    seen_ids = set()
    errors = []

    for i, w in enumerate(words):
        wid = w.get("id")
        if not wid:
            errors.append(f"Word at index {i} is missing 'id'")
            continue
        if wid in seen_ids:
            errors.append(f"Duplicate word ID: '{wid}'")
        seen_ids.add(wid)

        for rf in required_fields:
            if rf not in w or w[rf] is None or str(w[rf]).strip() == "":
                errors.append(f"Word '{wid}' is missing required field '{rf}'")

        if w.get("difficulty") not in ("Easy", "Medium", "Hard"):
            errors.append(f"Word '{wid}' has invalid difficulty: '{w.get('difficulty')}' (must be Easy/Medium/Hard)")

    return errors, len(seen_ids)


def validate_verbs(verbs):
    required_fields = ["id", "hanzi", "pinyin", "zhuyin", "tr", "en"]
    seen_ids = set()
    errors = []

    for i, v in enumerate(verbs):
        vid = v.get("id")
        if not vid:
            errors.append(f"Verb at index {i} is missing 'id'")
            continue
        if vid in seen_ids:
            errors.append(f"Duplicate verb ID: '{vid}'")
        seen_ids.add(vid)

        for rf in required_fields:
            if rf not in v or v[rf] is None:
                errors.append(f"Verb '{vid}' is missing required field '{rf}'")

    return errors, len(seen_ids)


def validate_sentences(sentences):
    required_fields = ["id", "hanzi", "pinyin", "zhuyin", "tr_full", "en_full", "tokens"]
    seen_ids = set()
    errors = []

    for i, s in enumerate(sentences):
        sid = s.get("id")
        if not sid:
            errors.append(f"Sentence at index {i} is missing 'id'")
            continue
        if sid in seen_ids:
            errors.append(f"Duplicate sentence ID: '{sid}'")
        seen_ids.add(sid)

        for rf in required_fields:
            if rf not in s or s[rf] is None:
                errors.append(f"Sentence '{sid}' is missing required field '{rf}'")

    return errors, len(seen_ids)


def main():
    print("🔍 Validating Dictionary-IAC dataset integrity...")
    meta = load_json("metadata.json")
    words = load_json("words/words.json")
    verbs = load_json("verbs/verbs.json")
    sentences = load_json("sentences/sentences.json")
    levels = load_json("curriculum/levels.json")
    purposes = load_json("curriculum/purposes.json")
    seed = load_json("seed_data.json")

    all_errors = []

    # 1. Validate Words
    w_errors, w_count = validate_words(words)
    all_errors.extend(w_errors)

    # 2. Validate Verbs
    v_errors, v_count = validate_verbs(verbs)
    all_errors.extend(v_errors)

    # 3. Validate Sentences
    s_errors, s_count = validate_sentences(sentences)
    all_errors.extend(s_errors)

    # 4. Validate metadata counts
    m_counts = meta.get("counts", {})
    if m_counts.get("words") != w_count:
        all_errors.append(f"metadata.json counts.words ({m_counts.get('words')}) does not match actual count ({w_count})")
    if m_counts.get("verbs") != v_count:
        all_errors.append(f"metadata.json counts.verbs ({m_counts.get('verbs')}) does not match actual count ({v_count})")
    if m_counts.get("sentences") != s_count:
        all_errors.append(f"metadata.json counts.sentences ({m_counts.get('sentences')}) does not match actual count ({s_count})")

    # 5. Check consolidated seed_data.json count parity
    if len(seed.get("words", [])) != w_count:
        all_errors.append(f"seed_data.json words ({len(seed.get('words', []))}) does not match words/words.json count ({w_count})")
    if len(seed.get("verbs", [])) != v_count:
        all_errors.append(f"seed_data.json verbs ({len(seed.get('verbs', []))}) does not match verbs/verbs.json count ({v_count})")

    if all_errors:
        print(f"❌ Validation FAILED with {len(all_errors)} error(s):")
        for err in all_errors:
            print(f"  - {err}")
        sys.exit(1)

    print("✅ All validation checks PASSED!")
    print(f"   - Version: v{meta.get('version')}")
    print(f"   - Words: {w_count}")
    print(f"   - Verbs: {v_count}")
    print(f"   - Sentences: {s_count}")
    print(f"   - Levels: {len(levels)}")
    print(f"   - Purposes: {len(purposes)}")


if __name__ == "__main__":
    main()
