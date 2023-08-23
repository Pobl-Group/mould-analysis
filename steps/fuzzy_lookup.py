"""
Return a DataFrame containing the mould analysis dataset.

Takes a DataFrame as input and applies functions from thefuzz and Levenshtien
libraries, returning the mould analysis dataset DataFrame.

Typical usage:
    ```
    from steps.fuzzy_lookup import get_fuzzy_lookup
    
    get_fuzzy_lookup(df, key_words, stop_words)
    ```
"""


import re
from pandas import DataFrame
from string import punctuation
from thefuzz import fuzz
from Levenshtein import distance as levenshtien_distance


def _preprocess_text(text: str) -> str:
    """
    String cleaning

    Takes a string and performs a number of cleansing tasks to keep them uniform.

    Args:
        text (String): string to be standardised.

    Returns:
        text (String): standardised string
    """

    text = text.lower()  # lowercase text conversion
    text = re.sub(r"[0-9]", " ", text)  # remove numbers
    text = re.sub(f"[{re.escape(punctuation)}]", " ", text)  # remove punctuation
    text = " ".join(text.split())  # Remove extra spaces, tabs, and new lines

    return text


def get_fuzzy_lookup(df: DataFrame, key_words: list, stop_words: list) -> DataFrame:
    """
    Performs a fuzzy lookup on a given DataFrame and provides metrics on the lookup.

    Manipulates the string of the description column in given DataFrame, produces
    fuzzy and levenstein values comparing description against list of key and
    stop words.

    Args:
        df (Dataframe): Dataframe with an ID and a 'description' column

    Returns:
        df (Dataframe): Dataframe of original and new descriptions and scores
            for those descriptions
    """

    df["original_description"] = df["description"]

    df["description"] = df["description"].fillna(" ")

    df["description"] = df["description"].map(_preprocess_text)

    stop_word_removal = lambda x: " ".join(w for w in x.split() if not w in stop_words)

    df["description"] = df["description"].apply(stop_word_removal)

    for index, row in df.iterrows():

        fuzzy_score = []

        max_fuzzy_score = []

        levenshtien_score = []

        set_ratio = []

        simple_search = 0

        for token in set(row["description"].split(" ")):

            for keyword in key_words:

                fuzzy_score.append(fuzz.ratio(token, keyword))

                levenshtien_score.append(levenshtien_distance(token, keyword))

            max_fuzzy_score = max(fuzzy_score)

            min_levenshtien_score = min(levenshtien_score)

            if token in key_words:

                simple_search = 100

        set_ratio = fuzz.partial_token_set_ratio(key_words, row["description"])

        df.loc[index, "one_to_one_ratio"] = max_fuzzy_score

        df.loc[index, "set_ratio"] = set_ratio

        df.loc[index, "leven_score"] = min_levenshtien_score

        df.loc[index, "simple_search"] = simple_search

        df.loc[index, "best_score"] = max(max_fuzzy_score, set_ratio, simple_search)

    return df
