# Verbs Schema Specification (`verbs/verbs.json`)

This document specifies the exact JSON structure for Taiwanese Mandarin verbs, 3-tap pronoun conjugation grids, object examples, and Traditional Zhuyin keyboard orders in `verbs/verbs.json`.

---

## 1. Schema Definition

```typescript
interface VerbEntry {
  id: string;                     // Unique slug starting with 'v_' (e.g. 'v_chi')
  hanzi: string;                  // Verb in Traditional Chinese (e.g. '吃')
  pinyin: string;                 // Pinyin with tone (e.g. 'chī')
  zhuyin: string;                 // Zhuyin Fuhao (e.g. 'ㄔ')
  tr: string;                     // Turkish translation of infinitive (e.g. 'Yemek')
  en: string;                     // English translation of infinitive (e.g. 'To eat')
  taiwan_note?: string;           // Cultural nuance (e.g. 'Used in 吃飽了沒 greeting')
  level_id: number;               // Progression level (1 to 5)
  difficulty: "Easy" | "Medium" | "Hard";
  category: string;               // Category (e.g. 'Daily Actions', 'Dining')
  icon?: string;                  // Single emoji representing the verb (e.g. '🍜')
  pronoun_rows?: PronounRow[];    // 6-pronoun conjugation patterns
  examples?: VerbExample[];       // 3-Tap object phrase examples
  keyboard_keys?: string[];       // Zhuyin keyboard typing sequence
  translations?: Record<string, string>; // 10-language translations
}

interface PronounRow {
  key: "wo" | "ni" | "ta" | "tamen" | "nimen" | "women";
  pronoun_hanzi: string;          // e.g. '我'
  pronoun_pinyin: string;         // e.g. 'wǒ'
  pronoun_zhuyin: string;         // e.g. 'ㄨㄛˇ'
  phrase_hanzi: string;           // e.g. '我吃'
  phrase_pinyin: string;          // e.g. 'wǒ chī'
  phrase_zhuyin: string;          // e.g. 'ㄨㄛˇ ㄔ'
  tr: string;                     // e.g. 'Ben yiyorum'
  en: string;                     // e.g. 'I eat'
}

interface VerbExample {
  hanzi: string;                  // e.g. '我吃香蕉'
  pinyin: string;                 // e.g. 'wǒ chī xiāng jiāo'
  zhuyin: string;                 // e.g. 'ㄨㄛˇ ㄔ ㄒㄧㄤ ㄐㄧㄠ'
  tr: string;                     // e.g. 'Ben muz yerim'
  en: string;                     // e.g. 'I eat banana'
  object_label: string;           // e.g. 'Banana (香蕉)'
}
```

---

## 2. The 6-Pronoun Pattern Standard

Every verb must provide the authentic Taiwanese 6-pronoun sequence in `pronoun_rows`:

1. `wo`: **我** (`wǒ` / `ㄨㄛˇ`) — I
2. `ni`: **你** (`nǐ` / `ㄋㄧˇ`) — You (singular)
3. `ta`: **他/她/它** (`tā` / `ㄊㄚ`) — He / She / It
4. `tamen`: **他們** (`tā men` / `ㄊㄚ ˙ㄇㄣ`) — They
5. `nimen`: **你們** (`nǐ men` / `ㄋㄧˇ ˙ㄇㄣ`) — You (plural)
6. `women`: **我們** (`wǒ men` / `ㄨㄛˇ ˙ㄇㄣ`) — We

---

## 3. Traditional Zhuyin Keyboard (`ㄅㄆㄇㄈ`) Sequence Standard

The `keyboard_keys` array lists the exact sequential keystrokes on a Traditional Taiwan Zhuyin keyboard layout:
- Example for **吃** (`ㄔ` / 1st tone): `["ㄔ", " "]` (Space activates first tone in Taiwanese IMEs).
- Example for **好** (`ㄏㄠˇ` / 3rd tone): `["ㄏ", "ㄠ", "ˇ"]`.
- Example for **去** (`ㄑㄩˋ` / 4th tone): `["ㄑ", "ㄩ", "ˋ"]`.

