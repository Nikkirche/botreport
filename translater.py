from requests import post, get
from json import dumps, loads

IAM_TOKEN = "t1.9euelZqJjMnGzcqZjZCUmc2Wl8_Kze3rnpWazY3Ik8qLlJeXisyOjM-NnMnl9PdoO3kA-u93ZTW13fT3KGp2APrvd2U1tQ.2zJOxE6O6LIb5zxOZZDSqHg7HlUVBaidWPIMCHSKGPu2MT5r7JrO1LVtaWg1qfaqGHcDhBcigZax-qvcQLFWDw"
url = "https://translate.api.cloud.yandex.net/translate/v2/translate"


def translate(text: str) -> str:
    data = {
        "folder_id": "b1gpoqph9r3nvu2knf3f",
        "texts": [text],
        "targetLanguageCode": "ru",
        "sourceLanguageCode": "en"
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {IAM_TOKEN}"
    }
    response = post(url=url, data=dumps(data), headers=headers)

    return loads(response.text)["translations"][0]['text']


if __name__ == '__main__':
    # print(translate('''"West Bromwich Albion" vs "Newcastle United"
    # And so "Ajayi Semi" gets a yellow card.
    #
    # An excellent player, Jay Ajayi is from United Kingdom , was born on 1993-06-15  and is 6 ft 0 in (1.83 m) tall ;
    # weighs 223 lb (101 kg)'''))
    print(translate(""""Астон Вилла" против Вулверхэмптон Уондерерс
Луис Дуглас skhlopotal "gorchichnik" 

Luizão is coming from Brazil and was born on 1975-11-14 , is of 1.81 m (5 ft 11 in . Luizão weighs 76 кг"""))