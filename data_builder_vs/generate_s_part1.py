import json
import re

# Load base dictionaries
with open('/Users/tarikozluk/Desktop/Dictionary-IAC/words/words.json') as f:
    words_db = json.load(f)
with open('/Users/tarikozluk/Desktop/Dictionary-IAC/verbs/verbs.json') as f:
    verbs_db = json.load(f)

vocab_lookup = {}
for w in words_db:
    vocab_lookup[w['hanzi']] = w
for v in verbs_db:
    if v['hanzi'] not in vocab_lookup:
        vocab_lookup[v['hanzi']] = v

# Define the 100 sentences for Part 1 (IDs: s_tw_001 to s_tw_100)
# Format of each tuple:
# (id, level_id, difficulty, order, day_label, hanzi, pinyin, zhuyin, tr_full, en_full, es_full, de_full, fr_full, it_full, ja_full, ko_full, pt_full, hi_full, grammar_tip, token_raw_list)

raw_sentences = [
    # 1
    ("s_tw_001", 1, "Easy", 1, "Day 1",
     "我要一杯珍珠奶茶，微糖微冰。",
     "Wǒ yào yì bēi zhēn zhū nǎi chá, wéi táng wéi bīng.",
     "ㄨㄛˇ ㄧㄠˋ ㄧˋ ㄅㄟ ㄓㄣ ㄓㄨ ㄋㄞˇ ㄔㄚˊ，ㄨㄟˊ ㄊㄤˊ ㄨㄟˊ ㄅㄧㄥ。",
     "Ben bir bardak boba çayı istiyorum, az şekerli ve az buzlu.",
     "I want a cup of pearl milk tea, low sugar and light ice.",
     "Quiero un té con leche y perlas, poco azúcar y poco hielo.",
     "Ich möchte einen Milchtee mit Perlen, wenig Zucker und wenig Eis.",
     "Je voudrais un thé au lait aux perles, peu sucré et peu de glaçons.",
     "Vorrei un bubble tea, poco zucchero e poco ghiaccio.",
     "タピオカミルクティーを一杯、微糖微氷でお願いします。",
     "버블티 한 잔 주세요, 덜 달게 얼음 적게요.",
     "Eu quero um bubble tea, com pouco açúcar e pouco gelo.",
     "मुझे एक कप बबल टी चाहिए, कम चीनी और कम बर्फ के साथ।",
     "In Taiwanese beverage shops, customizing sweetness (微糖 wéi táng = 30%) and ice level (微冰 wéi bīng) is universal and expected.",
     ["我", "要", "一杯", "珍珠奶茶", "，", "微糖", "微冰", "。"]),

    # 2
    ("s_tw_002", 1, "Easy", 2, "Day 2",
     "老闆，請問這個小吃可以外帶嗎？",
     "Lǎo bǎn, qǐng wèn zhè ge xiǎo chī kě yǐ wài dài ma?",
     "ㄌㄠˇ ㄅㄢˇ，ㄑㄧㄥˇ ㄨㄣˋ ㄓㄜˋ ˙ㄍㄜ ㄒㄧㄠˇ ㄔ ㄎㄜˇ ㄧˇ ㄨㄞˋ ㄉㄞˋ ˙ㄇㄚ？",
     "Patron, afedersiniz bu atıştırmalık paket yaptırılabilir mi?",
     "Boss, excuse me, can this snack be ordered for takeout?",
     "Jefe, disculpe, ¿este tentempié se puede pedir para llevar?",
     "Chef, Verzeihung, kann man diesen Snack zum Mitnehmen bestellen?",
     "Patron, excusez-moi, ce snack peut-il être commandé à emporter ?",
     "Capo, scusi, questo snack si può avere da asporto?",
     "店主さん、すみません、この軽食はテイクアウトできますか？",
     "사장님, 실례지만 이 간식 포장 되나요?",
     "Chefe, com licença, este lanche pode ser para viagem?",
     "मालिक, सुनिए, क्या यह स्नैक पैक कराया जा सकता है?",
     "Addressing shopkeepers as 老闆 (lǎo bǎn) is standard polite street etiquette in Taiwan. 外帶 (wài dài) means takeout.",
     ["老闆", "，", "請問", "這個", "小吃", "可以", "外帶", "嗎", "？"]),

    # 3
    ("s_tw_003", 1, "Easy", 3, "Day 3",
     "這碗牛肉麵加湯不用錢，味道非常香。",
     "Zhè wǎn niú ròu miàn jiā tāng bú yòng qián, wèi dào fēi cháng xiāng.",
     "ㄓㄜˋ ㄨㄢˇ ㄋㄧㄡˊ ㄖㄡˋ ㄇㄧㄢˋ ㄐㄧㄚ ㄊㄤ ㄅㄨˊ ㄩㄥˋ ㄑㄧㄢˊ，ㄨㄟˋ ㄉㄠˋ ㄈㄟ ㄔㄤˊ ㄒㄧㄤ。",
     "Bu kase dana erişteli çorbaya çorba ekletmek ücretsizdir, kokusu çok lezzetlidir.",
     "Adding soup to this bowl of beef noodles is free, and the taste is very aromatic.",
     "Añadir caldo a este tazón de fideos con carne es gratis, y sabe muy sabroso.",
     "Mehr Suppe zu dieser Schüssel Rindfleischnudeln ist kostenlos und sehr aromatisch.",
     "Ajouter du bouillon à ce bol de nouilles au bœuf est gratuit, et le goût est très savoureux.",
     "Aggiungere brodo a questa ciotola di tagliolini di manzo è gratis, ed è profumatissimo.",
     "この牛肉麺はスープのおかわりが無料で、とても香ばしいです。",
     "이 우육면은 국물 리필이 무료이고, 풍미가 아주 좋습니다.",
     "Adicionar caldo a esta tigela de macarrão com carne é grátis e o aroma é incrível.",
     "इस बीफ नूडल्स के कटोरे में सूप दोबारा डलवाना मुफ्त है, और स्वाद बहुत सुगंधित है।",
     "Traditional Taiwanese beef noodle restaurants often offer free soup broth refills (加湯 jiā tāng) and house-made mustard greens (酸菜).",
     ["這", "一碗", "牛肉麵", "加湯", "不用錢", "，", "味道", "非常", "香", "。"]),

    # 4
    ("s_tw_004", 1, "Easy", 4, "Day 4",
     "我們今天晚上一起去士林夜市逛街吃小吃吧！",
     "Wǒ men jīn tiān wǎn shang yì qǐ qù shì lín yè shì guàng jiē chī xiǎo chī ba!",
     "ㄨㄛˇ ㄇㄣ˙ ㄐㄧㄣ ㄊㄧㄢ ㄨㄢˇ ㄕㄤ˙ ㄧˋ ㄑㄧˇ ㄑㄩˋ ㄕˋ ㄌㄧㄣˊ ㄧㄝˋ ㄕˋ ㄍㄨㄤˋ ㄐㄧㄝ ㄔ ㄒㄧㄠˇ ㄔ ˙ㄅㄚ！",
     "Biz bu akşam birlikte Shilin Gece Pazarı'na gidip gezelim ve sokak lezzetleri yiyelim!",
     "Let's go to Shilin Night Market together tonight to stroll and eat street food!",
     "¡Vamos juntos al mercado nocturno de Shilin esta noche a pasear y comer antojitos!",
     "Lass uns heute Abend zusammen zum Shilin-Nachtmarkt gehen, bummeln und Streetfood essen!",
     "Allons ensemble au marché de nuit de Shilin ce soir pour nous promener et manger de la street food !",
     "Andiamo insieme al mercato notturno di Shilin stasera a passeggiare e mangiare street food!",
     "今夜一緒に士林夜市へ行って散策しながら屋台グルメを食べよう！",
     "오늘 밤 우리 다 같이 스린 야시장에 가서 구경하고 길거리 음식 먹자!",
     "Vamos juntos ao mercado noturno de Shilin hoje à noite passear e comer petiscos!",
     "चलो आज रात हम सब मिलकर शिलिन नाइट मार्केट घूमें और स्ट्रीट फूड खाएं!",
     "逛街 (guàng jiē) combined with 夜市 (yè shì) is the hallmark of Taiwanese evening social culture.",
     ["我們", "今天", "晚上", "一起", "去", "士林夜市", "逛街", "吃", "小吃", "吧", "！"]),

    # 5
    ("s_tw_005", 1, "Easy", 5, "Day 5",
     "這份臭豆腐炸得很酥脆，配泡菜超好吃。",
     "Zhè fèn chòu dòu fu zhà de hěn sū cuì, pèi pào cài chāo hǎo chī.",
     "ㄓㄜˋ ㄈㄣˋ ㄔㄡˋ ㄉㄡˋ ㄈㄨ˙ ㄓㄚˋ ˙ㄉㄜ ㄏㄣˇ ㄙㄨ ㄘㄨㄟˋ，ㄆㄟˋ ㄆㄠˋ ㄘㄞˋ ㄔㄠ ㄏㄠˇ ㄔ。",
     "Bu porsiyon kokuşmuş tofu çok çıtır kızartılmış, turşuyla birlikte aşırı lezzetli.",
     "This portion of stinky tofu is fried crispy, and pairing it with Taiwanese kimchi is super delicious.",
     "Esta porción de tofu apestoso está muy crujiente, y acompañada de kimchi taiwanés está riquísima.",
     "Dieser Stinkende Tofu ist knusprig frittiert und mit eingelegtem Kohl super lecker.",
     "Cette portion de tofu puant est très croustillante, et avec le chou mariné c'est super bon.",
     "Questa porzione di stinky tofu è fritta ben croccante, con i crauti taiwanesi è buonissima.",
     "この臭豆腐はサクサクに揚がっていて、台湾風キムチと一緒に食べると超美味しいです。",
     "이 취두부는 바삭하게 튀겨져서 양배추 김치와 곁들여 먹으면 정말 맛있어요.",
     "Esta porção de tofu fedorento é frita bem crocante, e com conserva taiwanesa fica super gostosa.",
     "यह स्टिंकी टोफू बहुत कुरकुरा तला हुआ है, और ताइवानी किमची के साथ बहुत स्वादिष्ट लगता है।",
     "Taiwanese deep-fried stinky tofu is always accompanied by pickled sweet-and-sour cabbage (泡菜 pào cài) to balance rich flavors.",
     ["這", "一份", "臭豆腐", "炸", "的", "很", "酥脆", "，", "配", "泡菜", "超", "好吃", "。"]),

    # 6
    ("s_tw_006", 1, "Easy", 6, "Day 6",
     "請問小籠包一籠有幾顆？我們想點兩籠。",
     "Qǐng wèn xiǎo lóng bāo yì lóng yǒu jǐ kē? Wǒ men xiǎng diǎn liǎng lóng.",
     "ㄑㄧㄥˇ ㄨㄣˋ ㄒㄧㄠˇ ㄌㄨㄥˊ ㄅㄠ ㄧˋ ㄌㄨㄥˊ ㄧㄡˇ ㄐㄧˇ ㄎㄜ? ㄨㄛˇ ㄇㄣ˙ ㄒㄧㄤˇ ㄉㄧㄢˇ ㄌㄧㄤˇ ㄌㄨㄥˊ。",
     "Afedersiniz, bir sepette kaç adet xiaolongbao var? Biz iki sepet sipariş vermek istiyoruz.",
     "Excuse me, how many xiaolongbao are in one steamer? We want to order two steamers.",
     "Disculpe, ¿cuántos xiaolongbao vienen en una vaporera? Queremos pedir dos vaporeras.",
     "Entschuldigung, wie viele Xiaolongbao sind in einem Dämpfkorb? Wir möchten zwei Körbe bestellen.",
     "Excusez-moi, combien de xiaolongbao y a-t-il dans un panier vapeur ? Nous voulons en commander deux.",
     "Scusi, quanti xiaolongbao ci sono in un cestello a vapore? Vorremmo ordinarne due.",
     "すみません、小籠包は一セイロに何個入っていますか？二セイロ注文したいです。",
     "실례지만 소롱포 한 판에 몇 개 나와요? 두 판 주문하고 싶어요.",
     "Com licença, quantos xiaolongbao vêm em um cesto de vapor? Queremos pedir dois cestos.",
     "सुनिए, एक स्टीमर बास्केट में कितने शियाओलोंगबाओ होते हैं? हम दो बास्केट ऑर्डर करना चाहते हैं।",
     "Steamer baskets of dumplings in Taiwan are measured using the classifier 籠 (lóng).",
     ["請問", "小籠包", "一籠", "有", "幾顆", "？", "我們", "想", "點", "兩籠", "。"]),

    # 7
    ("s_tw_007", 1, "Easy", 7, "Day 7",
     "早餐我想吃一份原味蛋餅配熱豆漿。",
     "Zǎo cān wǒ xiǎng chī yí fèn yuán wèi dàn bǐng pèi rè dòu jiāng.",
     "ㄗㄠˇ ㄘㄢ ㄨㄛˇ ㄒㄧㄤˇ ㄔ ㄧˊ ㄈㄣˋ ㄩㄢˊ ㄨㄟˋ ㄉㄢˋ ㄅㄧㄥˇ ㄆㄟˋ ㄖㄜˋ ㄉㄡˋ ㄐㄧㄤ。",
     "Kahvaltıda bir porsiyon sade yumurtalı krep ve yanında sıcak soya sütü içmek istiyorum.",
     "For breakfast, I want an original egg crepe paired with hot soy milk.",
     "Para desayunar quiero un crepe de huevo tradicional con leche de soya caliente.",
     "Zum Frühstück möchte ich einen traditionellen Eierpfannkuchen mit heißer Sojamilch.",
     "Pour le petit déjeuner, je veux une crêpe aux œufs nature accompagnée de lait de soja chaud.",
     "Per colazione vorrei una crepe all'uovo tradizionale con latte di soia caldo.",
     "朝食にはプレーン蛋餅と温かい豆乳を一緒に食べたいです。",
     "아침으로 오리지널 딴빙 하나와 따뜻한 두유를 곁들여 먹고 싶어요.",
     "No café da manhã quero uma panqueca de ovo tradicional com leite de soja quente.",
     "नाश्ते में मुझे पारंपरिक अंडा पैनकेक और गरम सोया दूध चाहिए।",
     "Taiwanese breakfast shops (美而美, 永和豆漿) are legendary for freshly griddled 蛋餅 (dàn bǐng) and rich 豆漿 (dòu jiāng).",
     ["早餐", "我", "想", "吃", "一份", "原味", "蛋餅", "配", "熱豆漿", "。"]),

    # 8
    ("s_tw_008", 1, "Easy", 8, "Day 8",
     "台灣的芒果冰分量很大，兩個人吃剛剛好。",
     "Tái wān de máng guǒ bīng fèn liàng hěn dà, liǎng ge rén chī gāng gāng hǎo.",
     "ㄊㄞˊ ㄨㄢ ˙ㄉㄜ ㄇㄤˊ ㄍㄨㄛˇ ㄅㄧㄥ ㄈㄣˋ ㄌㄧㄤˋ ㄏㄣˇ ㄉㄚˋ，ㄌㄧㄤˇ ˙ㄍㄜ ㄖㄣˊ ㄔ ㄍㄤ ㄍㄤ ㄏㄠˇ。",
     "Tayvan'ın mangolu traşlanmış buzu çok porsiyonludur, iki kişinin yemesi tam uygundur.",
     "Taiwanese mango shaved ice has generous portions, just right for two people to share.",
     "El hielo raspado de mango en Taiwán viene en porciones grandes, ideal para compartir entre dos.",
     "Taiwans Mango-Raspeleis hat riesige Portionen, genau richtig für zwei Personen.",
     "La glace pilée à la mangue de Taïwan est très copieuse, juste parfait pour deux personnes.",
     "La granita al mango taiwanese ha porzioni abbondanti, perfetta da condividere in due.",
     "台湾のマンゴーかき氷はボリューム満点で、二人でシェアしてちょうど良いです。",
     "대만의 망고 빙수는 양이 아주 많아서 두 사람이 나눠 먹기에 딱 좋습니다.",
     "A raspadinha de manga de Taiwan tem porções fartas, perfeita para duas pessoas dividirem.",
     "ताइवान की मैंगो शेव्ड आइस का हिस्सा बहुत बड़ा होता है, दो लोगों के साझा करने के लिए बिल्कुल सही।",
     "剛剛好 (gāng gāng hǎo) means 'just right'. Taiwanese shaved ice (雪花冰 or 刨冰) is heaped with fresh seasonal fruit and condensed milk.",
     ["台灣", "的", "芒果冰", "分量", "很", "大", "，", "兩個人", "吃", "剛剛好", "。"]),

    # 9
    ("s_tw_009", 1, "Easy", 9, "Day 9",
     "請幫我外帶兩份滷肉飯加一顆滷蛋。",
     "Qǐng bāng wǒ wài dài liǎng fèn lǔ ròu fàn jiā yì kē lǔ dàn.",
     "ㄑㄧㄥˇ ㄅㄤ ㄨㄛˇ ㄨㄞˋ ㄉㄞˋ ㄌㄧㄤˇ ㄈㄣˋ ㄌㄨˇ ㄖㄡˋ ㄈㄢˋ ㄐㄧㄚ ㄧˋ ㄎㄜ ㄌㄨˇ ㄉㄢˋ。",
     "Lütfen bana iki porsiyon braised pork rice ve bir adet haşlanmış marine yumurta paket yapınız.",
     "Please pack two orders of braised pork rice with a braised egg for takeout.",
     "Por favor, prepárame para llevar dos platos de arroz con cerdo estofado y un huevo marinado.",
     "Bitte packen Sie mir zwei Portionen geschmortes Schweinefleisch auf Reis mit einem marinierten Ei zum Mitnehmen ein.",
     "S'il vous plaît, emballez à emporter deux bols de riz au porc braisé avec un œuf mariné.",
     "Per favore, mi prepari da asporto due porzioni di riso con maiale stufato e un uovo marinato.",
     "ルーロー飯を二人前と煮卵を一つテイクアウトでお願いします。",
     "루로우판 두 그릇과 조림 달걀 하나 포장해 주세요.",
     "Por favor, embale para viagem duas porções de arroz com porco refogado e um ovo marinado.",
     "कृपया दो ब्रेज़्ड पोर्क राइस और एक ब्रेज़्ड अंडा पैक कर दीजिए।",
     "滷肉飯 (lǔ ròu fàn) is Taiwan's undisputed national comfort dish, frequently ordered with a braised egg (滷蛋) and tofu (油豆腐).",
     ["請", "幫", "我", "外帶", "兩份", "滷肉飯", "加", "一顆", "滷蛋", "。"]),

    # 10
    ("s_tw_010", 1, "Easy", 10, "Day 10",
     "這家鹽酥雞要加辣、加九層塔嗎？",
     "Zhè jiā yán sū jī yào jiā là, jiā jiǔ céng tǎ ma?",
     "ㄓㄜˋ ㄐㄧㄚ ㄧㄢˊ ㄙㄨ ㄐㄧ ㄧㄠˋ ㄐㄧㄚ ㄌㄚˋ，ㄐㄧㄚ ㄐㄧㄡˇ ㄘㄥˊ ㄊㄚˇ ˙ㄇㄚ？",
     "Bu tuzlu biberli tavukçuya acı ve Tayvan fesleğeni ekletelim mi?",
     "For this Taiwanese fried chicken, do you want spicy powder and Taiwanese basil?",
     "En este pollo frito taiwanés, ¿quieres que le pongan picante y albahaca taiwanesa?",
     "Möchtest du für dieses taiwanesische Brathähnchen Schärfe und thailändisches Basilikum?",
     "Pour ce poulet frit taïwanais, veux-tu ajouter du piment et du basilic taïwanais ?",
     "Per questo pollo fritto taiwanese, vuoi aggiungere piccante e basilico taiwanese?",
     "この台湾風唐揚げは辛味とバジルを追加しますか？",
     "이 대만식 닭튀김에 매운 가루와 대만 바질을 넣을까요?",
     "Neste frango frito taiwanês, você quer pimenta e manjericão fresco?",
     "इस ताइवानी फ्राइड चिकन में क्या आप मिर्च और ताइवानी तुलसी डलवाना चाहते हैं?",
     "At Taiwanese 鹽酥雞 (yán sū jī) stands, deep-fried fresh basil (九層塔 jiǔ céng tǎ) and pepper salt (胡椒鹽) give the signature aroma.",
     ["這家", "鹽酥雞", "要", "加辣", "，", "加", "九層塔", "嗎", "？"]),

    # 11
    ("s_tw_011", 1, "Easy", 11, "Day 11",
     "不好意思，請問你們有素食的菜單嗎？",
     "Bù hǎo yì si, qǐng wèn nǐ men yǒu sù shí de cài dān ma?",
     "ㄅㄨˋ ㄏㄠˇ ㄧˋ ㄙ˙，ㄑㄧㄥˇ ㄨㄣˋ ㄋㄧˇ ㄇㄣ˙ ㄧㄡˇ ㄙㄨˋ ㄕˊ ˙ㄉㄜ ㄘㄞˋ ㄉㄢ ˙ㄇㄚ？",
     "Affedersiniz, acaba vejetaryen menünüz var mı?",
     "Excuse me, do you have a vegetarian menu?",
     "Disculpe, ¿tienen un menú vegetariano?",
     "Entschuldigung, haben Sie eine vegetarische Speisekarte?",
     "Excusez-moi, avez-vous un menu végétarien ?",
     "Mi scusi, avete un menù vegetariano?",
     "すみません、ベジタリアン向けのメニューはありますか？",
     "실례지만 채식 메뉴가 따로 있나요?",
     "Com licença, vocês têm um cardápio vegetariano?",
     "माफ़ कीजिए, क्या आपके पास शाकाहारी मेनू है?",
     "Taiwan is one of the most vegetarian-friendly places in the world. Look for 素食 (sù shí) or the Buddhist swastika sign (卍).",
     ["不好意思", "，", "請問", "你們", "有", "素食", "的", "菜單", "嗎", "？"]),

    # 12
    ("s_tw_012", 2, "Easy", 12, "Day 12",
     "這家熱炒店的菜色很多，而且白飯免費吃到飽。",
     "Zhè jiā rè chǎo diàn de cài sè hěn duō, ér qiě bái fàn miǎn fèi chī dào bǎo.",
     "ㄓㄜˋ ㄐㄧㄚ ㄖㄜˋ ㄔㄠˇ ㄉㄧㄢˋ ˙ㄉㄜ ㄘㄞˋ ㄙㄜˋ ㄏㄣˇ ㄉㄨㄛ，ㄦˊ ㄑㄧㄝˇ ㄅㄞˊ ㄈㄢˋ ㄇㄧㄢˇ ㄈㄟˋ ㄔ ㄉㄠˋ ㄅㄠˇ。",
     "Bu sıcak tava lokantasında yemek çeşidi çoktur ve üstelik beyaz pirinç pilavı sınırsız ücretsizdir.",
     "This stir-fry diner has numerous dishes, and white rice is free and all-you-can-eat.",
     "Este restaurante de salteados tiene muchos platos y el arroz blanco es gratis e ilimitado.",
     "Dieses Stir-Fry-Lokal bietet viele Gerichte und weißer Reis ist kostenlos zum Sattessen.",
     "Ce restaurant de plats sautés a beaucoup de choix, et le riz blanc est à volonté et gratuit.",
     "Questa taverna taiwanese offre molti piatti e il riso bianco è gratuito a volontà.",
     "この居酒屋（熱炒店）はメニューが豊富で、白ご飯も食べ放題無料です。",
     "이 대만식 포장마차 식당은 메뉴가 다양하고 밥도 무료로 무한리필입니다.",
     "Este restaurante de refogados tem muitos pratos e o arroz branco é grátis à vontade.",
     "इस ताइवानी हलचल-तलने वाले रेस्तरां में बहुत सारे व्यंजन हैं, और सफेद चावल मुफ्त में भरपेट मिलते हैं।",
     "吃到飽 (chī dào bǎo) means 'all-you-can-eat'. Taiwanese 熱炒店 (rè chǎo diàn) are famous for affordable stir-fries and cold Taiwan Beer.",
     ["這家", "熱炒店", "的", "菜色", "很", "多", "，", "而且", "白飯", "免費", "吃到飽", "。"]),

    # 13
    ("s_tw_013", 1, "Easy", 13, "Day 13",
     "請問你們收信用卡還是只能付現金？",
     "Qǐng wèn nǐ men shōu xìn yòng kǎ hái shì zhǐ néng fù xiàn jīn?",
     "ㄑㄧㄥˇ ㄨㄣˋ ㄋㄧˇ ㄇㄣ˙ ㄕㄡ ㄒㄧㄣˋ ㄩㄥˋ ㄎㄚˇ ㄏㄞˊ ㄕˋ ㄓˇ ㄋㄥˊ ㄈㄨˋ ㄒㄧㄢˋ ㄐㄧㄣ？",
     "Afedersiniz, kredi kartı kabul ediyor musunuz yoksa sadece nakit mi?",
     "Excuse me, do you accept credit cards or is it cash only?",
     "Disculpe, ¿aceptan tarjeta de crédito o solo efectivo?",
     "Entschuldigung, nehmen Sie Kreditkarten oder geht nur Barzahlung?",
     "Excusez-moi, acceptez-vous les cartes de crédit ou uniquement les espèces ?",
     "Scusi, accettate carte di credito o solo contanti?",
     "すみません、クレジットカードは使えますか？それとも現金のみですか？",
     "실례지만 신용카드 받으시나요, 아니면 현금만 가능한가요?",
     "Com licença, vocês aceitam cartão de crédito ou apenas dinheiro?",
     "माफ़ कीजिए, क्या आप क्रेडिट कार्ड लेते हैं या केवल नकद?",
     "Many street food stalls in Taiwan only accept cash (現金 xiàn jīn) or Line Pay, while convenience stores and restaurants accept cards and EasyCard (悠遊卡).",
     ["請問", "你們", "收", "信用卡", "還是", "只能", "付", "現金", "？"]),

    # 14
    ("s_tw_014", 1, "Easy", 14, "Day 14",
     "喝冬瓜檸檬去冰半糖最消暑。",
     "Hē dōng guā níng méng qù bīng bàn táng zuì xiāo shǔ.",
     "ㄏㄜ ㄉㄨㄥ ㄍㄨㄚ ㄋㄧㄥˊ ㄇㄥˊ ㄑㄩˋ ㄅㄧㄥ ㄅㄢˋ ㄊㄤˊ ㄗㄨㄟˋ ㄒㄧㄠ ㄕㄨˇ。",
     "Buzsuz ve yarı şekerli kış kavunu limonlu içecek içmek yaz sıcağını en iyi giderendir.",
     "Drinking winter melon lemon tea with no ice and half sugar is the best way to beat the summer heat.",
     "Beber té de melón de invierno con limón sin hielo y medio azúcar es lo mejor para combatir el calor.",
     "Wintermelonen-Zitronentee ohne Eis und halbsüß ist das Beste gegen die Sommerhitze.",
     "Boire du thé de courge cireuse au citron sans glaçon et mi-sucré est idéal pour se rafraîchir en été.",
     "Bere tè di zucca invernale e limone senza ghiaccio e poco zucchero rinfresca tantissimo d'estate.",
     "氷なし・半糖のトウガンレモン茶を飲むのが一番の暑さ対策です。",
     "얼음 빼고 반당으로 한 동과레몬티를 마시면 더위가 싹 가십니다.",
     "Beber chá de melão de inverno com limão sem gelo e meio açúcar é ótimo para refrescar no calor.",
     "बिना बर्फ और आधी चीनी वाली विंटर मेलन लेमन टी पीना गर्मी भगाने का सबसे अच्छा तरीका है।",
     "去冰 (qù bīng) means no ice. 冬瓜檸檬 (dōng guā níng méng) balances sweet caramelized winter melon punch with sour fresh lime.",
     ["喝", "冬瓜檸檬", "去冰", "半糖", "最", "消暑", "。"]),

    # 15
    ("s_tw_015", 1, "Easy", 15, "Day 15",
     "蚵仔煎淋上特製甜辣醬真是絕配！",
     "Ó-á-chian lín shàng tè zhì tián là jiàng zhēn shì jué pèi!",
     "ㄜˊ ㄗˇ ㄐㄧㄢ ㄌㄧㄣˊ ㄕㄤˋ ㄊㄜˋ ㄓˋ ㄊㄧㄢˊ ㄌㄚˋ ㄐㄧㄤˋ ㄓㄣ ㄕˋ ㄐㄩㄝˊ ㄆㄟˋ！",
     "İstiridyeli omletin üzerine özel tatlı-acı sos gezdirmek gerçekten mükemmel bir uyum!",
     "Oyster omelet drizzled with special sweet chili sauce is truly a match made in heaven!",
     "¡La tortilla de ostras bañada con salsa dulce picante es una combinación perfecta!",
     "Austern-Omelett beträufelt mit süß-scharfer Sauce ist einfach die perfekte Kombination!",
     "L'omelette aux huîtres nappée de sauce aigre-douce pimentée est un mariage parfait !",
     "L'omelette di ostriche con sopra la salsa agrodolce piccante è un abbinamento favoloso!",
     "牡蠣オムレツに特製スイートチリソースをかけると本当に絶品です！",
     "굴전(어아젠)에 특제 스위트 칠리소스를 뿌려 먹으면 환상의 궁합입니다!",
     "A omelete de ostras regada com molho agridoce apimentado é uma combinação perfeita!",
     "ऑयस्टर ऑमलेट पर विशेष मीठी-तीखी चटनी डालना सचमुच लाजवाब संगम है!",
     "蚵仔煎 is pronounced 'ó-á-chian' from Taiwanese Hokkien. The pink sweet chili sauce is unique to Taiwan.",
     ["蚵仔煎", "淋上", "特製", "甜辣醬", "真是", "絕配", "！"]),

    # 16
    ("s_tw_016", 1, "Easy", 16, "Day 16",
     "請問內用要先找位子還是先櫃台點餐？",
     "Qǐng wèn nèi yòng yào xiān zhǎo wèi zi hái shì xiān guì tái diǎn cān?",
     "ㄑㄧㄥˇ ㄨㄣˋ ㄋㄟˋ ㄩㄥˋ ㄧㄠˋ ㄒㄧㄢ ㄓㄠˇ ㄨㄟˋ ˙ㄗ ㄏㄞˊ ㄕˋ ㄒㄧㄢ ㄍㄨㄟˋ ㄊㄞˊ ㄉㄧㄢˇ ㄘㄢ？",
     "Afedersiniz, burada yemek için önce masa mı bulmalıyız yoksa önce kasadan sipariş mi vermeliyiz?",
     "Excuse me, for dining in, should we find a table first or order at the counter first?",
     "Disculpe, para comer aquí, ¿buscamos mesa primero o pedimos en el mostrador?",
     "Entschuldigung, suchen wir für den Verzehr hier erst einen Platz oder bestellen wir an der Theke?",
     "Excusez-moi, pour manger sur place, doit-on d'abord trouver une table ou commander au comptoir ?",
     "Scusi, per mangiare qui, dobbiamo prima trovare un tavolo o ordinare alla cassa?",
     "すみません、イートインの場合は先に席を取りますか、それとも先にレジで注文ですか？",
     "실례지만 매장 식사는 먼저 자리를 잡나요, 아니면 카운터에서 먼저 주문하나요?",
     "Com licença, para comer no local devemos procurar uma mesa primeiro ou pedir no balcão?",
     "माफ़ कीजिए, यहाँ खाने के लिए पहले टेबल ढूँढें या काउंटर पर ऑर्डर करें?",
     "內用 (nèi yòng) means dining in. In busy Taiwanese eateries, practice varies: some require finding a seat (找位子) first, others order at the counter (櫃台).",
     ["請問", "內用", "要", "先", "找位子", "還是", "先", "櫃台", "點餐", "？"]),

    # 17
    ("s_tw_017", 2, "Easy", 17, "Day 17",
     "這杯高山烏龍茶茶香濃郁，回甘順口。",
     "Zhè bēi gāo shān wū lóng chá chá xiāng nóng yù, huí gān shùn kǒu.",
     "ㄓㄜˋ ㄅㄟ ㄍㄠ ㄕㄢ ㄨ ㄌㄨㄥˊ ㄔㄚˊ ㄔㄚˊ ㄒㄧㄤ ㄋㄨㄥˊ ㄩˋ，ㄏㄨㄟˊ ㄍㄢ ㄕㄨㄣˋ ㄎㄡˇ。",
     "Bu bardak yüksek rakım Oolong çayının aroması zengin, damakta bıraktığı tatlı tat pürüzsüz ve hoştur.",
     "This cup of high-mountain oolong tea has a rich tea aroma with a smooth, sweet aftertaste.",
     "Esta taza de té oolong de alta montaña tiene un aroma intenso y un regusto dulce muy suave.",
     "Diese Tasse Hochland-Oolong-Tee hat ein reiches Aroma und einen samtigen, süßlichen Nachgeschmack.",
     "Cette tasse de thé oolong de haute montagne a un arôme riche avec un arrière-goût doux et soyeux.",
     "Questa tazza di tè oolong d'alta quota ha un aroma ricco con un retrogusto dolce e morbido.",
     "この高山ウーロン茶は豊かな香りで、まろやかで甘い余韻が楽しめます。",
     "이 고산 우롱차는 찻잎 향이 진하고, 목 넘김이 부드러우며 끝맛이 달콤합니다.",
     "Esta xícara de chá oolong de alta montanha tem aroma rico e um retrogosto adocicado suave.",
     "इस हाई-माउंटेन ऊलोंग चाय का स्वाद बहुत गहरा है और इसका मीठा बाद का स्वाद बहुत सहज है।",
     "回甘 (huí gān) describes the sweet lingering aftertaste prized in traditional Taiwanese high-mountain tea culture (高山茶).",
     ["這", "一杯", "高山烏龍茶", "茶香", "濃郁", "，", "回甘", "順口", "。"]),

    # 18
    ("s_tw_018", 2, "Easy", 18, "Day 18",
     "剛出爐的胡椒餅外皮酥脆，小心咬下去會噴汁。",
     "Gāng chū lú de hú jiāo bǐng wài pí sū cuì, xiǎo xīn yǎo xià qù huì pēn zhī.",
     "ㄍㄤ ㄔㄨ ㄌㄨˊ ˙ㄉㄜ ㄏㄨˊ ㄐㄧㄠ ㄅㄧㄥˇ ㄨㄞˋ ㄆㄧˊ ㄙㄨ ㄘㄨㄟˋ，ㄒㄧㄠˇ ㄒㄧㄣ ㄧㄠˇ ㄒㄧㄚˋ ㄑㄩˋ ㄏㄨㄟˋ ㄆㄣ ㄓ。",
     "Fırından yeni çıkmış karabiberli çöreğin dış kabuğu çıtırdır, ısırırken suyunu püskürtmemesine dikkat edin.",
     "Freshly baked pepper buns have a crispy crust, be careful because juice will squirt out when biting.",
     "Los bollos de pimienta recién horneados son crujientes por fuera, ten cuidado al morder porque salpica jugo caliente.",
     "Frisch gebackene Pfefferbrötchen sind außen knusprig, Vorsicht beim Hineinbeißen, der heiße Saft spritzt leicht heraus.",
     "Les petits pains au poivre tout juste sortis du four sont croustillants, attention en mordant car le jus chaud jaillit.",
     "I panini al pepe appena sfornati sono croccanti fuori, attenzione quando si morde perché schizza succo caldo.",
     "焼き立ての胡椒餅は外側がサクサクで、噛むと肉汁が飛び散るので注意してください。",
     "방금 화덕에서 구워 나온 후추빵은 겉이 바삭하니 한입 베어 물 때 육즙이 튈 수 있어 조심해야 합니다.",
     "Os pãezinhos de pimenta recém-assados são crocantes por fora, cuidado ao morder pois o caldo espirra.",
     "ताज़ी बेक की हुई काली मिर्च की रोटियां बाहर से कुरकुरी होती हैं, काटते समय सावधान रहें क्योंकि गरम रस बाहर छिटक सकता है।",
     "胡椒餅 (hú jiāo bǐng) baked in clay tandoor-style ovens in night markets (like Raohe) are packed with scallions, pork, and rich hot broth.",
     ["剛出爐", "的", "胡椒餅", "外皮", "酥脆", "，", "小心", "咬", "下去", "會", "噴汁", "。"]),

    # 19
    ("s_tw_019", 2, "Easy", 19, "Day 19",
     "我要一份大腸包小腸，加蒜頭和酸菜。",
     "Wǒ yào yí fèn dà cháng bāo xiǎo cháng, jiā suàn tóu hàn suān cài.",
     "ㄨㄛˇ ㄧㄠˋ ㄧˊ ㄈㄣˋ ㄉㄚˋ ㄔㄤˊ ㄅㄠ ㄒㄧㄠˇ ㄔㄤˊ，ㄐㄧㄚ ㄙㄨㄢˋ ㄊㄡˊ ㄏㄢˋ ㄙㄨㄢ ㄘㄞˋ。",
     "Ben bir porsiyon pirinç sosisli sosis sandviç istiyorum, sarımsak ve ekşi lahana turşulu olsun.",
     "I want an order of Taiwanese sausage in sticky rice wrap, with fresh garlic and pickled mustard greens.",
     "Quiero una orden de salchicha taiwanesa envuelta en arroz glutinoso, con ajo y verduras encurtidas.",
     "Ich möchte eine Portion taiwanesische Wurst im Klebreis-Mantel mit Knoblauch und Sauergemüse.",
     "Je voudrais une portion de saucisse taïwanaise dans son wrap de riz gluant, avec de l'ail et des légumes marinés.",
     "Vorrei una porzione di salsiccia taiwanese avvolta nel riso glutinoso, con aglio e verdure sottaceto.",
     "大腸包小腸（もち米ソーセージ包み）を一人前、ニンニクと高菜漬け入りでお願いします。",
     "대창포소창(찹쌀순대 소시지) 하나 주세요, 마늘과 갓절임 넣어주세요.",
     "Quero uma porção de linguiça no arroz glutinoso, com alho e conserva de mostarda.",
     "मुझे स्टिकी राइस में लिपटी ताइवानी सॉसेज चाहिए, लहसुन और खट्टी सरसों के साथ।",
     "大腸包小腸 (dà cháng bāo xiǎo cháng) is Taiwan's 'rice hot dog'—a sweet grilled pork sausage nestled inside a grilled sticky rice sausage.",
     ["我", "要", "一份", "大腸包小腸", "，", "加", "蒜頭", "和", "酸菜", "。"]),

    # 20
    ("s_tw_020", 2, "Easy", 20, "Day 20",
     "天氣冷的時候，吃一鍋熱騰騰的薑母鴨最暖身。",
     "Tiān qì lěng de shí hou, chī yì guō rè téng téng de jiāng mǔ yā zuì nuǎn shēn.",
     "ㄊㄧㄢ ㄑㄧˋ ㄌㄥˇ ˙ㄉㄜ ㄕˊ ㄏㄡ˙，ㄔ ㄧˋ ㄍㄨㄛ ㄖㄜˋ ㄊㄥˊ ㄊㄥˊ ˙ㄉㄜ ㄐㄧㄤ ㄇㄨˇ ㄧㄚ ㄗㄨㄟˋ ㄋㄨㄢˇ ㄕㄣ。",
     "Hava soğuk olduğunda, dumanı tüten bir tencere zencefilli ördek güveci yemek vücudu en güzel ısıtır.",
     "When the weather is cold, eating a steaming pot of ginger duck warms up the body the most.",
     "Cuando hace frío, comer una olla humeante de pato al jengibre reconforta el cuerpo.",
     "Wenn das Wetter kalt ist, wärmt ein dampfender Topf Ingwerente den Körper am besten.",
     "Quand il fait froid, manger une marmite fumante de canard au gingembre réchauffe le corps.",
     "Quando fa freddo, una pentola fumante di anatra allo zenzero riscalda benissimo il corpo.",
     "寒い季節には、アツアツのショウガ鴨鍋を食べるのが一番体が温まります。",
     "날씨가 쌀쌀할 때는 김이 모락모락 나는 생강 오리탕 한 냄비가 몸을 따뜻하게 녹여줍니다.",
     "Quando o tempo esfria, comer uma panela fumegante de pato com gengibre aquece o corpo.",
     "जब ठंड होती है, तो अदरक वाली बत्तख का भाप छोड़ता बर्तन खाना शरीर को सबसे ज़्यादा गर्माहट देता है।",
     "薑母鴨 (jiāng mǔ yā) with rice wine and black sesame oil is Taiwan's premier winter dietary nourishment (冬令進補) tradition.",
     ["天氣", "冷", "的", "時候", "，", "吃", "一鍋", "熱騰騰", "的", "薑母鴨", "最", "暖身", "。"])
]

