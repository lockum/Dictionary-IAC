import json
import os
import sys
from datetime import datetime, timezone

BASE_DIR = '/Users/tarikozluk/Desktop/Dictionary-IAC'
sys.path.append(os.path.join(BASE_DIR, 'data_builder_vs'))

from helpers import zhuyin_to_keys, PRONOUN_INFO

def convert_verb_tuple(item):
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

def main():
    print("🚀 Starting Integration of 350 Verbs and 200 Sentences...")

    # 1. Load original verbs
    verbs_path = os.path.join(BASE_DIR, 'verbs/verbs.json')
    with open(verbs_path, 'r', encoding='utf-8') as f:
        existing_verbs = json.load(f)
    print(f"Original verbs: {len(existing_verbs)}")

    # 2. Load and convert new verbs
    new_verbs = []
    for part_file in ['v_part1.json', 'v_part2.json', 'v_part3.json', 'v_part4.json']:
        p_path = os.path.join(BASE_DIR, 'data_builder_vs', part_file)
        with open(p_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"  Loaded {part_file}: {len(data)} items")
        for item in data:
            new_verbs.append(convert_verb_tuple(item))

    print(f"Total new verbs converted: {len(new_verbs)}")
    assert len(new_verbs) == 350, f"Expected 350 new verbs, got {len(new_verbs)}"

    all_verbs = existing_verbs + new_verbs
    print(f"Combined verbs total: {len(all_verbs)} (expected 382)")
    assert len(all_verbs) == 382

    # Save verbs.json
    with open(verbs_path, 'w', encoding='utf-8') as f:
        json.dump(all_verbs, f, ensure_ascii=False, indent=2)
    print("✅ Successfully updated verbs/verbs.json!")

    # 3. Load original sentences
    sentences_path = os.path.join(BASE_DIR, 'sentences/sentences.json')
    with open(sentences_path, 'r', encoding='utf-8') as f:
        existing_sentences = json.load(f)
    print(f"Original sentences: {len(existing_sentences)}")

    # 4. Load new sentences
    new_sentences = []
    for s_file in ['s_part1.json', 's_part2.json']:
        s_path = os.path.join(BASE_DIR, 'data_builder_vs', s_file)
        with open(s_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"  Loaded {s_file}: {len(data)} items")
        new_sentences.extend(data)

    print(f"Total new sentences loaded: {len(new_sentences)}")
    assert len(new_sentences) == 200, f"Expected 200 new sentences, got {len(new_sentences)}"

    all_sentences = existing_sentences + new_sentences
    print(f"Combined sentences total: {len(all_sentences)} (expected 218)")
    assert len(all_sentences) == 218

    # Save sentences.json
    with open(sentences_path, 'w', encoding='utf-8') as f:
        json.dump(all_sentences, f, ensure_ascii=False, indent=2)
    print("✅ Successfully updated sentences/sentences.json!")

    # 5. Update metadata.json
    meta_path = os.path.join(BASE_DIR, 'metadata.json')
    with open(meta_path, 'r', encoding='utf-8') as f:
        metadata = json.load(f)

    metadata['version'] = '1.2.0'
    metadata['last_updated'] = datetime.now(timezone.utc).isoformat()
    metadata['counts']['verbs'] = len(all_verbs)
    metadata['counts']['sentences'] = len(all_sentences)

    with open(meta_path, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, ensure_ascii=False, indent=2)
    print(f"✅ Successfully updated metadata.json! (verbs={len(all_verbs)}, sentences={len(all_sentences)}, version=v{metadata['version']})")

    # 6. Update seed_data.json
    seed_path = os.path.join(BASE_DIR, 'seed_data.json')
    with open(seed_path, 'r', encoding='utf-8') as f:
        seed = json.load(f)

    seed['version'] = '1.2.0'
    seed['metadata'] = metadata
    seed['verbs'] = all_verbs
    seed['sentences'] = all_sentences

    with open(seed_path, 'w', encoding='utf-8') as f:
        json.dump(seed, f, ensure_ascii=False, indent=2)
    print("✅ Successfully updated seed_data.json!")

    print("\n🎉 ALL DATA INTEGRATION COMPLETE!")

if __name__ == '__main__':
    main()
