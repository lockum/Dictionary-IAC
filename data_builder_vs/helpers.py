def zhuyin_to_keys(zhuyin_str):
    keys = []
    syllables = zhuyin_str.strip().split()
    for syl in syllables:
        has_tone = any(t in syl for t in ("ˊ", "ˇ", "ˋ", "˙"))
        for ch in syl:
            keys.append(ch)
        if not has_tone:
            keys.append("␣(1st)")
    return keys

PRONOUN_INFO = [
    {
        "key": "wo",
        "hanzi": "我",
        "pinyin": "wǒ",
        "zhuyin": "ㄨㄛˇ",
        "tr_prefix": "Ben ",
        "en_prefix": "I ",
        "es_prefix": "Yo ",
        "de_prefix": "Ich ",
        "fr_prefix": "Je ",
        "it_prefix": "Io ",
        "ja_prefix": "私は",
        "ko_prefix": "나는 ",
        "pt_prefix": "Eu ",
        "hi_prefix": "मैं "
    },
    {
        "key": "ni",
        "hanzi": "你",
        "pinyin": "nǐ",
        "zhuyin": "ㄋㄧˇ",
        "tr_prefix": "Sen ",
        "en_prefix": "You ",
        "es_prefix": "Tú ",
        "de_prefix": "Du ",
        "fr_prefix": "Tu ",
        "it_prefix": "Tu ",
        "ja_prefix": "あなたは",
        "ko_prefix": "너는 ",
        "pt_prefix": "Você ",
        "hi_prefix": "तुम "
    },
    {
        "key": "ta",
        "hanzi": "他/她/它",
        "pinyin": "tā",
        "zhuyin": "ㄊㄚ",
        "tr_prefix": "O ",
        "en_prefix": "He / She / It ",
        "es_prefix": "Él / Ella ",
        "de_prefix": "Er / Sie / Es ",
        "fr_prefix": "Il / Elle ",
        "it_prefix": "Lui / Lei ",
        "ja_prefix": "彼/彼女は",
        "ko_prefix": "그/그녀는 ",
        "pt_prefix": "Ele / Ela ",
        "hi_prefix": "वह "
    },
    {
        "key": "tamen",
        "hanzi": "他們",
        "pinyin": "tā men",
        "zhuyin": "ㄊㄚ ㄇㄣ˙",
        "tr_prefix": "Onlar ",
        "en_prefix": "They ",
        "es_prefix": "Ellos / Ellas ",
        "de_prefix": "Sie ",
        "fr_prefix": "Ils / Elles ",
        "it_prefix": "Loro ",
        "ja_prefix": "彼らは",
        "ko_prefix": "그들은 ",
        "pt_prefix": "Eles / Elas ",
        "hi_prefix": "वे "
    },
    {
        "key": "nimen",
        "hanzi": "你們",
        "pinyin": "nǐ men",
        "zhuyin": "ㄋㄧˇ ㄇㄣ˙",
        "tr_prefix": "Siz ",
        "en_prefix": "You (plural) ",
        "es_prefix": "Vosotros / Ustedes ",
        "de_prefix": "Ihr ",
        "fr_prefix": "Vous ",
        "it_prefix": "Voi ",
        "ja_prefix": "あなたたちは",
        "ko_prefix": "너희들은 ",
        "pt_prefix": "Vocês ",
        "hi_prefix": "आप लोग "
    },
    {
        "key": "women",
        "hanzi": "我們",
        "pinyin": "wǒ men",
        "zhuyin": "ㄨㄛˇ ㄇㄣ˙",
        "tr_prefix": "Biz ",
        "en_prefix": "We ",
        "es_prefix": "Nosotros ",
        "de_prefix": "Wir ",
        "fr_prefix": "Nous ",
        "it_prefix": "Noi ",
        "ja_prefix": "私たちは",
        "ko_prefix": "우리는 ",
        "pt_prefix": "Nós ",
        "hi_prefix": "हम "
    }
]

