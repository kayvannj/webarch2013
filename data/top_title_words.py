"""
    python find_top_titles.py anonymous-msweb.data
"""
    
import csv
import fileinput
from sys import stdout


def csv_readline(line):
    """Given a sting CSV line, return a list of strings."""
    for row in csv.reader([line]):
        return row


def main():
    csv_writer = csv.writer(stdout)
    words = {}
    for line in fileinput.input():
        cell = csv_readline(line)
        if cell[0] == 'A':
            cell = cell[3:-1]
            for t in cell:
                for w in t.split(" "):
                    if w not in words.keys():
                        words[w]=1    
                    else:
                        words[w]+=1


    sorted_words =  sorted(words.iteritems(), key=lambda x: x[1])
    sorted_words.reverse()

    for i in range(10):
        print "{0}\t{1}".format(sorted_words[i][0],sorted_words[i][1])


if __name__ == '__main__':
    main()
