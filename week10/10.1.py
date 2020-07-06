from sklearn.feature_extraction import CountVectorizer

with open('moby_dick.txt', 'r') as book:
    vectorizer = CountVectorizer()

    fit = vectorizer.fit_transform(book)
    document_idx = vectorizer.vocabulary_['wood']
    document_count = sum(res[:,document_idx])
    print('document occurs {} times in the text'.format(document_count))