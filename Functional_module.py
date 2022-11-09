from nltk import PorterStemmer
from sklearn.metrics.pairwise import  cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer



def consine_sim_vectors(vec1,vec2):
    vec1 = vec1.reshape(1, -1)
    vec2 = vec2.reshape(1,-1)
    return cosine_similarity(vec1,vec2)[0][0]





def _processing_text(text):

    stemmer = PorterStemmer()
    buf = " "
    sentence = []
    for i in text:
        if i == " " or i == "" or i == "\n":
            buf = stemmer.stem(buf)
            sentence.append(buf.lstrip())
            buf = ""
        buf += i
    return sentence


def add_dict(array, dict_text):
    for w in array:
        if w in dict_text:
            dict_text[w] += 1
        else:
            dict_text[w] = 1
    return dict_text


def search_sentence(array_one, array_two):
    use_sentence = False
    x = len(array_one)
    y = len(array_two)
    if y > x:
        special_arrey = []
        num1 = 0
        while y > x:
            special_arrey.append(" ".join(array_one[num1:x - 1]))
            num1 = x
            x += x
        special_arrey.append(" ".join(array_two))
        vectorizer = CountVectorizer().fit_transform(special_arrey)
        vectors = vectorizer.toarray()
        end_result = []
        for i in range(len(vectors)):
            for j in range(len(vectors)):
                end_result.append(consine_sim_vectors(vectors[i], vectors[j]))

        for i in end_result:
            if i >= 0.6 and i != 1:
                use_sentence = True
                break
        print(vectors)

    if y == x:
        special_arrey = []
        special_arrey.append(" ".join(array_one))
        special_arrey.append(" ".join(array_two))
        vectorizer = CountVectorizer().fit_transform(special_arrey)
        vectors = vectorizer.toarray()
        end_result = consine_sim_vectors(vectors[0], vectors[1])
        if end_result >= 0.6 and end_result != 1:
            use_sentence = True
    return use_sentence