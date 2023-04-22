import googletrans
from googletrans import *


translator = googletrans.Translator() 
text = "انا اسمي احمد"

if translator.detect(text).lang != "en":
    # Open a file to write the English text
    text = translator.translate(text,dest='en').text
with open('englishText.txt', 'w', encoding='utf-8') as file:
# Write Arabic text to the file
    file.write(text)
    
file.close()