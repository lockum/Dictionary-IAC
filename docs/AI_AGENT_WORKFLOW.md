# AI Agent Contribution Workflow

This document provides explicit, deterministic instructions for AI coding assistants (Antigravity, Claude, ChatGPT, Codex, Gemini) when requested to add new vocabulary, verbs, categories, or sentences to **Dictionary-IAC**.

---

## 1. Operating Rules for AI Agents

1. **Strictly Traditional Characters (繁體中文)**:
   - Always output authentic Taiwanese Traditional Chinese characters.
   - **Forbidden**: Simplified characters (e.g., never output `买`, `头`, `说`, `饭`, `谢`).
   - **Required**: Traditional equivalents (e.g., `買`, `頭`, `說`, `飯`, `謝`).
2. **Accurate Taiwanese Zhuyin (注音符號)**:
   - Always provide the authentic Taiwanese phonetic transcription for every syllable.
   - Tone mark conventions:
     - 1st tone: No mark (or space ` `)
     - 2nd tone: `ˊ` (U+02CA)
     - 3rd tone: `ˇ` (U+02C7)
     - 4th tone: `ˋ` (U+02CB)
     - Neutral tone: `˙` (U+02D9) at the beginning of the syllable (e.g., `˙ㄍㄜ`, `˙ㄇㄣ`)
3. **Pinyin with Tone Marks**:
   - Provide standard Hanyu Pinyin with tone marks: `ā, á, ǎ, à`, `ē, é, ě, è`, `ī, í, ǐ, ì`, `ō, ó, ǒ, ò`, `ū, ú, ǔ, ù`, `ǖ, ǘ, ǚ, ǜ`.
4. **Authentic Taiwanese Lifestyle**:
   - Taiwan has unique terms distinct from mainland Mandarin. Always prefer Taiwanese terminology:
     - Taxi: 計程車 (`jì chéng chē`), not 出租车
     - Fork: 叉子 (`chā zi`)
     - Potato: 馬鈴薯 (`mǎ líng shǔ`), not 土豆
     - Cheese: 起司 (`qǐ sī`), not 奶酪
     - Boba: 珍珠 (`zhēn zhū`), not 波霸
     - Check please: 買單 (`mǎi dān`), not 结账

---

## 2. Step-by-Step Execution Plan for AI Agents

When the user asks: *"Add 10 new words about X to Dictionary-IAC"* or *"Add verbs regarding Y"*:

### Step 1: Inspect Existing Entries
- Read `words/words.json` (or `verbs/verbs.json`).
- Collect all existing `id` and `hanzi` values into sets to ensure **zero duplicates**.

### Step 2: Generate New Entries
- Create IDs with semantic lowercase slugs (e.g. `w_danbing`, `w_kaixin`, `v_kan`).
- Fill all required fields matching [`VOCABULARY_SCHEMA.md`](VOCABULARY_SCHEMA.md) or [`VERBS_SCHEMA.md`](VERBS_SCHEMA.md).
- Generate translations for all 10 supported language codes:
  `tr`, `en`, `es`, `de`, `fr`, `it`, `ja`, `ko`, `pt`, `hi`.

### Step 3: Append to Specific JSON Files
- Append the new items into `words/words.json` (or `verbs/verbs.json`, `sentences/sentences.json`).
- Ensure proper comma formatting and valid JSON.

### Step 4: Update `metadata.json`
- Increment `counts.words`, `counts.verbs`, or `counts.sentences`.
- Bump the semantic version in `metadata.json`:
  - New words/verbs added: Bump minor version (e.g. `1.0.0` ➔ `1.1.0`).
  - Typo fix or correction: Bump patch version (e.g. `1.1.0` ➔ `1.1.1`).
- Set `last_updated` to current ISO-8601 UTC timestamp: `new Date().toISOString()`.

### Step 5: Update Consolidated `seed_data.json`
- Ensure `seed_data.json` snapshot is updated with the new items in `words`, `verbs`, or `sentences` so the all-in-one file stays in 100% sync with the modular subdirectories.

### Step 6: Run Automated Validation
- Run the schema validator:
  ```bash
  python3 docs/validate.py
  ```
- If any error or duplicate ID is reported, fix it immediately before finishing.

---

## 3. Quick Reference Template for New Words

```json
{
  "id": "w_<slug>",
  "hanzi": "繁體漢字",
  "pinyin": "pīn yīn",
  "zhuyin": "ㄓㄨˋ ㄧㄣ",
  "tr": "Türkçe anlamı",
  "en": "English meaning",
  "taiwan_note": "Authentic usage in Taiwan (e.g. how locals say it).",
  "level_id": 1,
  "difficulty": "Easy",
  "category": "Daily Life",
  "translations": {
    "tr": "Türkçe",
    "en": "English",
    "es": "Español",
    "de": "Deutsch",
    "fr": "Français",
    "it": "Italiano",
    "ja": "日本語",
    "ko": "한국어",
    "pt": "Português",
    "hi": "हिन्दी"
  }
}
```
