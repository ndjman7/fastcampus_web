# 1. 일단 회문인지 파악.
# 2. 재귀호출로 모든 경우의 수를 만든다.(Memorize)
# 3. 경우의 수 에서 회문을 파악하면 리스트에 넣어준다.

def is_palindrome(word):
    return True if(word == word[::-1]) else False

def make_all_word(word,start):
    if word == ""
    new_word = ""
    for char in word:
        new_word +=char
