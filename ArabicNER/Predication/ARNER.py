import json
# preprocessing
def preprocess(text):
    """ Simple Arabic tokenizer and sentencizer. It is a space-based tokenizer. I use some rules to handle
    tokenition exception like words containing the preposition 'و'. For example 'ووالدته' is tokenized to 'و والدته'
    :param text: Arabic text to handle
    :return: tokenized sentences
    """
    try:
        text = text.decode('utf-8')
    except(UnicodeDecodeError, AttributeError):
        pass
    text = text.strip()
    tokenizer_exceptions = ["وظف", "وضعها", "وضعه", "وقفنا", "وصفوها", "وجهوا", "والدته", "والده", "وادي", "وضعية",
                            "واجهات", "وفرتها", "وقاية", "وفا", "وزيرنا", "وزارتي", "وجهاها", "واردة", "وضعته",
                            "وضعتها", "وجاهة", "وهمية", "واجهة", "واضعاً", "واقعي", "ودائع", "واعدا", "واع", "واسعا",
                            "ورائها", "وحدها", "وزارتي", "وزارتي", "والدة", "وزرائها", "وسطاء", "وليامز", "وافق",
                            "والدها", "وسم", "وافق", "وجهها", "واسعة", "واسع", "وزنها", "وزنه",
                            "وصلوا", "والدها", "وصولاً", "وضوحاً", "وجّهته", "وضعته", "ويكيليكس", "وحدها", "وزيراً",
                            "وقفات", "وعر", "واقيًا", "وقوف", "وصولهم", "وارسو", "واجهت", "وقائية", "وضعهم",
                            "وسطاء", "وظيفته", "ورائه", "واسع", "ورط", "وظفت", "وقوف", "وافقت", "وفدًا", "وصلتها",
                            "وثائقي", "ويليان", "وساط", "وُقّع", "وَقّع", "وخيمة", "ويست", "والتر", "وهران", "ولاعة",
                            "ولايت", "والي", "واجب", "وظيفتها", "ولايات", "واشنطن", "واصف",
                            "وقح", "وعد", "وقود", "وزن", "وقوع", "ورشة", "وقائع", "وتيرة", "وساطة", "وفود", "وفات",
                            "وصاية", "وشيك", "وثائق", "وطنية", "وجهات", "وجهت", "وعود", "وضعهم", "وون", "وسعها", "وسعه",
                            "ولاية", "واصفاً", "واصلت", "وليان", "وجدتها", "وجدته", "وديتي", "وطأت", "وطأ", "وعودها",
                            "وجوه", "وضوح", "وجيز", "ورثنا", "ورث", "واقع", "وهم", "واسعاً", "وراثية", "وراثي", "والاس",
                            "واجهنا", "وابل", "ويكيميديا", "واضحا", "واضح", "وصفته", "واتساب", "وحدات", "ون",
                            "وورلد", "والد", "وكلاء", "وتر", "وثيق", "وكالة", "وكالات", "و احدة", "واحد", "وصيته",
                            "وصيه", "ويلمينغتون", "ولد", "وزر", "وعي", "وفد", "وصول", "وقف", "وفاة", "ووتش", "وسط",
                            "وزراء", "وزارة", "ودي", "وصيف", "ويمبلدون", "وست", "وهج", "والد", "وليد", "وثار",
                            "وجد", "وجه", "وقت", "ويلز", "وجود", "وجيه", "وحد", "وحيد", "ودا", "وداد", "ودرو",
                            "ودى", "وديع", "وراء", "ورانس", "ورث", "ورَّث", "ورد", "وردة", "ورق", "ورم", "وزير",
                            "وسام", "وسائل", "وستون", "وسط", "وسن", "وسيط", "وسيلة", "وسيم", "وصاف", "وصف", "وصْفَ",
                            "وصل", "وضع", "وطن", "وعاء", "وفاء", "وفق", "وفيق", "وقت", "وقع", "وكال", "وكيل",
                            "ولاء", "ولف", "وهب", "وباء", "ونستون", "وضح", "وجب", "وقّع", "ولنغتون", "وحش",
                            "وفر", "ولادة", "ولي", "وفيات", "وزار", "وجّه", "وهماً", "وجَّه", "وظيفة", "وظائف", "وقائي"]

    sentence_splitter_exceptions = ["د.", "كي.", "في.", "آر.", "بى.", "جى.", "دى.", "جيه.", "ان.", "ال.", "سى.", "اس.",
                                    "اتش.", "اف."]

    sentence_splitters = ['.', '!', '؟', '\n']
    text = text.replace('،', ' ، ')
    text = text.replace('*', ' * ')
    text = text.replace('’', ' ’ ')
    text = text.replace('‘', ' ‘ ')
    text = text.replace(',', ' , ')
    text = text.replace('(', ' ( ')
    text = text.replace(')', ' ) ')
    text = text.replace('/', ' / ')
    text = text.replace('[', ' [ ')
    text = text.replace(']', ' ] ')
    text = text.replace('|', ' | ')
    text = text.replace('؛', ' ؛ ')
    text = text.replace('«', ' « ')
    text = text.replace('»', ' » ')
    text = text.replace('!', ' ! ')
    text = text.replace('-', ' - ')
    text = text.replace('“', ' “ ')
    text = text.replace('”', ' ” ')
    text = text.replace('"', ' " ')
    text = text.replace('؟', ' ؟ ')
    text = text.replace(':', ' : ')
    text = text.replace('…', ' … ')
    text = text.replace('..', ' .. ')
    text = text.replace('...', ' ... ')
    text = text.replace('\'', ' \' ')
    text = text.replace('\n', ' \n ')
    text = text.replace('  ', ' ')
    tokens = text.split()
    for i, token in enumerate(tokens):
        if token[-1] in sentence_splitters:
            is_exceptions = token in sentence_splitter_exceptions
            if not is_exceptions:
                tokens[i] = token[:-1] + ' ' + token[-1] + 'SENT_SPLITTER'
    tokens = ' '.join(tokens).split()
    for i, token in enumerate(tokens):
        if token.startswith('و'):
            is_exceptions = [token.startswith(exception) and len(token) <= len(exception) + 1 for exception in
                             tokenizer_exceptions]
            if True not in is_exceptions:
                tokens[i] = token[0] + ' ' + token[1:]
    text = (' '.join(tokens))
    text = text.replace(' وال', ' و ال')
    text = text.replace(' لل', ' ل ل')
    text = text.replace(' لإ', ' ل إ')
    text = text.replace(' بالأ', ' ب الأ')
    text = text.replace('وفقا ل', 'وفقا ل ')
    text = text.replace('نسبة ل', 'نسبة ل ')
 
    text = text.replace(' بال', ' ب ال')
    text = text.replace(' بب', ' ب ب')
    text = text.replace(' بم', ' ب م')
    return text
