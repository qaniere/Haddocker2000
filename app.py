import os
import time
import requests
from gtts import gTTS
from playsound import playsound


class Haddocker:

    def __init__(self, display_menu = False, iterations = 1, voice = "fr"):
        
        if os.path.isdir("sentences"):
            pass
        else:
            os.mkdir("sentences")

        if display_menu:
            print("Bienvenue marin d'eau douce !")
            iterations = int(input("Combien de fois voulez-vous générer des politesses ? >> "))
            voice = input("Quelle voix souhaitez-vous entendre ? (Française = fr, Québecoise = ca) >> ")

        for i in range(iterations):
            sentence = self.get_insults()
            filename = self.generate_voice(sentence, voice)
            self.play_sentence(filename)


    def get_insults(self) -> str:

        data = requests.get("http://www.zoglu.net/haddock/index.php")
        data = data.text.split("\n")

        for i in range(len(data)):
            if "insults" in data[i]:
                sentence = data[i].replace('<td><em id="insults">', "")
                sentence = sentence.replace("</em></td>", "")
                break

        return sentence


    def generate_voice(self, sentence:str, voice:str) -> str:

        filename = "sentences/" + str(time.time()) + ".mp3"
        tts = gTTS(sentence, lang="fr", tld=voice)
        tts.save(filename)
        
        return filename


    def play_sentence(self, filename:str):

        playsound(filename)
        os.remove(filename)

if __name__ == "__main__":
    app = Haddocker(display_menu=True)
