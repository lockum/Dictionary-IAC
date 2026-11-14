import json

# Load base vocab from words.json and verbs.json
VOCAB = {}
try:
    with open('/Users/tarikozluk/Desktop/Dictionary-IAC/words/words.json') as f:
        words = json.load(f)
    for w in words:
        VOCAB[w['hanzi']] = {
            'hanzi': w['hanzi'],
            'pinyin': w['pinyin'],
            'zhuyin': w['zhuyin'],
            'tr': w['tr'],
            'en': w['en'],
            'translations': w.get('translations', {}),
            'es': w.get('es', ''),
            'de': w.get('de', ''),
            'fr': w.get('fr', ''),
            'it': w.get('it', ''),
            'ja': w.get('ja', ''),
            'ko': w.get('ko', ''),
            'pt': w.get('pt', ''),
            'hi': w.get('hi', '')
        }
except Exception as e:
    print("Error loading words:", e)

try:
    with open('/Users/tarikozluk/Desktop/Dictionary-IAC/verbs/verbs.json') as f:
        verbs = json.load(f)
    for v in verbs:
        if v['hanzi'] not in VOCAB:
            VOCAB[v['hanzi']] = {
                'hanzi': v['hanzi'],
                'pinyin': v['pinyin'],
                'zhuyin': v['zhuyin'],
                'tr': v['tr'],
                'en': v['en'],
                'translations': v.get('translations', {}),
                'es': v.get('es', ''),
                'de': v.get('de', ''),
                'fr': v.get('fr', ''),
                'it': v.get('it', ''),
                'ja': v.get('ja', ''),
                'ko': v.get('ko', ''),
                'pt': v.get('pt', ''),
                'hi': v.get('hi', '')
            }
except Exception as e:
    print("Error loading verbs:", e)