print(f"Loaded initial {len(raw_sentences)} items. Generating remaining 80 for Part 1...")

# Generate items 21-100 programmatically with high precision
domain_specs = [
    # 21-30 Food & Errands
    ("s_tw_021", 2, "Easy", 21, "Day 21", "麻辣火鍋的鴨血和豆腐可以免費無限續加。", "Málà huǒ guō de yā xiě hàn dòu fu kě yǐ miǎn fèi wú xiàn xù jiā.", "ㄇㄚˊ ㄌㄚˋ ㄏㄨㄛˇ ㄍㄨㄛ ˙ㄉㄜ ㄧㄚ ㄒㄧㄝˇ ㄏㄢˋ ㄉㄡˋ ㄈㄨ˙ ㄎㄜˇ ㄧˇ ㄇㄧㄢˇ ㄈㄟˋ ㄨˊ ㄒㄧㄢˋ ㄒㄩˋ ㄐㄧㄚ。", "Baharatlı acı güveçteki ördek kanı peltesi ve tofu ücretsiz olarak sınırsız yenilenebilir.", "The duck blood jelly and tofu in spicy hotpot can be refilled infinitely for free.", "La gelatina de sangre de pato y el tofu del hotpot picante se pueden rellenar gratis de forma ilimitada.", "Das Entenblut und der Tofu im scharfen Feuertopf können kostenlos unbegrenzt nachgefüllt werden.", "Le sang de canard gélifié et le tofu de la fondue sichuanaise se rechargent gratuitement et à volonté.", "Il sangue d'anatra rappreso e il tofu nell'hotpot piccante si possono ricaricare gratis e illimitatamente.", "麻辣火鍋の鴨血と豆腐は無料で何回でもおかわり自由です。", "마라 훠궈의 오리 선지와 두부는 무료로 무제한 리필이 가능합니다.", "O sangue de pato e o tofu no hotpot apimentado podem ser repostos de graça e à vontade.", "मसालेदार हॉटपॉट में बत्तख का खून और टोफू असीमित रूप से मुफ्त में दोबारा लिया जा सकता है।", "In Taiwanese-style spicy hotpot (麻辣火鍋), simmering braised duck blood (鴨血) and tofu (豆腐) are standard complimentary free-flow items.", ["麻辣火鍋", "的", "鴨血", "和", "豆腐", "可以", "免費", "無限", "續加", "。"]),
    ("s_tw_022", 2, "Easy", 22, "Day 22", "請問甜不辣吃完後可以加高湯喝嗎？", "Qǐng wèn tián bú là chī wán hòu kě yǐ jiā gāo tāng hē ma?", "ㄑㄧㄥˇ ㄨㄣˋ ㄊㄧㄢˊ ㄅㄨˊ ㄌㄚˋ ㄔ ㄨㄢˊ ㄏㄡˋ ㄎㄜˇ ㄧˇ ㄐㄧㄚ ㄍㄠ ㄊㄤ ㄏㄜ ˙ㄇㄚ？", "Afedersiniz, tianbula balık köftelerini bitirdikten sonra çorba suyu ekletip içebilir miyiz?", "Excuse me, after finishing the tianbula, can I add hot broth to drink?", "Disculpe, después de terminar el tianbula, ¿puedo pedir caldo caliente para beber?", "Entschuldigung, kann man nach dem Verzehr von Tianbula heiße Brühe in die Schüssel nachfüllen lassen?", "Excusez-moi, après avoir fini les beignets de poisson tianbula, peut-on ajouter du bouillon pour boire ?", "Scusi, dopo aver finito il tianbula posso aggiungere brodo caldo da bere?", "すみません、天ぷらを食べ終わった後、スープを足して飲んでもいいですか？", "실례지만 텐부라를 다 먹은 후에 육수를 부어 마셔도 되나요?", "Com licença, depois de comer o tianbula posso pedir para adicionar caldo quente para beber?", "माफ़ कीजिए, क्या तियानबुला खाने के बाद कटोरी में गरम सूप डलवाकर पी सकते हैं?", "Traditional Taiwanese etiquette for 甜不辣 (tempura fishcakes): drink hot kelp broth mixed with leftover sweet sauce in the bowl.", ["請問", "甜不辣", "吃完", "後", "可以", "加", "高湯", "喝", "嗎", "？"]),
    ("s_tw_023", 1, "Easy", 23, "Day 23", "雞排請不要切，這樣才能鎖住肉汁。", "Jī pái qǐng bú yào qiē, zhè yàng cái néng suǒ zhù ròu zhī.", "ㄐㄧ ㄆㄞˊ ㄑㄧㄥˇ ㄅㄨˊ ㄧㄠˋ ㄑㄧㄝ，ㄓㄜˋ ㄧㄤˋ ㄘㄞˊ ㄋㄥˊ ㄙㄨㄛˇ ㄓㄨˋ ㄖㄡˋ ㄓ。", "Tavuk şinitzelini lütfen dilimlemeyin, ancak bu sayede etin suyu içinde kalır.", "Please don't cut the chicken cutlet, so it locks in the juice.", "Por favor no cortes la chuleta de pollo frita, así se retiene todo el jugo.", "Bitte schneiden Sie das Hähnchenschnitzel nicht durch, damit der Fleischsaft erhalten bleibt.", "S'il vous plaît ne coupez pas l'escalope de poulet, afin de préserver tout son jus.", "Per favore non tagli la cotoletta di pollo, così conserva tutto il succo della carne.", "フライドチキンは切らないでください、そうすると肉汁が閉じ込められます。", "지파이는 자르지 말아 주세요, 그래야 육즙을 그대로 가둘 수 있어요.", "Por favor não corte o filé de frango frito, assim mantém todo o caldo da carne.", "कृपया चिकन कटलेट को मत काटिए, ताकि उसका रस अंदर ही सुरक्षित रहे।", "Taiwanese giant fried chicken cutlets (豪大大雞排) taste juiciest when eaten whole without cutting (不切 bù qiē).", ["雞排", "請", "不要", "切", "，", "這樣", "才能", "鎖住", "肉汁", "。"]),
    ("s_tw_024", 1, "Easy", 24, "Day 24", "台灣水果很甜，尤其是愛文芒果和金鑽鳳梨。", "Tái wān shuǐ guǒ hěn tián, yóu qí shì ài wén máng guǒ hàn jīn zuàn fèng lí.", "ㄊㄞˊ ㄨㄢ ㄕㄨㄟˇ ㄍㄨㄛˇ ㄏㄣˇ ㄊㄧㄢˊ，ㄧㄡˊ ㄑㄧˊ ㄕˋ ㄞˋ ㄨㄣˊ ㄇㄤˊ ㄍㄨㄛˇ ㄏㄢˋ ㄐㄧㄣ ㄗㄨㄢˋ ㄈㄥˋ ㄌㄧˊ。", "Tayvan meyveleri çok tatlıdır, bilhassa Irwin mangosu ve Altın Elmas ananası.", "Taiwanese fruits are sweet, especially Irwin mangoes and Golden Diamond pineapples.", "Las frutas de Taiwán son muy dulces, especialmente el mango Irwin y la piña diamante de oro.", "Früchte aus Taiwan sind sehr süß, besonders die Irwin-Mangos und die Golden-Diamond-Ananas.", "Les fruits taïwanais sont très sucrés, en particulier les mangues Irwin et les ananas Golden Diamond.", "La frutta taiwanese è dolcissima, specialmente il mango Irwin e l'ananas diamante d'oro.", "台湾の果物はとても甘く、特に愛文マンゴーと金鑚パイナップルは絶品です。", "대만 과일은 당도가 매우 높은데, 특히 애플망고와 골드 파인애플이 유명합니다.", "As frutas de Taiwan são muito doces, especialmente a manga Irwin e o abacaxi diamante dourado.", "ताइवान के फल बहुत मीठे होते हैं, विशेष रूप से इरविन आम और गोल्डन डायमंड अनानास।", "Taiwan is crowned the 'Fruit Kingdom' (水果王國). Irwin mangoes (愛文芒果) and Golden Diamond pineapples (金鑽鳳梨) are world-famous exports.", ["台灣", "水果", "很", "甜", "，", "尤其是", "愛文芒果", "和", "金鑽鳳梨", "。"]),
    ("s_tw_025", 2, "Easy", 25, "Day 25", "我們在夜市邊走邊吃，體驗道地的台灣夜生活。", "Wǒ men zài yè shì biān zǒu biān chī, tǐ yàn dào dì de tái wān yè shēng huó.", "ㄨㄛˇ ㄇㄣ˙ ㄗㄞˋ ㄧㄝˋ ㄕˋ ㄅㄧㄢ ㄗㄡˇ ㄅㄧㄢ ㄔ，ㄊㄧˇ ㄧㄢˋ ㄉㄠˋ ㄉㄧˋ ˙ㄉㄜ ㄊㄞˊ ㄨㄢ ㄧㄝˋ ㄕㄥ ㄏㄨㄛˊ。", "Biz gece pazarında hem yürüyüp hem yiyerek otantik Tayvan gece hayatını deneyimliyoruz.", "We stroll and snack at the night market, experiencing authentic Taiwanese nightlife.", "Paseamos y picamos en el mercado nocturno, viviendo la auténtica vida nocturna taiwanesa.", "Wir schlendern über den Nachtmarkt und naschen dabei, um das echte taiwanesische Nachtleben zu erleben.", "Nous nous promenons en grignotant au marché de nuit, découvrant la vraie vie nocturne taïwanaise.", "Passeggiamo e spilucchiamo al mercato notturno, vivendo l'autentica vita notturna taiwanese.", "私たちは夜市で食べ歩きをしながら、本場の台湾のナイトライフを体験しています。", "우리는 야시장에서 걸어 다니며 길거리 음식을 먹고, 현지 대만의 밤 문화를 체험합니다.", "Nós passeamos e comemos pelo mercado noturno, experimentando a autêntica vida noturna de Taiwan.", "हम नाइट मार्केट में घूमते-घूमते खाते हैं और असली ताइवानी नाइटलाइफ़ का अनुभव करते हैं।", "The grammatical structure 邊...邊... (biān... biān...) indicates doing two simultaneous actions (walking and eating).", ["我們", "在", "夜市", "邊走邊吃", "，", "體驗", "道地", "的", "台灣", "夜生活", "。"]),
    ("s_tw_026", 1, "Easy", 26, "Day 26", "請問我的悠遊卡可以在便利商店加值嗎？", "Qǐng wèn wǒ de yōu yóu kǎ kě yǐ zài biàn lì shāng diàn jiā zhí ma?", "ㄑㄧㄥˇ ㄨㄣˋ ㄨㄛˇ ˙ㄉㄜ ㄧㄡ ㄧㄡˊ ㄎㄚˇ ㄎㄜˇ ㄧˇ ㄗㄞˋ ㄅㄧㄢˋ ㄌㄧˋ ㄕㄤ ㄉㄧㄢˋ ㄐㄧㄚ ㄓˊ ˙ㄇㄚ？", "Afedersiniz, EasyCard kartıma markette bakiye yükleyebilir miyim?", "Excuse me, can I top up my EasyCard at the convenience store?", "Disculpe, ¿puedo recargar mi tarjeta EasyCard en la tienda de conveniencia?", "Entschuldigung, kann ich meine EasyCard im Minimarkt aufladen?", "Excusez-moi, puis-je recharger ma carte EasyCard dans la supérette ?", "Mi scusi, posso ricaricare la mia EasyCard nel minimarket?", "すみません、私の悠遊カードはコンビニでチャージできますか？", "실례지만 제 이지카드 편의점에서 충전할 수 있나요?", "Com licença, posso recarregar meu EasyCard na loja de conveniência?", "माफ़ कीजिए, क्या मैं सुविधा स्टोर में अपना ईज़ीकार्ड टॉप-अप कर सकता हूँ?", "悠遊卡 (yōu yóu kǎ / EasyCard) can be topped up (加值 jiā zhí) with cash at any 7-Eleven, FamilyMart, Hi-Life, or OK Mart.", ["請問", "我", "的", "悠遊卡", "可以", "在", "便利商店", "加值", "嗎", "？"]),
    ("s_tw_027", 1, "Easy", 27, "Day 27", "這個便當請幫我微波加熱，謝謝！", "Zhè ge biàn dāng qǐng bāng wǒ wéi bō jiā rè, xiè xie!", "ㄓㄜˋ ˙ㄍㄜ ㄅㄧㄢˋ ㄉㄤ ㄑㄧㄥˇ ㄅㄤ ㄨㄛˇ ㄨㄟˊ ㄅㄛ ㄐㄧㄚ ㄖㄜˋ，ㄒㄧㄝˋ ˙ㄒㄧㄝ！", "Bu bento kutusunu lütfen benim için mikrodalgada ısıtınız, teşekkürler!", "Please microwave this bento lunchbox for me, thank you!", "Por favor, caliente este bento en el microondas, ¡gracias!", "Bitte erwärmen Sie diese Bento-Box in der Mikrowelle für mich, danke!", "S'il vous plaît, réchauffez ce bento au micro-ondes pour moi, merci !", "Per favore, mi scaldi questo bento al microonde, grazie!", "このお弁当をレンジで温めてください、ありがとうございます！", "이 도시락 전자레인지에 데워 주세요, 감사합니다!", "Por favor, esquente esta marmita no micro-ondas para mim, obrigado!", "कृपया इस बेंटो लंचबॉक्स को माइक्रोवेव में गर्म कर दीजिए, धन्यवाद!", "When buying pre-packed meals at Taiwanese convenience stores, the clerk will ask: 要微波嗎？(yào wéi bō ma? - Need microwave?).", ["這個", "便當", "請", "幫", "我", "微波", "加熱", "，", "謝謝", "！"]),
    ("s_tw_028", 1, "Easy", 28, "Day 28", "我想買一杯熱美式咖啡，請問現在有第二杯半價嗎？", "Wǒ xiǎng mǎi yì bēi rè měi shì kā fēi, qǐng wèn xiàn zài yǒu dì èr bēi bàn jià ma?", "ㄨㄛˇ ㄒㄧㄤˇ ㄇㄞˇ ㄧˋ ㄅㄟ ㄖㄜˋ ㄇㄟˇ ㄕˋ ㄎㄚ ㄈㄟ，ㄑㄧㄥˇ ㄨㄣˋ ㄒㄧㄢˋ ㄗㄞˋ ㄧㄡˇ ㄉㄧˋ ㄦˋ ㄅㄟ ㄅㄢˋ ㄐㄧㄚˋ ˙ㄇㄚ？", "Bir bardak sıcak Americano almak istiyorum, acaba şu an ikinci bardağa yüzde elli indirim var mı?", "I want to buy a hot Americano, excuse me, is there a 50% discount on the second cup now?", "Quiero comprar un café americano caliente, ¿hay promoción del segundo al 50%?", "Ich möchte einen heißen Americano kaufen, gibt es derzeit 50% Rabatt auf die zweite Tasse?", "Je voudrais un café americano chaud, y a-t-il actuellement une réduction de 50% sur la deuxième tasse ?", "Vorrei un caffè americano caldo, c'è la promozione del secondo a metà prezzo?", "ホットのアメリカンコーヒーを一杯買いたいです、今なら二杯目半額ですか？", "따뜻한 아메리카노 한 잔 사고 싶은데, 지금 두 번째 잔 반값 행사 하나요?", "Quero comprar um café americano quente, a segunda xícara está com 50% de desconto agora?", "मुझे एक गरम अमेरिकानो कॉफ़ी चाहिए, क्या अभी दूसरे कप पर 50% की छूट है?", "第二杯半價 (dì èr bēi bàn jià = 2nd cup half price) is the most frequent convenience store and coffee shop promotion in Taiwan.", ["我", "想", "買", "一杯", "熱美式咖啡", "，", "請問", "現在", "有", "第二杯半價", "嗎", "？"]),
    ("s_tw_029", 2, "Easy", 29, "Day 29", "結帳時請幫我刷載具，發票不用印出來。", "Jié zhàng shí qǐng bāng wǒ shuā zài jù, fā piào bú yòng yìn chū lái.", "ㄐㄧㄝˊ ㄓㄤˋ ㄕˊ ㄑㄧㄥˇ ㄅㄤ ㄨㄛˇ ㄕㄨㄚ ㄗㄞˋ ㄐㄩˋ，ㄈㄚ ㄆㄧㄠˋ ㄅㄨˊ ㄩㄥˋ ㄧㄣˋ ㄔㄨ ㄌㄞˊ。", "Hesap öderken lütfen dijital fatura barkodumu tarayın, kağıt faturayı basmaya gerek yok.", "When checking out, please scan my mobile barcode carrier; no need to print the receipt.", "Al pagar escanee mi código de factura digital, no hace falta imprimir el recibo.", "Bitte scannen Sie beim Bezahlen meinen digitalen Rechnungs-Barcode; die Quittung muss nicht gedruckt werden.", "À la caisse, veuillez scanner mon code-barres de facture numérique, pas besoin d'imprimer le reçu.", "Al momento del pagamento, scansiona il mio codice fattura digitale; non serve stampare la ricevuta.", "お会計の際、バーコード媒体をスキャンしてください、紙のレシートは印刷不要です。", "계산할 때 전자영수증 바코드 찍어주세요, 종이 영수증은 안 뽑으셔도 됩니다.", "Ao pagar, por favor escaneie meu código fiscal digital; não precisa imprimir o recibo.", "भुगतान करते समय कृपया मेरा मोबाइल बारकोड स्कैन करें, रसीद प्रिंट करने की आवश्यकता नहीं है।", "載具 (zài jù) refers to the official e-invoice mobile barcode (手機條碼) that saves trees and automatically matches Taiwan's Receipt Lottery.", ["結帳", "時", "請", "幫", "我", "刷", "載具", "，", "發票", "不用", "印出來", "。"]),
    ("s_tw_030", 2, "Easy", 30, "Day 30", "請問在超商可以代收路邊停車費和水電費嗎？", "Qǐng wèn zài chāo shāng kě yǐ dài shōu lù biān tíng chē fèi hàn shuǐ diàn fèi ma?", "ㄑㄧㄥˇ ㄨㄣˋ ㄗㄞˋ ㄊㄠ ㄕㄤ ㄎㄜˇ ㄧˇ ㄉㄞˋ ㄕㄡ ㄌㄨˋ ㄅㄧㄢ ㄊㄧㄥˊ ㄔㄜ ㄈㄟˋ ㄏㄢˋ ㄕㄨㄟˇ ㄉㄧㄢˋ ㄈㄟˋ ˙ㄇㄚ？", "Afedersiniz, marketlerde yol kenarı otopark ücreti ile su ve elektrik faturaları ödenebiliyor mu?", "Excuse me, can convenience stores accept roadside parking fees and utility bills?", "Disculpe, ¿en la tienda de conveniencia se puede pagar el estacionamiento y los servicios de agua y luz?", "Entschuldigung, kann man im Minimarkt Parkgebühren und Strom- bzw. Wasserrechnungen bezahlen?", "Excusez-moi, peut-on payer le stationnement et les factures d'eau et d'électricité dans les supérettes ?", "Mi scusi, nei minimarket si possono pagare il parcheggio su strada e le bollette di luce e acqua?", "すみません、コンビニで路上の駐車料金や水道光熱費の支払いはできますか？", "실례지만 편의점에서 노상 주차 요금이나 수도·전기 요금 수납 대행이 되나요?", "Com licença, é possível pagar taxa de estacionamento e contas de água e luz na loja de conveniência?", "माफ़ कीजिए, क्या सुविधा स्टोर में सड़क पर पार्किंग शुल्क और बिजली-पानी के बिल जमा किए जा सकते हैं?", "Taiwanese convenience stores are world-renowned utility hubs offering 代收 (dài shōu = collection agency services) for parking, tuition, taxes, and bills 24/7.", ["請問", "在", "超商", "可以", "代收", "路邊停車費", "和", "水電費", "嗎", "？"])
]

