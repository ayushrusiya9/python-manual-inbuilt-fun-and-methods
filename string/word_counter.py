def word_counter(sent):
    count = 0
    # is_word = False
    for ch in sent:
        if ch == ' ':
            count += 1
            # is_word = True
        # elif ch == ' ':
            # is_word = False

    return count + 1

sentance = 'my name is ayush rusiya'
print(word_counter(sentance))