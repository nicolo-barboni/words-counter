import streamlit as st
import re
from collections import Counter


def most_frequent_words(titles):
    """
    Takes a list of title strings and returns a list of tuples (word, count)
    sorted by frequency in descending order.
    """
    words = []
    for title in titles:
        # Convert to lowercase and extract words (ignoring punctuation)
        title_words = re.findall(r'\b\w+\b', title.lower())
        words.extend(title_words)
    return Counter(words).most_common()


st.title("Word Frequency Counter")

st.write("Enter your titles below (one per line):")
titles_input = st.text_area("Titles")

if st.button("Compute Frequencies"):
    # Split the input by lines and remove any empty lines
    titles = [line for line in titles_input.split("\n") if line.strip() != ""]

    if titles:
        result = most_frequent_words(titles)
        st.write("### Word Frequencies:")
        str_result = ''
        for word, count in result:
            str_result += f"{word}: number of times repeated {count}\n"
        text_to_show = st.text(str_result)
    else:
        st.error("Please enter at least one title.")
