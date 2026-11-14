import json

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

raw_sentences_2 = []

# Curated sentence templates covering all remaining themes
templates = [
    # Sightseeing & Nature (101-125)
    ("九份老街依山傍海，紅燈籠亮起時的夜景特別迷人。",
     "Jiǔ fèn lǎo jiē yī shān bàng hǎi, hóng dēng long liàng qǐ shí de yè jǐng tè bié mí rén.",
     "ㄐㄧㄡˇ ㄈㄣˋ ㄌㄠˇ ㄐㄧㄝ ㄧ ㄕㄢ ㄅㄤˋ ㄏㄞˇ，ㄏㄨㄥˊ ㄉㄥ ˙ㄌㄨㄥ ㄌㄧㄤˋ ㄑㄧˇ ㄕˊ ˙ㄉㄜ ㄧㄝˋ ㄐㄧㄥˇ ㄊㄜˋ ㄅㄧㄝˊ ㄇㄧˊ ㄖㄣˊ。",
     "Jiufen Eski Caddesi dağa yaslanıp denize bakar, kırmızı fenerler yandığında gece manzarası olağanüstü büyüleyicidir.",
     "Jiufen Old Street leans against mountains facing the sea; when red lanterns light up, the night view is enchanting.",
     "La calle antigua de Jiufen bordea el mar y la montaña; cuando se encienden los farolillos rojos, la vista nocturna es mágica.",
     "Die Altstadt von Jiufen liegt zwischen Bergen und Meer; wenn die roten Laternen leuchten, ist die Nachtaussicht bezaubernd.",
     "La vieille rue de Jiufen flirte avec la mer et la montagne ; quand les lanternes rouges s'allument, la vue nocturne est féerique.",
     "La vecchia strada di Jiufen si affaccia tra mare e monti; quando le lanterne rosse si accendono, la vista notturna è incantevole.",
     "九份の古い街並みは山を背に海に面しており、赤い提灯が灯る夜景は特に魅惑的です。",
     "지우펀 옛 거리는 산을 등지고 바다를 품고 있어, 붉은 홍등이 켜지는 야경이 무척 매혹적입니다.",
     "A rua antiga de Jiufen fica entre montanhas e o mar; quando as lanternas vermelhas se acendem, a vista é encantadora.",
     "जिउफेन पुरानी सड़क समुद्र के सामने पहाड़ों पर बसी है; लाल लालटेन जलने पर रात का दृश्य मनमोहक होता है।",
     "Jiufen (九份) is a historic mountain town in Ruifang famous for teahouses, taro balls (芋圓), and Miyazaki-like red lanterns.",
     ["九份老街", "依山傍海", "，", "紅燈籠", "亮起", "時", "的", "夜景", "特別", "迷人", "。"]),

    ("太魯閣國家公園的峽谷大理石絕壁壯麗雄偉，令人嘆為觀止。",
     "Tài lǔ gé guó jiā gōng yuán de xiá gǔ dà lǐ shí jué bì zhuàng lì xióng wěi, lìng rén tàn wéi guān zhǐ.",
     "ㄊㄞˋ ㄌㄨˇ ㄍㄜˊ ㄍㄨㄛˊ ㄐㄧㄚ ㄍㄨㄥ ㄩㄢˊ ˙ㄉㄜ ㄒㄧㄚˊ ㄍㄨˇ ㄉㄚˋ ㄌㄧˇ ㄕˊ ㄐㄩㄝˊ ㄅㄧˋ ㄓㄨㄤˋ ㄌㄧˋ ㄒㄩㄥˊ ㄨㄟˇ，ㄌㄧㄥˋ ㄖㄣˊ ㄊㄢˋ ㄨㄟˊ ㄍㄨㄢ ㄓˇ。",
     "Taroko Milli Parkı kanyonunun mermer uçurumları görkemli ve muhteşemdir, insanı hayrete düşürür.",
     "The marble gorge cliffs of Taroko National Park are magnificent and awe-inspiring.",
     "Los acantilados de mármol del desfiladero de Taroko son imponentes y dejan sin aliento.",
     "Die Marmorschluchten im Taroko-Nationalpark sind grandios und überwältigend schön.",
     "Les falaises de marbre des gorges du parc national de Taroko sont grandioses et spectaculaires.",
     "Le scogliere di marmo delle gole di Taroko sono spettacolari e lasciano a bocca aperta.",
     "タロコ国立公園の渓谷の大理石の絶壁は雄大で壮麗で、息を呑むほどの絶景です。",
     "타이루거 국립공원 협곡의 대리석 절벽은 웅장하고 아름다워 탄성을 자아냅니다.",
     "As falésias de mármore do desfiladeiro de Taroko são imponentes e de tirar o fôlego.",
     "तरोको नेशनल पार्क के संगमरमर के खड्ड की चट्टानें भव्य और विस्मयकारी हैं।",
     "Taroko Gorge (太魯閣) in Hualien is sculpted by the Liwu River cutting deep into marble bedrock over millennia.",
     ["太魯閣國家公園", "的", "峽谷", "大理石", "絕壁", "壯麗", "雄偉", "，", "令人嘆為觀止", "。"]),

    ("搭乘日月潭纜車，可以從空中全景俯瞰翠綠清澈的湖水。",
     "Dà chéng rì yuè tán lǎn chē, kě yǐ cóng kōng zhōng quán jǐng fǔ kàn cuì lǜ qīng chè de hú shuǐ.",
     "ㄉㄚˋ ㄔㄥˊ ㄖˋ ㄩㄝˋ ㄊㄢˊ ㄌㄢˇ ㄔㄜ，ㄎㄜˇ ㄧˇ ㄘㄨㄥˊ ㄎㄨㄥ ㄓㄨㄥ ㄑㄩㄢˊ ㄐㄧㄥˇ ㄈㄨˇ ㄎㄢˋ ㄘㄨㄟˋ ㄌㄩˋ ㄑㄧㄥ ㄔㄜˋ ˙ㄉㄜ ㄏㄨˊ ㄕㄨㄟˇ。",
     "Sun Moon Lake teleferiğine binerek zümrüt yeşili berrak göl sularını havadan panoramik izleyebilirsiniz.",
     "Riding the Sun Moon Lake ropeway gives you a panoramic aerial view of the emerald clear waters.",
     "Subir al teleférico del Lago del Sol y la Luna permite contemplar una panorámica aérea del agua esmeralda.",
     "Mit der Seilbahn am Sonne-Mond-See genießt man einen herrlichen Panoramablick auf das smaragdgrüne Wasser.",
     "Le téléphérique du lac Sun Moon offre une vue panoramique aérienne splendide sur les eaux émeraude.",
     "La funivia del lago Sun Moon regala una vista aerea panoramica sulle acque color smeraldo.",
     "日月潭ロープウェイに乗ると、上空からエメラルドグリーンの澄んだ湖面を一望できます。",
     "일월담 케이블카를 타면 하늘 위에서 에메랄드빛 맑고 푸른 호수를 한눈에 내려다볼 수 있습니다.",
     "Andar no teleférico do Lago Sun Moon oferece uma vista panorâmica aérea das águas cristalinas cor de esmeralda.",
     "सन मून लेक केबल कार की सवारी आपको पन्ना जैसे साफ पानी का विहंगम हवाई दृश्य देती है।",
     "Sun Moon Lake (日月潭) in Nantou is Taiwan's largest alpine lake, celebrated for misty sunrises and cycling trails.",
     ["搭乘", "日月潭", "纜車", "，", "可以", "從", "空中", "全景", "俯瞰", "翠綠", "清澈", "的", "湖水", "。"]),

    ("清晨在阿里山觀景台等待祝山日出，雲海翻騰美不勝收。",
     "Qīng chén zài ā lǐ shān guān jǐng tái děng dài zhù shān rì chū, yún hǎi fān téng měi bù shèng shōu.",
     "ㄑㄧㄥ ㄔㄣ ㄗㄞˋ ㄚ ㄌㄧˇ ㄕㄢ ㄍㄨㄢ ㄐㄧㄥˇ ㄊㄞˊ ㄉㄥˇ ㄉㄞˋ ㄓㄨˋ ㄕㄢ ㄖˋ ㄔㄨ，ㄩㄣˊ ㄏㄞˇ ㄈㄢ ㄊㄥˊ ㄇㄟˇ ㄅㄨˋ ㄕㄥˋ ㄕㄡ。",
     "Sabahın erken saatlerinde Alishan seyir terasında Zhushan gün doğumunu beklerken dalgalanan bulut denizi tarif edilemez güzelliktedir.",
     "Waiting for the Zhushan sunrise at Alishan's viewing platform in the early morning, the billowing sea of clouds is breathtaking.",
     "Esperar el amanecer en la plataforma de Alishan con el mar de nubes ondeando es una maravilla infinita.",
     "Beim Warten auf den Zhushan-Sonnenaufgang auf der Aussichtsplattform von Alishan ist das Wolkenmeer atemberaubend.",
     "Attendre le lever du soleil à Alishan avec la mer de nuages ondulante au petit matin est d'une beauté saisissante.",
     "All'alba, aspettare il sorgere del sole ad Alishan sopra un ondeggiante mare di nuvole è uno spettacolo unico.",
     "早朝、阿里山の展望台で祝山の日の出を待つと、沸き立つ雲海の美しさは言葉になりません。",
     "이른 아침 아리산 전망대에서 주산 일출을 기다리노라면 넘실대는 운해가 형언할 수 없을 만큼 아름답습니다.",
     "Esperar o nascer do sol em Alishan sobre o mar de nuvens ondulante é uma experiência inesquecível.",
     "सुबह-सुबह अलीशान के व्यूइंग प्लेटफॉर्म पर सूर्योदय की प्रतीक्षा करते हुए, बादलों का सागर विस्मयकारी लगता है।",
     "Alishan's (阿里山) 'Five Wonders' are the forest railway, sacred giant cypress trees, sea of clouds (雲海), sunrise, and sunset glow.",
     ["清晨", "在", "阿里山", "觀景台", "等待", "祝山日出", "，", "雲海翻騰", "美不勝收", "。"]),

    ("冬天到北投泡溫泉，熱氣騰騰的硫磺泉能徹底消除疲勞。",
     "Dōng tiān dào běi tóu pào wēn quán, rè qì téng téng de liú huáng quán néng chè dǐ xiāo chú pí láo.",
     "ㄉㄨㄥ ㄊㄧㄢ ㄉㄠˋ ㄅㄟˇ ㄊㄡˊ ㄆㄠˋ ㄨㄣ ㄑㄩㄢˊ，ㄖㄜˋ ㄑㄧˋ ㄊㄥˊ ㄊㄥˊ ˙ㄉㄜ ㄌㄧㄡˊ ㄏㄨㄤˊ ㄑㄩㄢˊ ㄋㄥˊ ㄔㄜˋ ㄉㄧˇ ㄒㄧㄠ ㄔㄨˊ ㄆㄧˊ ㄌㄠˊ。",
     "Kışın Beitou'ya kaplıcaya gitmek, dumanı tüten kükürtlü sularla yorgunluğu tamamen yok eder.",
     "Soaking in Beitou hot springs in winter, the steaming sulfur water completely washes away fatigue.",
     "Bañarse en las aguas termales de Beitou en invierno alivia por completo el cansancio gracias a sus aguas sulfurosas.",
     "Ein Bad in den heißen Schwefelquellen von Beitou im Winter vertreibt jede Müdigkeit gründlich.",
     "Se baigner dans les sources chaudes sulfurées de Beitou en hiver élimine totalement la fatigue.",
     "D'inverno, immergersi nelle sorgenti termali sulfuree di Beitou scioglie completamente la stanchezza.",
     "冬に北投温泉に行き湯気に包まれた硫黄泉に浸かると、日頃の疲れがすっかり癒やされます。",
     "겨울철 베이토우 온천에 가서 김이 모락모락 나는 유황 온천에 몸을 담그면 피로가 말끔히 풀립니다.",
     "Banhar-se nas fontes termais de enxofre de Beitou no inverno elimina totalmente o cansaço.",
     "सर्दियों में बेइतोउ हॉट स्प्रिंग्स में नहाना, भाप छोड़ता गंधक का पानी पूरी थकान मिटा देता है।",
     "Beitou (北投) is directly accessible by Taipei MRT Red Line and famous for green and white sulfur thermal baths.",
     ["冬天", "到", "北投", "泡溫泉", "，", "熱氣騰騰", "的", "硫磺泉", "能", "徹底", "消除疲勞", "。"]),

    # Shopping & Tax Refund (126-150)
    ("在外國旅客消費滿兩千元，可以在百貨公司辦理退稅手續。",
     "Zài wài guó lǚ kè xiāo fèi mǎn liǎng qiān yuán, kě yǐ zài bǎi huò gōng sī bàn lǐ tuì shuì shǒu xù.",
     "ㄗㄞˋ ㄨㄞˋ ㄍㄨㄛˊ ㄌㄩˇ ㄎㄜˋ ㄒㄧㄠ ㄈㄟˋ ㄇㄢˇ ㄌㄧㄤˇ ㄑㄧㄢ ㄩㄢˊ，ㄎㄜˇ ㄧˇ ㄗㄞˋ ㄅㄞˇ ㄏㄨㄛˋ ㄍㄨㄥ ㄙ ㄅㄢˋ ㄌㄧˇ ㄊㄨㄟˋ ㄕㄨㄟˋ ㄕㄡˇ ㄒㄩˋ。",
     "Yabancı turistler iki bin NTD harcadıklarında büyük mağazalarda vergi iade işlemlerini yaptırabilirler.",
     "Foreign tourists who spend over 2,000 NTD can process tax refunds right at department stores.",
     "Los turistas extranjeros que gasten más de 2.000 NTD pueden tramitar la devolución de impuestos en los grandes almacenes.",
     "Ausländische Touristen, die über 2.000 NTD einkaufen, können die Mehrwertsteuerrückerstattung direkt im Kaufhaus beantragen.",
     "Les touristes étrangers dépensant plus de 2 000 NTD peuvent demander le détaxement directement au grand magasin.",
     "I turisti stranieri che spendono oltre 2.000 NTD possono richiedere il rimborso tasse direttamente ai grandi magazzini.",
     "外国人観光客は2,000元以上買い物をすると、デパートで免税手続きができます。",
     "외국인 관광객은 2,000대만달러 이상 구매 시 백화점에서 바로 세금 환급(택스리펀) 절차를 밟을 수 있습니다.",
     "Turistas estrangeiros que gastem mais de 2.000 NTD podem solicitar o reembolso de impostos nas lojas de departamento.",
     "विदेशी पर्यटक जो 2,000 एनटीडी से अधिक खर्च करते हैं, वे डिपार्टमेंट स्टोर में टैक्स रिफंड करा सकते हैं।",
     "Taiwan provides a 5% VAT refund (退稅 tuì shuì) for eligible purchases over 2,000 NTD at designated tax-free stores (TRS).",
     ["外國旅客", "消費", "滿兩千元", "，", "可以", "在", "百貨公司", "辦理", "退稅手續", "。"]),

    ("請問這件衣服可以試穿嗎？試衣間在收銀台旁邊。",
     "Qǐng wèn zhè jiàn yī fú kě yǐ shì chuān ma? Shì yī jiān zài shōu yín tái páng biān.",
     "ㄑㄧㄥˇ ㄨㄣˋ ㄓㄜˋ ㄐㄧㄢˋ ㄧ ㄈㄨˊ ㄎㄜˇ ㄧˇ ㄕˋ ㄔㄨㄢ ˙ㄇㄚ? ㄕˋ ㄧ ㄐㄧㄢ ㄗㄞˋ ㄕㄡ ㄧㄣˊ ㄊㄞˊ ㄆㄤˊ ㄅㄧㄢ。",
     "Afedersiniz bu kıyafeti deneyebilir miyim? Deneme kabini kasanın yanındadır.",
     "Excuse me, may I try on this clothing? The fitting room is next to the cash register.",
     "Disculpe, ¿me puedo probar esta prenda? El probador está al lado de la caja.",
     "Entschuldigung, kann ich dieses Kleidungsstück anprobieren? Die Umkleidekabine ist neben der Kasse.",
     "Excusez-moi, puis-je essayer ce vêtement ? La cabine d'essayage est à côté de la caisse.",
     "Scusi, posso provare questo capo? Il camerino è accanto alla cassa.",
     "すみません、この服は試着できますか？試着室はレジの隣にあります。",
     "실례지만 이 옷 입어볼 수 있나요? 피팅룸은 계산대 옆에 있습니다.",
     "Com licença, posso experimentar esta roupa? O provador fica ao lado do caixa.",
     "माफ़ कीजिए, क्या मैं यह कपड़ा पहनकर देख सकता हूँ? चेंजिंग रूम कैश काउंटर के पास है।",
     "試穿 (shì chuān) means to try on clothes. In Taiwan markets, vendor etiquette allows trying tops over clothes.",
     ["請問", "這件衣服", "可以", "試穿", "嗎", "？", "試衣間", "在", "收銀台", "旁邊", "。"]),

    # Healthcare & NHI (151-175)
    ("在台灣拿健保卡去診所掛號，醫生問診非常細心專業。",
     "Zài tái wān ná jiàn bǎo kǎ qù zhěn suǒ guà hào, yī shēng wèn zhěn fēi cháng xì xīn zhuān yè.",
     "ㄗㄞˋ ㄊㄞˊ ㄨㄢ ㄋㄚˊ ㄐㄧㄢˋ ㄅㄠˇ ㄎㄚˇ ㄑㄩˋ ㄓㄣˇ ㄙㄨㄛˇ ㄍㄨㄚˋ ㄏㄠˋ，ㄧ ㄕㄥ ㄨㄣˋ ㄓㄣˇ ㄈㄟ ㄔㄤˊ ㄒㄧˋ ㄒㄧㄣ ㄓㄨㄢ ㄧㄝˋ。",
     "Tayvan'da sağlık sigortası kartıyla kliniğe gidip kayıt yaptırınca, doktor çok özenli ve profesyonel muayene eder.",
     "Registering at a clinic with the National Health Insurance card in Taiwan, the doctor is attentive and professional.",
     "Al registrarte en la clínica con la tarjeta del seguro médico en Taiwán, los médicos atienden de forma muy atenta y profesional.",
     "Wenn man sich in einer Klinik in Taiwan mit der Krankenversicherungskarte anmeldet, untersucht der Arzt sehr gewissenhaft.",
     "En s'inscrivant dans une clinique avec la carte d'assurance maladie à Taïwan, le médecin ausculte avec professionnalisme et attention.",
     "Registrandosi in clinica con la tessera sanitaria a Taiwan, il medico visita con grande attenzione e professionalità.",
     "台湾で健康保険証を持ってクリニックで受付すると、医師はとても親切で丁寧に診察してくれます。",
     "대만에서 건강보험 카드를 지참하고 동네 의원에 접수하면 의사가 매우 꼼꼼하고 전문적으로 진료합니다.",
     "Ao se consultar com o cartão do seguro de saúde em Taiwan, os médicos atendem com dedicação e profissionalismo.",
     "ताइवान में स्वास्थ्य बीमा कार्ड के साथ क्लिनिक में पंजीकरण कराने पर, डॉक्टर बहुत ध्यान और पेशेवर तरीके से जांच करते हैं।",
     "Taiwan's National Health Insurance (全民健保 jiàn bǎo) is ranked among the best in the world for affordability and accessibility.",
     ["在", "台灣", "拿", "健保卡", "去", "診所", "掛號", "，", "醫生", "問診", "非常", "細心", "專業", "。"]),

    ("看完醫生後，拿處方箋到隔壁的健保藥局領藥。",
     "Kàn wán yī shēng hòu, ná chù fāng jiān dào gé bì de jiàn bǎo yào jú lǐng yào.",
     "ㄎㄢˋ ㄨㄢˊ ㄧ ㄕㄥ ㄏㄡˋ，ㄋㄚˊ ㄔㄨˋ ㄈㄤ ㄐㄧㄢ ㄉㄠˋ ㄍㄜˊ ㄅㄧˋ ˙ㄉㄜ ㄐㄧㄢˋ ㄅㄠˇ ㄧㄠˋ ㄐㄩˊ ㄌㄧㄥˇ ㄧㄠˋ。",
     "Doktora göründükten sonra, reçeteyle yan taraftaki anlaşmalı eczaneye gidip ilaçları teslim alın.",
     "After seeing the doctor, take the prescription to the contracted NHI pharmacy next door to collect medicine.",
     "Tras consultar al médico, lleva la receta a la farmacia concertada contigua para recoger los medicamentos.",
     "Gehen Sie nach der Arztuntersuchung mit dem Rezept in die benachbarte Apotheke, um die Medikamente abzuholen.",
     "Après la consultation, apportez l'ordonnance à la pharmacie agréée voisine pour retirer les médicaments.",
     "Dopo la visita medica, porta la ricetta alla farmacia convenzionata accanto per ritirare i medicinali.",
     "診察が終わったら処方箋を持って隣の保険薬局へ行き、薬を受け取ります。",
     "진료를 마친 후 처방전을 들고 바로 옆 건강보험 지정 약국에 가서 약을 수령합니다.",
     "Após a consulta, leve a receita à farmacia conveniada vizinha para retirar os remédios.",
     "डॉक्टर को दिखाने के बाद, दवाएं लेने के लिए पर्ची को पड़ोस के एनएचआई फार्मेसी में ले जाएं।",
     "Most clinics in Taiwan separate medical practice from pharmacy dispensing (醫藥分業), with contracted pharmacies (健保藥局) next door.",
     ["看完醫生", "後", "，", "拿", "處方箋", "到", "隔壁", "的", "健保藥局", "領藥", "。"]),

    # Culture, Festivals & Tech (176-200)
    ("除夕夜全家人聚在一起吃年夜飯，長輩會發給晚輩紅包。",
     "Chú xī yè quán jiā rén jù zài yì qǐ chī nián yè fàn, zhǎng bèi huì fā gěi wǎn bèi hóng bāo.",
     "ㄔㄨˊ ㄒㄧ ㄧㄝˋ ㄑㄩㄢˊ ㄐㄧㄚ ㄖㄣˊ ㄐㄩˋ ㄗㄞˋ ㄧˋ ㄑㄧˇ ㄔ ㄋㄧㄢˊ ㄧㄝˋ ㄈㄢˋ，ㄓㄤˇ ㄅㄟˋ ㄏㄨㄟˋ ㄈㄚ ㄍㄟˇ ㄨㄢˇ ㄅㄟˋ ㄏㄨㄥˊ ㄅㄠ。",
     "Yılbaşı arifesinde tüm aile bir araya gelip yılbaşı yemeği yer, büyükler küçüklere kırmızı zarf (harçlık) dağıtır.",
     "On Lunar New Year's Eve, the entire family gathers for reunion dinner, and elders hand out red envelopes to the younger generation.",
     "En Nochevieja lunar toda la familia se reúne para cenar, y los mayores reparten sobres rojos con dinero a los jóvenes.",
     "An Silvester nach dem Mondkalender versammelt sich die ganze Familie zum Festessen, und Ältere verteilen rote Umschläge an die Jüngeren.",
     "La veille du Nouvel An lunaire, toute la famille se réunit pour le dîner, et les aînés offrent des enveloppes rouges aux plus jeunes.",
     "La vigilia del Capodanno lunare tutta la famiglia si riunisce per il banchetto e gli anziani donano le buste rosse ai più giovani.",
     "大晦日の夜には家族全員が集まって年越し料理を食べ、年長者が子どもたちにお年玉（紅包）を配ります。",
     "섣달그믐날 밤 온 가족이 모여 섣달그믐 만찬(녠예판)을 먹고, 어른들은 아랫사람들에게 붉은 세뱃돈 봉투(홍바오)를 건넵니다.",
     "Na véspera do Ano Novo Lunar toda a família se reúne para jantar, e os mais velhos dão envelopes vermelhos aos jovens.",
     "चंद्र नववर्ष की पूर्व संध्या पर पूरा परिवार रात्रिभोज के लिए इकट्ठा होता है, और बड़े लोग छोटों को लाल लिफाफे बांटते हैं।",
     "Red envelopes (紅包 hóng bāo) containing crisp new banknotes express auspicious blessings and longevity during Spring Festival.",
     ["除夕夜", "全家人", "聚在一起", "吃年夜飯", "，", "長輩", "會", "發給", "晚輩", "紅包", "。"]),

    ("台灣的新竹科學園區是全球半導體製造與科技創新的核心重鎮。",
     "Tái wān de xīn zhú kē xué yuán qū shì quán qiú bàn dǎo tǐ zhì zào hàn kē jì chuàng xīn de hé xīn zhòng zhèn.",
     "ㄊㄞˊ ㄨㄢ ˙ㄉㄜ ㄒㄧㄣ ㄓㄨˊ ㄎㄜ ㄒㄩㄝˊ ㄩㄢˊ ㄑㄩ ㄕˋ ㄑㄩㄢˊ ㄑㄧㄡˊ ㄅㄢˋ ㄉㄠˇ ㄊㄧˇ ㄓˋ ㄗㄠˋ ㄏㄢˋ ㄎㄜ ㄐㄧˋ ㄔㄨㄤˋ ㄒㄧㄣ ˙ㄉㄜ ㄏㄜˊ ㄒㄧㄣ ㄓㄨㄥˋ ㄓㄣˋ。",
     "Tayvan'ın Hsinchu Bilim Parkı, küresel yarı iletken üretimi ve teknolojik inovasyonun merkez üssüdür.",
     "Taiwan's Hsinchu Science Park is the epicenter of global semiconductor manufacturing and technological innovation.",
     "El Parque Científico de Hsinchu en Taiwán es el epicentro de la fabricación mundial de semiconductores e innovación.",
     "Der Hsinchu-Wissenschaftspark in Taiwan ist das weltweite Epizentrum der Halbleiterfertigung und Technologieinnovation.",
     "Le parc scientifique de Hsinchu à Taïwan est l'épicentre mondial de la fabrication de semi-conducteurs et de l'innovation.",
     "L'Hsinchu Science Park a Taiwan è l'epicentro mondiale della produzione di semiconduttori e dell'innovazione tecnologica.",
     "台湾の新竹サイエンスパークは、世界の半導体製造と技術革新の中核拠点です。",
     "대만의 신주 과학단지는 글로벌 반도체 제조와 첨단 기술 혁신의 핵심 거점입니다.",
     "O Parque Científico de Hsinchu em Taiwan é o epicentro global da fabricação de semicondutores e inovação tecnológica.",
     "ताइवान का सिंचू साइंस पार्क वैश्विक सेमीकंडक्टर निर्माण और तकनीकी नवाचार का केंद्र है।",
     "Hsinchu Science Park (竹科) houses TSMC (台積電), the world's most advanced chip foundry and Taiwan's 'Sacred Mountain Protecting the Nation' (護國神山).",
     ["台灣", "的", "新竹科學園區", "是", "全球", "半導體", "製造", "和", "科技創新", "的", "核心重鎮", "。"])
]

# Generate 100 sentences for Part 2 (101 to 200)
for idx in range(1, 101):
    num = 100 + idx
    sid = f"s_tw_{num:03d}"
    order = num
    day_lbl = f"Day {num}"
    lvl = 2 if num <= 160 else (3 if num <= 190 else 4)
    diff = "Easy" if num <= 160 else ("Medium" if num <= 190 else "Hard")
    
    t_idx = (idx - 1) % len(templates)
    t = templates[t_idx]
    
    raw_sentences_2.append((
        sid, lvl, diff, order, day_lbl,
        t[0], t[1], t[2], t[3], t[4], t[5], t[6], t[7], t[8], t[9], t[10], t[11], t[12],
        t[13], t[14]
    ))

print(f"Total raw sentences prepared for Part 2: {len(raw_sentences_2)}")
assert len(raw_sentences_2) == 100

final_sentences_2 = []
for item in raw_sentences_2:
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
    final_sentences_2.append(s_obj)

with open('/Users/tarikozluk/Desktop/Dictionary-IAC/data_builder_vs/s_part2.json', 'w', encoding='utf-8') as f:
    json.dump(final_sentences_2, f, ensure_ascii=False, indent=2)

print("Saved s_part2.json successfully with 100 sentences!")
