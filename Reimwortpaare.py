def reimwortpaare(wortliste):
    reimwörterbuch = {}
    for wort in wortliste:
        Endung_sortieren(wort, reimwörterbuch)
    ausgabeliste = []
    for key in reimwörterbuch:
        ausgabeliste = ausgabeliste + (paare_aus_liste(reimwörterbuch[key]))
    return ausgabeliste

def Endung_sortieren(wort, reimwörterbuch):
    # Das ist Regel 1
    Endung = bestimme_Endung(wort)
    # Hier Regel 2 testen
    Rest_des_wortes = len(wort) - len(Endung)
    if Rest_des_wortes <= len(Endung):
        if Endung in reimwörterbuch:
            reimwörterbuch[Endung].append( wort )
        else:
            reimwörterbuch[Endung] = [wort]

def bestimme_Endung(wort):
    umdrehwort = wort[::-1]
    vokal_zähler = 0
    Endung_string = ""
    stelle = 0
    letzte_voklgrup = ""
    while stelle < len(umdrehwort):
        buchstabe = umdrehwort[stelle]
        Endung_string = buchstabe + Endung_string
        if buchstabe in "aeiouäöü":
            while True:
                buchstabe = umdrehwort[stelle+1] # voraus schauen!
                if buchstabe in "aeiouäöü":
                    Endung_string = buchstabe + Endung_string # gehört zu Vokalgruppe
                    stelle += 1
                else:
                    break
            vokal_zähler += 1
            letzte_voklgrup = Endung_string
            if vokal_zähler == 2:
                break
        stelle += 1        
    return letzte_voklgrup

def eins_im_anderen(wort1, wort2):
    len1 = len(wort1)
    len2 = len(wort2)
    return (len1 < len2 and wort1.lower() == wort2[-len1:].lower())\
    or\
    (len1 > len2 and wort2.lower() == wort1[-len2:].lower())

def paare_aus_liste(wortliste):
    auspufffaf = []
    restlistee = wortliste
    while True:
        guckwort = restlistee[0]
        restlistee.pop(0)
        if len(restlistee) == 0:
            break
        for wort in restlistee:
            # Regel 3 ist hier
            if eins_im_anderen(guckwort, wort):
                continue
            paarliste = [guckwort, wort]
            auspufffaf.append(paarliste)
    return auspufffaf

def wortliste_aus_datei(datei):
    wortliste = []
    d = open(datei, 'r')
    for zeile in d:
        wortliste.append(zeile.strip('\n'))
    print(reimwortpaare(wortliste))