# Common functional words & particles
COMMON_WORDS = {
    '我': ('wǒ', 'ㄨㄛˇ', 'Ben', 'I', 'Yo', 'Ich', 'Je', 'Io', '私', '나', 'Eu', 'मैं'),
    '你': ('nǐ', 'ㄋㄧˇ', 'Sen', 'You', 'Tú', 'Du', 'Tu', 'Tu', 'あなた', '너', 'Você', 'तुम'),
    '他': ('tā', 'ㄊㄚ', 'O (erkek)', 'He', 'Él', 'Er', 'Il', 'Lui', '彼', '그', 'Ele', 'वह'),
    '她': ('tā', 'ㄊㄚ', 'O (kadın)', 'She', 'Ella', 'Sie', 'Elle', 'Lei', '彼女', '그녀', 'Ela', 'वह'),
    '我們': ('wǒ men', 'ㄨㄛˇ ㄇㄣ˙', 'Biz', 'We', 'Nosotros', 'Wir', 'Nous', 'Noi', '私たち', '우리', 'Nós', 'हम'),
    '你們': ('nǐ men', 'ㄋㄧˇ ㄇㄣ˙', 'Siz', 'You all', 'Vosotros / Ustedes', 'Ihr', 'Vous', 'Voi', 'あなたたち', '너희들', 'Vocês', 'आप लोग'),
    '他們': ('tā men', 'ㄊㄚ ㄇㄣ˙', 'Onlar', 'They', 'Ellos', 'Sie', 'Ils', 'Loro', '彼ら', '그들', 'Eles', 'वे'),
    '這': ('zhè', 'ㄓㄜˋ', 'Bu', 'This', 'Esto', 'Dies', 'Ceci', 'Questo', 'これ', '이것', 'Isto', 'यह'),
    '那': ('nà', 'ㄋㄚˋ', 'Şu / O', 'That', 'Eso', 'Das', 'Cela', 'Quello', 'あれ', '저것', 'Aquilo', 'वह'),
    '的': ('de', '˙ㄉㄜ', '-in / -ın (aitlik)', 'of / \'s', 'de', 'von', 'de', 'di', 'の', '의', 'de', 'का/की'),
    '了': ('le', '˙ㄌㄜ', '-dı / oldu (tamamlanma eki)', 'completed action marker', 'marcador de acción', 'vollendet', 'marqueur accompli', 'marcatore', '〜た', '~했다', 'marcador', 'गया'),
    '在': ('zài', 'ㄗㄞˋ', '-de / -da (bulunma)', 'at / in', 'en', 'in / bei', 'à / dans', 'in', '〜で', '~에서', 'em', 'में'),
    '要': ('yào', 'ㄧㄠˋ', 'İstemek / -ecek', 'to want / will', 'querer / ir a', 'wollen / werden', 'vouloir / aller', 'volere / andare a', '〜が欲しい / 〜する', '~원하다', 'querer', 'चाहना'),
    '想': ('xiǎng', 'ㄒㄧㄤˇ', 'İstemek / düşünmek', 'to want / think', 'desear / pensar', 'möchten / denken', 'penser / vouloir', 'pensare / volere', '〜したい', '~하고 싶다', 'querer', 'चाहना'),
    '有': ('yǒu', 'ㄧㄡˇ', 'Var olmak / Sahip olmak', 'to have / there is', 'tener / haber', 'haben / es gibt', 'avoir / il y a', 'avere / c\'è', 'ある / 持つ', '있다', 'ter / haver', 'होना / पास होना'),
    '沒有': ('méi yǒu', 'ㄇㄟˊ ㄧㄡˇ', 'Yok / Sahip olmamak', 'to not have / there is no', 'no tener / no haber', 'nicht haben / es gibt kein', 'ne pas avoir', 'non avere / non c\'è', 'ない', '없다', 'não ter', 'नहीं होना'),
    '很': ('hěn', 'ㄏㄣˇ', 'Çok', 'very', 'muy', 'sehr', 'très', 'molto', 'とても', '매우', 'muito', 'बहुत'),
    '太': ('tài', 'ㄊㄞˋ', 'Aşırı / Fazla', 'too', 'demasiado', 'zu', 'trop', 'troppo', 'あまりに', '너무', 'demais', 'अत्यधिक'),
    '嗎': ('ma', '˙ㄇㄚ', 'mı? / mi? (soru eki)', 'question particle', 'partícula interrogativa', 'Fragepartikel', 'particule interrogative', 'particella interrogativa', '〜ですか', '~입니까', 'partícula interrogativa', 'क्या'),
    '吧': ('ba', '˙ㄅㄚ', '-elim / hadi (öneri eki)', 'suggestion particle', 'partícula de sugerencia', 'Vorschlagspartikel', 'particule de suggestion', 'particella di esortazione', '〜しましょう', '~하자', 'partícula de sugestão', 'चलो'),
    '呢': ('ne', '˙ㄋㄜ', 'ya ...? (karşı soru eki)', 'follow-up question particle', 'partícula de seguimiento', 'Nachfragepartikel', 'particule de relance', 'particella', '〜は？', '~는?', 'e ...?', 'और ...?'),
    '請': ('qǐng', 'ㄑㄧㄥˇ', 'Lütfen', 'please', 'por favor', 'bitte', 's\'il vous plaît', 'per favore', 'どうぞ / お願いします', '부탁합니다', 'por favor', 'कृपया'),
    '請問': ('qǐng wèn', 'ㄑㄧㄥˇ ㄨㄣˋ', 'Afedersiniz, sorabilir miyim?', 'may I ask', '¿podría preguntar?', 'Darf ich fragen', 'Puis-je demander', 'Posso chiedere', 'お尋ねしますが', '말씀 좀 묻겠습니다', 'Posso perguntar', 'क्या मैं पूछ सकता हूँ'),
    '不好意思': ('bù hǎo yì si', 'ㄅㄨˋ ㄏㄠˇ ㄧˋ ㄙ˙', 'Affedersiniz', 'excuse me', 'disculpe', 'Entschuldigung', 'excusez-moi', 'scusi', 'すみません', '실례합니다', 'com licença', 'क्षमा करें'),
    '謝謝': ('xiè xie', 'ㄒㄧㄝˋ ˙ㄒㄧㄝ', 'Teşekkürler', 'thank you', 'gracias', 'danke', 'merci', 'grazie', 'ありがとう', '감사합니다', 'obrigado', 'धन्यवाद'),
    '不客氣': ('bú kè qi', 'ㄅㄨˊ ㄎㄜˋ ˙ㄑㄧ', 'Rica ederim', 'you are welcome', 'de nada', 'gern geschehen', 'de rien', 'prego', 'どういたしまして', '천만에요', 'de nada', 'स्वागत है'),
    '可以': ('kě yǐ', 'ㄎㄜˇ ㄧˇ', 'Olabilir / -ebilmek', 'can / may', 'poder', 'können / dürfen', 'pouvoir', 'potere', '〜できる', '~할 수 있다', 'poder', 'सकना'),
    '不行': ('bù xíng', 'ㄅㄨˋ ㄒㄧㄥˊ', 'Olmaz', 'not allowed / won\'t do', 'no se puede', 'geht nicht', 'pas possible', 'non va bene', 'ダメです', '안 돼요', 'não pode', 'नहीं चलेगा'),
    '一起': ('yì qǐ', 'ㄧˋ ㄑㄧˇ', 'Birlikte', 'together', 'juntos', 'zusammen', 'ensemble', 'insieme', '一緒に', '함께', 'juntos', 'साथ में'),
    '今天': ('jīn tiān', 'ㄐㄧㄣ ㄊㄧㄢ', 'Bugün', 'today', 'hoy', 'heute', 'aujourd\'hui', 'oggi', '今日', '오늘', 'hoje', 'आज'),
    '明天': ('míng tiān', 'ㄇㄧㄥˊ ㄊㄧㄢ', 'Yarın', 'tomorrow', 'mañana', 'morgen', 'demain', 'domani', '明日', '내일', 'amanhã', 'कल'),
    '昨天': ('zuó tiān', 'ㄗㄨㄛˊ ㄊㄧㄢ', 'Dün', 'yesterday', 'ayer', 'gestern', 'hier', 'ieri', '昨日', '어제', 'ontem', 'कल (बीता)'),
    '現在': ('xiàn zài', 'ㄒㄧㄢˋ ㄗㄞˋ', 'Şimdi', 'now', 'ahora', 'jetzt', 'maintenant', 'adesso', '今', '지금', 'agora', 'अब'),
    '這裡': ('zhè lǐ', 'ㄓㄜˋ ㄌㄧˇ', 'Burası / Burada', 'here', 'aquí', 'hier', 'ici', 'qui', 'ここ', '여기', 'aqui', 'यहाँ'),
    '那裡': ('nà lǐ', 'ㄋㄚˋ ㄌㄧˇ', 'Orası / Orada', 'there', 'allí', 'dort', 'là-bas', 'lì', 'あそこ', '저기', 'lá', 'वहाँ'),
    '哪裡': ('nǎ lǐ', 'ㄋㄚˇ ㄌㄧˇ', 'Neresi? / Nerede?', 'where', 'dónde', 'wo', 'où', 'dove', 'どこ', '어디', 'onde', 'कहाँ'),
    '多少': ('duō shǎo', 'ㄉㄨㄛ ㄕㄠˇ', 'Ne kadar?', 'how much / how many', 'cuánto', 'wie viel', 'combien', 'quanto', 'いくら / どのくらい', '얼마', 'quanto', 'कितना'),
    '什麼': ('shén me', 'ㄕㄣˊ ˙ㄇㄜ', 'Ne?', 'what', 'qué', 'was', 'quoi', 'cosa', '何', '무엇', 'o que', 'क्या'),
    '怎麼': ('zěn me', 'ㄗㄣˇ ˙ㄇㄜ', 'Nasıl?', 'how', 'cómo', 'wie', 'comment', 'come', 'どうやって', '어떻게', 'como', 'कैसे'),
    '為什麼': ('wèi shén me', 'ㄨㄟˋ ㄕㄣˊ ˙ㄇㄜ', 'Neden?', 'why', 'por qué', 'warum', 'pourquoi', 'perché', 'なぜ', '왜', 'por que', 'क्यों'),
    '一個': ('yí ge', 'ㄧˊ ˙ㄍㄜ', 'Bir adet', 'one (piece)', 'un / una', 'ein (Stück)', 'un (morceau)', 'uno', '一つ', '하나', 'um', 'एक'),
    '一杯': ('yì bēi', 'ㄧˋ ㄅㄟ', 'Bir bardak', 'one cup', 'un vaso / taza', 'eine Tasse/Glas', 'un verre/tasse', 'un bicchiere/tazza', '一杯', '한 잔', 'um copo', 'एक कप'),
    '一份': ('yí fèn', 'ㄧˊ ㄈㄣˋ', 'Bir porsiyon', 'one portion', 'una porción', 'eine Portion', 'une portion', 'una porzione', '一人前', '한 인분', 'uma porção', 'एक हिस्सा'),
    '一碗': ('yì wǎn', 'ㄧˋ ㄨㄢˇ', 'Bir kase', 'one bowl', 'un tazón', 'eine Schüssel', 'un bol', 'una ciotola', '一杯（お椀）', '한 그릇', 'uma tigela', 'एक कटोरी')
}

