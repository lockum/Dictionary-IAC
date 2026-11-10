# Dictionary-IAC Documentation Index

This directory provides data schemas, linguistic guidelines, and contribution workflows for **Dictionary-IAC**.

---

## Documentation Sections

| Document | Purpose |
|---|---|
| **[VOCABULARY_SCHEMA.md](VOCABULARY_SCHEMA.md)** | Full JSON schema, field requirements, and examples for `words/words.json`. |
| **[VERBS_SCHEMA.md](VERBS_SCHEMA.md)** | Verbs schema, pronoun matrices, object examples, and Traditional Zhuyin keyboard orders for `verbs/verbs.json`. |
| **[SENTENCES_SCHEMA.md](SENTENCES_SCHEMA.md)** | Sentence card structure, token breakdowns, and grammar notes for `sentences/sentences.json`. |
| **[AI_AGENT_WORKFLOW.md](AI_AGENT_WORKFLOW.md)** | **Primary guide for AI Agents**: Rules for generating authentic Traditional Taiwanese entries, updating versions, and merging snapshots. |
| **[validate.py](validate.py)** | Command-line validation script to verify schema compliance and detect duplicate IDs. |

---

## Quality Principles

1. **Strictly Traditional Characters (繁體中文 • 台灣)**: Always use standard Taiwanese Traditional characters (e.g., 台灣, 開心, 買單, 吃飯, 為什麼). Never use Simplified Chinese (简体中文).
2. **Standard Taiwanese Zhuyin Fuhao (注音符號)**: Accompany every Hanzi with correct Zhuyin (e.g., ㄋㄧˇ ㄏㄠˇ). Include tone marks (ˊ for 2nd tone, ˇ for 3rd tone, ˋ for 4th tone, ˙ for neutral/5th tone).
3. **10-Language Translation Matrix**: Entries include full translations for Turkish (`tr`), English (`en`), Spanish (`es`), German (`de`), French (`fr`), Italian (`it`), Japanese (`ja`), Korean (`ko`), Portuguese (`pt`), and Hindi (`hi`).
4. **Authentic Taiwanese Lifestyle**: Notes reflect authentic Taiwanese daily life, night markets, breakfast culture, MRT navigation, and social politeness.
