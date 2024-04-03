def main():
    book_path = 'books/frankenstein.txt'
    text = get_books_path(book_path)
    count_words = get_amount_of_words(text)
    count_letters = get_amount_of_letters(text)
    sort_letters = get_sort_letters(count_letters)

    print(f'--- Begin report of {book_path} ---')
    print(f'{count_words} words found in the document')
    for sort in sort_letters:
        if sort['chr'].isalpha():
            print(f'The "{sort['chr']}" was found {sort['num']} times')
    print('--- End report ---')
        


def num(d):
    return d['num']

def get_sort_letters(sort):
    sorted_list = []
    for s in sort:
        sorted_list.append({'chr':s, 'num':sort[s]})
        sorted_list.sort(reverse=True, key=num)
    return sorted_list



def get_amount_of_letters(text):
    chart_dict = {}
    for t in text:
        lowered = t.lower()
        if lowered in chart_dict:
            chart_dict[lowered] += 1
        else:
            chart_dict[lowered] = 1
    return chart_dict


def get_amount_of_words(text):
    words = text.split()
    return len(words)
    


    

def get_books_path(path):
    with open(path) as file:
        return file.read()

main()