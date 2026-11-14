import json

data = [
    # 1. 笑
    [
        "v_xiao", "笑", "xiào", "ㄒㄧㄠˋ", "Gülmek", "To laugh / smile",
        "台灣人經常面帶微笑，讓人感覺十分親切溫暖。",
        1, "Easy", "Daily Actions", "😄",
        "Reír / Sonreír", "Lachen / Lächeln", "Rire / Sourire", "Ridere / Sorridere", "笑う", "웃다", "Rir / Sorrir", "हंसना / मुस्कुराना",
        "gül", "smile",
        "笑話", "xiào huà", "ㄒㄧㄠˋ ㄏㄨㄚˋ", "🤣", "Fıkra / Şaka", "joke",
        "大家開心地笑", "dà jiā kāi xīn de xiào", "ㄉㄚˋ ㄐㄧㄚ ㄎㄞ ㄒㄧㄣ ˙ㄉㄜ ㄒㄧㄠˋ",
        "Herkes neşeyle gülüyor", "Everyone is laughing happily"
    ],
    # 2. 哭
    [
        "v_ku", "哭", "kū", "ㄎㄨ", "Ağlamak", "To cry",
        "看感人的台灣電影《海角七號》時，很多觀眾都哭了。",
        1, "Easy", "Daily Actions", "😢",
        "Llorar", "Weinen", "Pleurer", "Piangere", "泣く", "울다", "Chorar", "रोना",
        "ağla", "cry",
        "眼淚", "yǎn lèi", "ㄧㄢˇ ㄌㄟˋ", "💧", "Gözyaşı", "tears",
        "小孩子在哭", "xiǎo hái zi zài kū", "ㄒㄧㄠˇ ㄏㄞˊ ˙ㄗ ㄗㄞˋ ㄎㄨ",
        "Küçük çocuk ağlıyor", "The child is crying"
    ],
    # 3. 生氣
    [
        "v_shengqi", "生氣", "shēng qì", "ㄕㄥ ㄑㄧˋ", "Kızmak / Öfkelenmek", "To get angry",
        "遇到不合理的事情不要生氣，理智溝通最有效。",
        1, "Easy", "Daily Actions", "😡",
        "Enojarse", "Wütend werden", "Se fâcher", "Arrabbiarsi", "怒る", "화내다", "Zangar-se", "गुस्सा होना",
        "kız", "get angry",
        "原因", "yuán yīn", "ㄩㄢˊ ㄧㄣ", "💢", "Neden", "reason",
        "請不要生氣", "qǐng bú yào shēng qì", "ㄑㄧㄥˇ ㄅㄨˊ ㄧㄠˋ ㄕㄥ ㄑㄧˋ",
        "Lütfen kızmayın", "Please don't get angry"
    ],
    # 4. 擔心
    [
        "v_danxin", "擔心", "dān xīn", "ㄉㄢ ㄒㄧㄣ", "Endişelenmek", "To worry",
        "出門在外要注意安全，不要讓父母擔心。",
        1, "Easy", "Daily Actions", "😟",
        "Preocuparse", "Sich Sorgen machen", "S'inquiéter", "Preoccuparsi", "心配する", "걱정하다", "Preocupar-se", "चिंता करना",
        "endişelen", "worry",
        "安全", "ān quán", "ㄢ ㄑㄩㄢˊ", "🛡️", "Güvenlik", "safety",
        "別擔心，一切順利", "bié dān xīn, yí qiè shùn lì", "ㄅㄧㄝˊ ㄉㄢ ㄒㄧㄣ，ㄧˊ ㄑㄧㄝˋ ㄕㄨㄣˋ ㄌㄧˋ",
        "Endişelenme, her şey yolunda", "Don't worry, everything is going smoothly"
    ],
    # 5. 害怕
    [
        "v_haipa", "害怕", "hài pà", "ㄏㄞˋ ㄆㄚˋ", "Korkmak", "To be afraid",
        "走在夜市人潮眾多很熱鬧，完全不用害怕。",
        1, "Easy", "Daily Actions", "😨",
        "Tener miedo", "Angst haben", "Avoir peur", "Avere paura", "恐れる", "무서워하다", "Ter medo", "डरना",
        "kork", "fear",
        "黑暗", "hēi àn", "ㄏㄟ ㄢˋ", "🌑", "Karanlık", "darkness",
        "他害怕打雷", "tā hài pà dǎ léi", "ㄊㄚ ㄏㄞˋ ㄆㄚˋ ㄉㄚˇ ㄌㄟˊ",
        "O gök gürültüsünden korkar", "He is afraid of thunder"
    ],
    # 6. 緊張
    [
        "v_jinzhang", "緊張", "jǐn zhāng", "ㄐㄧㄣˇ ㄓㄤ", "Gerilmek / Heyecanlanmak", "To be nervous",
        "上台做中文簡報時，深呼吸可以減輕緊張。",
        2, "Easy", "Daily Actions", "😰",
        "Ponerse nervioso", "Nervös sein", "Être nerveux", "Essere nervoso", "緊張する", "긴장하다", "Ficar nervoso", "घबराना",
        "heyecanlan", "be nervous",
        "考試", "kǎo shì", "ㄎㄠˇ ㄕˋ", "📝", "Sınav", "exam",
        "考試前我很緊張", "kǎo shì qián wǒ hěn jǐn zhāng", "ㄎㄠˇ ㄕˋ ㄑㄧㄢˊ ㄨㄛˇ ㄏㄣˇ ㄐㄧㄣˇ ㄓㄤ",
        "Sınavdan önce çok gerginim", "I am very nervous before the exam"
    ],
    # 7. 放鬆
    [
        "v_fangsong", "放鬆", "fàng sōng", "ㄈㄤˋ ㄙㄨㄥ", "Rahatlamak / Gevşemek", "To relax",
        "週末到北投泡溫泉是放鬆身心最好的方式。",
        2, "Easy", "Daily Actions", "🧘",
        "Relajarse", "Sich entspannen", "Se détendre", "Rilassarsi", "リラックスする", "긴장을 풀다", "Relaxar", "आराम करना",
        "rahatla", "relax",
        "心情", "xīn qíng", "ㄒㄧㄣ ㄑㄧㄥˊ", "🍃", "Ruh hali", "mood",
        "放鬆心情聽音樂", "fàng sōng xīn qíng tīng yīn yuè", "ㄈㄤˋ ㄙㄨㄥ ㄒㄧㄣ ㄑㄧㄥˊ ㄊㄧㄥ ㄧㄣ ㄩㄝˋ",
        "Müzik dinleyerek ruh halini rahatlatmak", "Relax your mood listening to music"
    ],
    # 8. 放心
    [
        "v_fangxin", "放心", "fàng xīn", "ㄈㄤˋ ㄒㄧㄣ", "İçi rahat etmek", "To feel relieved / assured",
        "台灣治安良好，晚上獨自散步也能很放心。",
        1, "Easy", "Daily Actions", "😌",
        "Estar tranquilo", "Beruhigt sein", "Être rassuré", "Stare tranquillo", "安心する", "안심하다", "Ficar tranquilo", "निश्चिंत होना",
        "içi rahat et", "feel assured",
        "事情", "shì qíng", "ㄕˋ ㄑㄧㄥˊ", "✔️", "Durum", "matter",
        "你可以放心交給我", "nǐ kě yǐ fàng xīn jiāo gěi wǒ", "ㄋㄧˇ ㄎㄜˇ ㄧˇ ㄈㄤˋ ㄒㄧㄣ ㄐㄧㄠ ㄍㄟˇ ㄨㄛˇ",
        "Gönül rahatlığıyla bana bırakabilirsin", "You can rest assured and leave it to me"
    ],
    # 9. 傷心
    [
        "v_shangxin", "傷心", "shāng xīn", "ㄕㄤ ㄒㄧㄣ", "Üzülmek", "To feel sad / heartbroken",
        "失落時有朋友陪在身邊，就不會那麼傷心了。",
        2, "Easy", "Daily Actions", "💔",
        "Estar triste", "Traurig sein", "Être triste", "Essere triste", "悲しむ", "슬퍼하다", "Ficar triste", "दुखी होना",
        "üzül", "feel sad",
        "事情", "shì qíng", "ㄕˋ ㄑㄧㄥˊ", "🌧️", "Olay", "matter",
        "別為這件事傷心", "bié wèi zhè jiàn shì shāng xīn", "ㄅㄧㄝˊ ㄨㄟˋ ㄓㄜˋ ㄐㄧㄢˋ ㄕˋ ㄕㄤ ㄒㄧㄣ",
        "Bu olay için üzülme", "Don't feel sad over this matter"
    ],
    # 10. 失望
    [
        "v_shiwang", "失望", "shī wàng", "ㄕ ㄨㄤˋ", "Hayal kırıklığına uğramak", "To be disappointed",
        "夜市的美食從來不會讓人失望，樣樣精緻可口。",
        2, "Easy", "Daily Actions", "😞",
        "Decepcionarse", "Enttäuscht sein", "Être déçu", "Rimanere deluso", "失望する", "실망하다", "Ficar desapontado", "निराश होना",
        "hayal kırıklığına uğra", "be disappointed",
        "結果", "jié guǒ", "ㄐㄧㄝˊ ㄍㄨㄛˇ", "📉", "Sonuç", "result",
        "我對比賽結果很失望", "wǒ duì bǐ sài jié guǒ hěn shī wàng", "ㄨㄛˇ ㄉㄨㄟˋ ㄅㄧˇ ㄙㄞˋ ㄐㄧㄝˊ ㄍㄨㄛˇ ㄏㄣˇ ㄕ ㄨㄤˋ",
        "Maçın sonucundan dolayı çok hayal kırıklığına uğradım", "I am very disappointed with the match result"
    ],
    # 11. 滿意
    [
        "v_manyi", "滿意", "mǎn yì", "ㄇㄢˇ ㄧˋ", "Memnun kalmak", "To be satisfied",
        "客人都對這次台灣環島旅行的安排感到非常滿意。",
        2, "Easy", "Daily Actions", "😊",
        "Estar satisfecho", "Zufrieden sein", "Être satisfait", "Essere soddisfatto", "満足する", "만족하다", "Estar satisfeito", "संतुष्ट होना",
        "memnun kal", "be satisfied",
        "服務", "fú wù", "ㄈㄨˊ ㄨˋ", "⭐", "Hizmet", "service",
        "我們對服務很滿意", "wǒ men duì fú wù hěn mǎn yì", "ㄨㄛˇ ㄇㄣ˙ ㄉㄨㄟˋ ㄈㄨˊ ㄨˋ ㄏㄣˇ ㄇㄢˇ ㄧˋ",
        "Hizmetten çok memnunuz", "We are very satisfied with the service"
    ],
    # 12. 期待
    [
        "v_qidai", "期待", "qí dài", "ㄑㄧˊ ㄉㄞˋ", "Dört gözle beklemek", "To look forward to",
        "我很期待下週去墾丁看海渡假。",
        2, "Easy", "Daily Actions", "🤩",
        "Esperar con ilusión", "Sich freuen auf", "Attendre avec impatience", "Non vedere l'ora", "楽しみに待つ", "기대하다", "Aguardar com expectativa", "उत्सुकता से प्रतीक्षा करना",
        "dört gözle bekle", "look forward to",
        "假期", "jià qī", "ㄐㄧㄚˋ ㄑㄧ", "🏖️", "Tatil", "vacation",
        "我們非常期待假期", "wǒ men fēi cháng qí dài jià qī", "ㄨㄛˇ ㄇㄣ˙ ㄈㄟ ㄔㄤˊ ㄑㄧˊ ㄉㄞˋ ㄐㄧㄚˋ ㄑㄧ",
        "Tatili dört gözle bekliyoruz", "We are looking forward to the holidays"
    ],
    # 13. 嫉妒
    [
        "v_jidu", "嫉妒", "jí dù", "ㄐㄧˊ ㄉㄨˋ", "Kıskanmak (haset)", "To envy / be jealous",
        "不要嫉妒別人的成功，要多學習對方的長處。",
        3, "Medium", "Daily Actions", "😒",
        "Tener celos / Envidiar", "Beneiden / Eifersüchtig sein", "Jalouser", "Essere geloso / Invidiare", "嫉妬する", "질투하다", "Ter ciúmes / Invejar", "ईर्ष्या करना",
        "kıskan", "envy",
        "才能", "cái néng", "ㄘㄞˊ ㄋㄥˊ", "✨", "Yetenek", "talent",
        "不必嫉妒別人的運氣", "bú bì jí dù bié rén de yùn qì", "ㄅㄨˊ ㄅㄧˋ ㄐㄧˊ ㄉㄨˋ ㄅㄧㄝˊ ㄖㄣˊ ˙ㄉㄜ ㄩㄣˋ ㄑㄧˋ",
        "Başkalarının şansını kıskanmaya gerek yok", "No need to envy other people's luck"
    ],
    # 14. 羨慕
    [
        "v_xianmu", "羨慕", "xiàn mù", "ㄒㄧㄢˋ ㄇㄨˋ", "İmrenmek", "To admire / envy positively",
        "看到外國朋友能講流利的台灣華語，大家都很羨慕。",
        2, "Easy", "Daily Actions", "😍",
        "Envidiar sanamente / Admirar", "Beneiden (positiv)", "Envier avec admiration", "Invidiare (positivamente)", "羨む", "부러워하다", "Invejar (positivamente)", "ईर्ष्या/सराहना करना",
        "imren", "admire",
        "生活", "shēng huó", "ㄕㄥ ㄏㄨㄛˊ", "🏖️", "Yaşam tarzı", "lifestyle",
        "我很羨慕他的生活", "wǒ hěn xiàn mù tā de shēng huó", "ㄨㄛˇ ㄏㄣˇ ㄒㄧㄢˋ ㄇㄨˋ ㄊㄚ ˙ㄉㄜ ㄕㄥ ㄏㄨㄛˊ",
        "Onun yaşamına çok imreniyorum", "I really admire his lifestyle"
    ],
    # 15. 佩服
    [
        "v_peifu", "佩服", "pèi fú", "ㄆㄟˋ ㄈㄨˊ", "Hayran kalmak / Takdir etmek", "To admire / respect",
        "他堅持每天晨跑十公里，毅力真令人佩服。",
        2, "Easy", "Daily Actions", "🫡",
        "Admirar", "Bewundern", "Admirer", "Ammirare", "感心する / 敬服する", "존경하다 / 감탄하다", "Admirar", "प्रशंसा करना",
        "hayran kal", "admire",
        "毅力", "yì lì", "ㄧˋ ㄌㄧˋ", "💪", "Azim", "willpower",
        "我深深佩服他的勇氣", "wǒ shēn shēn pèi fú tā de yǒng qì", "ㄨㄛˇ ㄕㄣ ㄕㄣ ㄆㄟˋ ㄈㄨˊ ㄊㄚ ˙ㄉㄜ ㄩㄥˇ ㄑㄧˋ",
        "Cesaretine derin bir hayranlık duyuyorum", "I deeply admire his courage"
    ],
    # 16. 懷疑
    [
        "v_huaiyi", "懷疑", "huái yí", "ㄏㄨㄞˊ ㄧˊ", "Şüphelenmek", "To doubt / suspect",
        "收到來路不明的可疑簡訊，要懷疑是否為詐騙。",
        2, "Easy", "Daily Actions", "🤨",
        "Dudar / Sospechar", "Zweifeln / Verdächtigen", "Douter / Suspecter", "Dubitare / Sospettare", "疑う", "의심하다", "Duvidar / Suspeitar", "संदेह करना",
        "şüphelen", "doubt",
        "動機", "dòng jī", "ㄉㄨㄥˋ ㄐㄧ", "❓", "Motif", "motive",
        "我懷疑這是一場騙局", "wǒ huái yí zhè shì yì chǎng piàn jú", "ㄨㄛˇ ㄏㄨㄞˊ ㄧˊ ㄓㄜˋ ㄕˋ ㄧˋ ㄔㄤˇ ㄆㄧㄢˋ ㄐㄩˊ",
        "Bunun bir aldatmaca olduğundan şüpheleniyorum", "I suspect this is a scam"
    ],
    # 17. 相信
    [
        "v_xiangxin", "相信", "xiāng xìn", "ㄒㄧㄤ ㄒㄧㄣˋ", "İnanmak", "To believe",
        "我相信只要付出努力，一定能在台灣找到好機會。",
        1, "Easy", "Daily Actions", "🤝",
        "Creer", "Glauben", "Croire", "Credere", "信じる", "믿다", "Acreditar", "विश्वास करना",
        "inan", "believe",
        "朋友", "péng yǒu", "ㄆㄥˊ ㄧㄡˇ", "👥", "Arkadaş", "friend",
        "我相信你的能力", "wǒ xiāng xìn nǐ de néng lì", "ㄨㄛˇ ㄒㄧㄤ ㄒㄧㄣˋ ㄋㄧˇ ˙ㄉㄜ ㄋㄥˊ ㄌㄧˋ",
        "Yeteneğine inanıyorum", "I believe in your ability"
    ],
    # 18. 信任
    [
        "v_xinren", "信任", "xìn rèn", "ㄒㄧㄣˋ ㄖㄣˋ", "Güvenmek", "To trust",
        "團隊成員之間彼此信任是合作成功的基石。",
        2, "Easy", "Daily Actions", "🔒",
        "Confiar", "Vertrauen", "Faire confiance", "Fidarsi", "信頼する", "신뢰하다", "Confiar", "भरोसा करना",
        "güven", "trust",
        "夥伴", "huǒ bàn", "ㄏㄨㄛˇ ㄅㄢˋ", "🤝", "Ortak", "partner",
        "我們完全信任彼此", "wǒ men wán quán xìn rèn bǐ cǐ", "ㄨㄛˇ ㄇㄣ˙ ㄨㄢˊ ㄑㄩㄢˊ ㄒㄧㄣˋ ㄖㄣˋ ㄅㄧˇ ㄘˇ",
        "Birbirimize tamamen güveniyoruz", "We completely trust each other"
    ],
    # 19. 猜
    [
        "v_cai", "猜", "cāi", "ㄘㄞ", "Tahmin etmek", "To guess",
        "元宵節在台灣廟宇有猜燈謎的傳統民俗活動。",
        1, "Easy", "Daily Actions", "🤔",
        "Adivinar", "Raten", "Deviner", "Indovinare", "当てる", "맞히다 / 추측하다", "Adivinhar", "अनुमान लगाना",
        "tahmin et", "guess",
        "答案", "dá àn", "ㄉㄚˊ ㄢˋ", "❓", "Cevap", "answer",
        "你猜猜看是誰", "nǐ cāi cai kàn shì shéi", "ㄋㄧˇ ㄘㄞ ˙ㄘㄞ ㄎㄢˋ ㄕˋ ㄕㄟˊ",
        "Tahmin et bakalım kim", "Guess who it is"
    ],
    # 20. 認為
    [
        "v_renwei", "認為", "rèn wéi", "ㄖㄣˋ ㄨㄟˊ", "Düşünmek / Zannetmek", "To think / consider",
        "我認為台灣的珍珠奶茶是全世界最好喝的。",
        1, "Easy", "Daily Actions", "💭",
        "Considerar / Opinar", "Meinen / Halten für", "Considérer / Penser", "Ritenere", "考える / 思う", "여기다 / 생각하다", "Considerar", "मानना / सोचना",
        "düşün", "consider",
        "看法", "kàn fǎ", "ㄎㄢˋ ㄈㄚˇ", "💡", "Görüş", "view",
        "我認為這個提議很好", "wǒ rèn wéi zhè ge tí yì hěn hǎo", "ㄨㄛˇ ㄖㄣˋ ㄨㄟˊ ㄓㄜˋ ˙ㄍㄜ ㄊㄧˊ ㄧˋ ㄏㄣˇ ㄏㄠˇ",
        "Bence bu öneri gayet iyi", "I consider this proposal very good"
    ],
    # 21. 感覺
    [
        "v_ganjue", "感覺", "gǎn jué", "ㄍㄢˇ ㄐㄩㄝˊ", "Hissetmek", "To feel / sense",
        "漫步在九份老街的山城，感覺像走進了童話世界。",
        1, "Easy", "Daily Actions", "✨",
        "Sentir", "Fühlen / Empfinden", "Sentir / Ressentir", "Sentire", "感じる", "느끼다", "Sentir", "महसूस करना",
        "hisset", "feel",
        "氣氛", "qì fēn", "ㄑㄧˋ ㄈㄣ", "🏮", "Atmosfer", "atmosphere",
        "我感覺非常舒服", "wǒ gǎn jué fēi cháng shū fú", "ㄨㄛˇ ㄍㄢˇ ㄐㄩㄝˊ ㄈㄟ ㄔㄤˊ ㄕㄨ ㄈㄨˊ",
        "Çok rahat hissediyorum", "I feel very comfortable"
    ],
    # 22. 體會
    [
        "v_tihui", "體會", "tǐ huì", "ㄊㄧˇ ㄏㄨㄟˋ", "Deneyimlemek / İdrak etmek", "To experience / realize",
        "親身在台灣生活一段時間，才能深刻體會人情味。",
        3, "Medium", "Culture & Society", "🧘",
        "Experimentar / Comprender", "Nachempfinden / Erfahren", "Ressentir profondément", "Comprendere appieno", "体験して理解する", "체득하다", "Experimentar profundamente", "अनुभव करना",
        "idrak et", "experience deeply",
        "人情味", "rén qíng wèi", "ㄖㄣˊ ㄑㄧㄥˊ ㄨㄟˋ", "❤️", "İnsani sıcaklık", "human warmth",
        "深刻體會當地的風土民情", "shēn kè tǐ huì dāng dì de fēng tǔ mín qíng", "ㄕㄣ ㄎㄜˋ ㄊㄧˇ ㄏㄨㄟˋ ㄉㄤ ㄉㄧˋ ˙ㄉㄜ ㄈㄥ ㄊㄨˇ ㄇㄧㄣˊ ㄑㄧㄥˊ",
        "Yerel adetleri ve insani sıcaklığı derinden idrak etmek", "Deeply experience local customs and traditions"
    ],
    # 23. 領悟
    [
        "v_lingwu", "領悟", "lǐng wù", "ㄌㄧㄥˇ ㄨˋ", "Kavramak / Aydınlanmak", "To comprehend / grasp",
        "經過多年練習書法，他終於領悟了筆法精髓。",
        3, "Medium", "Culture & Society", "💡",
        "Comprender / Intuir", "Begreifen / Erkennen", "Saisir / Réaliser", "Intuire / Cogliere", "悟る", "깨닫다", "Compreender", "आत्मसात करना",
        "kavra", "comprehend",
        "道理", "dào lǐ", "ㄉㄠˋ ㄌㄧˇ", "📜", "Hakikat / İlke", "truth",
        "他領悟了人生的哲理", "tā lǐng wù le rén shēng de zhé lǐ", "ㄊㄚ ㄌㄧㄥˇ ㄨˋ ˙ㄌㄜ ㄖㄣˊ ㄕㄥ ˙ㄉㄜ ㄓㄜˊ ㄌㄧˇ",
        "O hayatın felsefesini kavradı", "He comprehended the philosophy of life"
    ],
    # 24. 明白
    [
        "v_mingbai", "明白", "míng bai", "ㄇㄧㄥˊ ˙ㄅㄞ", "Anlamak / Açık olmak", "To understand / clear",
        "老師講解得很清楚，大家一聽就明白了。",
        1, "Easy", "Daily Actions", "💡",
        "Entender / Comprender", "Verstehen", "Comprendre", "Capire", "分かる / 理解する", "이해하다", "Entender", "समझना",
        "anla", "understand",
        "意思", "yì si", "ㄧˋ ㄙ˙", "📖", "Anlam", "meaning",
        "我明白你的意思了", "wǒ míng bai nǐ de yì si le", "ㄨㄛˇ ㄇㄧㄥˊ ˙ㄅㄞ ㄋㄧˇ ˙ㄉㄜ ㄧˋ ㄙ˙ ˙ㄌㄜ",
        "Ne demek istediğini anladım", "I understood what you mean"
    ],
    # 25. 懂
    [
        "v_dong", "懂", "dǒng", "ㄉㄨㄥˇ", "Anlamak / Bilmek", "To know / understand",
        "你懂這句台語俚語的意思嗎？",
        1, "Easy", "Daily Actions", "🧠",
        "Saber / Entender", "Verstehen / Können", "Comprendre / Savoir", "Intendersi di", "理解する", "알다 / 이해하다", "Entender", "समझना",
        "anla", "understand",
        "語言", "yǔ yán", "ㄩˇ ㄧㄢˊ", "🗣️", "Dil", "language",
        "他很懂台灣茶藝", "tā hěn dǒng tái wān chá yì", "ㄊㄚ ㄏㄣˇ ㄉㄨㄥˇ ㄊㄞˊ ㄨㄢ ㄔㄚˊ ㄧˋ",
        "O Tayvan çay sanatından çok iyi anlar", "He knows a lot about Taiwanese tea art"
    ],
    # 26. 記
    [
        "v_ji", "記", "jì", "ㄐㄧˋ", "Hatırlamak / Not etmek", "To remember / note down",
        "記單字要配合注音符號和例句，效果最好。",
        1, "Easy", "Education", "📝",
        "Recordar / Anotar", "Merken / Notieren", "Retenir / Noter", "Ricordare / Annotare", "覚える / 記録する", "기억하다 / 적다", "Lembrar / Anotar", "याद रखना",
        "hatırla", "remember",
        "單字", "dān zì", "ㄉㄢ ㄗˋ", "📖", "Kelime", "vocabulary",
        "我把重點記在筆記本上", "wǒ bǎ zhòng diǎn jì zài bǐ jì běn shàng", "ㄨㄛˇ ㄅㄚˇ ㄓㄨㄥˋ ㄉㄧㄢˇ ㄐㄧˋ ㄗㄞˋ ㄅㄧˇ ㄐㄧˋ ㄅㄣˇ ㄕㄤˋ",
        "Önemli noktaları deftere not ediyorum", "I note down key points in my notebook"
    ],
    # 27. 忘
    [
        "v_wang", "忘", "wàng", "ㄨㄤˋ", "Unutmak", "To forget",
        "出門搭公車前別忘了帶悠遊卡。",
        1, "Easy", "Daily Actions", "🤦",
        "Olvidar", "Vergessen", "Oublier", "Dimenticare", "忘れる", "잊다", "Esquecer", "भूलना",
        "unut", "forget",
        "鑰匙", "yào shi", "ㄧㄠˋ ˙ㄕ", "🔑", "Anahtar", "keys",
        "我差點忘了這件事", "wǒ chà diǎn wàng le zhè jiàn shì", "ㄨㄛˇ ㄔㄚˋ ㄉㄧㄢˇ ㄨㄤˋ ˙ㄌㄜ ㄓㄜˋ ㄐㄧㄢˋ ㄕˋ",
        "Neredeyse bu olayı unutuyordum", "I almost forgot this matter"
    ],
    # 28. 想念
    [
        "v_xiangnian", "想念", "xiǎng niàn", "ㄒㄧㄤˇ ㄋㄧㄢˋ", "Özlemek", "To miss someone",
        "在國外留學時，最想念的就是台灣的夜市小吃。",
        2, "Easy", "Daily Actions", "💭",
        "Extrañar", "Vermissen", "Manquer", "Sentire la mancanza", "恋しく思う", "그리워하다", "Sentir saudades", "याद करना",
        "özle", "miss",
        "家鄉", "jiā xiāng", "ㄐㄧㄚ ㄒㄧㄤ", "🏡", "Memleket", "hometown",
        "我很想念台灣的朋友", "wǒ hěn xiǎng niàn tái wān de péng yǒu", "ㄨㄛˇ ㄏㄣˇ ㄒㄧㄤˇ ㄋㄧㄢˋ ㄊㄞˊ ㄨㄢ ˙ㄉㄜ ㄆㄥˊ ㄧㄡˇ",
        "Tayvan'daki arkadaşlarımı çok özlüyorum", "I miss my Taiwanese friends very much"
    ],
    # 29. 懷念
    [
        "v_huainian", "懷念", "huái niàn", "ㄏㄨㄞˊ ㄋㄧㄢˋ", "Yad etmek / Özlemle anmak", "To cherish memory of",
        "長大後常常懷念小時候在阿嬤家的純樸時光。",
        2, "Easy", "Daily Actions", "🕰️",
        "Añorar", "Zurückdenken an", "Avoir la nostalgie de", "Rimpiangere", "懐かしむ", "그리워하다", "Sentir nostalgia", "यादों को संजोना",
        "yad et", "cherish memory",
        "童年", "tóng nián", "ㄊㄨㄥˊ ㄋㄧㄢˊ", "🪁", "Çocukluk", "childhood",
        "大家都很懷念過去的美好時光", "dà jiā dōu hěn huái niàn guò qù de měi hǎo shí guāng", "ㄉㄚˋ ㄐㄧㄚ ㄉㄡ ㄏㄣˇ ㄏㄨㄞˊ ㄋㄧㄢˋ ㄍㄨㄛˋ ㄑㄩˋ ˙ㄉㄜ ㄇㄟˇ ㄏㄠˇ ㄕˊ ㄍㄨㄤ",
        "Herkes geçmişteki güzel günleri özlemle anıyor", "Everyone cherishes the good old times"
    ],
    # 30. 猶豫
    [
        "v_youyu", "猶豫", "yóu yù", "ㄧㄡˊ ㄩˋ", "Tereddüt etmek", "To hesitate",
        "夜市美食琳瑯滿目，常常讓人猶豫不知道該先吃哪一樣。",
        2, "Easy", "Daily Actions", "🤷",
        "Dudar / Vacilar", "Zögern", "Hésiter", "Esitare", "躊躇する", "망설이다", "Hesitar", "संकोच करना",
        "tereddüt et", "hesitate",
        "選擇", "xuǎn zé", "ㄒㄩㄢˇ ㄗㄜˊ", "⚖️", "Seçim", "choice",
        "不要猶豫，趕快做決定", "bú yào yóu yù, gǎn kuài zuò jué dìng", "ㄅㄨˊ ㄧㄠˋ ㄧㄡˊ ㄩˋ，ㄍㄢˇ ㄎㄨㄞˋ ㄗㄨㄛˋ ㄐㄩㄝˊ ㄉㄧㄥˋ",
        "Tereddüt etme, hemen karar ver", "Don't hesitate, make a decision quickly"
    ],
    # 31. 決定
    [
        "v_jueding", "決定", "jué dìng", "ㄐㄩㄝˊ ㄉㄧㄥˋ", "Karar vermek", "To decide",
        "我決定明年春天去阿里山看櫻花和日出。",
        1, "Easy", "Daily Actions", "🎯",
        "Decidir", "Entscheiden", "Décider", "Decidere", "決める", "결정하다", "Decidir", "निर्णय लेना",
        "karar ver", "decide",
        "計畫", "jì huà", "ㄐㄧˋ ㄏㄨㄚˋ", "📅", "Plan", "plan",
        "我們決定出發", "wǒ men jué dìng chū fā", "ㄨㄛˇ ㄇㄣ˙ ㄐㄩㄝˊ ㄉㄧㄥˋ ㄔㄨ ㄈㄚ",
        "Yola çıkmaya karar verdik", "We decided to set off"
    ],
    # 32. 選擇
    [
        "v_xuanze", "選擇", "xuǎn zé", "ㄒㄩㄢˇ ㄗㄜˊ", "Seçmek / Tercih etmek", "To choose / select",
        "在台灣飲料店買茶，可以自選糖度與冰塊。",
        1, "Easy", "Daily Actions", "☑️",
        "Elegir / Seleccionar", "Wählen", "Choisir", "Scegliere", "選択する", "선택하다", "Escolher", "चुनना",
        "seç", "choose",
        "甜度", "tián dù", "ㄊㄧㄢˊ ㄉㄨˋ", "🧋", "Tatlılık derecesi", "sweetness",
        "我選擇微糖微冰", "wǒ xuǎn zé wéi táng wéi bīng", "ㄨㄛˇ ㄒㄩㄢˇ ㄗㄜˊ ㄨㄟˊ ㄊㄤˊ ㄨㄟˊ ㄅㄧㄥ",
        "Az şeker ve az buzu seçiyorum", "I choose low sugar and light ice"
    ],
    # 33. 堅持
    [
        "v_jianchi", "堅持", "jiān chí", "ㄐㄧㄢ ㄔˊ", "Israr etmek / Azmetmek", "To persist",
        "許多老店堅持使用傳統手工製法，保持原汁原味。",
        2, "Easy", "Daily Actions", "🧗",
        "Persistir / Insistir", "Beharren / Durchhalten", "Persister", "Insistere / Perseverare", "堅持する", "고수하다", "Persistir", "डटे रहना",
        "ısrar et", "persist",
        "品質", "pǐn zhí", "ㄆㄧㄣˇ ㄓˊ", "⭐", "Kalite", "quality",
        "老店堅持純手工製作", "lǎo diàn jiān chí chún shǒu gōng zhì zuò", "ㄌㄠˇ ㄉㄧㄢˋ ㄐㄧㄢ ㄔˊ ㄔㄨㄣˊ ㄕㄡˇ ㄍㄨㄥ ㄓˋ ㄗㄨㄛˋ",
        "Tarihi dükkan tamamen el yapımı üretimde ısrar ediyor", "The heritage shop insists on pure handmade production"
    ],
    # 34. 放棄
    [
        "v_fangqi", "放棄", "fàng qì", "ㄈㄤˋ ㄑㄧˋ", "Vazgeçmek", "To give up",
        "學語言雖然有挑戰，但絕不要輕易放棄。",
        2, "Easy", "Daily Actions", "🏳️",
        "Rendirse / Abandonar", "Aufgeben", "Abandonner", "Arrendersi", "諦める", "포기하다", "Desistir", "हार मानना",
        "vazgeç", "give up",
        "機會", "jī huì", "ㄐㄧ ㄏㄨㄟˋ", "🚪", "Fırsat", "opportunity",
        "不要輕易放棄希望", "bú yào qīng yì fàng qì xī wàng", "ㄅㄨˊ ㄧㄠˋ ㄑㄧㄥ ㄧˋ ㄈㄤˋ ㄑㄧˋ ㄒㄧ ㄨㄤˋ",
        "Umudundan kolayca vazgeçme", "Don't give up hope easily"
    ],
    # 35. 挑
    [
        "v_tiao", "挑", "tiāo", "ㄊㄧㄠ", "Seçmek / Ayıklamak", "To pick / choose",
        "在台灣傳統水果攤，老闆會幫你挑最甜的芒果。",
        1, "Easy", "Shopping", "🧺",
        "Escoger", "Aussuchen", "Choisir / Trier", "Scegliere", "選ぶ", "고르다", "Escolher", "चुनना",
        "seç", "pick",
        "水果", "shuǐ guǒ", "ㄕㄨㄟˇ ㄍㄨㄛˇ", "🥭", "Meyve", "fruit",
        "我幫你挑一顆西瓜", "wǒ bāng nǐ tiāo yì kē xī guā", "ㄨㄛˇ ㄅㄤ ㄋㄧˇ ㄊㄧㄠ ㄧˋ ㄎㄜ ㄒㄧ ㄍㄨㄚ",
        "Sana bir karpuz seçeyim", "Let me pick a watermelon for you"
    ],
    # 36. 選
    [
        "v_xuan", "選", "xuǎn", "ㄒㄩㄢˇ", "Seçmek", "To select",
        "菜單上這麼多美味小吃，真不知道該選哪一種。",
        1, "Easy", "Daily Actions", "🔘",
        "Seleccionar", "Auswählen", "Sélectionner", "Selezionare", "選定する", "선택하다", "Selecionar", "चयन करना",
        "seç", "select",
        "座位", "zuò wèi", "ㄗㄨㄛˋ ㄨㄟˋ", "💺", "Koltuk", "seat",
        "請選一個喜歡的位子", "qǐng xuǎn yí ge xǐ huān de wèi zi", "ㄑㄧㄥˇ ㄒㄩㄢˇ ㄧˊ ˙ㄍㄜ ㄒㄧˇ ㄏㄨㄢ ˙ㄉㄜ ㄨㄟˋ ˙ㄗ",
        "Lütfen beğendiğiniz bir koltuk seçiniz", "Please select a seat you like"
    ],
    # 37. 試
    [
        "v_shi", "試", "shì", "ㄕˋ", "Denemek", "To try",
        "沒吃過臭豆腐的話，一定要試試看台灣的炸臭豆腐！",
        1, "Easy", "Daily Actions", "🥄",
        "Probar", "Probieren", "Essayer", "Provare", "試す", "시도하다", "Provar", "कोशिश करना",
        "dene", "try",
        "味道", "wèi dào", "ㄨㄟˋ ㄉㄠˋ", "🍜", "Tat", "flavor",
        "我想試試看這個口味", "wǒ xiǎng shì shi kàn zhè ge kǒu wèi", "ㄨㄛˇ ㄒㄧㄤˇ ㄕˋ ˙ㄕ ㄎㄢˋ ㄓㄜˋ ˙ㄍㄜ ㄎㄡˇ ㄨㄟˋ",
        "Bu lezzeti denemek istiyorum", "I want to try this flavor"
    ],
    # 38. 付款
    [
        "v_fukuan", "付款", "fù kuǎn", "ㄈㄨˋ ㄎㄨㄢˇ", "Ödeme yapmak", "To pay / make payment",
        "在台灣很多商家支援悠遊卡或Line Pay行動付款。",
        1, "Easy", "Shopping", "💳",
        "Pagar", "Bezahlen", "Payer", "Pagare", "支払う", "결제하다", "Pagar", "भुगतान करना",
        "ödeme yap", "pay",
        "帳單", "zhàng dān", "ㄓㄤˋ ㄉㄢ", "🧾", "Fatura / Hesap", "bill",
        "請到櫃台付款", "qǐng dào guì tái fù kuǎn", "ㄑㄧㄥˇ ㄉㄠˋ ㄍㄨㄟˋ ㄊㄞˊ ㄈㄨˋ ㄎㄨㄢˇ",
        "Lütfen kasada ödeme yapınız", "Please pay at the counter"
    ],
    # 39. 轉帳
    [
        "v_zhuanzhang", "轉帳", "zhuǎn zhàng", "ㄓㄨㄢˇ ㄓㄤˋ", "Havale / EFT yapmak", "To transfer funds",
        "台灣的超商ATM和手機網銀隨時都能跨行轉帳。",
        2, "Easy", "Finance", "📲",
        "Transferir dinero", "Überweisen", "Effectuer un virement", "Fare un bonifico", "振込する", "계좌이체하다", "Fazer transferência", "पैसे ट्रांसफर करना",
        "havale yap", "transfer funds",
        "金額", "jīn é", "ㄐㄧㄣ ㄜˊ", "💰", "Meblağ", "amount",
        "我用手機轉帳給你", "wǒ yòng shǒu jī zhuǎn zhàng gěi nǐ", "ㄨㄛˇ ㄩㄥˋ ㄕㄡˇ ㄐㄧ ㄓㄨㄢˇ ㄓㄤˋ ㄍㄟˇ ㄋㄧˇ",
        "Sana telefondan havale yapıyorum", "I transfer money to you using mobile banking"
    ],
    # 40. 存錢
    [
        "v_cunqian", "存錢", "cún qián", "ㄘㄨㄣˊ ㄑㄧㄢˊ", "Para biriktirmek / yatırmak", "To save / deposit money",
        "從小養成存錢的習慣，有助於未來實現理財目標。",
        1, "Easy", "Finance", "🏦",
        "Ahorrar / Depositar", "Sparen / Einzahlen", "Épargner / Déposer", "Risparmiare", "貯金する", "저금하다", "Poupar", "बचत करना",
        "para biriktir", "save money",
        "銀行", "yín háng", "ㄧㄣˊ ㄏㄤˊ", "🏛️", "Banka", "bank",
        "我把薪水存進銀行", "wǒ bǎ xīn shuǐ cún jìn yín háng", "ㄨㄛˇ ㄅㄚˇ ㄒㄧㄣ ㄕㄨㄟˇ ㄘㄨㄣˊ ㄐㄧㄣˋ ㄧㄣˊ ㄏㄤˊ",
        "Maaşımı bankaya yatırıyorum", "I deposit my salary into the bank"
    ],
    # 41. 領錢
    [
        "v_lingqian", "領錢", "lǐng qián", "ㄌㄧㄥˇ ㄑㄧㄢˊ", "Para çekmek", "To withdraw money",
        "在台灣的7-Eleven或全家便利商店到處都能領錢。",
        1, "Easy", "Finance", "🏧",
        "Retirar dinero", "Geld abheben", "Retirer de l'argent", "Prelevare denaro", "お金を引き出す", "돈을 찾다", "Sacar dinheiro", "पैसे निकालना",
        "para çek", "withdraw money",
        "現金", "xiàn jīn", "ㄒㄧㄢˋ ㄐㄧㄣ", "💵", "Nakit", "cash",
        "我去ATM領錢", "wǒ qù ATM lǐng qián", "ㄨㄛˇ ㄑㄩˋ ATM ㄌㄧㄥˇ ㄑㄧㄢˊ",
        "ATM'den para çekmeye gidiyorum", "I go to the ATM to withdraw money"
    ],
    # 42. 借錢
    [
        "v_jieqian", "借錢", "jiè qián", "ㄐㄧㄝˋ ㄑㄧㄢˊ", "Borç almak", "To borrow money",
        "朋友相處談錢傷感情，盡量不要向朋友借錢。",
        1, "Easy", "Finance", "🤝",
        "Pedir prestado", "Geld leihen", "Emprunter de l'argent", "Chiedere un prestito", "金を借りる", "돈을 빌리다", "Pedir dinheiro emprestado", "पैसे उधार लेना",
        "borç al", "borrow money",
        "朋友", "péng yǒu", "ㄆㄥˊ ㄧㄡˇ", "👤", "Arkadaş", "friend",
        "他向銀行借錢買房", "tā xiàng yín háng jiè qián mǎi fáng", "ㄊㄚ ㄒㄧㄤˋ ㄧㄣˊ ㄏㄤˊ ㄐㄧㄝˋ ㄑㄧㄢˊ ㄇㄞˇ ㄈㄤˊ",
        "Ev almak için bankadan borç aldı", "He borrowed money from the bank to buy a house"
    ],
    # 43. 還錢
    [
        "v_huanqian", "還錢", "huán qián", "ㄏㄨㄢˊ ㄑㄧㄢˊ", "Borç ödemek / geri vermek", "To repay money",
        "有借有還，再借不難，欠錢一定要準時還錢。",
        1, "Easy", "Finance", "💸",
        "Devolver dinero", "Geld zurückzahlen", "Rembourser", "Restituire denaro", "金を返す", "돈을 갚다", "Pagar a dívida", "पैसे लौटाना",
        "borç öde", "repay money",
        "債務", "zhài wù", "ㄓㄞˋ ㄨˋ", "📜", "Borç", "debt",
        "我下個月一定還錢", "wǒ xià ge yuè yí dìng huán qián", "ㄨㄛˇ ㄒㄧㄚˋ ˙ㄍㄜ ㄩㄝˋ ㄧˊ ㄉㄧㄥˋ ㄏㄨㄢˊ ㄑㄧㄢˊ",
        "Gelecek ay mutlaka borcumu öderim", "I will definitely repay the money next month"
    ],
    # 44. 殺價
    [
        "v_shajia", "殺價", "shā jià", "ㄕㄚ ㄐㄧㄚˋ", "Pazarlık etmek", "To bargain / haggle",
        "在台灣各大百貨和超商都是公定價，但五分埔批發街可以殺價。",
        2, "Easy", "Shopping", "🏷️",
        "Regatear", "Feilschen", "Marchander", "Mercanteggiare", "値切る", "가격을 깎다", "Pechinchar", "मोलभाव करना",
        "pazarlık et", "bargain",
        "價格", "jià gé", "ㄐㄧㄚˋ ㄍㄜˊ", "💰", "Fiyat", "price",
        "買衣服時可以適度殺價", "mǎi yī fú shí kě yǐ shì dù shā jià", "ㄇㄞˇ ㄧ ㄈㄨˊ ㄕˊ ㄎㄜˇ ㄧˇ ㄕˋ ㄉㄨˋ ㄕㄚ ㄐㄧㄚˋ",
        "Kıyafet alırken ölçülü pazarlık yapılabilir", "You can haggle moderately when buying clothes"
    ],
    # 45. 打折
    [
        "v_dazhe", "打折", "dǎ zhé", "ㄉㄚˇ ㄓㄜˊ", "İndirim yapmak", "To give a discount",
        "百貨公司週年慶期間，專櫃常常打八折或滿千送百。",
        1, "Easy", "Shopping", "🏷️",
        "Hacer descuento", "Rabatt gewähren", "Faire une réduction", "Fare uno sconto", "割引する", "할인하다", "Dar desconto", "छूट देना",
        "indirim yap", "discount",
        "商品", "shāng pǐn", "ㄕㄤ ㄆㄧㄣˇ", "🛍️", "Ürün", "goods",
        "這件商品今天打八折", "zhè jiàn shāng pǐn jīn tiān dǎ bā zhé", "ㄓㄜˋ ㄐㄧㄢˋ ㄕㄤ ㄆㄧㄣˇ ㄐㄧㄣ ㄊㄧㄢ ㄉㄚˇ ㄅㄚ ㄓㄜˊ",
        "Bu ürün bugün yüzde 20 indirimli", "This item has a 20% discount today"
    ],
    # 46. 退費
    [
        "v_tuifei", "退費", "tuì fèi", "ㄊㄨㄟˋ ㄈㄟˋ", "İade almak / Para iadesi", "To refund",
        "活動因颱風取消，主辦單位會全額退費。",
        2, "Easy", "Finance", "💵",
        "Reembolsar", "Erstatten", "Rembourser", "Rimborsare", "返金する", "환불하다", "Reembolsar", "धनवापसी करना",
        "iade al", "refund",
        "費用", "fèi yòng", "ㄈㄟˋ ㄩㄥˋ", "💰", "Ücret", "expenses",
        "店家辦理全額退費", "diàn jiā bàn lǐ quán é tuì fèi", "ㄉㄧㄢˋ ㄐㄧㄚ ㄅㄢˋ ㄌㄧˇ ㄑㄩㄢˊ ㄜˊ ㄊㄨㄟˋ ㄈㄟˋ",
        "Dükkan tam para iadesi yaptı", "The store processed a full refund"
    ],
    # 47. 兌換
    [
        "v_duihuan", "兌換", "duì huàn", "ㄉㄨㄟˋ ㄏㄨㄢˋ", "Bozdurmak / Takas etmek", "To exchange / redeem",
        "全家和7-11累積的會員點數，可以兌換咖啡和零食。",
        2, "Easy", "Shopping", "🔄",
        "Canjear", "Umtauschen / Einlösen", "Échanger / Convertir", "Convertire / Riscattare", "引き換える", "교환하다", "Trocar / Resgatar", "बदलना",
        "takas et", "redeem",
        "贈品", "zèng pǐn", "ㄗㄥˋ ㄆㄧㄣˇ", "🎁", "Hediye ürün", "gift",
        "累積點數兌換咖啡", "lěi jī diǎn shù duì huàn kā fēi", "ㄌㄟˇ ㄐㄧ ㄉㄧㄢˇ ㄕㄨˋ ㄉㄨㄟˋ ㄏㄨㄢˋ ㄎㄚ ㄈㄟ",
        "Puan biriktirip kahveye dönüştürmek", "Accumulate points to redeem coffee"
    ],
    # 48. 捐
    [
        "v_juan", "捐", "juān", "ㄐㄧㄢ", "Bağışlamak", "To donate",
        "在台灣結帳時，很多人習慣把統一發票捐給慈善團體。",
        1, "Easy", "Culture & Society", "❤️",
        "Donar", "Spenden", "Donner", "Donare", "寄付する", "기부하다", "Doar", "दान करना",
        "bağışla", "donate",
        "發票", "fā piào", "ㄈㄚ ㄆㄧㄠˋ", "🧾", "Fiş / Fatura", "receipt",
        "順手捐發票做愛心", "shùn shǒu juān fā piào zuò ài xīn", "ㄕㄨㄣˋ ㄕㄡˇ ㄐㄩㄢ ㄈㄚ ㄆㄧㄠˋ ㄗㄨㄛˋ ㄞˋ ㄒㄧㄣ",
        "Sevgiyle fişleri bağışlamak", "Donate receipts to do charity"
    ],
    # 49. 生病
    [
        "v_shengbing", "生病", "shēng bìng", "ㄕㄥ ㄅㄧㄥˋ", "Hastalanmak", "To fall ill",
        "生病時要多喝溫開水，按時休息才能早日康復。",
        1, "Easy", "Health", "🤒",
        "Enfermarse", "Krank werden", "Tomber malade", "Ammalarsi", "病気になる", "병나다", "Ficar doente", "बीमार पड़ना",
        "hastalan", "fall ill",
        "身體", "shēn tǐ", "ㄕㄣ ㄊㄧˇ", "🩺", "Vücut", "body",
        "他不小心生病了", "tā bù xiǎo xīn shēng bìng le", "ㄊㄚ ㄅㄨˋ ㄒㄧㄠˇ ㄒㄧㄣ ㄕㄥ ㄅㄧㄥˋ ˙ㄌㄜ",
        "O kazara hastalandı", "He accidentally fell ill"
    ],
    # 50. 看病
    [
        "v_kanbing", "看病", "kàn bìng", "ㄎㄢˋ ㄅㄧㄥˋ", "Doktora gitmek", "To see a doctor",
        "台灣全民健保制度完善，看病方便又便宜。",
        1, "Easy", "Health", "🏥",
        "Ir al médico", "Zum Arzt gehen", "Consulter un médecin", "Andare dal dottore", "診察を受ける", "진료를 받다", "Ir ao médico", "डॉक्टर को दिखाना",
        "doktora git", "see doctor",
        "醫生", "yī shēng", "ㄧ ㄕㄥ", "👨‍⚕️", "Doktor", "doctor",
        "拿健保卡去診所看病", "ná jiàn bǎo kǎ qù zhěn suǒ kàn bìng", "ㄋㄚˊ ㄐㄧㄢˋ ㄅㄠˇ ㄎㄚˇ ㄑㄩˋ ㄓㄣˇ ㄙㄨㄛˇ ㄎㄢˋ ㄅㄧㄥˋ",
        "Sağlık kartıyla kliniğe doktora gitmek", "Go to the clinic with health insurance card to see a doctor"
    ],
    # 51. 吃藥
    [
        "v_chiyao", "吃藥", "chī yào", "ㄔ ㄧㄠˋ", "İlaç içmek / almak", "To take medicine",
        "醫生開的感冒藥要三餐飯後按時吃藥。",
        1, "Easy", "Health", "💊",
        "Tomar medicina", "Medikamente einnehmen", "Prendre des médicaments", "Prendere medicine", "薬を飲む", "약을 먹다", "Tomar remédio", "दवा खाना",
        "ilaç iç", "take medicine",
        "藥品", "yào pǐn", "ㄧㄠˋ ㄆㄧㄣˇ", "💊", "İlaç", "medicine",
        "記得按時吃藥", "jì de àn shí chī yào", "ㄐㄧˋ ˙ㄉㄜ ㄢˋ ㄕˊ ㄔ ㄧㄠˋ",
        "İlaçlarını vaktinde almayı unutma", "Remember to take your medicine on time"
    ],
    # 52. 打針
    [
        "v_dazhen", "打針", "dǎ zhēn", "ㄉㄚˇ ㄓㄣ", "İğne olmak / aşı olmak", "To get an injection",
        "秋冬季節，台灣長者和幼童會定期打流感疫苗預防感冒。",
        1, "Easy", "Health", "💉",
        "Ponerse una inyección", "Eine Spritze bekommen", "Faire une piqûre", "Fare un'iniezione", "注射する", "주사를 맞다", "Tomar injeção", "सुई लगवाना",
        "iğne ol", "get injection",
        "疫苗", "yì miáo", "ㄧˋ ㄇㄧㄠˊ", "🧪", "Aşı", "vaccine",
        "小朋友害怕打針", "xiǎo péng yǒu hài pà dǎ zhēn", "ㄒㄧㄠˇ ㄆㄥˊ ㄧㄡˇ ㄏㄞˋ ㄆㄚˋ ㄉㄚˇ ㄓㄣ",
        "Çocuklar iğne olmaktan korkar", "Children are afraid of getting injections"
    ],
    # 53. 開刀
    [
        "v_kaidao", "開刀", "kāi dāo", "ㄎㄞ ㄉㄠ", "Ameliyat olmak / yapmak", "To undergo / perform surgery",
        "台灣醫療水準先進，許多重大開刀手術成功率極高。",
        2, "Easy", "Health", "🩺",
        "Operar / Operarse", "Operieren", "Opérer", "Operare", "手術する", "수술하다", "Operar", "ऑपरेशन करना",
        "ameliyat ol", "operate",
        "手術", "shǒu shù", "ㄕㄡˇ ㄕㄨˋ", "🏥", "Ameliyat", "surgery",
        "醫生成功完成開刀手術", "yī shēng chéng gōng wán chéng kāi dāo shǒu shù", "ㄧ ㄕㄥ ㄔㄥˊ ㄍㄨㄥ ㄨㄢˊ ㄔㄥˊ ㄎㄞ ㄉㄠ ㄕㄡˇ ㄕㄨˋ",
        "Doktor ameliyatı başarıyla tamamladı", "The doctor successfully completed the surgery"
    ],
    # 54. 復原
    [
        "v_fuyuan", "復原", "fù yuán", "ㄈㄨˋ ㄩㄢˊ", "İyileşmek / Toparlanmak", "To recover",
        "好好休養幾天，身體很快就能復原了。",
        2, "Easy", "Health", "🌱",
        "Recuperarse", "Genesen", "Récupérer", "Rimettersi / Guarire", "回復する", "회복하다", "Recuperar-se", "ठीक होना",
        "iyileş", "recover",
        "健康", "jiàn kāng", "ㄐㄧㄢˋ ㄎㄤ", "💪", "Sağlık", "health",
        "祝你早日復原", "zhù nǐ zǎo rì fù yuán", "ㄓㄨˋ ㄋㄧˇ ㄗㄠˇ ㄖˋ ㄈㄨˋ ㄩㄢˊ",
        "Geçmiş olsun, tez zamanda iyileşmeni dilerim", "Wish you a speedy recovery"
    ],
    # 55. 感染
    [
        "v_ganran", "感染", "gǎn rǎn", "ㄍㄢˇ ㄖㄢˇ", "Enfeksiyon kapmak", "To be infected",
        "傷口要保持清潔乾燥，避免細菌感染。",
        3, "Medium", "Health", "🦠",
        "Infectarse", "Sich infizieren", "S'infecter", "Infettarsi", "感染する", "감염되다", "Infetar-se", "संक्रमित होना",
        "enfeksiyon kap", "get infected",
        "病毒", "bìng dú", "ㄅㄧㄥˋ ㄉㄨˊ", "🔬", "Virüs", "virus",
        "小心避免傷口感染", "xiǎo xīn bì miǎn shāng kǒu gǎn rǎn", "ㄒㄧㄠˇ ㄒㄧㄣ ㄅㄧˋ ㄇㄧㄢˇ ㄕㄤ ㄎㄡˇ ㄍㄢˇ ㄖㄢˇ",
        "Yaranın mikrop kapmasını dikkatle önlemek", "Carefully prevent wound infection"
    ],
    # 56. 傳染
    [
        "v_chuanran", "傳染", "chuán rǎn", "ㄔㄨㄢˊ ㄖㄢˇ", "Bulaşmak / Bulaştırmak", "To transmit / infect",
        "感冒期間出門搭捷運戴口罩，防止傳染給他人。",
        2, "Easy", "Health", "😷",
        "Contagiar", "Übertragen / Anstecken", "Transmettre / Contaminer", "Contagiare", "伝染する", "전염되다", "Contagiar", "संक्रमण फैलाना",
        "bulaş", "transmit",
        "疾病", "jí bìng", "ㄐㄧˊ ㄅㄧㄥˋ", "⚠️", "Hastalık", "disease",
        "戴口罩防止疾病傳染", "dài kǒu zhào fáng zhǐ jí bìng chuán rǎn", "ㄉㄞˋ ㄎㄡˇ ㄓㄠˋ ㄈㄤˊ ㄓˇ ㄐㄧˊ ㄅㄧㄥˋ ㄔㄨㄢˊ ㄖㄢˇ",
        "Hastalık bulaşmasını önlemek için maske takmak", "Wear masks to prevent disease transmission"
    ],
    # 57. 消毒
    [
        "v_xiaodu", "消毒", "xiāo dú", "ㄒㄧㄠ ㄉㄨˊ", "Dezenfekte etmek", "To disinfect",
        "在台灣很多餐廳門口都會放酒精噴霧供顧客消毒雙手。",
        2, "Easy", "Health", "🧴",
        "Desinfectar", "Desinfizieren", "Désinfecter", "Disinfettare", "消毒する", "소독하다", "Desinfetar", "कीटाणुरहित करना",
        "dezenfekte et", "disinfect",
        "雙手", "shuāng shǒu", "ㄕㄨㄤ ㄕㄡˇ", "🤲", "Eller", "hands",
        "用餐前先用酒精消毒", "yòng cān qián xiān yòng jiǔ jīng xiāo dú", "ㄩㄥˋ ㄘㄢ ㄑㄧㄢˊ ㄒㄧㄢ ㄩㄥˋ ㄐㄧㄡˇ ㄐㄧㄥ ㄒㄧㄠ ㄉㄨˊ",
        "Yemekten önce elleri alkolle dezenfekte etmek", "Disinfect with alcohol before meals"
    ],
    # 58. 包紮
    [
        "v_baozha", "包紮", "bāo zā", "ㄅㄠ ㄗㄚ", "Sarmak / Pansuman yapmak", "To bandage / dress wound",
        "護理師動作輕巧熟練地幫受傷的同學包紮傷口。",
        2, "Easy", "Health", "🩹",
        "Vendar", "Verbinden", "Bander / Panser", "Fasciare", "包帯を巻く", "붕대를 감다", "Enfaixar", "पट्टी बांधना",
        "pansuman yap", "bandage",
        "傷口", "shāng kǒu", "ㄕㄤ ㄎㄡˇ", "🩹", "Yara", "wound",
        "護士幫忙包紮傷口", "hù shi bāng máng bāo zā shāng kǒu", "ㄏㄨˋ ˙ㄕ ㄅㄤ ㄇㄤˊ ㄅㄠ ㄗㄚ ㄕㄤ ㄎㄡˇ",
        "Hemşire yarayı sarmaya yardımcı oluyor", "The nurse helps bandage the wound"
    ],
    # 59. 量體溫
    [
        "v_liangtiwen", "量體溫", "liáng tǐ wēn", "ㄌㄧㄤˊ ㄊㄧˇ ㄨㄣ", "Ateş ölçmek", "To measure body temperature",
        "感到發冷頭暈時，第一件事就是拿出額溫槍量體溫。",
        1, "Easy", "Health", "🌡️",
        "Tomar la temperatura", "Fieber messen", "Prendre la température", "Misurare la febbre", "体温を測る", "체온을 재다", "Medir a temperatura", "तापमान मापना",
        "ateş ölç", "measure temperature",
        "額頭", "é tóu", "ㄜˊ ㄊㄡˊ", "👤", "Alın", "forehead",
        "進診所前先量體溫", "jìn zhěn suǒ qián xiān liáng tǐ wēn", "ㄐㄧㄣˋ ㄓㄣˇ ㄙㄨㄛˇ ㄑㄧㄢˊ ㄒㄧㄢ ㄌㄧㄤˊ ㄊㄧˇ ㄨㄣ",
        "Kliniğe girmeden önce ateş ölçtürmek", "Measure body temperature before entering clinic"
    ],
    # 60. 咳嗽
    [
        "v_kesou", "咳嗽", "ké sou", "ㄎㄜˊ ㄙㄡ˙", "Öksürmek", "To cough",
        "在公共場所咳嗽時，記得用紙巾掩住口鼻。",
        1, "Easy", "Health", "🗣️",
        "Toser", "Husten", "Tousser", "Tossire", "咳をする", "기침하다", "Tossir", "खांसना",
        "öksür", "cough",
        "喉嚨", "hóu lóng", "ㄏㄡˊ ㄌㄨㄥˊ", "🧣", "Boğaz", "throat",
        "他感冒一直咳嗽", "tā gǎn mào yì zhí ké sou", "ㄊㄚ ㄍㄢˇ ㄇㄠˋ ㄧˋ ㄓˊ ㄎㄜˊ ㄙㄡ˙",
        "O üşüttü ve durmadan öksürüyor", "He caught a cold and keeps coughing"
    ],
    # 61. 打噴嚏
    [
        "v_dapenti", "打噴嚏", "dǎ pēn tì", "ㄉㄚˇ ㄆㄣ ㄊㄧˋ", "Hapşırmak", "To sneeze",
        "台灣春天花開或空氣品質差時，過敏的人容易打噴嚏。",
        1, "Easy", "Health", "🤧",
        "Estornudar", "Niesen", "Éternuer", "Starnutire", "くしゃみをする", "재채기하다", "Espirrar", "छींकना",
        "hapşır", "sneeze",
        "鼻子", "bí zi", "ㄅㄧˊ ˙ㄗ", "👃", "Burun", "nose",
        "他對花粉過敏打噴嚏", "tā duì huā fěn guò mǐn dǎ pēn tì", "ㄊㄚ ㄉㄨㄟˋ ㄏㄨㄚ ㄈㄣˇ ㄍㄨㄛˋ ㄇㄧㄣˇ ㄉㄚˇ ㄆㄣ ㄊㄧˋ",
        "Polen alerjisinden dolayı hapşırıyor", "He sneezes due to pollen allergy"
    ],
    # 62. 發燒
    [
        "v_fashao", "發燒", "fā shāo", "ㄈㄚ ㄕㄠ", "Ateşlenmek", "To have a fever",
        "如果體溫超過38度就代表發燒，需要多補充水分並看醫生。",
        1, "Easy", "Health", "🌡️",
        "Tener fiebre", "Fieber haben", "Avoir de la fièvre", "Avere la febbre", "熱を出す", "열이 나다", "Ter febre", "बुखार होना",
        "ateşlen", "have a fever",
        "體溫", "tǐ wēn", "ㄊㄧˇ ㄨㄣ", "🔥", "Ateş", "temperature",
        "小寶寶半夜發燒了", "xiǎo bǎo bao bàn yè fā shāo le", "ㄒㄧㄠˇ ㄅㄠˇ ˙ㄅㄠ ㄅㄢˋ ㄧㄝˋ ㄈㄚ ㄕㄠ ˙ㄌㄜ",
        "Bebek gece yarısı ateşlendi", "The baby got a fever in the middle of the night"
    ],
    # 63. 受傷
    [
        "v_shoushang", "受傷", "shòu shāng", "ㄕㄡˋ ㄕㄤ", "Yaralanmak", "To be injured",
        "騎腳踏車或機車一定要戴安全帽，避免碰撞受傷。",
        1, "Easy", "Health", "🤕",
        "Herirse / Lesionarse", "Sich verletzen", "Se blesser", "Ferirsi", "怪我する", "다치다", "Ferir-se", "चोट लगना",
        "yaralan", "get injured",
        "腿部", "tuǐ bù", "ㄊㄨㄟˇ ㄅㄨˋ", "🦵", "Bacak", "leg",
        "打籃球不小心受傷", "dǎ lán qiú bù xiǎo xīn shòu shāng", "ㄉㄚˇ ㄌㄢˊ ㄑㄧㄡˊ ㄅㄨˋ ㄒㄧㄠˇ ㄒㄧㄣ ㄕㄡˋ ㄕㄤ",
        "Basketbol oynarken kazara yaralanmak", "Accidentally get injured while playing basketball"
    ],
    # 64. 流血
    [
        "v_liuxie", "流血", "liú xiě", "ㄌㄧㄡˊ ㄒㄧㄝˇ", "Kanamak", "To bleed",
        "切菜時如果不慎割到手流血，要先加壓止血。",
        1, "Easy", "Health", "🩸",
        "Sangrar", "Bluten", "Saigner", "Sanguinare", "出血する", "피가 나다", "Sangrar", "खून बहना",
        "kana", "bleed",
        "手指", "shǒu zhǐ", "ㄕㄡˇ ㄓˇ", "🖐️", "Parmak", "finger",
        "傷口正在流血", "shāng kǒu zhèng zài liú xiě", "ㄕㄤ ㄎㄡˇ ㄓㄥˋ ㄗㄞˋ ㄌㄧㄡˊ ㄒㄧㄝˇ",
        "Yara kanıyor", "The wound is bleeding"
    ],
    # 65. 投票
    [
        "v_toupiao", "投票", "tóu piào", "ㄊㄡˊ ㄆㄧㄠˋ", "Oy kullanmak", "To vote",
        "台灣每到大選日，許多北漂族都會搭高鐵返鄉投票。",
        1, "Easy", "Culture & Society", "🗳️",
        "Votar", "Wählen / Abstimmen", "Voter", "Votare", "投票する", "투표하다", "Votar", "वोट देना",
        "oy kullan", "vote",
        "候選人", "hòu xuǎn rén", "ㄏㄡˋ ㄒㄩㄢˇ ㄖㄣˊ", "👥", "Aday", "candidate",
        "公民積極返鄉投票", "gōng mín jī jí fǎn xiāng tóu piào", "ㄍㄨㄥ ㄇㄧㄣˊ ㄐㄧ ㄐㄧˊ ㄈㄢˇ ㄒㄧㄤ ㄊㄡˊ ㄆㄧㄠˋ",
        "Vatandaşlar oy kullanmak için memleketlerine dönüyor", "Citizens return home actively to vote"
    ],
    # 66. 當選
    [
        "v_dangxuan", "當選", "dāng xuǎn", "ㄉㄤ ㄒㄩㄢˇ", "Seçilmek", "To be elected",
        "開票當晚，當選人會發表感言感謝選民的支持。",
        2, "Easy", "Culture & Society", "🏅",
        "Ser elegido", "Gewählt werden", "Être élu", "Essere eletto", "当選する", "당선되다", "Ser eleito", "चुना जाना",
        "seçil", "be elected",
        "市長", "shì zhǎng", "ㄕˋ ㄓㄤˇ", "🏛️", "Belediye Başkanı", "mayor",
        "恭喜他順利當選", "gōng xǐ tā shùn lì dāng xuǎn", "ㄍㄨㄥ ㄒㄧˇ ㄊㄚ ㄕㄨㄣˋ ㄌㄧˋ ㄉㄤ ㄒㄩㄢˇ",
        "Başarıyla seçilmesini tebrik ederiz", "Congratulations on his successful election"
    ],
    # 67. 抗議
    [
        "v_kangyi", "抗議", "kàng yì", "ㄎㄤˋ ㄧˋ", "Protesto etmek", "To protest",
        "在自由民主的台灣，民眾有和平集會抗議表達訴求的權利。",
        2, "Easy", "Culture & Society", "📢",
        "Protestar", "Protestieren", "Protester", "Protestare", "抗議する", "항의하다", "Protestar", "विरोध करना",
        "protesto et", "protest",
        "不公", "bù gōng", "ㄅㄨˋ ㄍㄨㄥ", "⚖️", "Haksızlık", "injustice",
        "群眾上街和平抗議", "qún zhòng shàng jiē hé píng kàng yì", "ㄑㄩㄣˊ ㄓㄨㄥˋ ㄕㄤˋ ㄐㄧㄝ ㄏㄜˊ ㄆㄧㄥˊ ㄎㄤˋ ㄧˋ",
        "Halk sokaklarda barışçıl protesto yapıyor", "Crowds protest peacefully on the streets"
    ],
    # 68. 贊成
    [
        "v_zancheng", "贊成", "zàn chéng", "ㄗㄢˋ ㄔㄥˊ", "Onaylamak / Katılmak", "To agree / approve",
        "大家都非常贊成這個環保淨灘活動的提議。",
        2, "Easy", "Daily Actions", "👍",
        "Aprobar / Estar de acuerdo", "Zustimmen", "Approuver", "Approvare", "賛成する", "찬성하다", "Aprovar", "सहमत होना",
        "onayla", "agree",
        "提議", "tí yì", "ㄊㄧˊ ㄧˋ", "💡", "Öneri", "proposal",
        "我完全贊成你的方案", "wǒ wán quán zàn chéng nǐ de fāng àn", "ㄨㄛˇ ㄨㄢˊ ㄑㄩㄢˊ ㄗㄢˋ ㄔㄥˊ ㄋㄧˇ ˙ㄉㄜ ㄈㄤ ㄢˋ",
        "Senin planına tamamen katılıyorum", "I completely agree with your proposal"
    ],
    # 69. 反對
    [
        "v_fandui", "反對", "fǎn duì", "ㄈㄢˇ ㄉㄨㄟˋ", "Karşı çıkmak", "To oppose",
        "會議上如果有人反對，可以充分陳述各自的理由。",
        2, "Easy", "Daily Actions", "👎",
        "Oponerse", "Dagegen sein / Ablehnen", "S'opposer", "Opporsi", "反対する", "반대하다", "Opor-se", "विरोध करना",
        "karşı çık", "oppose",
        "意見", "yì jiàn", "ㄧˋ ㄐㄧㄢˋ", "🗣️", "Fikir", "opinion",
        "他堅決反對這項措施", "tā jiān jué fǎn duì zhè xiàng cuò shī", "ㄊㄚ ㄐㄧㄢ ㄐㄩㄝˊ ㄈㄢˇ ㄉㄨㄟˋ ㄓㄜˋ ㄒㄧㄤˋ ㄘㄨㄛˋ ㄕ",
        "O bu tedbire kesinlikle karşı çıkıyor", "He firmly opposes this measure"
    ],
    # 70. 支持
    [
        "v_zhichi", "支持", "zhī chí", "ㄓ ㄔˊ", "Desteklemek", "To support",
        "購買在地台灣小農產品，就是支持本土農業最好的方式。",
        1, "Easy", "Daily Actions", "💪",
        "Apoyar", "Unterstützen", "Soutenir", "Sostenere", "支持する", "지지하다", "Apoiar", "समर्थन करना",
        "destekle", "support",
        "小農", "xiǎo nóng", "ㄒㄧㄠˇ ㄋㄨㄥˊ", "🌾", "Küçük çiftçi", "small farmers",
        "我們全力支持朋友", "wǒ men quán lì zhī chí péng yǒu", "ㄨㄛˇ ㄇㄣ˙ ㄑㄩㄢˊ ㄌㄧˋ ㄓ ㄔˊ ㄆㄥˊ ㄧㄡˇ",
        "Arkadaşımızı tüm gücümüzle destekliyoruz", "We support our friend with all our strength"
    ],
    # 71. 保護
    [
        "v_baohu", "保護", "bǎo hù", "ㄅㄠˇ ㄏㄨˋ", "Korumak", "To protect",
        "台灣黑熊是瀕危保育動物，全社會共同努力保護牠們。",
        2, "Easy", "Daily Actions", "🛡️",
        "Proteger", "Schützen", "Protéger", "Proteggere", "保護する", "보호하다", "Proteger", "रक्षा करना",
        "koru", "protect",
        "環境", "huán jìng", "ㄏㄨㄢˊ ㄐㄧㄥˋ", "🌳", "Çevre", "environment",
        "大家攜手保護地球環境", "dà jiā xié shǒu bǎo hù dì qiú huán jìng", "ㄉㄚˋ ㄐㄧㄚ ㄒㄧㄝˊ ㄕㄡˇ ㄅㄠˇ ㄏㄨˋ ㄉㄧˋ ㄑㄧㄡˊ ㄏㄨㄢˊ ㄐㄧㄥˋ",
        "Herkes el ele verip dünya çevresini koruyor", "Everyone joins hands to protect the Earth's environment"
    ],
    # 72. 破壞
    [
        "v_pohuai", "破壞", "pò huài", "ㄆㄛˋ ㄏㄨㄞˋ", "Tahrip etmek / Bozmak", "To destroy / damage",
        "前往國家公園遊玩時，請勿隨意攀折花木破壞自然。",
        2, "Easy", "Daily Actions", "🔨",
        "Destruir / Dañar", "Zerstören", "Détruire", "Danneggiare", "破壊する", "파괴하다", "Destruir", "नष्ट करना",
        "tahrip et", "damage",
        "生態", "shēng tài", "ㄕㄥ ㄊㄞˋ", "🌿", "Ekoloji", "ecology",
        "請勿隨意破壞公物", "qǐng wù suí yì pò huài gōng wù", "ㄑㄧㄥˇ ㄨˋ ㄙㄨㄟˊ ㄧˋ ㄆㄛˋ ㄏㄨㄞˋ ㄍㄨㄥ ㄨˋ",
        "Lütfen kamu mallarını tahrip etmeyiniz", "Please do not vandalize public property"
    ],
    # 73. 遵守
    [
        "v_zunshou", "遵守", "zūn shǒu", "ㄗㄨㄣ ㄕㄡˇ", "Uymak / Riayet etmek", "To comply with / abide by",
        "騎乘機車遵守交通號誌和兩段式左轉規則。",
        2, "Easy", "Daily Actions", "📜",
        "Cumplir / Respetar", "Befolgen / Einhalten", "Respecter", "Rispettare", "遵守する", "준수하다", "Cumprir", "पालन करना",
        "uy", "comply with",
        "規則", "guī zé", "ㄍㄨㄟ ㄗㄜˊ", "🚦", "Kural", "rules",
        "大家嚴格遵守交通規則", "dà jiā yán gé zūn shǒu jiāo tōng guī zé", "ㄉㄚˋ ㄐㄧㄚ ㄧㄢˊ ㄍㄜˊ ㄗㄨㄣ ㄕㄡˇ ㄐㄧㄠ ㄊㄨㄥ ㄍㄨㄟ ㄗㄜˊ",
        "Herkes trafik kurallarına sıkı sıkıya uyuyor", "Everyone strictly obeys traffic rules"
    ],
    # 74. 違反
    [
        "v_weifan", "違反", "wéi fǎn", "ㄨㄟˊ ㄈㄢˇ", "İhlal etmek", "To violate",
        "在捷運站內飲食屬於違反大眾捷運法規，會被開罰。",
        2, "Easy", "Daily Actions", "⚠️",
        "Violar / Infringir", "Verstoßen gegen", "Enfreindre", "Violare", "違反する", "위반하다", "Violar", "उल्लंघन करना",
        "ihlal et", "violate",
        "法律", "fǎ lǜ", "ㄈㄚˇ ㄌㄩˋ", "⚖️", "Kanun", "laws",
        "在捷運站吃東西違反規定", "zài jié yùn zhàn chī dōng xi wéi fǎn guī dìng", "ㄗㄞˋ ㄐㄧㄝˊ ㄩㄣˋ ㄓㄢˋ ㄔ ㄉㄨㄥ ˙ㄒㄧ ㄨㄟˊ ㄈㄢˇ ㄍㄨㄟ ㄉㄧㄥˋ",
        "Metro istasyonunda yemek yemek kuralları ihlal eder", "Eating in MRT stations violates regulations"
    ],
    # 75. 罰款
    [
        "v_fakuan", "罰款", "fá kuǎn", "ㄈㄚˊ ㄎㄨㄢˇ", "Para cezası kesmek", "To fine",
        "違規紅燈右轉會被交通警察依法開單罰款。",
        2, "Easy", "Culture & Society", "👮",
        "Multar", "Mit Geldbuße belegen", "Mettre une amende", "Multare", "罰金を科す", "벌금을 물리다", "Multar", "जुर्माना लगाना",
        "para cezası kes", "fine",
        "違規", "wéi guī", "ㄨㄟˊ ㄍㄨㄟ", "🚫", "İhlal", "violation",
        "違法亂丟垃圾會被罰款", "wéi fǎ luàn diū lè sè huì bèi fá kuǎn", "ㄨㄟˊ ㄈㄚˇ ㄌㄨㄢˋ ㄉㄧㄡ ㄌㄜˋ ㄙㄜˋ ㄏㄨㄟˋ ㄅㄟˋ ㄈㄚˊ ㄎㄨㄢˇ",
        "Yere çöp atmak para cezasına tabidir", "Illegal littering will be fined"
    ],
    # 76. 報警
    [
        "v_baojing", "報警", "bào jǐng", "ㄅㄠˋ ㄐㄧㄥˇ", "Polise haber vermek", "To report to the police",
        "在台灣遇到緊急事故，立刻撥打110免費電話報警。",
        1, "Easy", "Daily Actions", "🚨",
        "Llamar a la policía", "Die Polizei rufen", "Appeler la police", "Chiamare la polizia", "警察に通報する", "경찰에 신고하다", "Chamar a polícia", "पुलिस को सूचना देना",
        "polise haber ver", "report to police",
        "警察", "jǐng chá", "ㄐㄧㄥˇ ㄔㄚˊ", "👮", "Polis", "police",
        "遺失錢包請立即報警", "yí shī qián bāo qǐng lì jí bào jǐng", "ㄧˊ ㄕ ㄑㄧㄢˊ ㄅㄠ ㄑㄧㄥˇ ㄌㄧˋ ㄐㄧˊ ㄅㄠˋ ㄐㄧㄥˇ",
        "Cüzdanınızı kaybederseniz derhal polise bildirin", "Please report to the police immediately if you lose your wallet"
    ],
    # 77. 求助
    [
        "v_qiuzhu", "求助", "qiú zhù", "ㄑㄧㄡˊ ㄓㄨˋ", "Yardım istemek", "To seek help",
        "外國旅客若遇到語言不通，可以向捷運旅客詢問處求助。",
        2, "Easy", "Daily Actions", "🆘",
        "Pedir ayuda", "Um Hilfe bitten", "Chercher de l'aide", "Chiedere aiuto", "助けを求める", "도움을 청하다", "Pedir ajuda", "मदद मांगना",
        "yardım iste", "seek help",
        "人員", "rén yuán", "ㄖㄣˊ ㄩㄢˊ", "👥", "Personel", "staff",
        "遇到困難及時向朋友求助", "yù dào kùn nán jí shí xiàng péng yǒu qiú zhù", "ㄩˋ ㄉㄠˋ ㄎㄨㄣˋ ㄋㄢˊ ㄐㄧˊ ㄕˊ ㄒㄧㄤˋ ㄆㄥˊ ㄧㄡˇ ㄑㄧㄡˊ ㄓㄨˋ",
        "Zorluk yaşandığında zamanında arkadaştan yardım istemek", "Seek help from friends promptly when facing difficulties"
    ],
    # 78. 救命
    [
        "v_jiuming", "救命", "jiù mìng", "ㄐㄧㄡˋ ㄇㄧㄥˋ", "Hayat kurtarmak / İmdat", "To save a life / Help!",
        "遇到溺水等緊急危險時要大聲呼喊「救命」！",
        1, "Easy", "Daily Actions", "🛟",
        "¡Socorro! / Salvar vida", "Zu Hilfe! / Leben retten", "Au secours ! / Sauver la vie", "Aiuto! / Salvare la vita", "助けて！ / 命を救う", "살려주세요 / 목숨을 구하다", "Socorro! / Salvar vidas", "जान बचाना / बचाओ!",
        "hayat kurtar", "save life",
        "生命", "shēng mìng", "ㄕㄥ ㄇㄧㄥˋ", "❤️", "Yaşam", "life",
        "醫生奮力搶救生命", "yī shēng fèn lì qiǎng jiù shēng mìng", "ㄧ ㄕㄥ ㄈㄣˋ ㄌㄧˋ ㄑㄧㄤˇ ㄐㄧㄡˋ ㄕㄥ ㄇㄧㄥˋ",
        "Doktor hayat kurtarmak için var gücüyle çabalıyor", "The doctor strives hard to save lives"
    ],
    # 79. 感謝
    [
        "v_ganxie", "感謝", "gǎn xiè", "ㄍㄢˇ ㄒㄧㄝˋ", "Teşekkür etmek / Minnet duymak", "To thank / appreciate",
        "台灣人經常說「非常感謝您」，表達深切的感激。",
        1, "Easy", "Daily Actions", "🙏",
        "Agradecer", "Danken / Dankbar sein", "Remercier", "Ringraziare", "感謝する", "감사하다", "Agradecer", "धन्यवाद करना",
        "teşekkür et", "thank",
        "幫助", "bāng zhù", "ㄅㄤ ㄓㄨˋ", "🤝", "Yardım", "help",
        "由衷感謝大家的支持", "yóu zhōng gǎn xiè dà jiā de zhī chí", "ㄧㄡˊ ㄓㄨㄥ ㄍㄢˇ ㄒㄧㄝˋ ㄉㄚˋ ㄐㄧㄚ ˙ㄉㄜ ㄓ ㄔˊ",
        "Herkesin desteğine yürekten teşekkür ederiz", "Sincerely thank everyone for their support"
    ],
    # 80. 慶祝
    [
        "v_qingzhu", "慶祝", "qìng zhù", "ㄑㄧㄥˋ ㄓㄨˋ", "Kutlamak", "To celebrate",
        "跨年夜成千上萬人聚集在市府廣場慶祝新年。",
        1, "Easy", "Culture & Society", "🎉",
        "Celebrar / Festejar", "Feiern", "Célébrer / Fêter", "Festeggiare", "祝う", "축하하다", "Celebrar", "मनाना",
        "kutla", "celebrate",
        "節日", "jié rì", "ㄐㄧㄝˊ ㄖˋ", "🎊", "Bayram / Festival", "festival",
        "大家開心地慶祝生日", "dà jiā kāi xīn de qìng zhù shēng rì", "ㄉㄚˋ ㄐㄧㄚ ㄎㄞ ㄒㄧㄣ ˙ㄉㄜ ㄑㄧㄥˋ ㄓㄨˋ ㄕㄥ ㄖˋ",
        "Herkes neşeyle doğum gününü kutluyor", "Everyone is happily celebrating the birthday"
    ],
    # 81. 祈禱
    [
        "v_qidao", "祈禱", "qí dǎo", "ㄑㄧˊ ㄉㄠˇ", "Dua etmek", "To pray",
        "在教堂或清真寺，信徒虔誠地祈禱世界和平。",
        2, "Easy", "Culture & Society", "🕊️",
        "Orar / Rezar", "Beten", "Prier", "Pregare", "祈る", "기도하다", "Rezar / Orar", "प्रार्थना करना",
        "dua et", "pray",
        "和平", "hé píng", "ㄏㄜˊ ㄆㄧㄥˊ", "🕊️", "Barış", "peace",
        "信徒虔誠地祈禱和平", "xìn tú qián chéng de qí dǎo hé píng", "ㄒㄧㄣˋ ㄊㄨˊ ㄑㄧㄢˊ ㄔㄥˊ ˙ㄉㄜ ㄑㄧˊ ㄉㄠˇ ㄏㄜˊ ㄆㄧㄥˊ",
        "İnananlar huşu içinde barış için dua ediyor", "Believers devoutly pray for peace"
    ],
    # 82. 保佑
    [
        "v_baoyou", "保佑", "bǎo yòu", "ㄅㄠˇ ㄧㄡˋ", "Korumak / Esirgemek (manevi)", "To bless and protect",
        "台灣民眾常到媽祖廟拜拜，祈求媽祖保佑合家平安。",
        2, "Easy", "Culture & Society", "🏮",
        "Bendecir y proteger", "Segnen und beschützen", "Bénir et protéger", "Proteggere / Benedire", "加護する", "보살피다", "Abençoar e proteger", "रक्षा और कृपा करना",
        "esirge", "bless and protect",
        "全家", "quán jiā", "ㄑㄩㄢˊ ㄐㄧㄚ", "👨‍👩‍👧‍👦", "Tüm aile", "whole family",
        "祈求神明保佑平安", "qí qiú shén míng bǎo yòu píng ān", "ㄑㄧˊ ㄑㄧㄡˊ ㄕㄣˊ ㄇㄧㄥˊ ㄅㄠˇ ㄧㄡˋ ㄆㄧㄥˊ ㄢ",
        "Tanrıdan huzur ve esenlik dilemek", "Pray to deities to bless and protect with safety"
    ],
    # 83. 許願
    [
        "v_xuyuan", "許願", "xǔ yuàn", "ㄒㄩˇ ㄩㄢˋ", "Dilek tutmak", "To make a wish",
        "在平溪放天燈時，大家會把心中的願望寫在天燈上許願。",
        1, "Easy", "Culture & Society", "🏮",
        "Pedir un deseo", "Sich etwas wünschen", "Faire un vœu", "Esprimere un desiderio", "願い事をする", "소원을 빌다", "Fazer um pedido", "मन्नत मांगना",
        "dilek tut", "make a wish",
        "天燈", "tiān dēng", "ㄊㄧㄢ ㄉㄥ", "🏮", "Dilek feneri", "sky lantern",
        "吹蠟燭前先許願", "chuī là zhú qián xiān xǔ yuàn", "ㄔㄨㄟ ㄌㄚˋ ㄓㄨˊ ㄑㄧㄢˊ ㄒㄧㄢ ㄒㄩˇ ㄩㄢˋ",
        "Mumları üflemeden önce dilek tut", "Make a wish before blowing out candles"
    ],
    # 84. 拜拜
    [
        "v_baibai", "拜拜", "bài bai", "ㄅㄞˋ ㄅㄞ˙", "Tapınakta dua etmek", "To worship / pray at temple",
        "每逢初一十五，台灣街頭隨處可見店家焚香拜拜祈求生意興隆。",
        1, "Easy", "Culture & Society", "🪔",
        "Rezar en el templo", "Im Tempel beten", "Prier au temple", "Pregare al tempio", "お参りする", "절하다 / 제사 지내다", "Rezar no templo", "पूजा करना",
        "tapınakta dua et", "worship at temple",
        "神明", "shén míng", "ㄕㄣˊ ㄇㄧㄥˊ", "🏮", "Tanrılar", "deities",
        "初一十五去廟裡拜拜", "chū yī shí wǔ qù miào lǐ bài bai", "ㄔㄨ ㄧ ㄕˊ ㄨˇ ㄑㄩˋ ㄇㄧㄠˋ ㄌㄧˇ ㄅㄞˋ ㄅㄞ˙",
        "Ay takviminin 1. ve 15. günlerinde tapınakta dua etmek", "Go to the temple to pray on the 1st and 15th of the lunar month"
    ],
    # 85. 跨年
    [
        "v_kuanian", "跨年", "kuà nián", "ㄎㄨㄚˋ ㄋㄧㄢˊ", "Yılbaşını kutlamak / Yeni yıla girmek", "To celebrate New Year's Eve",
        "台北101的跨年煙火每年吸引數十萬人一同倒數迎接新年。",
        1, "Easy", "Culture & Society", "🎆",
        "Celebrar el fin de año", "Silvester feiern", "Fêter le réveillon", "Festeggiare capodanno", "年を越す", "새해를 맞이하다", "Passar o réveillon", "नया साल मनाना",
        "yeni yıla gir", "celebrate NYE",
        "煙火", "yān huǒ", "ㄧㄢ ㄏㄨㄛˇ", "🎆", "Havai fişek", "fireworks",
        "我們一起看101跨年煙火", "wǒ men yì qǐ kàn 101 kuà nián yān huǒ", "ㄨㄛˇ ㄇㄣ˙ ㄧˋ ㄑㄧˇ ㄎㄢˋ 101 ㄎㄨㄚˋ ㄋㄧㄢˊ ㄧㄢ ㄏㄨㄛˇ",
        "Birlikte Taipei 101 yılbaşı havai fişeklerini izliyoruz", "We watch the Taipei 101 New Year's Eve fireworks together"
    ]
]

print(f"Total verbs in part 4: {len(data)}")
assert len(data) == 85, f"Expected 85, got {len(data)}"
for i, item in enumerate(data):
    assert len(item) == 32, f"Item {i} ({item[0]}) has len {len(item)} != 32"

with open('/Users/tarikozluk/Desktop/Dictionary-IAC/data_builder_vs/v_part4.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("Saved v_part4.json successfully!")
