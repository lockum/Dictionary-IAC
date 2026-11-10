# Vocabulary Schema Specification (`words/words.json`)

This document specifies the exact JSON structure for vocabulary cards in `words/words.json`.

---

## 1. Schema Definition

Each word in `words/words.json` must conform to the following object definition:

```typescript
interface WordEntry {
  id: string;              // Unique slug starting with 'w_' (e.g. 'w_kaixin')
  hanzi: string;           // Traditional Chinese characters (繁體中文)
  pinyin: string;          // Hanyu Pinyin with tone marks (e.g. 'kāi xīn')
  zhuyin: string;          // Traditional Zhuyin Fuhao (e.g. 'ㄎㄞ ㄒㄧㄣ')
  tr: string;              // Primary Turkish translation
  en: string;              // Primary English translation
  taiwan_note?: string;    // Contextual explanation or Taiwanese cultural usage note
  level_id: number;        // Level number (1 to 5)
  difficulty: "Easy" | "Medium" | "Hard";
  category: string;        // Categorical grouping (e.g., 'Daily Life', 'Food', 'Work')
  week_label?: string;     // Optional cohort label (e.g., 'Week 1', 'Week 2')
  translations?: {         // Full 10-language matrix
    tr: string;            // Turkish (Türkçe)
    en: string;            // English
    es: string;            // Spanish (Español)
    de: string;            // German (Deutsch)
    fr: string;            // French (Français)
    it: string;            // Italian (Italiano)
    ja: string;            // Japanese (日本語)
    ko: string;            // Korean (한국어)
    pt: string;            // Portuguese (Português)
    hi: string;            // Hindi (हिन्दी)
  };
}
```

---

## 2. Field Specifications & Requirements

| Field | Type | Required | Description & Constraints |
|---|---|---|---|
| `id` | `string` | **Yes** | Unique identifier prefixed with `w_`. Must use lowercase letters, numbers, and underscores (e.g. `w_chifan`, `w_danbing`). |
| `hanzi` | `string` | **Yes** | Traditional Chinese characters only (繁體中文). Never use Simplified Chinese (e.g., use 買 not 买, 謝謝 not 谢谢, 開 not 开). |
| `pinyin` | `string` | **Yes** | Standard Pinyin with unicode tone diacritics (`ā`, `á`, `ǎ`, `à`, `ō`, `ó`, etc.). Space-separated between characters. |
| `zhuyin` | `string` | **Yes** | Standard Taiwanese Zhuyin Fuhao syllables separated by spaces. Must include tone marks: 2nd tone `ˊ`, 3rd tone `ˇ`, 4th tone `ˋ`, neutral tone `˙`. |
| `tr` | `string` | **Yes** | Primary Turkish translation, clear and accurate. |
| `en` | `string` | **Yes** | Primary English translation. |
| `taiwan_note` | `string` | No | Authentic Taiwanese contextual note explaining how locals use it (e.g., in breakfast shops, convenience stores, or line chats). |
| `level_id` | `number` | **Yes** | An integer from `1` to `5` matching progression difficulty. |
| `difficulty` | `string` | **Yes** | Must be one of: `"Easy"`, `"Medium"`, or `"Hard"`. |
| `category` | `string` | **Yes** | The thematic topic (e.g., `"Daily Life"`, `"Food & Drinks"`, `"Work & Office"`, `"Transportation"`, `"Question Types"`). |
| `translations` | `object` | Recommended | Dictionary object containing 10-language translations (`tr`, `en`, `es`, `de`, `fr`, `it`, `ja`, `ko`, `pt`, `hi`). |

---

## 3. Concrete Example Entry

```json
{
  "id": "w_zhenzhunaicha",
  "hanzi": "珍珠奶茶",
  "pinyin": "zhēn zhū nǎi chá",
  "zhuyin": "ㄓㄣ ㄓㄨ ㄋㄞˇ ㄔㄚˊ",
  "tr": "Balonlu sütlü çay (Boba / Bubble Tea)",
  "en": "Bubble milk tea (Pearl milk tea)",
  "taiwan_note": "Taiwan's national drink. Often abbreviated as 珍奶 (zhēn nǎi).",
  "level_id": 1,
  "difficulty": "Easy",
  "category": "Food & Drinks",
  "translations": {
    "tr": "Balonlu sütlü çay",
    "en": "Bubble milk tea",
    "es": "Té de burbujas con leche",
    "de": "Bubble-Milchtee",
    "fr": "Thé au lait aux perles",
    "it": "Tè al latte con boba",
    "ja": "タピオカミルクティー",
    "ko": "버블 밀크티",
    "pt": "Chá com leite e bolhas",
    "hi": "बबल मिल्क टी"
  }
}
```

