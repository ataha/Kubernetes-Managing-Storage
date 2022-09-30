import os.path
import csv
from multiprocessing import Pool
import sys
import time
import re


words_to_replace = {}
with open('/Users/ahmedhagag/Downloads/Python-replace-script/replace.csv') as csv_file:
    for word in csv.reader(csv_file, delimiter=','):
        words_to_replace[word[0]] = word[1]

def process_file(name):
    '''Process one file: count number of lines and words'''
    start = time.time()
    inp = open(name, 'r')

    words_replaced = []
    ocurrences = 0
    lines = []

    allLines = inp.read().splitlines()
    print("[%s] [%s] Has %d lines" % (time.time() - start, name, len(allLines)))
    for line in allLines:
        for word in words_to_replace:
            if word.lower() in line.lower():
                line = re.sub(word, words_to_replace[word], line, flags=re.I)
                ocurrences += 1
                if [word, words_to_replace[word]] not in words_replaced:
                    words_replaced.append([word, words_to_replace[word]])
        lines.append(line)
    #print(words_replaced)
    #print()
    #print(lines)

    #print('===============')
    inp.close()

    for word in words_replaced:
        print("[%s] [%s] '%s' -> '%s'" % (time.time() - start, name, word[0], word[1]))

    if len(words_replaced):
        inp = open(name, 'w')
        inp.write("\n".join(lines))
        inp.close()
    else:
        print("[%s] [%s] No changes made" % (time.time() - start, name))

    print("[%s] [%s] Processed." % (time.time() - start, name))
    print()
    return ocurrences


def process_files_parallel(arg):
    p = Pool()
    #print('-------')
    #print(arg)
    results = p.map(process_file, arg)
    for x in range(len(arg)):
        print("Replacements made: %d" % results[x])

"""if __name__ == '__main__':
    #file = '/Users/ahmedhagag/Personal/PycharmProjects/Automate_boaring_stuff/venv/test-upword'
    process_files_parallel(sys.argv[1:])"""



if __name__ == '__main__':
    start = time.time()
    process_files_parallel(sys.argv[1:])
    print("Completed in", time.time()-start, "ms")

#print(words_to_replace)
#print('=====================')



#process_file('/Users/ahmedhagag/Personal/PycharmProjects/Automate_boaring_stuff/venv/test-upword')


