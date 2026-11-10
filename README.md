# Dictionary-IAC (Infrastructure as Content)

A version-controlled linguistic dataset for Traditional Taiwanese Mandarin (繁體中文與注音符號), designed for modern language learning platforms and natural language processing.

---

## 1. Overview

**Dictionary-IAC** decouples language content from application source code. It provides structured, curated vocabulary, Taiwanese Mandarin verbs, pronoun conjugation matrices, and progressive daily sentences across 10 global languages.

### Core Datasets

- **Vocabulary Deck (`words/`)**: High-frequency authentic vocabulary categorized by daily life, work, emotions, dining, culture, and Taiwanese lifestyle.
- **Verbs Training (`verbs/`)**: High-frequency verbs accompanied by authentic pronoun patterns (`我去`, `你去`, `他/她/它去`, `他們去`, `你們去`, `我們去`), object examples, and Traditional Zhuyin keyboard (`ㄅㄆㄇㄈ`) typing sequences.
- **Daily Sentences (`sentences/`)**: Progressive daily sentences graded from Easy to Hard with token-level bilingual breakdowns and Taiwanese grammar notes.
- **Curriculum Paths (`curriculum/`)**: Authentic thematic units, skill tree levels, and purpose tracks.

---

## 2. Directory Layout

```
Dictionary-IAC/
├── README.md                 # Project overview
├── metadata.json             # Dataset versioning & item counts
├── seed_data.json            # Consolidated snapshot dataset
├── words/
│   └── words.json            # Vocabulary entries
├── verbs/
│   └── verbs.json            # Verbs & pronoun conjugations
├── sentences/
│   └── sentences.json        # Graded sentence cards
├── curriculum/
│   ├── levels.json           # Progression levels
│   └── purposes.json         # Learning purposes
└── docs/                     # Schemas & AI Agent Contribution Guides
    ├── README.md             # Documentation index
    ├── VOCABULARY_SCHEMA.md  # Word schema specification & examples
    ├── VERBS_SCHEMA.md       # Verb schema & conjugation rules
    ├── SENTENCES_SCHEMA.md   # Sentence token schema
    ├── AI_AGENT_WORKFLOW.md  # Operational guide for AI assistants
    └── validate.py           # Automated schema & ID validator
```

---

## 3. Contributing & AI Agent Instructions

For full specifications on how to add new words, verbs, or sentences, please refer to the **[`docs/`](docs/README.md)** directory:

- Read **[`docs/AI_AGENT_WORKFLOW.md`](docs/AI_AGENT_WORKFLOW.md)** before generating or updating entries.
- Always validate entries by running:
  ```bash
  python3 docs/validate.py
  ```

---
*Maintained by Lockum • All Rights Reserved.*