#------------------------------------------------------------------------
#clean word from dump chars:

dump_chars = '!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~’،ـ؟؛«» '
def clean_word(word):
    word = word.translate(str.maketrans({key: None for key in dump_chars})) 
    #remove tashkeel
    p_tashkeel = re.compile(r'[\u0617-\u061A\u064B-\u0652]')
    word = re.sub(p_tashkeel,"", word)
    
    return word
# ---------------------------------------------
# load the model
import pickle
import re

# load the model from disk
modelfilename = r'C:\my lap\Graduation proj\ArabicNER\Predication\lsvm.sav'
loaded_model = pickle.load(open(modelfilename, 'rb'))

# load the vectorizer from disk
vectorizerfilename = r'C:\my lap\Graduation proj\ArabicNER\Predication\vectorizer.pickle'
loaded_vectorizer = pickle.load(open(vectorizerfilename, 'rb'))

# load the tfidf from disk
tfidffilename = r'C:\my lap\Graduation proj\ArabicNER\Predication\tfidf.pickle'
loaded_tfidf = pickle.load(open(tfidffilename, 'rb'))


# --------------------------------------------------------
def RunNER(phrase):
    phrase=preprocess(phrase)
    # print(phrase)
    arr = phrase.split()
    y = []
    token = []
    for x in arr:
        x=clean_word(x)
        x = [x]
        test_str = loaded_vectorizer.transform(x)
        test_tfstr = loaded_tfidf.transform(test_str)
        test_tfstr.shape
        token.append(x)
        y.append(loaded_model.predict(test_tfstr.toarray())[0])
    return token, y