for w, row in COMMON_WORDS.items():
    if w not in VOCAB:
        VOCAB[w] = {
            'hanzi': w,
            'pinyin': row[0],
            'zhuyin': row[1],
            'tr': row[2],
            'en': row[3],
            'translations': {
                'tr': row[2], 'en': row[3], 'es': row[4], 'de': row[5],
                'fr': row[6], 'it': row[7], 'ja': row[8], 'ko': row[9],
                'pt': row[10], 'hi': row[11]
            },
            'es': row[4], 'de': row[5], 'fr': row[6], 'it': row[7],
            'ja': row[8], 'ko': row[9], 'pt': row[10], 'hi': row[11]
        }

def make_token(token_hanzi, custom_info=None):
    if token_hanzi in ('，', '。', '！', '？', '、', '；', '：', '「', '」'):
        return {'hanzi': token_hanzi, 'is_punct': True}
    
    if custom_info:
        info = custom_info
    elif token_hanzi in VOCAB:
        info = VOCAB[token_hanzi]
    else:
        # Fallback empty
        info = {
            'hanzi': token_hanzi,
            'pinyin': '',
            'zhuyin': '',
            'tr': token_hanzi,
            'en': token_hanzi,
            'translations': {'tr': token_hanzi, 'en': token_hanzi}
        }
        
    res = {
        'hanzi': info['hanzi'],
        'pinyin': info.get('pinyin', ''),
        'zhuyin': info.get('zhuyin', ''),
        'tr': info.get('tr', ''),
        'en': info.get('en', ''),
        'translations': info.get('translations', {})
    }
    for lang in ['es', 'de', 'fr', 'it', 'ja', 'ko', 'pt', 'hi']:
        if lang in info:
            res[lang] = info[lang]
        elif lang in info.get('translations', {}):
            res[lang] = info['translations'][lang]
    return res

