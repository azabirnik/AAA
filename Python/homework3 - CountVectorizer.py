# Aleksei Zabirnik <azabirnik@gmail.com>
# Avito Academy homework 3 - CountVectorizer class

from typing import List


class CountVectorizer:
    """ CountVectorizer is a class a simple text vectorization """
    stop_words = {'a', 'the'}

    def __init__(self) -> None:
        """ Sets empty feature_names list """
        self.feature_names = None

    def fit_transform(self, corpus: List[str]) -> List[List[int]]:
        """ Transfprm corpus of texts into bag of words vectors """
        tokenized_texts = [text.lower().split() for text in corpus]
        self.feature_names = list(set([word for text in tokenized_texts for word in text])
                                  - self.stop_words)
        # self.feature_names.sort() may be added to use with bisect() search instead of index()
        feature_vectors = [[0]*len(self.feature_names) for x in range(len(tokenized_texts))]
        for i in range(len(tokenized_texts)):
            feature_vector = feature_vectors[i]
            tokenized_text = tokenized_texts[i]
            for word in tokenized_text:
                feature_vector[self.feature_names.index(word)] += 1
        return feature_vectors

    def get_feature_names(self) -> List[str]:
        """ Get names of features as a list """
        return self.feature_names


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    names_list = vectorizer.get_feature_names()
    for i in range(len(names_list)):
        print(f'{names_list[i]:>20}, {count_matrix[0][i]}, {count_matrix[1][i]}')