# --------------------------------------------------------
def ExtractSefat(txt):
    token, y = RunNER(txt)
    m = set()
    for i in range(0, len(token)):
        if (y[i] == "M"):
            m.add(token[i][0])
    return list(m)
#----------------------------------------------------------
def ExtractLocations(txt):
    token, y = RunNER(txt)
    l = set()
    for i in range(0, len(token)):
        if (y[i] == "B-LOC"):
            l.add(token[i][0])
    return list(l)

#=========================================================================
import mysql.connector

    
conn = mysql.connector.connect(
                host="db4free.net",
                user="fatimaelsaadny",
                database="al_sahaba_db",
                password="123456789")
    
#==========================================================================
def connect():
    """ Connect to MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(
                host="db4free.net",
                user="fatimaelsaadny",
                database="al_sahaba_db",
                password="123456789")
        if conn.is_connected():
            print('Connected to MySQL database')

    except Error as e:
        print(e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()
cursor = conn.cursor(buffered=True)
#====================================================================


def storeSefatInDb():
    ids = [2,21,22,23,24,25,26,27,28,29]
    print(ids)
 #1 fetch txt from database
    for id in ids:
        print(id)
        txt=cursor.execute('SELECT txtNarration FROM personalities where personId=%s', [id])
        txt =cursor.fetchone()
        print("txt",txt[0].decode("utf-8"))
        
        
        #2 Run Method
        res=ExtractSefat(txt[0].decode("utf-8"))
        print("result",res)
        
        
        #3 Store Ruselt
        records=cursor.execute('SELECT sefatName FROM `sefattable`')
        records = cursor.fetchall()
        print("records",records)
        newrec=list()
        for item in records:
            newrec.append(item[0])
        print("newrec",newrec)
        for sefa in res :
                if sefa not in newrec :
                    cursor.execute('INSERT INTO sefattable set sefatName =%s ',[sefa])
                    # conn.commit()
                    newsefa =cursor.execute('SELECT sefatName FROM `sefattable`ORDER BY sefatId DESC LIMIT 1')
                    newsefa = cursor.fetchone()
                    print("newsefa",newsefa)
                    
                    
        for sefa in res :  
            selectId =cursor.execute('SELECT sefatId FROM `sefattable`where sefatName=%s',[sefa])
            selectId=cursor.fetchone()
            print("selectId",selectId[0])
            ret = cursor.execute('INSERT INTO `personsefat`set `person_Id`=%s, `sefatId`=%s', (id,selectId[0]) )
            #conn.commit()
        
        ret = cursor.execute('SELECT sefatId FROM  personsefat where  person_Id =%s',[id])
        ret=cursor.fetchall()
        print("ret",ret)
    
#======================================================================
def storePlacesInDb():
 #1 fetch txt from database
    
    id=input("enter id: ")
    print(id)
    txt=cursor.execute('SELECT txtNarration FROM personalities where personId=%s', [id])
    txt =cursor.fetchone()
    print("txt",txt[0].decode("utf-8"))
    
    
    #2 Run Method
    res=ExtractLocations(txt[0].decode("utf-8"))
    print("result",res)
    
    
    #3 Store Ruselt
    records=cursor.execute('SELECT visitedPlaces FROM `placetble`')
    records = cursor.fetchall()
    print("records",records)
    newrec=list()
    for item in records:
        newrec.append(item[0])
    print("newrec",newrec)
    for place in res :
            if place not in newrec :
                cursor.execute('INSERT INTO placetble set visitedPlaces =%s ',[place])
                conn.commit()
                newsefa =cursor.execute('SELECT visitedPlaces FROM `placetble`ORDER BY placeId DESC LIMIT 1')
                newsefa = cursor.fetchone()
                print("newsefa",newsefa)
                
                
    for place in res :  
        selectId =cursor.execute('SELECT placeId FROM `placetble`where visitedPlaces=%s',[place])
        selectId=cursor.fetchone()
        print("selectId",selectId[0])
        ret = cursor.execute('INSERT INTO `visitedplaces`set `personId`=%s, `placeId`=%s', (id,selectId[0]) )
        conn.commit()
    
    ret = cursor.execute('SELECT placeId FROM  visitedplaces where  personId =%s',[id])
    ret=cursor.fetchall()
    print("ret",ret)
#=======================================================================
# while True:
#     storePlacesInDb()
#
