from typing import List, Iterable

def pipeline_step_one_get_short_words(words:List[str], max_length:int=10) -> Iterable[str]:
    """
    :param words: list of input words
    :param max_length: the max word length
    :return: words that are shorter than max_length
    """
    for word in words:
        if len(word) <= max_length:
            yield word

def pipeline_step_two_uppercase(words:Iterable[str]) -> Iterable[str]:
    """
    :param words: list of input words
    :return: words in uppercase
    """
    for word in words:
        yield word.upper()

def pipeline_step_three_print(words:Iterable[str]):
    """
    :param words: list of input words
    """
    for word in words:
        print(word)

def run_pipeline(words:List[str]):
    result_of_step_one = pipeline_step_one_get_short_words(words)
    result_of_step_two = pipeline_step_two_uppercase(result_of_step_one)
    pipeline_step_three_print(result_of_step_two)

words = ["theraininspainstaysonly", "on", "the", "plain"]

run_pipeline(words)


