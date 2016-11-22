import re


def words(wordm):
    wordy = re.findall(r"\b[0-9a-zA-Z]+\-?[a-zA-Z]+\b|\b[a-zA-Z]+\b", wordm)
    if len(wordy) == 0:
        return None
    else:
        return wordy


def phone_number(phnum):
    digits = re.findall(r"^\(?\d{3}\)?\s?\-?\.?\d{3}\s?\-?\.?\d{4}$", phnum)
    if len(digits) == 0:
        return None
    else:
        dictionary = {}
        areac = re.search(r"(^\(?\d{3})", phnum)
        if areac:
            areag = areac.group(1)
            areaf = areag[-3] + areag[-2] + areag[-1]
        digitsn = re.search(r"(\d{3}\s?\-?\.?\d{4}$)", phnum)
        if digitsn:
            digitsg = digitsn.group(1)
            digitss = digitsg[0] + digitsg[1] + digitsg[2] + "-" + digitsg[-4] + digitsg[-3] + digitsg[-2] + digitsg[-1]
        dictionary["area_code"] = areaf
        dictionary["number"] = digitss
        return dictionary


def money(mon):
    curmoney = re.search(r"^\$\d+$|^\$\d+\.\d\d$|^\$\d+\,\d{3}$|^\$\d+\,\d{3}\.\d\d$|^\$\d+\,\d{3}\,\d{3}$|^\$\d+\,\d{3}\,\d{3}\.\d\d$", mon)
    if curmoney is not None:
        dictionarym = {}
        numberper = re.findall(r"^\$\d+$|^\$\d+\.\d\d$|^\$\d+\,\d{3}$|^\$\d+\,\d{3}\.\d\d$|^\$\d+\,\d{3}\,\d{3}$|^\$\d+\,\d{3}\,\d{3}\.\d\d$", mon)
        cleanednum = ""
        for n in numberper[0]:
            if n in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:
                cleanednum += n
        amount = float(cleanednum)
        curex = numberper[0][0]
        dictionarym["currency"] = curex
        dictionarym["amount"] = amount
        return dictionarym


def zipcode(zippy):
    zipps = re.findall(r"^\d{5}$|^\d{5}\-\d{4}$", zippy)
    dictzip = {}
    if zipps:
        valzip = zipps[0]
        if len(valzip) == 5:
            dictzip["zip"] = valzip
            dictzip["plus4"] = None
            return dictzip
        else:
            firstf = valzip[0] + valzip[1] + valzip[2] + valzip[3] + valzip[4]
            last4 = valzip[6] + valzip[7] + valzip[8] + valzip[9]
            dictzip["zip"] = firstf
            dictzip["plus4"] = last4
            return dictzip


def date(dates):
    calendy = re.findall(r"^\d\d?\/\d\d?\/\d{4}$|^\d{4}\-\d\d?\-\d\d?$", dates)
    dictcal = {}
    if calendy:
        if "-" in calendy:
            year = int(calendy[0] + calendy[1] + calendy[2] + calendy[3])
            month = int(calendy[5] + calendy[6])
            day = int(calendy[8] + calendy[9])
            dictcal["month"] = month
            dictcal["day"] = day
            dictcl["year"] = year
            return dictcal
        else:
            year = int(calendy[-4] + calendy[-3] + calendy[-2] + calendy[-1])
            monthy = re.search(r"^(\d\d?)\/\d\d?\/\d{4}$|^\d{4}\-\d\d?\-\d\d?$", dates)
            if monthy:
                mont = monthy.group(0)
            month = int(mont)
            dayey = re.search(r"^\d\d?\/(\d\d?)\/\d{4}$|^\d{4}\-\d\d?\-\d\d?$", dates)
            if dayey:
                da = dayey.group(0)
            day = int(da)
            dictcal["month"] = month
            dictcal["day"] = day
            dictcl["year"] = year
            return dictcal



def email(document_to_search):
    return re.findall(r"", document_to_search)


def address(document_to_search):
    return re.findall(r"", document_to_search)