---

## 4. Concrete Example Entry

```json
{
  "id": "v_chi",
  "hanzi": "吃",
  "pinyin": "chī",
  "zhuyin": "ㄔ",
  "tr": "Yemek (fiil)",
  "en": "To eat",
  "taiwan_note": "A core daily verb. Locals greet with '吃飽了沒？' (Have you eaten yet?).",
  "level_id": 1,
  "difficulty": "Easy",
  "category": "Dining & Food",
  "icon": "🍜",
  "keyboard_keys": ["ㄔ", " "],
  "pronoun_rows": [
    {
      "key": "wo",
      "pronoun_hanzi": "我",
      "pronoun_pinyin": "wǒ",
      "pronoun_zhuyin": "ㄨㄛˇ",
      "phrase_hanzi": "我吃",
      "phrase_pinyin": "wǒ chī",
      "phrase_zhuyin": "ㄨㄛˇ ㄔ",
      "tr": "Ben yiyorum",
      "en": "I eat"
    },
    {
      "key": "ni",
      "pronoun_hanzi": "你",
      "pronoun_pinyin": "nǐ",
      "pronoun_zhuyin": "ㄋㄧˇ",
      "phrase_hanzi": "你吃",
      "phrase_pinyin": "nǐ chī",
      "phrase_zhuyin": "ㄋㄧˇ ㄔ",
      "tr": "Sen yiyorsun",
      "en": "You eat"
    },
    {
      "key": "ta",
      "pronoun_hanzi": "他",
      "pronoun_pinyin": "tā",
      "pronoun_zhuyin": "ㄊㄚ",
      "phrase_hanzi": "他吃",
      "phrase_pinyin": "tā chī",
      "phrase_zhuyin": "ㄊㄚ ㄔ",
      "tr": "O yiyor",
      "en": "He/She eats"
    },
    {
      "key": "tamen",
      "pronoun_hanzi": "他們",
      "pronoun_pinyin": "tā men",
      "pronoun_zhuyin": "ㄊㄚ ˙ㄇㄣ",
      "phrase_hanzi": "他們吃",
      "phrase_pinyin": "tā men chī",
      "phrase_zhuyin": "ㄊㄚ ˙ㄇㄣ ㄔ",
      "tr": "Onlar yiyorlar",
      "en": "They eat"
    },
    {
      "key": "nimen",
      "pronoun_hanzi": "你們",
      "pronoun_pinyin": "nǐ men",
      "pronoun_zhuyin": "ㄋㄧˇ ˙ㄇㄣ",
      "phrase_hanzi": "你們吃",
      "phrase_pinyin": "nǐ men chī",
      "phrase_zhuyin": "ㄋㄧˇ ˙ㄇㄣ ㄔ",
      "tr": "Siz yiyorsunuz",
      "en": "You all eat"
    },
    {
      "key": "women",
      "pronoun_hanzi": "我們",
      "pronoun_pinyin": "wǒ men",
      "pronoun_zhuyin": "ㄨㄛˇ ˙ㄇㄣ",
      "phrase_hanzi": "我們吃",
      "phrase_pinyin": "wǒ men chī",
      "phrase_zhuyin": "ㄨㄛˇ ˙ㄇㄣ ㄔ",
      "tr": "Biz yiyoruz",
      "en": "We eat"
    }
  ],
  "examples": [
    {
      "hanzi": "我吃香蕉",
      "pinyin": "wǒ chī xiāng jiāo",
      "zhuyin": "ㄨㄛˇ ㄔ ㄒㄧㄤ ㄐㄧㄠ",
      "tr": "Ben muz yerim",
      "en": "I eat banana",
      "object_label": "Banana (香蕉)"
    },
    {
      "hanzi": "我吃蘋果",
      "pinyin": "wǒ chī píng guǒ",
      "zhuyin": "ㄨㄛˇ ㄔ ㄆㄧㄥˊ ㄍㄨㄛˇ",
      "tr": "Ben elma yerim",
      "en": "I eat apple",
      "object_label": "Apple (蘋果)"
    }
  ]
}
```
