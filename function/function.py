sentence = '''
Meet my family. There are five of us – my parents, my elder brother, my baby sister and me. First, meet my mum and dad, Ja
ne and Michael. My mum enjoys reading and my dad enjoys playing chess with my brother Ken. My mum slim and is rather tall. She has long red hair and 
'''

words=sentence.split()
print(words)
for word in words:
    if sentence.count(word)>0:
        origen=word
        temp=word.upper()
        sentence=sentence.replace(origen, temp)
print(sentence)