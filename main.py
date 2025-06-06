import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    call: sys.exit(1)

franky = sys.argv[1]

def main(get_book_text):
    with open(get_book_text) as f:
        book_text = f.read()
    return book_text

# franky = "books/frankenstein.txt"

# print(main(franky))

frankwords = main(franky)

from stats import wordcounter
from stats import tpcfreq
from stats import freqsort
from stats import sort_on

wordcount = wordcounter(frankwords)
charcount = tpcfreq(frankwords)
charlist = freqsort(frankwords)

diclist = []
diclist = freqsort(frankwords)
diclist.sort(reverse=True, key=sort_on)

def flatdic(sorted):
    sortlist = []
    for dic in sorted:
        entry = (f"{dic['char']}: {dic['num']}")
        sortlist.append(entry)
        print(entry)
    return sortlist

finlist = []
# print(f"{charlist}")
# print(diclist)
# formatting the report

print("============ BOOKBOT ============")
print(f"Analyzing book found at {franky}...")
print("----------- Word Count -----------")
print(f"Found {wordcount} total words")
print(f"--------- Character Count -------")
finlist = flatdic(diclist)
print(f"============= END ===============")