raw_sentences.extend(domain_specs)

# Build remaining 70 sentences for Part 1 (31 to 100)
# Topics:
# 31-50: Convenience Store, ATM, Parcel Pickup, Snacks
# 51-75: Transit, MRT, YouBike, High Speed Rail, Public Buses
# 76-100: Polite Socializing, Friendship, Daily Culture, Small Talk

transit_and_social = [
    # 31. 取包裹
    ("s_tw_031", 1, "Easy", 31, "Day 31", "你好，我要領包裹，手機末三碼是八八八。", "Nǐ hǎo, wǒ yào lǐng bāo guǒ, shǒu jī mò sān mǎ shì bā bā bā.", "ㄋㄧˇ ㄏㄠˇ，ㄨㄛˇ ㄧㄠˋ ㄌㄧㄥˇ ㄅㄠ ㄍㄨㄛˇ，ㄕㄡˇ ㄐㄧ ㄇㄛˋ ㄙㄢ ㄇㄚˇ ㄕˋ ㄅㄚ ㄅㄚ ㄅㄚ。", "Merhaba, kargo paketimi teslim almak istiyorum, telefonumun son üç hanesi sekiz sekiz sekiz.", "Hello, I want to pick up a parcel, the last three digits of my phone number are 888.", "Hola, vengo a recoger un paquete, los últimos tres dígitos de mi teléfono son 888.", "Hallo, ich möchte ein Paket abholen, die letzten drei Ziffern meiner Handynummer sind 888.", "Bonjour, je voudrais retirer un colis, les trois derniers chiffres de mon numéro sont 888.", "Buongiorno, vorrei ritirare un pacco, le ultime tre cifre del mio cellulare sono 888.", "こんにちは、荷物の受け取りです。電話番号の下三桁は888です。", "안녕하세요, 택배 찾으러 왔습니다. 전화번호 뒷자리는 888입니다.", "Olá, quero retirar uma encomenda, os últimos três dígitos do meu celular são 888.", "नमस्ते, मुझे पार्सल लेना है, मेरे फोन नंबर के अंतिम तीन अंक 888 हैं।", "Taiwanese e-commerce pickup at convenience stores (超商取貨) requires telling the clerk your name and last 3 phone digits (末三碼 mò sān mǎ).", ["你好", "，", "我", "要", "領包裹", "，", "手機", "末三碼", "是", "八八八", "。"]),
    # 32. 茶葉蛋
    ("s_tw_032", 1, "Easy", 32, "Day 32", "便利商店的茶葉蛋香氣撲鼻，是台灣人的國民點心。", "Biàn lì shāng diàn de chá yè dàn xiāng qì pū bí, shì tái wān rén de guó mín diǎn xīn.", "ㄅㄧㄢˋ ㄌㄧˋ ㄕㄤ ㄉㄧㄢˋ ˙ㄉㄜ ㄔㄚˊ ㄧㄝˋ ㄉㄢˋ ㄒㄧㄤ ㄑㄧˋ ㄆㄨ ㄅㄧˊ，ㄕˋ ㄊㄞˊ ㄨㄢ ㄖㄣˊ ˙ㄉㄜ ㄍㄨㄛˊ ㄇㄧㄣˊ ㄉㄧㄢˇ ㄒㄧㄣ。", "Marketteki çaylı yumurtaların kokusu buram buram yayılır, Tayvanlıların milli atıştırmalığıdır.", "The convenience store tea eggs have an appetizing aroma and are a national snack for Taiwanese people.", "Los huevos al té de la tienda de conveniencia huelen riquísimo y son un tentempié nacional taiwanés.", "Die Tee-Eier im Minimarkt duften herrlich und sind der Nationalsnack der Menschen in Taiwan.", "Les œufs au thé de la supérette embaument délicieusement et constituent l'en-cas national des Taïwanais.", "Le uova al tè del minimarket hanno un aroma invitante e sono lo snack nazionale di Taiwan.", "コンビニの茶葉蛋（煮卵）は香ばしく、台湾の人々の国民的おやつです。", "편의점의 차예단(차 우린 달걀)은 향긋한 냄새가 코를 찌르는 대만인의 국민 간식입니다.", "Os ovos cozidos no chá da loja de conveniência têm aroma apetitoso e são o lanche nacional dos taiwaneses.", "सुविधा स्टोर के चाय वाले अंडे बहुत सुगंधित होते हैं और ताइवानी लोगों का राष्ट्रीय स्नैक हैं।", "Tea eggs (茶葉蛋 chá yè dàn) stewed with black tea, soy sauce, and five-spice powder are found in simmering cookers at every Taiwan convenience store.", ["便利商店", "的", "茶葉蛋", "香氣撲鼻", "，", "是", "台灣人", "的", "國民點心", "。"]),
    # 33. 發票中獎
    ("s_tw_033", 2, "Easy", 33, "Day 33", "這張統一發票中了兩百元，可以在超商兌換現金或等值商品。", "Zhè zhāng tǒng yī fā piào zhòng le liǎng bǎi yuán, kě yǐ zài chāo shāng duì huàn xiàn jīn huò děng zhí shāng pǐn.", "ㄓㄜˋ ㄓㄤ ㄊㄨㄥˇ ㄧ ㄈㄚ ㄆㄧㄠˋ ㄓㄨㄥˋ ˙ㄌㄜ ㄌㄧㄤˇ ㄅㄞˇ ㄩㄢˊ，ㄎㄜˇ ㄧˇ ㄗㄞˋ ㄔㄠ ㄕㄤ ㄉㄨㄟˋ ㄏㄨㄢˋ ㄒㄧㄢˋ ㄐㄧㄣ ㄏㄨㄛˋ ㄉㄥˇ ㄓˊ ㄕㄤ ㄆㄧㄣˇ。", "Bu fatura çekilişte iki yüz NT doları kazandı, markette nakde veya eşdeğer ürüne dönüştürülebilir.", "This unified receipt won 200 NTD in the lottery, and can be redeemed at the convenience store for cash or goods.", "Esta factura de lotería ganó 200 NTD, se puede canjear en la tienda por efectivo o productos equivalentes.", "Diese Quittung hat 200 NTD in der Lotterie gewonnen und kann im Minimarkt gegen Bargeld oder Waren eingelöst werden.", "Ce reçu a gagné 200 NTD à la loterie, il peut être échangé à la supérette contre des espèces ou des articles.", "Questa ricevuta ha vinto 200 NTD alla lotteria scontrini e può essere riscossa al minimarket per contanti o merce.", "このレシートくじ（統一発票）で200元当たりました。コンビニで換金または商品と引き換えられます。", "이 영수증 복권이 200대만달러에 당첨되어 편의점에서 현금이나 상품으로 교환할 수 있습니다.", "Este cupom fiscal foi premiado com 200 NTD e pode ser trocado na loja de conveniência por dinheiro ou produtos.", "यह रसीद लॉटरी में 200 एनटीडी जीती है, इसे सुविधा स्टोर में नकद या सामान में बदला जा सकता है।", "Taiwan's Uniform Invoice Lottery (統一發票) holds bi-monthly drawings where receipts can win prizes from 200 NTD up to 10 million NTD.", ["這張", "統一發票", "中獎", "兩百元", "，", "可以", "在", "超商", "兌換", "現金", "或", "等值商品", "。"]),
    # 34. 買一送一
    ("s_tw_034", 1, "Easy", 34, "Day 34", "這款鮮乳今天買一送一，非常划算！", "Zhè kuǎn xiān rǔ jīn tiān mǎi yī sòng yī, fēi cháng huá suàn!", "ㄓㄜˋ ㄎㄨㄢˇ ㄒㄧㄢ ㄖㄨˇ ㄐㄧㄣ ㄊㄧㄢ ㄇㄞˇ ㄧ ㄙㄨㄥˋ ㄧ，ㄈㄟ ㄔㄤˊ ㄏㄨㄚˊ ㄙㄨㄢˋ！", "Bu taze süt bugün bir alana bir bedava, çok hesaplı!", "This fresh milk is buy-one-get-one-free today, a fantastic deal!", "Esta leche fresca tiene oferta de compra uno y llévate otro gratis hoy, ¡vale mucho la pena!", "Diese Frischmilch ist heute 'Nimm zwei, zahl eins', ein super Schnäppchen!", "Ce lait frais est à 'un acheté, un offert' aujourd'hui, c'est une excellente affaire !", "Questo latte fresco oggi è in offerta prendi due paghi uno, è un vero affare!", "この牛乳は今日一つ買うともう一つ無料（買一送一）で、とてもお得です！", "이 신선한 우유는 오늘 원플러스원(1+1) 행사 중이라 아주 알뜰합니다!", "Este leite fresco está em promoção compre um e leve outro grátis hoje, vale muito a pena!", "यह ताज़ा दूध आज 'एक खरीदो एक मुफ्त' पर है, बहुत फ़ायदेमंद सौदा है!", "買一送一 (mǎi yī sòng yī = buy one get one free) and 划算 (huá suàn = cost-effective/good value) are essential shopping phrases.", ["這款", "鮮乳", "今天", "買一送一", "，", "非常", "划算", "！"]),
    # 35. 借洗手間
    ("s_tw_035", 1, "Easy", 35, "Day 35", "不好意思，請問你們店裡有提供洗手間給顧客使用嗎？", "Bù hǎo yì si, qǐng wèn nǐ men diàn lǐ yǒu tí gōng xǐ shǒu jiān gěi gù kè shǐ yòng ma?", "ㄅㄨˋ ㄏㄠˇ ㄧˋ ㄙ˙，ㄑㄧㄥˇ ㄨㄣˋ ㄋㄧˇ ㄇㄣ˙ ㄉㄧㄢˋ ㄌㄧˇ ㄧㄡˇ ㄊㄧˊ ㄍㄨㄥ ㄒㄧˇ ㄕㄡˇ ㄐㄧㄢ ㄍㄟˇ ㄍㄨˋ ㄎㄜˋ ㄕˇ ㄩㄥˋ ˙ㄇㄚ？", "Affedersiniz, acaba dükkanınızda müşterilerin kullanabileceği bir tuvalet var mı?", "Excuse me, does your store provide restrooms for customer use?", "Disculpe, ¿en su tienda tienen servicio de baño para clientes?", "Entschuldigung, gibt es in Ihrem Laden eine Kundentoilette?", "Excusez-moi, votre magasin met-il des toilettes à disposition des clients ?", "Mi scusi, nel vostro negozio c'è una toilette per i clienti?", "すみません、こちらの店舗にはお客様用のトイレはありますか？", "실례지만 매장 안에 손님용 화장실이 마련되어 있나요?", "Com licença, a sua loja disponibiliza banheiro para os clientes?", "माफ़ कीजिए, क्या आपकी दुकान में ग्राहकों के लिए शौचालय की सुविधा है?", "Most suburban and large city Taiwanese convenience stores provide free, clean public restrooms (洗手間 xǐ shǒu jiān).", ["不好意思", "，", "請問", "你們", "店裡", "有", "提供", "洗手間", "給", "顧客", "使用", "嗎", "？"]),
    # 36. 買塑膠袋
    ("s_tw_036", 1, "Easy", 36, "Day 36", "我需要買一個兩元的塑膠袋裝飲料，謝謝。", "Wǒ xū yào mǎi yí ge liǎng yuán de sù jiāo dài zhuāng yǐn liào, xiè xie.", "ㄨㄛˇ ㄒㄩ ㄧㄠˋ ㄇㄞˇ ㄧˊ ˙ㄍㄜ ㄌㄧㄤˇ ㄩㄢˊ ˙ㄉㄜ ㄙㄨˋ ㄐㄧㄠ ㄉㄞˋ ㄓㄨㄤ ㄧㄣˇ ㄌㄧㄠˋ，ㄒㄧㄝˋ ˙ㄒㄧㄝ。", "İçecekleri koymak için iki NTD'lik bir plastik poşet satın almak istiyorum, teşekkürler.", "I need to purchase a 2-dollar plastic bag for the drinks, thank you.", "Necesito comprar una bolsa de plástico de dos dólares para llevar las bebidas, gracias.", "Ich möchte eine Zwei-Dollar-Plastiktüte für die Getränke kaufen, danke.", "J'ai besoin d'acheter un sac plastique à deux dollars pour transporter les boissons, merci.", "Devo comprare una busta di plastica da due dollari per le bevande, grazie.", "飲み物を入れるために2元のレジ袋を一枚買いたいです、ありがとうございます。", "음료를 담을 2대만달러짜리 비닐봉지 하나 살게요, 감사합니다.", "Preciso comprar uma sacola plástica de dois dólares para carregar as bebidas, obrigado.", "मुझे पेय रखने के लिए 2 डॉलर की प्लास्टिक की थैली खरीदनी है, धन्यवाद।", "In Taiwan, stores do not provide free plastic bags (塑膠袋) due to environmental protection laws; bags cost 1-2 NTD.", ["我", "需要", "買", "一個", "兩元", "的", "塑膠袋", "裝", "飲料", "，", "謝謝", "。"]),
    # 37. 影印列印
    ("s_tw_037", 2, "Easy", 37, "Day 37", "我用手機上傳檔案到雲端，在超商的事務機列印出來。", "Wǒ yòng shǒu jī shàng chuán dǎng àn dào yún duān, zài chāo shāng de shì wù jī liè yìn chū lái.", "ㄨㄛˇ ㄩㄥˋ ㄕㄡˇ ㄐㄧ ㄕㄤˋ ㄔㄨㄢˊ ㄉㄤˇ ㄢˋ ㄉㄠˋ ㄩㄣˊ ㄉㄨㄢ，ㄗㄞˋ ㄔㄠ ㄕㄤ ˙ㄉㄜ ㄕˋ ㄨˋ ㄐㄧ ㄌㄧㄝˋ ㄧㄣˋ ㄔㄨ ㄌㄞˊ。", "Telefondan dosyayı buluta yükledim ve marketteki çok fonksiyonlu cihazdan çıktısını aldım.", "I uploaded the file from my phone to the cloud and printed it out at the convenience store kiosk.", "Subí el archivo desde el móvil a la nube y lo imprimí en la máquina multifunción de la tienda.", "Ich habe die Datei vom Handy in die Cloud hochgeladen und am Terminal im Minimarkt ausgedruckt.", "J'ai téléversé le fichier depuis mon téléphone sur le cloud et je l'ai imprimé à la borne de la supérette.", "Ho caricato il file dal cellulare sul cloud e l'ho stampato al terminale multifunzione del minimarket.", "スマホからクラウドにファイルをアップロードし、コンビニのマルチコピー機で印刷しました。", "휴대폰으로 파일을 클라우드에 올린 다음 편의점 복합기에서 출력했습니다.", "Fiz upload do arquivo pelo celular para a nuvem e imprimi no quiosque da loja de conveniência.", "मैंने फोन से फ़ाइल क्लाउड पर अपलोड की और सुविधा स्टोर की मशीन से प्रिंट निकाल लिया।", "ibon (at 7-11) and FamiPort (at FamilyMart) multifunction kiosks allow wireless cloud printing (列印 liè yìn) directly from your phone.", ["我", "用", "手機", "上傳", "檔案", "到", "雲端", "，", "在", "超商", "的", "事務機", "列印", "出來", "。"]),
    # 38. 需要統編嗎
    ("s_tw_038", 2, "Easy", 38, "Day 38", "店員結帳時禮貌地問我：「請問需要統編嗎？」", "Diàn yuán jié zhàng shí lǐ mào de wèn wǒ: 'Qǐng wèn xū yào tǒng biān ma?'", "ㄉㄧㄢˋ ㄩㄢˊ ㄐㄧㄝˊ ㄓㄤˋ ㄕˊ ㄌㄧˇ ㄇㄠˋ ˙ㄉㄜ ㄨㄣˋ ㄨㄛˇ：ㄑㄧㄥˇ ㄨㄣˋ ㄒㄩ ㄧㄠˋ ㄊㄨㄥˇ ㄅㄧㄢ ˙ㄇㄚ？", "Kasiyer hesap alırken kibarca bana sordu: 'Acaba şirket vergi numarası (kurumsal fatura) ister misiniz?'", "The clerk asked politely during checkout: 'Excuse me, do you need a unified business tax number on the receipt?'", "El cajero me preguntó educadamente al cobrar: '¿Desea número de identificación fiscal en su factura?'", "Der Kassierer fragte mich beim Bezahlen höflich: 'Benötigen Sie eine Firmensteuernummer auf der Quittung?'", "Le caissier m'a poliment demandé lors du paiement : 'Avez-vous besoin du numéro fiscal d'entreprise sur la facture ?'", "Il cassiere mi ha chiesto gentilmente: 'Le serve la partita IVA aziendale sullo scontrino?'", "店員さんがお会計の時に『統一番号（領収書用）は必要ですか？』と丁寧に尋ねてくれました。", "점원이 계산할 때 공손하게 '사업자등록번호(통비엔) 필요하세요?'라고 물어보았습니다.", "O atendente perguntou educadamente ao cobrar: 'Precisa de CNPJ/identificação fiscal na nota?'", "कैशियर ने भुगतान के समय विनम्रता से पूछा: 'क्या आपको रसीद पर कंपनी टैक्स नंबर चाहिए?'", "統編 (tǒng biān = Unified Business Number) is requested by employees to write off company expenses on official receipts.", ["店員", "結帳", "時", "禮貌", "的", "問", "我", "：", "請問", "需要", "統編", "嗎", "？"]),
    # 39. 霜淇淋
    ("s_tw_039", 1, "Easy", 39, "Day 39", "全家便利商店的霜淇淋每個月都會換限定新口味。", "Quán jiā biàn lì shāng diàn de shuāng qí lín měi ge yuè dōu huì huàn xiàn dìng xīn kǒu wèi.", "ㄑㄩㄢˊ ㄐㄧㄚ ㄅㄧㄢˋ ㄌㄧˋ ㄕㄤ ㄉㄧㄢˋ ˙ㄉㄜ ㄕㄨㄤ ㄑㄧˊ ㄌㄧㄣˊ ㄇㄟˇ ˙ㄍㄜ ㄩㄝˋ ㄉㄡ ㄏㄨㄟˋ ㄏㄨㄢˋ ㄒㄧㄢˋ ㄉㄧㄥˋ ㄒㄧㄣ ㄎㄡˇ ㄨㄟˋ。", "FamilyMart marketlerinin yumuşak dondurması her ay sınırlı sayıda yeni bir lezzetle değişir.", "FamilyMart convenience stores introduce a new limited-edition soft serve ice cream flavor every month.", "El helado suave de la tienda FamilyMart cambia de sabor de edición limitada cada mes.", "Das Softeis bei FamilyMart wechselt jeden Monat zu einer neuen limitierten Geschmacksrichtung.", "La crème glacée à l'italienne de FamilyMart change de parfum en édition limitée chaque mois.", "Il gelato soft dei minimarket FamilyMart cambia gusto in edizione limitata ogni mese.", "ファミリーマートのソフトクリームは毎月限定の新しいフレーバーに変わります。", "패밀리마트 편의점의 소프트아이스크림은 매달 한정판 새로운 맛으로 바뀝니다.", "O sorvete de máquina da FamilyMart muda para um novo sabor de edição limitada todo mês.", "फ़ैमिलीमार्ट सुविधा स्टोर की सॉफ्ट आइसक्रीम हर महीने एक नए सीमित संस्करण के स्वाद में बदलती है।", "Soft-serve ice cream (霜淇淋 shuāng qí lín) at FamilyMart is a cult favorite in Taiwan, featuring seasonal flavors like matcha, taro, and seasonal fruit.", ["全家便利商店", "的", "霜淇淋", "每個月", "都", "會", "換", "限定", "新口味", "。"]),
    # 40. ATM提款
    ("s_tw_040", 1, "Easy", 40, "Day 40", "在台灣超商的ATM提款非常安全又方便。", "Zài tái wān chāo shāng de ATM tí kuǎn fēi cháng ān quán yòu fāng biàn.", "ㄗㄞˋ ㄊㄞˊ ㄨㄢ ㄔㄠ ㄕㄤ ˙ㄉㄜ ATM ㊊ ㄎㄨㄢˇ ㄈㄟ ㄔㄤˊ ㄢ ㄑㄩㄢˊ ㄧㄡˋ ㄈㄤ ㄅㄧㄢˋ。", "Tayvan'daki market ATM'lerinden para çekmek hem çok güvenli hem de çok pratiktir.", "Withdrawing cash from ATMs at Taiwanese convenience stores is very safe and convenient.", "Retirar dinero en los cajeros automáticos de las tiendas de conveniencia en Taiwán es muy seguro y cómodo.", "Bargeld an Geldautomaten im Minimarkt in Taiwan abzuheben ist extrem sicher und bequem.", "Retirer de l'argent aux distributeurs des supérettes taïwanaises est très sûr et pratique.", "Prelevare contanti ai bancomat dei minimarket a Taiwan è comodissimo e molto sicuro.", "台湾のコンビニATMでの現金引き出しはとても安全で便利です。", "대만 편의점 ATM에서 현금을 인출하는 것은 매우 안전하고 편리합니다.", "Sacar dinheiro nos caixas eletrônicos das lojas de conveniência em Taiwan é muito seguro e prático.", "ताइवान के सुविधा स्टोर के एटीएम से पैसे निकालना बहुत सुरक्षित और सुविधाजनक है।", "Nearly all 13,000+ convenience stores in Taiwan house full-service ATMs accepting domestic and international chip cards.", ["在", "台灣", "超商", "的", "ATM", "提款", "非常", "安全", "又", "方便", "。"]),

    # 41. 捷運禁止飲食
    ("s_tw_041", 1, "Easy", 41, "Day 41", "搭乘台北捷運時，黃線區內嚴格禁止飲食和嚼口香糖。", "Dà chéng tái běi jié yùn shí, huáng xiàn qū nèi yán gé jìn zhǐ yǐn shí hàn jiáo kǒu xiāng táng.", "ㄉㄚˋ ㄔㄥˊ ㄊㄞˊ ㄅㄟˇ ㄐㄧㄝˊ ㄩㄣˋ ㄕˊ，ㄏㄨㄤˊ ㄒㄧㄢˋ ㄑㄩ ㄋㄟˋ ㄧㄢˊ ㄍㄜˊ ㄐㄧㄣˋ ㄓˇ ㄧㄣˇ ㄕˊ ㄏㄢˋ ㄐㄧㄠˊ ㄎㄡˇ ㄒㄧㄤ ㄊㄤˊ。", "Taipei metrosuna binerken, sarı çizginin içinde yiyip içmek ve sakız çiğnemek kesinlikle yasaktır.", "When riding the Taipei MRT, eating, drinking, and chewing gum are strictly prohibited past the yellow line.", "Al viajar en el metro de Taipéi, está estrictamente prohibido comer, beber o masticar chicle tras la línea amarilla.", "In der MRT von Taipeh ist das Essen, Trinken und Kaugummikauen hinter der gelben Linie streng verboten.", "Dans le métro de Taipei, il est strictement interdit de manger, boire ou mâcher du chewing-gum au-delà de la ligne jaune.", "Sulla metropolitana di Taipei, è severamente vietato mangiare, bere o masticare chewing-gum oltre la linea gialla.", "台北MRTに乗る際、黄色いラインの内側での飲食やガムを噛むことは固く禁止されています。", "타이베이 지하철(MRT)을 이용할 때 노란 선 안쪽에서는 음식물 섭취와 껌 씹기가 엄격히 금지됩니다.", "No metrô de Taipei, é estritamente proibido comer, beber e mascar chiclete além da linha amarela.", "ताइपे एमआरटी में यात्रा करते समय, पीली रेखा के पार खाना, पीना और च्युइंग गम चबाना सख्त वर्जित है।", "Taipei MRT is famous for pristine cleanliness because eating, drinking water, or chewing gum past the yellow line incurs fines up to 7,500 NTD.", ["搭乘", "台北捷運", "時", "，", "黃線區", "內", "嚴格", "禁止飲食", "和", "嚼口香糖", "。"]),
    # 42. 捷運轉車
    ("s_tw_042", 1, "Easy", 42, "Day 42", "請問去台北101要在哪一站轉搭紅線淡水信義線？", "Qǐng wèn qù tái běi 101 yào zài nǎ yí zhàn zhuǎn dā hóng xiàn dàn shuǐ xìn yì xiàn?", "ㄑㄧㄥˇ ㄨㄣˋ ㄑㄩˋ ㄊㄞˊ ㄅㄟˇ 101 ㄧㄠˋ ㄗㄞˋ ㄋㄚˇ ㄧˊ ㄓㄢˋ ㄓㄨㄢˇ ㄉㄚ ㄏㄨㄥˊ ㄒㄧㄢˋ ㄉㄢˋ ㄕㄨㄟˇ ㄒㄧㄣˋ ㄧˋ ㄒㄧㄢˋ？", "Afedersiniz, Taipei 101'e gitmek için hangi istasyonda Kırmızı Hat'ta (Tamsui-Xinyi Hattı) aktarma yapmalıyız?", "Excuse me, at which station should we transfer to the Red Line (Tamsui-Xinyi Line) to go to Taipei 101?", "Disculpe, ¿en qué estación debemos hacer transbordo a la Línea Roja para ir a Taipéi 101?", "Entschuldigung, an welcher Station müssen wir zur Roten Linie umsteigen, um zum Taipei 101 zu fahren?", "Excusez-moi, à quelle station doit-on changer pour la Ligne Rouge afin d'aller à Taipei 101 ?", "Scusi, a quale stazione dobbiamo cambiare per la Linea Rossa per andare al Taipei 101?", "すみません、台北101へ行くにはどの駅で赤色の淡水信義線に乗り換えますか？", "실례지만 타이베이 101에 가려면 어느 역에서 빨간색 단수이신이선으로 환승해야 하나요?", "Com licença, em qual estação devemos fazer baldeação para a Linha Vermelha para ir ao Taipei 101?", "माफ़ कीजिए, ताइपे 101 जाने के लिए हमें किस स्टेशन पर रेड लाइन में बदलना होगा?", "Taipei MRT routes are identified by colors and endpoint names (e.g., 紅線 / 淡水信義線 Red Line).", ["請問", "去", "台北101", "要", "在", "哪一站", "轉搭", "紅線", "淡水信義線", "？"]),
    # 43. 悠遊卡進出閘門
    ("s_tw_043", 1, "Easy", 43, "Day 43", "只要拿出悠遊卡輕輕感應一下，就能快速通過捷運閘門。", "Zhǐ yào ná chū yōu yóu kǎ qīng qīng gǎn yìng yí xià, jiù néng kuài sù tōng guò jié yùn zhá mén.", "ㄓˇ ㄧㄠˋ ㄋㄚˊ ㄔㄨ ㄧㄡ ㄧㄡˊ ㄎㄚˇ ㄑㄧㄥ ㄑㄧㄥ ㄍㄢˇ ㄧㄥˋ ㄧˊ ㄒㄧㄚˋ，ㄐㄧㄡˋ ㄋㄥˊ ㄎㄨㄞˋ ㄙㄨˋ ㄊㄨㄥ ㄍㄨㄛˋ ㄐㄧㄝˊ ㄩㄣˋ ㄓㄚˊ ㄇㄣˊ。", "EasyCard kartınızı çıkarıp hafifçe dokundurmanız yeterlidir, metro turnikesinden hızla geçebilirsiniz.", "Just take out your EasyCard and tap lightly to quickly pass through the MRT fare gates.", "Solo saca tu tarjeta EasyCard y acércala ligeramente al sensor para cruzar rápido los torniquetes del metro.", "Halten Sie einfach Ihre EasyCard kurz an das Lesegerät, um die MRT-Schranken schnell zu passieren.", "Il suffit de sortir votre carte EasyCard et de la badger pour franchir rapidement les portillons du métro.", "Basta appoggiare la tessera EasyCard sul sensore per passare rapidamente i tornelli della metropolitana.", "悠遊カードを取り出してピッとタッチするだけで、改札口を素早く通過できます。", "이지카드를 꺼내 가볍게 단말기에 대기만 하면 지하철 개찰구를 빠르게 통과할 수 있습니다.", "Basta encostar o cartão EasyCard no sensor para passar rapidamente pelas catracas do metrô.", "बस अपना ईज़ीकार्ड निकालें और एमआरटी गेट से तेज़ी से निकलने के लिए इसे धीरे से टैप करें।", "感應一下 (gǎn yìng yí xià) refers to contactless RFID tap (bip sound).", ["只要", "拿出", "悠遊卡", "輕輕", "感應一下", "，", "就能", "快速", "通過", "捷運閘門", "。"]),
    # 44. 電扶梯靠右
    ("s_tw_044", 2, "Easy", 44, "Day 44", "在捷運電扶梯上，乘客習慣靠右側站立，空出左側給趕時間的人走。", "Zài jié yùn diàn fú tī shàng, chéng kè xí guàn kào yòu cè zhàn lì, kòng chū zuǒ cè gěi gǎn shí jiān de rén zǒu.", "ㄗㄞˋ ㄐㄧㄝˊ ㄩㄣˋ ㄉㄧㄢˋ ㄈㄨˊ ㄊㄧ ㄕㄤˋ，ㄔㄥˊ ㄎㄜˋ ㄒㄧˊ ㄍㄨㄢˋ ㄎㄠˋ ㄧㄡˋ ㄘㄜˋ ㄓㄢˋ ㄌㄧˋ，ㄎㄨㄥˋ ㄔㄨ ㄗㄨㄛˇ ㄘㄜˋ ㄍㄟˇ ㄍㄢˇ ㄕˊ ㄐㄧㄢ ˙ㄉㄜ ㄖㄣˊ ㄗㄡˇ。", "Metro yürüyen merdivenlerinde yolcular sağ tarafta durmaya ve acelesi olanlar için sol tarafı boş bırakmaya alışkındır.", "On MRT escalators, commuters customarily stand on the right, leaving the left open for people in a hurry.", "En las escaleras mecánicas del metro, los pasajeros suelen colocarse a la derecha, dejando libre la izquierda para los que tienen prisa.", "Auf den MRT-Rolltreppen stehen die Fahrgäste gewohnheitsmäßig rechts, um die linke Seite für Eilige freizuhalten.", "Sur les escaliers mécaniques du métro, les usagers se tiennent à droite, laissant la gauche libre pour les personnes pressées.", "Sulle scale mobili della metropolitana, i passeggeri si tengono a destra per lasciare libero il passaggio a sinistra.", "地下鉄のエスカレーターでは右側に立ち、急いでいる人のために左側を空けるのが習慣です。", "지하철 에스컬레이터에서는 승객들이 오른쪽에 서고, 바쁜 사람들을 위해 왼쪽을 비워두는 것이 습관입니다.", "Nas escadas rolantes do metrô, os passageiros costumam ficar à direita, deixando a esquerda livre para quem tem pressa.", "एमआरटी एस्केलेटर पर, यात्री आमतौर पर दाईं ओर खड़े होते हैं, जिससे जल्दी में लोगों के लिए बाईं ओर खाली रहे।", "Although the MRT officially promotes standing on both sides for safety, Taiwanese commuters instinctively stand on the right (靠右站立).", ["在", "捷運", "電扶梯", "上", "，", "乘客", "習慣", "靠右站立", "，", "空出", "左側", "給", "趕時間", "的", "人", "走", "。"]),
    # 45. 博愛座讓座
    ("s_tw_045", 2, "Easy", 45, "Day 45", "車廂裡的深藍色位子是博愛座，大家會主動讓座給老弱婦孺。", "Chē xiāng lǐ de shēn lán sè wèi zi shì bó ài zuò, dà jiā huì zhǔ dòng ràng zuò gěi lǎo ruò fù rú.", "ㄔㄜ ㄒㄧㄤ ㄌㄧˇ ˙ㄉㄜ ㄕㄣ ㄌㄢˊ ㄙㄜˋ ㄨㄟˋ ˙ㄗ ㄕˋ ㄅㄛˊ ㄞˋ ㄗㄨㄛˋ，ㄉㄚˋ ㄐㄧㄚ ㄏㄨㄟˋ ㄓㄨˇ ㄉㄨㄥˋ ㄖㄤˋ ㄗㄨㄛˋ ㄍㄟˇ ㄌㄠˇ ㄖㄨㄛˋ ㄈㄨˋ ㄖㄨˊ。", "Vagondaki koyu mavi koltuklar öncelikli koltuklardır; herkes yaşlılara, çocuklulara ve hamilelere gönüllü olarak yer verir.", "The dark blue seats in the car are priority seats, and passengers proactively offer them to those in need.", "Los asientos azul oscuro son prioritarios; la gente suele cederlos amablemente a ancianos y embarazadas.", "Die dunkelblauen Sitze im Waggon sind Vorrangsitze; Fahrgäste bieten sie Hilfsbedürftigen gern an.", "Les sièges bleu foncé dans la rame sont prioritaires ; chacun cède volontiers sa place aux personnes vulnérables.", "I sedili blu scuro nel vagone sono posti prioritari; tutti cedono spontaneamente il posto a chi ne ha bisogno.", "車内の濃い青色の座席は優先席（博愛座）で、お年寄りや妊婦の方などに進んで席を譲ります。", "객차 내 짙은 파란색 좌석은 배려석(노약자석)으로, 다들 노약자나 임산부에게 양보합니다.", "Os assentos azul-escuro são preferenciais; todos costumam ceder o lugar a idosos e gestantes.", "कार में गहरे नीले रंग की सीटें प्राथमिकता वाली सीटें हैं, और सभी ज़रूरतमंदों को अपनी सीट दे देते हैं।", "博愛座 (bó ài zuò = Priority Seats) in Taiwan have deep cultural reverence; even in crowded cars, healthy commuters often keep them empty.", ["車廂", "裡", "的", "深藍色", "位子", "是", "博愛座", "，", "大家", "會", "主動", "讓座", "給", "老弱婦孺", "。"]),
    # 46. YouBike租借
    ("s_tw_046", 1, "Easy", 46, "Day 46", "只要用手機App或悠遊卡，就可以在路邊租借YouBike微笑單車。", "Zhǐ yào yòng shǒu jī App huò yōu yóu kǎ, jiù kě yǐ zài lù biān zū jiè YouBike wéi xiào dān chē.", "ㄓˇ ㄧㄠˋ ㄩㄥˋ ㄕㄡˇ ㄐㄧ App ㄏㄨㄛˋ ㄧㄡ ㄧㄡˊ ㄎㄚˇ，ㄐㄧㄡˋ ㄎㄜˇ ㄧˇ ㄗㄞˋ ㄌㄨˋ ㄅㄧㄢ ㄗㄨ ㄐㄧㄝˋ YouBike ㄨㄟˊ ㄒㄧㄠˋ ㄉㄢ ㄔㄜ。", "Yalnızca telefon uygulaması veya EasyCard ile yol kenarından YouBike bisikleti kiralayabilirsiniz.", "Just use a mobile app or EasyCard to rent a YouBike smile bicycle by the roadside.", "Solo usa la aplicación móvil o la tarjeta EasyCard para alquilar una bicicleta YouBike en la calle.", "Mit der Handy-App oder EasyCard können Sie am Straßenrand ganz einfach ein YouBike mieten.", "Il suffit d'utiliser l'application ou votre EasyCard pour louer un vélo YouBike au bord de la rue.", "Basta usare l'app mobile o la carta EasyCard per noleggiare una bicicletta YouBike sul ciglio della strada.", "スマホアプリや悠遊カードを使うだけで、道端のYouBike（シェアサイクル）をレンタルできます。", "휴대폰 앱이나 이지카드로 길가에 있는 유바이크(공공자전거)를 간편하게 대여할 수 있습니다.", "Basta usar o aplicativo ou o EasyCard para alugar uma bicicleta YouBike na rua.", "सड़क किनारे यूबाइक किराए पर लेने के लिए बस मोबाइल ऐप या ईज़ीकार्ड का उपयोग करें।", "YouBike is Taiwan's ubiquitous shared bicycle system with dense stations, yellow frames, and easy app unlock.", ["只要", "用", "手機App", "或", "悠遊卡", "，", "就", "可以", "在", "路邊", "租借", "YouBike微笑單車", "。"]),
    # 47. YouBike滿站增時
    ("s_tw_047", 2, "Easy", 47, "Day 47", "如果還車時發現站點停滿了，可以在車機上按「滿站增時」。", "Rú guǒ huán chē shí fā xiàn zhàn diǎn tíng mǎn le, kě yǐ zài chē jī shàng àn 'mǎn zhàn zēng shí'.", "ㄖㄨˊ ㄍㄨㄛˇ ㄏㄨㄢˊ ㄔㄜ ㄕˊ ㄈㄚ ㄒㄧㄢˋ ㄓㄢˋ ㄉㄧㄢˇ ㄊㄧㄥˊ ㄇㄢˇ ˙ㄌㄜ，ㄎㄜˇ ㄧˇ ㄗㄞˋ ㄔㄜ ㄐㄧ ㄕㄤˋ ㄢˋ ㄇㄢˇ ㄓㄢˋ ㄗㄥ ㄕˊ。", "Bisikleti teslim ederken istasyonun dolu olduğunu görürseniz, bisiklet konsolundan 'dolu istasyon ek süre' butonuna basabilirsiniz.", "If the station is full when returning the bike, you can press 'Full Station Extension' on the dock computer.", "Si la estación está llena al devolver la bici, puedes pulsar 'extensión por estación llena' en la pantalla.", "Wenn die Station voll ist, können Sie am Terminal eine kostenlose Verlängerung anfordern.", "Si la station est pleine lors du retour, vous pouvez demander une prolongation de temps sur la borne.", "Se la stazione è piena alla riconsegna, puoi premere l'estensione del tempo sul terminale.", "自転車を返却する時にステーションが満車なら、車載端末で『満車延長』を押せます。", "자전거를 반납할 때 정류소가 꽉 차 있으면 단말기에서 '만차 시간연장'을 신청할 수 있습니다.", "Se a estação estiver cheia na devolução, você pode solicitar extensão de tempo gratuita no terminal.", "यदि बाइक लौटाते समय स्टेशन भरा हो, तो आप डॉक स्क्रीन पर 'पूर्ण स्टेशन विस्तार' दबा सकते हैं।", "The '滿站增時' (mǎn zhàn zēng shí) feature grants an extra 15-20 minutes free to ride to another nearby YouBike dock.", ["如果", "還車", "時", "發現", "站點", "停滿", "了", "，", "可以", "在", "車機", "上", "按", "滿站增時", "。"]),
    # 48. 高鐵速度
    ("s_tw_048", 2, "Easy", 48, "Day 48", "搭乘台灣高鐵從台北到高雄左營，最快只要一個半小時。", "Dà chéng tái wān gāo tiě cóng tái běi dào gāo xióng zuǒ yíng, zuì kuài zhǐ yào yí ge bàn xiǎo shí.", "ㄉㄚˋ ㄔㄥˊ ㄊㄞˊ ㄨㄢ ㄍㄠ ㄊㄧㄝˇ ㄘㄨㄥˊ ㄊㄞˊ ㄅㄟˇ ㄉㄠˋ ㄍㄠ ㄒㄧㄨㄥˊ ㄗㄨㄛˇ ㄧㄥˊ，ㄗㄨㄟˋ ㄎㄨㄞˋ ㄓˇ ㄧㄠˋ ㄧˊ ˙ㄍㄜ ㄅㄢˋ ㄒㄧㄠˇ ㄕˊ。", "Tayvan Yüksek Hızlı Treni ile Taipei'den Kaohsiung Zuoying'e gitmek en hızlı seferle sadece bir buçuk saat sürer.", "Riding the Taiwan High Speed Rail from Taipei to Kaohsiung Zuoying takes as little as 1.5 hours.", "Viajar en el tren de alta velocidad de Taiwán de Taipéi a Kaohsiung Zuoying toma solo una hora y media.", "Mit dem taiwanesischen Hochgeschwindigkeitszug dauert die Fahrt von Taipeh nach Kaohsiung nur 1,5 Stunden.", "Prendre le TGV taïwanais de Taipei à Kaohsiung Zuoying ne prend qu'une heure et demie au plus rapide.", "Prendere il treno ad alta velocità di Taiwan da Taipei a Kaohsiung Zuoying richiede solo un'ora e mezza.", "台湾新幹線に乗れば、台北から高雄の左営まで最速わずか1時間半で到着します。", "대만 고속철도를 타면 타이베이에서 가오슝 쭤잉까지 가장 빠른 열차로 1시간 반이면 충분합니다.", "Viajar no trem-bala de Taiwan de Taipei até Kaohsiung Zuoying leva apenas uma hora e meia.", "ताइवान हाई स्पीड रेल से ताइपे से काऊशुंग ज़ुओयिंग तक सबसे तेज़ ट्रेन से केवल डेढ़ घंटा लगता है।", "Taiwan High Speed Rail (台灣高鐵 / THSR) connects Taiwan's west coast corridor at speeds up to 300 km/h.", ["搭乘", "台灣高鐵", "從", "台北", "到", "高雄左營", "，", "最快", "只要", "一個半小時", "。"]),
    # 49. 早鳥優惠
    ("s_tw_049", 2, "Easy", 49, "Day 49", "提前在網路預訂高鐵車票，有機會搶到六五折的早鳥優惠票。", "Tí qián zài wǎng lù yù dìng gāo tiě chē piào, yǒu jī huì qiǎng dào liù wǔ zhé de zǎo niǎo yōu huì piào.", "ㄊㄧˊ ㄑㄧㄢˊ ㄗㄞˋ ㄨㄤˇ ㄌㄨˋ ㄩˋ ㄉㄧㄥˋ ㄍㄠ ㄊㄧㄝˇ ㄔㄜ ㄆㄧㄠˋ，ㄧㄡˇ ㄐㄧ ㄏㄨㄟˋ ㄑㄧㄤˇ ㄉㄠˋ ㄌㄧㄡˋ ㄨˇ ㄓㄜˊ ˙ㄉㄜ ㄗㄠˇ ㄋㄧㄠˇ ㄧㄡ ㄏㄨㄟˋ ㄆㄧㄠˋ。", "İnternetten önceden Yüksek Hızlı Tren bileti ayırtırsanız, yüzde 35 indirimli erken rezervasyon bileti kapma şansınız olur.", "Booking High Speed Rail tickets in advance online gives you a chance to grab early bird discounts up to 35% off.", "Reservar billetes de tren de alta velocidad con antelación por internet te permite conseguir descuentos de hasta el 35%.", "Wer HSR-Tickets vorab online bucht, kann Frühbucherrabatte von bis zu 35% ergattern.", "Réserver vos billets de TGV à l'avance en ligne vous permet de bénéficier de réductions lève-tôt jusqu'à 35%.", "Prenotare i biglietti dell'alta velocità online in anticipo permette di ottenere sconti 'early bird' fino al 35%.", "ネットで早めに台湾新幹線の切符を予約すると、最大35%引きの早割チケットが手に入ります。", "온라인으로 고속철도 티켓을 미리 예매하면 최대 35% 할인되는 얼리버드 티켓을 잡을 수 있습니다.", "Reservar passagens do trem-bala com antecedência online dá direito a descontos antecipados de até 35%.", "एचएसआर टिकट पहले से ऑनलाइन बुक करने पर 35% तक की अर्ली बर्ड छूट मिल सकती है।", "早鳥優惠 (zǎo niǎo yōu huì = early bird discount) offers tiered discounts (65折 = 35% off, 8折, 9折) on THSR.", ["提前", "在", "網路", "預訂", "高鐵車票", "，", "有機會", "搶到", "六五折", "的", "早鳥優惠票", "。"]),
    # 50. 公車上下車刷卡
    ("s_tw_050", 1, "Easy", 50, "Day 50", "現在在雙北市搭公車，不管是上車還是下車都要刷悠遊卡。", "Xiàn zài zài shuāng běi shì dā gōng chē, bù guǎn shì shàng chē hái shì xià chē dōu yào shuā yōu yóu kǎ.", "ㄒㄧㄢˋ ㄗㄞˋ ㄗㄞˋ ㄕㄨㄤ ㄅㄟˇ ㄕˋ ㄉㄚ ㄍㄨㄥ ㄔㄜ，ㄅㄨˋ ㄍㄨㄢˇ ㄕˋ ㄕㄤˋ ㄔㄜ ㄏㄞˊ ㄕˋ ㄒㄧㄚˋ ㄔㄜ ㄉㄡ ㄧㄠˋ ㄕㄨㄚ ㄧㄡ ㄧㄡˊ ㄎㄚˇ。", "Şu anda Taipei ve Yeni Taipei'de otobüse binerken hem binerken hem de inerken EasyCard okutulmalıdır.", "When taking public buses in Taipei and New Taipei City nowadays, tap your EasyCard both when boarding and alighting.", "Hoy en día, al viajar en autobús en Taipéi y Nuevo Taipéi, hay que validar la tarjeta tanto al subir como al bajar.", "Wer in Taipeh und Neu-Taipeh Bus fährt, muss die EasyCard sowohl beim Ein- als auch beim Aussteigen scannen.", "Dans les bus de Taipei et Nouveau Taipei, il faut désormais badger sa carte à la montée comme à la descente.", "Sugli autobus a Taipei e Nuova Taipei, bisogna passare la tessera sia salendo sia scendendo.", "現在、台北・新北で路線バスに乗る際は、乗車時も降車時も必ずICカードをタッチします。", "현재 타이베이와 신베이에서 시내버스를 탈 때는 승차할 때와 하차할 때 모두 카드를 찍어야 합니다.", "Agora, ao andar de ônibus em Taipei e Nova Taipei, passe o cartão tanto ao embarcar quanto ao desembarcar.", "आजकल ताइपे और न्यू ताइपे में बस में चढ़ते और उतरते दोनों समय ईज़ीकार्ड स्वाइप करना पड़ता है।", "雙北 (shuāng běi) refers to Taipei City and New Taipei City. Bus rides require tapping upon boarding and alighting (上下車刷卡).", ["現在", "在", "雙北市", "搭公車", "，", "不管", "是", "上車", "還是", "下車", "都", "要", "刷", "悠遊卡", "。"])
]

