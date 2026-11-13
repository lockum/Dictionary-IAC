def make_word(id, hanzi, pinyin, zhuyin, tr, en, taiwan_note, level_id, difficulty, category, translations, week_label=None):
    if week_label is None:
        week_label = f"Week {level_id}"
    res = {
        "id": id,
        "hanzi": hanzi,
        "pinyin": pinyin,
        "zhuyin": zhuyin,
        "tr": tr,
        "en": en,
        "taiwan_note": taiwan_note,
        "level_id": level_id,
        "difficulty": difficulty,
        "category": category,
        "week_label": week_label,
        "translations": translations
    }
    for lang in ["es", "de", "fr", "it", "ja", "ko", "pt", "hi"]:
        if lang in translations:
            res[lang] = translations[lang]
    return res