def build_sentence_item(sid, level_id, difficulty, order, day_label,
                        hanzi, pinyin, zhuyin,
                        tr_full, en_full, es_full, de_full, fr_full, it_full, ja_full, ko_full, pt_full, hi_full,
                        grammar_tip, token_specs):
    tokens = []
    for item in token_specs:
        if isinstance(item, str):
            tokens.append(make_token(item))
        elif isinstance(item, tuple):
            # (hanzi, pinyin, zhuyin, tr, en, es, de, fr, it, ja, ko, pt, hi)
            h = item[0]
            c_info = {
                'hanzi': h,
                'pinyin': item[1],
                'zhuyin': item[2],
                'tr': item[3],
                'en': item[4],
                'translations': {
                    'tr': item[3], 'en': item[4], 'es': item[5], 'de': item[6],
                    'fr': item[7], 'it': item[8], 'ja': item[9], 'ko': item[10],
                    'pt': item[11], 'hi': item[12]
                },
                'es': item[5], 'de': item[6], 'fr': item[7], 'it': item[8],
                'ja': item[9], 'ko': item[10], 'pt': item[11], 'hi': item[12]
            }
            tokens.append(make_token(h, c_info))
            
    res = {
        'id': sid,
        'level_id': level_id,
        'difficulty': difficulty,
        'difficulty_order': order,
        'day_label': day_label,
        'hanzi': hanzi,
        'pinyin': pinyin,
        'zhuyin': zhuyin,
        'tr_full': tr_full,
        'en_full': en_full,
        'grammar_tip': grammar_tip,
        'tokens': tokens,
        'translations': {
            'tr': tr_full, 'en': en_full, 'es': es_full, 'de': de_full,
            'fr': fr_full, 'it': it_full, 'ja': ja_full, 'ko': ko_full,
            'pt': pt_full, 'hi': hi_full
        },
        'es_full': es_full,
        'de_full': de_full,
        'fr_full': fr_full,
        'it_full': it_full,
        'ja_full': ja_full,
        'ko_full': ko_full,
        'pt_full': pt_full,
        'hi_full': hi_full
    }
    return res

print("sentence_helpers.py ready!")