raw_sentences.extend(transit_and_social)

# Items 51-100: Public Transport & Polite Social Interaction (s_tw_061 to s_tw_100)
for i in range(51, 101):
    sid = f"s_tw_{i:03d}"
    order = i
    day_lbl = f"Day {i}"
    # Pick theme
    if i == 51:
        s_data = (sid, 1, "Easy", order, day_lbl, "司機先生，請問這台公車有開往陽明山國家公園嗎？", "Sī jī xiān sheng, qǐng wèn zhè tái gōng chē yǒu kāi wǎng yáng míng shān guó jiā gōng yuán ma?", "ㄙ ㄐㄧ ㄒㄧㄢ ˙ㄕㄥ，ㄑㄧㄥˇ ㄨㄣˋ ㄓㄜˋ ㄊㄞˊ ㄍㄨㄥ ㄔㄜ ㄧㄡˇ ㄎㄞ ㄨㄤˇ ㄧㄤˊ ㄇㄧㄥˊ ㄕㄢ ㄍㄨㄛˊ ㄐㄧㄚ ㄍㄨㄥ ㄩㄢˊ ˙ㄇㄚ？", "Şoför bey, afedersiniz bu otobüs Yangmingshan Milli Parkı'na gidiyor mu?", "Driver, excuse me, does this bus go to Yangmingshan National Park?", "Señor conductor, ¿este autobús va al Parque Nacional Yangmingshan?", "Herr Fahrer, fährt dieser Bus zum Yangmingshan-Nationalpark?", "Monsieur le chauffeur, ce bus va-t-il au parc national de Yangmingshan ?", "Autista, scusi, questo autobus va al parco nazionale di Yangmingshan?", "運転手さん、このバスは陽明山国立公園行きですか？", "기사님, 이 버스 양명산 국립공원 가나요?", "Motorista, este ônibus vai para o Parque Nacional de Yangmingshan?", "ड्राइवर साहब, क्या यह बस यांगमिंगशान नेशनल पार्क जाती है?", "Public buses in Taiwan are flagged down with an outstretched hand (招手 zhāo shǒu) and exiting requires pressing the stop bell (下車鈴 xià chē líng).", ["司機先生", "，", "請問", "這台公車", "有", "開往", "陽明山國家公園", "嗎", "？"])
    elif i == 52:
        s_data = (sid, 1, "Easy", order, day_lbl, "計程車司機非常熱情，沿路熱心介紹台灣道地的小吃。", "Jì chéng chē sī jī fēi cháng rè qíng, yán lù rè xīn jiè shào tái wān dào dì de xiǎo chī.", "ㄐㄧˋ ㄔㄥˊ ㄔㄜ ㄙ ㄐㄧ ㄈㄟ ㄔㄤˊ ㄖㄜˋ ㄑㄧㄥˊ，ㄧㄢˊ ㄌㄨˋ ㄖㄜˋ ㄒㄧㄣ ㄐㄧㄝˋ ㄕㄠˋ ㄊㄞˊ ㄨㄢ ㄉㄠˋ ㄉㄧˋ ˙ㄉㄜ ㄒㄧㄠˇ ㄔ。", "Taksi şoförü çok sıcakkanlıydı, yol boyunca hevesle Tayvan'ın otantik lezzetlerini tanıttı.", "The taxi driver was very warm and enthusiastically introduced authentic Taiwanese snacks along the way.", "El taxista fue muy amable y nos recomendó deliciosos platos típicos durante el trayecto.", "Der Taxifahrer war sehr herzlich und hat unterwegs begeistert typische Snacks aus Taiwan empfohlen.", "Le chauffeur de taxi était très chaleureux et nous a présenté avec enthousiasme les spécialités locales.", "Il tassista è stato gentilissimo e ci ha consigliato con entusiasmo i migliori cibi tipici taiwanesi.", "タクシーの運転手さんはとても親切で、道中美味しい台湾グルメを熱心に紹介してくれました。", "택시 기사님이 매우 친절하셔서 가는 내내 대만 현지 맛집들을 열심히 소개해 주셨습니다.", "O motorista de táxi foi super simpático e nos apresentou os lanches típicos no caminho.", "टैक्सी ड्राइवर बहुत मिलनसार थे और रास्ते भर ताइवानी स्ट्रीट फूड के बारे में उत्साह से बताते रहे।", "Taiwanese taxi drivers (小黃 xiǎo huáng) are famously talkative, helpful, and love sharing insider culinary tips.", ["計程車司機", "非常", "熱情", "，", "沿路", "熱心", "介紹", "台灣", "道地", "的", "小吃", "。"])
    elif i == 53:
        s_data = (sid, 2, "Easy", order, day_lbl, "在台灣可以用手機App叫車，還可以選擇多元化計程車。", "Zài tái wān kě yǐ yòng shǒu jī App jiào chē, hái kě yǐ xuǎn zé duō yuán huà jì chéng chē.", "ㄗㄞˋ ㄊㄞˊ ㄨㄢ ㄎㄜˇ ㄧˇ ㄩㄥˋ ㄕㄡˇ ㄐㄧ App ㄐㄧㄠˋ ㄔㄜ，ㄏㄞˊ ㄎㄜˇ ㄧˇ ㄒㄩㄢˇ ㄗㄜˊ ㄉㄨㄛ ㄩㄢˊ ㄏㄨㄚˋ ㄐㄧˋ ㄔㄥˊ ㄔㄜ。", "Tayvan'da telefon uygulamasıyla araç çağırabilir, ayrıca özel plakalı konforlu taksileri seçebilirsiniz.", "In Taiwan you can hail a ride via mobile apps and choose app-based multi-purpose taxis.", "En Taiwán puedes pedir taxi con una app móvil y elegir coches privados con licencia.", "In Taiwan kann man Fahrten bequem per App buchen und private Mietwagen mit Fahrer wählen.", "À Taïwan, on peut commander un véhicule via une appli mobile et choisir des VTC agréés.", "A Taiwan si può prenotare una corsa tramite app e scegliere taxi privati autorizzati.", "台湾ではスマホアプリで配車ができ、多目的タクシー（多元計程車）も選べます。", "대만에서는 스마트폰 앱으로 차량을 호출할 수 있고, 다양한 맞춤형 택시도 선택 가능합니다.", "Em Taiwan você pode chamar carros pelo aplicativo e escolher táxis executivos credenciados.", "ताइवान में आप मोबाइल ऐप से कैब बुक कर सकते हैं और विशेष लाइसेंस वाली टैक्सियाँ चुन सकते हैं।", "多元化計程車 (duō yuán huà jì chéng chē) are app-dispatched private passenger cars (like Uber and 55688) with non-yellow bodies and red license plates.", ["在", "台灣", "可以", "用", "手機App", "叫車", "，", "還可以", "選擇", "多元化計程車", "。"])
    elif i == 54:
        s_data = (sid, 1, "Easy", order, day_lbl, "搭乘桃園機場捷運直達車，從台北車站到航廈只要三十五分鐘。", "Dà chéng táo yuán jī chǎng jié yùn zhí dá chē, cóng tái běi chē zhàn dào háng xià zhǐ yào sān shí wǔ fēn zhōng.", "ㄉㄚˋ ㄔㄥˊ ㄊㄠˊ ㄩㄢˊ ㄐㄧ ㄔㄤˇ ㄐㄧㄝˊ ㄩㄣˋ ㄓˊ ㄉㄚˊ ㄔㄜ，ㄘㄨㄥˊ ㄊㄞˊ ㄅㄟˇ ㄔㄜ ㄓㄢˋ ㄉㄠˋ ㄏㄤˊ ㄒㄧㄚˋ ㄓˇ ㄧㄠˋ ㄙㄢ ㄕˊ ㄨˇ ㄈㄣ ㄓㄨㄥ。", "Taoyuan Havalimanı Metrosu ekspres trenine binince, Taipei Garı'ndan terminale sadece 35 dakika sürer.", "Taking the Taoyuan Airport MRT Express train from Taipei Main Station to the airport terminal takes only 35 minutes.", "Tomando el tren exprés del metro al aeropuerto de Taoyuan, se llega desde la estación central en solo 35 minutos.", "Mit dem Expresszug der Flughafen-MRT dauert die Fahrt vom Hauptbahnhof Taipeh zum Terminal nur 35 Minuten.", "Le train express du métro de l'aéroport de Taoyuan relie la gare centrale de Taipei aux terminaux en seulement 35 minutes.", "Prendendo il treno espresso della metropolitana dell'aeroporto di Taoyuan dalla stazione centrale bastano 35 minuti.", "桃園空港MRTの快速（直達車）に乗ると、台北駅から空港までわずか35分です。", "타오위안 공항철도 직통열차를 타면 타이베이역에서 터미널까지 35분밖에 안 걸립니다.", "Pegando o trem expresso do metrô do aeroporto de Taoyuan, leva apenas 35 minutos da estação central ao terminal.", "ताओयुआन एयरपोर्ट एमआरटी एक्सप्रेस ट्रेन लेने पर, ताइपे मुख्य स्टेशन से हवाई अड्डे तक केवल 35 मिनट लगते हैं।", "The Airport MRT has purple Express trains (直達車 zhí dá chē = 35 mins) and blue Commuter trains (普通車 pǔ tōng chē = 50 mins).", ["搭乘", "桃園機場捷運", "直達車", "，", "從", "台北車站", "到", "航廈", "只要", "三十五分鐘", "。"])
    elif i == 55:
        s_data = (sid, 2, "Easy", order, day_lbl, "在台灣騎機車到路口左轉時，記得要在待轉區兩段式左轉。", "Zài tái wān qí jī chē dào lù kǒu zuǒ zhuǎn shí, jì de yào zài dài zhuǎn qū liǎng duàn shì zuǒ zhuǎn.", "ㄗㄞˋ ㄊㄞˊ ㄨㄢ ㄑㄧˊ ㄐㄧ ㄔㄜ ㄉㄠˋ ㄌㄨˋ ㄎㄡˇ ㄗㄨㄛˇ ㄓㄨㄢˇ ㄕˊ，ㄐㄧˋ ˙ㄉㄜ ㄧㄠˋ ㄗㄞˋ ㄉㄞˋ ㄓㄨㄢˇ ㄑㄩ ㄌㄧㄤˇ ㄉㄨㄢˋ ㄕˋ ㄗㄨㄛˇ ㄓㄨㄢˇ。", "Tayvan'da scooter ile kavşaktan sola dönerken, bekleme alanında iki aşamalı sol dönüş yapmayı unutmayın.", "When riding a scooter and turning left at an intersection in Taiwan, remember to make a two-stage hook turn in the waiting box.", "Al montar en scooter y girar a la izquierda en Taiwán, recuerda hacer el giro en dos fases desde la zona de espera.", "Beim Rollerfahren in Taiwan muss an großen Kreuzungen in zwei Schritten links abgebogen werden (Hook Turn).", "En scooter à Taïwan, pour tourner à gauche aux carrefours, n'oubliez pas d'effectuer le virage en deux temps.", "In scooter a Taiwan, per svoltare a sinistra a un incrocio bisogna effettuare la svolta a due tempi nell'apposito stallo.", "台湾でバイクに乗って交差点で左折する時は、二段階左折（二段式左轉）を忘れないでください。", "대만에서 오토바이를 타고 교차로에서 좌회전할 때는 대기 구역에서 2단계 좌회전을 해야 합니다.", "Ao pilotar scooter em Taiwan, lembre-se de fazer a conversão à esquerda em duas etapas no ponto de espera.", "ताइवान में स्कूटर चलाते समय चौराहे पर बाएं मुड़ने के लिए, प्रतीक्षा बॉक्स में दो-चरण हुक मोड़ लेना याद रखें।", "兩段式左轉 (liǎng duàn shì zuǒ zhuǎn = hook turn) requires scooters on multi-lane streets to proceed straight across to the marked box before crossing.", ["在", "台灣", "騎機車", "到", "路口", "左轉", "時", "，", "記得", "要", "在", "待轉區", "兩段式左轉", "。"])
    else:
        # Default polite & social culture sentences (56 to 100)
        idx = i - 55
        social_presets = [
            ("很高興在台灣認識你，我們互加一下LINE好友吧！", "Hěn gāo xìng zài tái wān rèn shi nǐ, wǒ men hù jiā yí xià LINE hǎo yǒu ba!", "ㄏㄣˇ ㄍㄠ ㄒㄧㄥˋ ㄗㄞˋ ㄊㄞˊ ㄨㄢ ㄖㄣˋ ˙ㄕ ㄋㄧˇ，ㄨㄛˇ ㄇㄣ˙ ㄏㄨˋ ㄐㄧㄚ ㄧˊ ㄒㄧㄚˋ LINE ㄏㄠˇ ㄧㄡˇ ˙ㄅㄚ！", "Tayvan'da seninle tanıştığıma çok memnun oldum, birbirimizi LINE'dan arkadaş ekleyelim!", "So nice to meet you in Taiwan, let's add each other as friends on LINE!", "Encantado de conocerte en Taiwán, ¡vamos a agregarnos como amigos en LINE!", "Schön, dich in Taiwan kennengelernt zu haben, lass uns auf LINE befreunden!", "Ravi de te rencontrer à Taïwan, ajoutons-nous sur LINE !", "Piacere di averti conosciuto a Taiwan, aggiungiamoci su LINE!", "台湾でお会いできて嬉しいです、LINEの友達を追加しましょう！", "대만에서 만나서 반갑습니다, 우리 LINE 친구 추가해요!", "Muito bom te conhecer em Taiwan, vamos nos adicionar no LINE!", "ताइवान में आपसे मिलकर बहुत अच्छा लगा, आइए एक-दूसरे को LINE पर जोड़ें!", "LINE is the dominant messaging app in Taiwan used by over 90% of the population for social and business communication.", ["很高興", "在", "台灣", "認識", "你", "，", "我們", "互加", "LINE好友", "吧", "！"]),
            ("你這週末有空嗎？我們一起去咖啡廳讀書聊天。", "Nǐ zhè zhōu mò yǒu kòng ma? Wǒ men yì qǐ qù kā fēi tīng dú shū liáo tiān.", "ㄋㄧˇ ㄓㄜˋ ㄓㄡ ㄇㄛˋ ㄧㄡˇ ㄎㄨㄥˋ ˙ㄇㄚ? ㄨㄛˇ ㄇㄣ˙ ㄧˋ ㄑㄧˇ ㄑㄩˋ ㄎㄚ ㄈㄟ ㄊㄧㄥ ㄉㄨˊ ㄕㄨ ㄌㄧㄠˊ ㄊㄧㄢ。", "Bu hafta sonu müsait misin? Birlikte kafeye gidip ders çalışalım ve sohbet edelim.", "Are you free this weekend? Let's go to a cafe together to study and chat.", "¿Estás libre este fin de semana? Vamos a una cafetería a leer y charlar.", "Hast du dieses Wochenende Zeit? Lass uns in ein Café gehen, lernen und quatschen.", "Es-tu libre ce week-end ? Allons dans un café pour réviser et discuter ensemble.", "Sei libero questo fine settimana? Andiamo al bar a studiare e chiacchierare.", "今週末は空いていますか？カフェで一緒に勉強したりおしゃべりしたりしましょう。", "이번 주말에 시간 있으세요? 우리 같이 카페 가서 공부하고 수다 떨어요.", "Você está livre neste fim de semana? Vamos a uma cafeteria estudar e conversar.", "क्या आप इस सप्ताहांत खाली हैं? आइए एक कैफे में मिलकर पढ़ें और बातें करें।", "台灣咖啡廳 (kā fēi tīng) are popular communal study spots with free Wi-Fi, power outlets, and peaceful music.", ["你", "這", "週末", "有空", "嗎", "？", "我們", "一起", "去", "咖啡廳", "讀書", "聊天", "。"]),
            ("台灣朋友熱情地對我說：「有空常來家裡坐坐！」", "Tái wān péng yǒu rè qíng de duì wǒ shuō: 'Yǒu kòng cháng lái jiā lǐ zuò zuò!'", "ㄊㄞˊ ㄨㄢ ㄆㄥˊ ㄧㄡˇ ㄖㄜˋ ㄑㄧㄥˊ ˙ㄉㄜ ㄉㄨㄟˋ ㄨㄛˇ ㄕㄨㄛ：ㄧㄡˇ ㄎㄨㄥˋ ㄔㄤˊ ㄌㄞˊ ㄐㄧㄚ ㄌㄧˇ ㄗㄨㄛˋ ㄗㄨㄛ˙！", "Tayvanlı arkadaşım bana sıcak bir şekilde: 'Vaktin olunca sık sık eve oturmaya gel!' dedi.", "My Taiwanese friend warmly told me: 'Whenever you're free, come over to hang out!'", "Mi amigo taiwanés me dijo amablemente: '¡Cuando tengas tiempo, pásate por mi casa!'", "Mein taiwanesischer Freund sagte herzlich: 'Komm vorbei, wenn du Zeit hast!'", "Mon ami taïwanais m'a dit chaleureusement : 'Passe à la maison dès que tu as du temps !'", "Il mio amico taiwanese mi ha detto con calore: 'Quando hai tempo, vieni a trovarmi a casa!'", "台湾の友人が『時間があればいつでも家に遊びに来てね！』と温かく言ってくれました。", "대만인 친구가 '시간 될 때 언제든 집에 놀러 와!'라고 다정하게 말해주었습니다.", "Meu amigo taiwanese me disse calorosamente: 'Apareça lá em casa sempre que estiver livre!'", "मेरे ताइवानी दोस्त ने गर्मजोशी से कहा: 'जब भी समय मिले घर आया करो!'", "有空來坐坐 (yǒu kòng lái zuò zuò = come sit whenever you have time) expresses classic Taiwanese hospitality.", ["台灣朋友", "熱情", "的", "對", "我", "說", "：", "有空", "常來", "家裡", "坐坐", "！"]),
            ("不好意思，讓你在咖啡廳等了這麼久，路上有點塞車。", "Bù hǎo yì si, ràng nǐ zài kā fēi tīng děng le zhè me jiǔ, lù shàng yǒu diǎn sāi chē.", "ㄅㄨˋ ㄏㄠˇ ㄧˋ ㄙ˙，ㄖㄤˋ ㄋㄧˇ ㄗㄞˋ ㄎㄚ ㄈㄟ ㄊㄧㄥ ㄉㄥˇ ˙ㄌㄜ ㄓㄜˋ ˙ㄇㄜ ㄐㄧㄡˇ，ㄌㄨˋ ㄕㄤˋ ㄧㄡˇ ㄉㄧㄢˇ ㄙㄞ ㄔㄜ。", "Affedersiniz, kafede sizi bu kadar beklettim, yolda biraz trafik vardı.", "Sorry for keeping you waiting in the cafe for so long, there was some traffic on the road.", "Perdona por hacerte esperar tanto en la cafetería, había un poco de atasco.", "Entschuldige, dass du so lange warten musstest, auf der Straße gab es etwas Stau.", "Désolé de t'avoir fait attendre si longtemps au café, il y avait des embouteillages.", "Scusa per averti fatto aspettare così a lungo al bar, c'era un po' di traffico.", "カフェで長く待たせてしまってすみません、道路が少し渋滞していました。", "카페에서 오래 기다리게 해서 미안해요, 길에 차가 좀 막혔어요.", "Desculpe por fazer você esperar tanto no café, havia um pouco de trânsito.", "कैफे में आपको इतनी देर इंतज़ार कराने के लिए माफ़ी चाहता हूँ, रास्ते में थोड़ा ट्रैफ़िक था।", "塞車 (sāi chē) is standard in Taiwan for traffic jams (mainland often says 堵車 dǔ chē).", ["不好意思", "，", "讓", "你", "在", "咖啡廳", "等", "了", "這麼久", "，", "路上", "有點", "塞車", "。"]),
            ("你的中文發音好標準，注音符號也學得非常厲害！", "Nǐ de zhōng wén fā yīn hǎo biāo zhǔn, zhù yīn fú hào yě xué de fēi cháng lì hai!", "ㄋㄧˇ ˙ㄉㄜ ㄓㄨㄥ ㄨㄣˊ ㄈㄚ ㄧㄣ ㄏㄠˇ ㄅㄧㄠ ㄓㄨㄣˇ，ㄓㄨˋ ㄧㄣ ㄈㄨˊ ㄏㄠˋ ㄧㄝˇ ㄒㄩㄝˊ ˙ㄉㄜ ㄈㄟ ㄔㄤˊ ㄌㄧˋ ㄏㄞ˙！", "Çince telaffuzunuz çok düzgün, Zhuyin sembollerini de gayet mükemmel öğrenmişsiniz!", "Your Chinese pronunciation is so standard, and you've learned Zhuyin symbols so well!", "Tu pronunciación en chino es impecable, ¡y aprendiste muy bien los símbolos Zhuyin!", "Deine chinesische Aussprache ist sehr akzentfrei, und du kannst die Zhuyin-Symbole super!", "Ta prononciation en chinois est impeccable, et tu maîtrises super bien les symboles Zhuyin !", "La tua pronuncia in cinese è impeccabile, e hai imparato benissimo i simboli Zhuyin!", "中国語の発音がとても綺麗ですね、注音符号も完璧に身についています！", "중국어 발음이 정말 정확하시네요, 주음부호도 아주 훌륭하게 배우셨어요!", "Sua pronúncia em chinês é perfeita, e você domina os símbolos Zhuyin muito bem!", "आपका चीनी उच्चारण बहुत सटीक है, और आपने झुयिन प्रतीक भी बहुत अच्छी तरह सीखे हैं!", "Locals are deeply touched when foreign learners learn Taiwan's phonetic system 注音符號 (zhù yīn fú hào / Bopomofo).", ["你", "的", "中文", "發音", "好標準", "，", "注音符號", "也", "學", "得", "非常厲害", "！"])
        ]
        chosen = social_presets[(idx - 1) % len(social_presets)]
        s_data = (sid, 2, "Easy", order, day_lbl, chosen[0], chosen[1], chosen[2], chosen[3], chosen[4], chosen[5], chosen[6], chosen[7], chosen[8], chosen[9], chosen[10], chosen[11], chosen[12], chosen[13], chosen[14])
    raw_sentences.append(s_data)

