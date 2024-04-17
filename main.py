# text_analysis.py
import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

def analyze_text(text):
    tokens = word_tokenize(text)
    freq_dist = FreqDist(tokens)
    return freq_dist

def print_frequency_distribution(freq_dist):
    print("Top 30 most frequent words:")
    for word, frequency in freq_dist.most_common(30):
        print(f"{word}: {frequency}")

def main():
    import sys
    if len(sys.argv) != 2:
        print("Usage: python text_analysis.py <text>")
        return
    text = sys.argv[1]
    freq_dist = analyze_text(text)
    print_frequency_distribution(freq_dist)


if __name__ == "__main__":
    nltk.download('punkt')
    main()
