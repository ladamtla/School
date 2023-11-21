
#semi-finished code, under writing...

import string
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def textSeparator(text):
    clean = ""
    marks = string.punctuation
    for ch in text:
        if ch == marks or ch == ".":
            pass
        else:
            clean += ch
    clean = clean.lower()
    clean = clean.split(" ")

    return clean

def containE(words: list):
    """
    :param words: lista a szavakról
    :return: Összes szó száma, "e" betű tartalmazása százalékban
    """
    all = len(words)
    cone = 0
    for word in words:
        for ch in word:
            if ch == "e":
                cone += 1
                break
    estat = cone/all*100
    return all, estat

def searcher(words, sword):
    """
    megszámolja a szavak között a szót és egy egész számot ad vissza
    :param words: lista a szavakról
    :param word: keresett szó
    :return: előfordulás egész számban
    """
    counter = 0
    for word in words:
        if word == sword:
            counter += 1
    return counter

def wordFrequency(words: list):
    """
    :param words: lista a szavakról
    :return: 2 lista: az első a lista az egyedi szavakból, a második az előfordulása számmal.
     + egyes szavak előfordulását adja írja ki
    """
    uniquewords = []
    frequency = []
    for word in words:
        if word in uniquewords:
            pass
        else:
            fr = searcher(words, word)
            frequency.append(fr)
            uniquewords.append(word)


    i = 0
    for uword in uniquewords:
        print(f"'{uword}' szó {frequency[i]} alkalommal fordul elő")
        i +=1

    return uniquewords, frequency

def wordCloudDrawer(matrix):
    # Szófelhő létrehozása a bemeneti mátrix alapján
    wordcloud_data = {word: freq for word, freq in matrix}
    wordcloud = WordCloud(width=600, height=600, background_color='white').generate_from_frequencies(wordcloud_data)

    # Grafikus megjelenítés
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

#Short text:
#text = "A textémát egyetemes szövegegységnek kell tekintenünk, hiszen ha egy szövegben nincsen legalább egy textéma, akkor a nyelvi szintekre épülő nyelvtan logikájának megfelelően azt kell mondanunk, hogy valamely kisebb nyelvi elem alkalmilag tölti be a szöveg szerepét. A textéma a szöveghez viszonyítva hasonló szerepet játszik, mint a tőmorféma a szavak megformálásában vagy az alany állítmányi szószerkezet a mondat kialakításában. A tipikus szövegmű minimális formai feltétele tehát a bekezdésnyi méretű szövegegység jelenléte."
#Long text:
text = "What is Chat GPT? ChatGPT is a state-of-the-art AI chatbot developed by OpenAI. It uses a neural network architecture to provide responses, which means that it can understand and answer questions without being explicitly told what the answer is. It can be used for a variety of tasks such as providing sales pitches, marketing strategies, proofreading code, and even drafting customer service emails. It’s like having a personal digital assistant that can help you with almost anything! Think of it as a super smart robot that can understand and respond to human language. Meet John, a talented programmer who is looking to start a company that uses his personally developed mobile application to connect restaurants and customers for booking and reservations. Even though the app was ready, John had difficulty getting together a team for his startup, needing separate people for sales, marketing, programming, content creation, and customer support. Hiring reliable manpower while being strict with his budget was getting difficult. He reached out to his friend Ryan who said John could start his company without hiring any new people, thanks to just a single AI-based tool. John couldn’t believe it, which led Ryan to introduce Chat GPT, the revolutionary AI chatbot being developed by OpenAI. It is a state-of-the-art natural language processing (NLP) model that uses a neural network architecture to provide responses. This means that the Chat GPT bot can answer questions without being explicitly told what the answer is, using its own intellect, unlike previous AI chatbots. So, how does Chat GPT help John in filling out his team? Regarding sales, Chat GPT can provide full-fledged sales pitches based on the correct prompts. It can provide tips on how to pitch your product businesses, removing the need for sales training completely, customized to your requirements and your prompts. If you don’t like some things about the response, you can ask for certain changes and the chatbot will make sure they are done. When it comes to marketing, Chat GPT can provide efficient marketing strategies which can help new entrepreneurs learn how to market their products to prospective clients. It can provide trending keywords that marketers can use for SEO purposes, while providing ad copies for your website and blog. Speaking of websites, since John can do a lot of the heavy lifting and programming, Chat GPT can help proofread the code and help out when looking for bugs to fix. Apart from basic bug fixing, it can also provide sample code structures for different programming languages, allowing John to focus more on improving core functionality and workflow rather than fixing basic code errors. Websites and blogs content is very helpful in gathering potential customer leads. The revolutionary bot can provide full-length blog posts with near-perfect fast accuracy in seconds, allowing further customization like choosing the length of the subject matter to the complexity of language. For John’s customer support, the bot can draft complete customer service emails based on the situation, saving time and resources. The tone of the message can be changed to reflect the nature of the message, creating an efficient alternative for call center professionals. John was left speechless seeing this level of versatility from Chat GPT and wanted to implement it right away. However, Ryan made sure John knew about some drawbacks of the chatbot before getting started. Since the bot is trained mostly on data up to 2021, many of the newer events may still need to be discovered by Chat GPT. Even basic stuff like asking about the current date and time is beyond its scope, much like the limited understanding of context despite providing near-lifelike solutions to certain problems. Even the accuracy of many responses can be questioned since the AI model is still learning and being developed. There is a section of the public that believes the revolutionary tool can one day replace Google search, but that day seems far-fetched so far because of the variety of issues people keep running into while using Chat GPT."

words = textSeparator(text)

print("Egyedi szvak külön-kölön a gyakoriságukkal:")
uwords, frequency = wordFrequency(words)
print("")


print("Szavak, külön-külön:")
print(words)
print("")

all, estat = containE(words)
print(f"Az összes szó száma: {all}, ebből {round(estat, 2)}% tartalmaz 'e' betűt.")

freMatrix = list(zip(uwords, frequency))
wordCloudDrawer(freMatrix)