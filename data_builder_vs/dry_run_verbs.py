import json
import os
import sys

sys.path.append('/Users/tarikozluk/Desktop/Dictionary-IAC/data_builder_vs')
from helpers import zhuyin_to_keys, PRONOUN_INFO

def convert_verb_tuple(item):
    # item has 32 elements
    vid, hanzi, pinyin, zhuyin, tr, en, taiwan_note, level_id, difficulty, category, icon, \
    es, de, fr, it, ja, ko, pt, hi, \
    stem_tr, stem_en, \
    obj_hanzi, obj_pinyin, obj_zhuyin, obj_icon, obj_tr, obj_en, \
    ex_hanzi, ex_pinyin, ex_zhuyin, ex_tr, ex_en = item
    
    translations = {
        "tr": tr, "en": en, "es": es, "de": de, "fr": fr,
        "it": it, "ja": ja, "ko": ko, "pt": pt, "hi": hi
    }
    
    obj_trans = {
        "tr": obj_tr, "en": obj_en,
        "es": obj_en, "de": obj_en, "fr": obj_en, "it": obj_en,
        "ja": obj_hanzi, "ko": obj_en, "pt": obj_en, "hi": obj_en
    }
    
    ex_trans = {
        "tr": ex_tr, "en": ex_en,
        "es": ex_en, "de": ex_en, "fr": ex_en, "it": ex_en,
        "ja": ex_hanzi, "ko": ex_en, "pt": ex_en, "hi": ex_en
    }
    
    # Conjugations
    conjugations = {}
    for p in PRONOUN_INFO:
        pkey = p["key"]
        conjugations[pkey] = {
            "tr": f"{p['tr_prefix']}{stem_tr}iyorum",
            "en": f"{p['en_prefix']}{stem_en}",
            "es": f"{p['es_prefix']}{es}",
            "de": f"{p['de_prefix']}{de}",
            "fr": f"{p['fr_prefix']}{fr}",
            "it": f"{p['it_prefix']}{it}",
            "ja": f"{p['ja_prefix']}{hanzi}",
            "ko": f"{p['ko_prefix']}{hanzi}",
            "pt": f"{p['pt_prefix']}{pt}",
            "hi": f"{p['hi_prefix']}{hi}"
        }
        
    pronoun_rows = []
    for p in PRONOUN_INFO:
        pkey = p["key"]
        p_hanzi = p["hanzi"]
        p_py = p["pinyin"]
        p_zy = p["zhuyin"]
        
        full_h = p_hanzi + hanzi
        full_py = p_py + " " + pinyin
        full_zy = p_zy + " " + zhuyin
        c_dict = conjugations[pkey]
        
        pronoun_rows.append({
            "pronoun_key": pkey,
            "pronoun_hanzi": p_hanzi,
            "pronoun_pinyin": p_py,
            "pronoun_zhuyin": p_zy,
            "hanzi": full_h,
            "pinyin": full_py,
            "zhuyin": full_zy,
            "keyboard_keys": zhuyin_to_keys(full_zy),
            "tr": c_dict["tr"],
            "en": c_dict["en"],
            "translations": c_dict
        })
        
    examples = [{
        "obj_hanzi": obj_hanzi,
        "obj_pinyin": obj_pinyin,
        "obj_zhuyin": obj_zhuyin,
        "obj_icon": obj_icon,
        "obj_translations": obj_trans,
        "hanzi": ex_hanzi,
        "pinyin": ex_pinyin,
        "zhuyin": ex_zhuyin,
        "translations": ex_trans,
        "id": f"{vid}_ex_1",
        "tr": ex_tr,
        "en": ex_en,
        "obj_tr": obj_tr,
        "obj_en": obj_en,
        "keyboard_keys": zhuyin_to_keys(ex_zhuyin),
        "obj_keyboard_keys": zhuyin_to_keys(obj_zhuyin)
    }]
    
    verb_obj = {
        "id": vid,
        "hanzi": hanzi,
        "pinyin": pinyin,
        "zhuyin": zhuyin,
        "difficulty": difficulty,
        "level_id": level_id,
        "icon": icon,
        "taiwan_note": taiwan_note,
        "translations": translations,
        "conjugations": conjugations,
        "examples": examples,
        "tr": tr,
        "en": en,
        "es": es,
        "de": de,
        "fr": fr,
        "it": it,
        "ja": ja,
        "ko": ko,
        "pt": pt,
        "hi": hi,
        "keyboard_keys": zhuyin_to_keys(zhuyin),
        "pronoun_rows": pronoun_rows
    }
    return verb_obj

parts = ['v_part1.json', 'v_part2.json', 'v_part3.json', 'v_part4.json']
all_converted = []
for p in parts:
    path = os.path.join('/Users/tarikozluk/Desktop/Dictionary-IAC/data_builder_vs', p)
    with open(path) as f:
        data = json.load(f)
    print(f"Loaded {p}: {len(data)} items")
    for item in data:
        all_converted.append(convert_verb_tuple(item))

print(f"Total converted new verbs: {len(all_converted)}")
assert len(all_converted) == 350
print("Sample converted verb keys:", list(all_converted[0].keys()))
print("Dry run passed successfully!")
