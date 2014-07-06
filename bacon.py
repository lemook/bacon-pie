from sys import argv
import itertools

#cipher will be a file with each char seperated by a space
cipher = open(argv[1],'rb').read().split(' ')

def split_seq(iterable, size):
    it = iter(iterable)
    item = list(itertools.islice(it, size))
    while item:
        yield item
        item = list(itertools.islice(it, size))

print len(argv)
if len(argv)>3:
  key=list(argv[2])
else:
  if ' ' in argv[2]:
    key = argv[2].replace('\n','').split(' ')
  else:
    key = argv[2]

bacon_map = {'AAAAA':'A','AAAAB':'B','AAABA':'C','AAABB':'D','AABAA':'E','AABAB':'F','AABBA':'G','AABBB':'H','ABAAA':'I','ABAAB':'K','ABABA':'L','ABABB':'M','ABBAA':'N','ABBAB':'O','ABBBA':'P','ABBBB':'Q','BAAAA':'R','BAAAB':'S','BAABA':'T','BAABB':'U','BABAA':'W','BABAB':'X','BABBA':'Y','BABBB':'Z'}

digrams = ['TH', 'HE', 'IN', 'ER', 'AN', 'RE', 'ED', 'ON', 'ES', 'ST', 'EN', 'AT', 'TO', 'NT', 'HA', 'ND', 'OU', 'EA', 'NG', 'AS', 'OR', 'TI', 'IS', 'ET', 'IT', 'AR', 'TE', 'SE', 'HI', 'OF']

trigrams = ['THE', 'ING', 'AND', 'HER', 'ERE', 'ENT', 'THA', 'NTH', 'WAS', 'ETH', 'FOR', 'DTH']

def score(w):
  r = 0
  for d in digrams:
    if d in w:
      r+=w.count(d)
  for d in trigrams:
    if d in w:
        r+=w.count(d)
  return r


def main():
  ret=""
  cipher_list = []
  for i in split_seq(cipher,5):
    cipher_list.append(i)
  for block in cipher_list:
    pattern = ""
    for character in block:
      t = ""
      for k in key:
        if character == k:
          t += "B"
      if t=="B":
        pattern+="B"
      else:
        pattern+="A"
    if pattern in bacon_map:
      ret+=bacon_map[pattern]
    else:
      ret+="!"
  scor=score(ret)
  print "[+]output: " + ret + " key: " + ''.join(key) + " " + str(scor)

main()