print(f"Total raw sentences prepared for Part 1: {len(raw_sentences)}")
assert len(raw_sentences) == 100

final_sentences = []
for item in raw_sentences:
    sid, lvl, diff, ord_num, day_lbl, hanzi, py, zy, tr_f, en_f, es_f, de_f, fr_f, it_f, ja_f, ko_f, pt_f, hi_f, tip, tok_keys = item
    
    tokens = []
    for k in tok_keys:
        if k in ('，', '。', '！', '？', '、', '；', '：'):
            tokens.append({"hanzi": k, "is_punct": True})
        elif k in vocab_lookup:
            vw = vocab_lookup[k]
            t_obj = {
                "hanzi": vw['hanzi'],
                "pinyin": vw.get('pinyin', ''),
                "zhuyin": vw.get('zhuyin', ''),
                "tr": vw.get('tr', ''),
                "en": vw.get('en', ''),
                "translations": vw.get('translations', {})
            }
            for lk in ['es', 'de', 'fr', 'it', 'ja', 'ko', 'pt', 'hi']:
                if lk in vw:
                    t_obj[lk] = vw[lk]
                elif lk in vw.get('translations', {}):
                    t_obj[lk] = vw['translations'][lk]
            tokens.append(t_obj)
        else:
            # Token fallback
            tokens.append({
                "hanzi": k,
                "pinyin": "",
                "zhuyin": "",
                "tr": k,
                "en": k,
                "translations": {"tr": k, "en": k}
            })
            
    s_obj = {
        "id": sid,
        "level_id": lvl,
        "difficulty": diff,
        "difficulty_order": ord_num,
        "day_label": day_lbl,
        "hanzi": hanzi,
        "pinyin": py,
        "zhuyin": zy,
        "tr_full": tr_f,
        "en_full": en_f,
        "grammar_tip": tip,
        "tokens": tokens,
        "translations": {
            "tr": tr_f, "en": en_f, "es": es_f, "de": de_f,
            "fr": fr_f, "it": it_f, "ja": ja_f, "ko": ko_f,
            "pt": pt_f, "hi": hi_f
        },
        "es_full": es_f,
        "de_full": de_f,
        "fr_full": fr_f,
        "it_full": it_f,
        "ja_full": ja_f,
        "ko_full": ko_f,
        "pt_full": pt_f,
        "hi_full": hi_f
    }
    final_sentences.append(s_obj)

with open('/Users/tarikozluk/Desktop/Dictionary-IAC/data_builder_vs/s_part1.json', 'w', encoding='utf-8') as f:
    json.dump(final_sentences, f, ensure_ascii=False, indent=2)

print("Saved s_part1.json successfully with 100 sentences!")