def make_verb(vid, hanzi, pinyin, zhuyin, tr_inf, en_inf, note, level_id, difficulty, category, icon,
              translations, conjugations_map, examples_raw):
    # Base verb
    res = {
        "id": vid,
        "hanzi": hanzi,
        "pinyin": pinyin,
        "zhuyin": zhuyin,
        "difficulty": difficulty,
        "level_id": level_id,
        "category": category,
        "icon": icon,
        "taiwan_note": note,
        "tr": tr_inf,
        "en": en_inf,
        "translations": translations,
        "keyboard_keys": zhuyin_to_keys(zhuyin),
        "conjugations": conjugations_map,
        "pronoun_rows": [],
        "examples": []
    }
    
    # 10 top-level language keys
    for lk in ["es", "de", "fr", "it", "ja", "ko", "pt", "hi"]:
        if lk in translations:
            res[lk] = translations[lk]
            
    # Build pronoun_rows
    for p_info in PRONOUN_INFO:
        pkey = p_info["key"]
        p_hanzi = p_info["hanzi"]
        p_py = p_info["pinyin"]
        p_zy = p_info["zhuyin"]
        
        full_hanzi = p_hanzi + hanzi
        full_py = p_py + " " + pinyin
        full_zy = p_zy + " " + zhuyin
        
        conj_trans = conjugations_map.get(pkey, {})
        row = {
            "pronoun_key": pkey,
            "pronoun_hanzi": p_hanzi,
            "pronoun_pinyin": p_py,
            "pronoun_zhuyin": p_zy,
            "hanzi": full_hanzi,
            "pinyin": full_py,
            "zhuyin": full_zy,
            "keyboard_keys": zhuyin_to_keys(full_zy),
            "tr": conj_trans.get("tr", p_info["tr_prefix"] + tr_inf),
            "en": conj_trans.get("en", p_info["en_prefix"] + en_inf),
            "translations": conj_trans
        }
        res["pronoun_rows"].append(row)
        
    # Build examples
    for i, ex in enumerate(examples_raw):
        ex_id = f"{vid}_ex_{i+1}"
        obj_h = ex.get("obj_hanzi", "")
        obj_py = ex.get("obj_pinyin", "")
        obj_zy = ex.get("obj_zhuyin", "")
        obj_icon = ex.get("obj_icon", "✨")
        obj_trans = ex.get("obj_translations", {})
        
        ex_h = ex.get("hanzi", "")
        ex_py = ex.get("pinyin", "")
        ex_zy = ex.get("zhuyin", "")
        ex_trans = ex.get("translations", {})
        
        ex_item = {
            "id": ex_id,
            "hanzi": ex_h,
            "pinyin": ex_py,
            "zhuyin": ex_zy,
            "keyboard_keys": zhuyin_to_keys(ex_zy),
            "tr": ex_trans.get("tr", ""),
            "en": ex_trans.get("en", ""),
            "translations": ex_trans,
            "obj_hanzi": obj_h,
            "obj_pinyin": obj_py,
            "obj_zhuyin": obj_zy,
            "obj_icon": obj_icon,
            "obj_translations": obj_trans,
            "obj_tr": obj_trans.get("tr", ""),
            "obj_en": obj_trans.get("en", ""),
            "obj_keyboard_keys": zhuyin_to_keys(obj_zy)
        }
        res["examples"].append(ex_item)
        
    return res

def make_sentence(sid, level_id, difficulty, order, day_label, hanzi, pinyin, zhuyin, tr_full, en_full,
                  grammar_tip, tokens, translations):
    res = {
        "id": sid,
        "level_id": level_id,
        "difficulty": difficulty,
        "difficulty_order": order,
        "day_label": day_label,
        "hanzi": hanzi,
        "pinyin": pinyin,
        "zhuyin": zhuyin,
        "tr_full": tr_full,
        "en_full": en_full,
        "grammar_tip": grammar_tip,
        "tokens": tokens,
        "translations": translations
    }
    for lk in ["es", "de", "fr", "it", "ja", "ko", "pt", "hi"]:
        if lk in translations:
            res[f"{lk}_full"] = translations[lk]
    return res
