# Sentences Schema Specification (`sentences/sentences.json`)

This document specifies the exact JSON structure for progressive daily sentences in `sentences/sentences.json`.

---

## 1. Schema Definition

```typescript
interface SentenceEntry {
  id: string;                     // Unique slug starting with 's_' (e.g. 's_easy_1')
  level_id: number;               // Unit level (1 to 5)
  difficulty: "Easy" | "Medium" | "Hard";
  difficulty_order: number;       // Progressive index for sorting (1, 2, 3...)
  day_label: string;              // e.g. 'Day 1', 'Day 2', 'Week 2'
  hanzi: string;                  // Full sentence in Traditional Chinese
  pinyin: string;                 // Full sentence Pinyin with tone marks
  zhuyin: string;                 // Full sentence Zhuyin syllables
  tr_full: string;                // Complete sentence Turkish translation
  en_full: string;                // Complete sentence English translation
  grammar_tip: string;            // Grammatical / cultural tip
  tokens: SentenceToken[];        // Token-level word breakdown
  translations?: Record<string, string>; // Full sentence translations in 10 languages
}

interface SentenceToken {
  hanzi: string;                  // Token characters or punctuation (e.g. '你好' or '，')
  pinyin?: string;                // Token Pinyin (omitted for punctuation)
  zhuyin?: string;                // Token Zhuyin (omitted for punctuation)
  tr?: string;                    // Turkish meaning of this specific token
  en?: string;                    // English meaning of this specific token
  is_punct?: boolean;             // True if punctuation mark
}
```

---

## 2. Concrete Example Entry

```json
{
  "id": "s_easy_1",
  "level_id": 1,
  "difficulty": "Easy",
  "difficulty_order": 1,
  "day_label": "Day 1",
  "hanzi": "老闆，請問這個多少錢？",
  "pinyin": "Lǎo bǎn, qǐng wèn zhè ge duō shǎo qián?",
  "zhuyin": "ㄌㄠˇ ㄅㄢˇ，ㄑㄧㄥˇ ㄨㄣˋ ㄓㄜˋ ˙ㄍㄜ ㄉㄨㄛ ㄕㄠˇ ㄑㄧㄢˊ？",
  "tr_full": "Patron, bakar mısınız bu ne kadar?",
  "en_full": "Boss, may I ask how much this is?",
  "grammar_tip": "請問 (qǐng wèn) is the polite Taiwanese way to ask a question before requesting information.",
  "tokens": [
    {
      "hanzi": "老闆",
      "pinyin": "lǎo bǎn",
      "zhuyin": "ㄌㄠˇ ㄅㄢˇ",
      "tr": "patron / dükkan sahibi",
      "en": "boss / shop owner"
    },
    {
      "hanzi": "，",
      "is_punct": true
    },
    {
      "hanzi": "請問",
      "pinyin": "qǐng wèn",
      "zhuyin": "ㄑㄧㄥˇ ㄨㄣˋ",
      "tr": "sorabilir miyim / bakar mısınız",
      "en": "may I ask"
    },
    {
      "hanzi": "這個",
      "pinyin": "zhè ge",
      "zhuyin": "ㄓㄜˋ ˙ㄍㄜ",
      "tr": "bu",
      "en": "this one"
    },
    {
      "hanzi": "多少錢",
      "pinyin": "duō shǎo qián",
      "zhuyin": "ㄉㄨㄛ ㄕㄠˇ ㄑㄧㄢˊ",
      "tr": "ne kadar (fiyat)",
      "en": "how much money"
    },
    {
      "hanzi": "？",
      "is_punct": true
    }
  ],
  "translations": {
    "tr": "Patron, bakar mısınız bu ne kadar?",
    "en": "Boss, may I ask how much this is?",
    "es": "¿Jefe, disculpe cuánto cuesta esto?",
    "de": "Chef, darf ich fragen, wie viel das kostet?",
    "fr": "Patron, puis-je vous demander combien cela coûte ?",
    "it": "Capo, posso chiedere quanto costa questo?",
    "ja": "店長、すみません、これはいくらですか？",
    "ko": "사장님, 실례지만 이거 얼마예요?",
    "pt": "Chefe, posso perguntar quanto custa isso?",
    "hi": "मालिक, क्या मैं पूछ सकता हूँ कि यह कितने का है?"
  }
}
```

