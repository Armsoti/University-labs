import nltk
from nltk.corpus import gutenberg, stopwords
from nltk.probability import FreqDist
import matplotlib.pyplot as plt

nltk.download('gutenberg')
nltk.download('punkt')
nltk.download('stopwords')

# Завантажуємо текст "Гамлета"
text = gutenberg.words('shakespeare-hamlet.txt')

print(f"Завдання для тексту: 'shakespeare-hamlet.txt'")
print("-" * 30)

total_words = len(text)
print(f"Загальна кількість слів у тексті: {total_words}")

words_raw = [word.lower() for word in text if word.isalpha()]
fdist_raw = FreqDist(words_raw)
top10_raw = fdist_raw.most_common(10)

print("10 найбільш вживаних слів (до очищення):")
print(top10_raw)

words_r, counts_r = zip(*top10_raw)
plt.figure(figsize=(10, 6))
plt.bar(words_r, counts_r, color='blue')
plt.title('Топ-10 слів у "Гамлеті" (до очищення)')
plt.xlabel('Слова')
plt.ylabel('Частота')
plt.show()


stop_words = set(stopwords.words('english'))
words_cleaned = [
    word.lower()
    for word in text
    if word.isalpha() and word.lower() not in stop_words
]

fdist_cleaned = FreqDist(words_cleaned)
top10_cleaned = fdist_cleaned.most_common(10)

print("10 найбільш вживаних слів (після очищення від стоп-слів):")
print(top10_cleaned)

words_c, counts_c = zip(*top10_cleaned)
plt.figure(figsize=(10, 6))
plt.bar(words_c, counts_c, color='green')
plt.title('Топ-10 слів у "Гамлеті" (після очищення)')
plt.xlabel('Слова')
plt.ylabel('Частота')
plt.show()