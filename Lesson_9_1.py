def popular_words(text, words):
    text_lower = text.lower()
    words_list = text_lower.split()
    dict_count = {}
    for word in words:
        dict_count[word] = 0
    # dict_count = {word: 0 for word in words}

    for word_in_text in words_list:
        if word_in_text in dict_count:
            dict_count[word_in_text] += 1

    return dict_count


assert popular_words('''Hi! When I was One I had just begun When I was Two I was nearly new ''',
                     ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
print('OK')
