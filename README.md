arg 1 is a space separated cipher text
arg 2 is a "type B" key

example usage:

```mook$ cat bacon-bacon.txt

A A A A B A A A A A A A A B A A B B A B A B B A A

mook$ python bacon.py bacon-bacon.txt B

[+]output: BACON key: B 1```

dictionary bruteforce method:

```for w in `cat dictionary.txt`; do python bacon.py bacon-bacon.txt $w;done```
