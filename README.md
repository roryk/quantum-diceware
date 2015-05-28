Quantum diceware password generation
========================================================================
[![Build Status](https://secure.travis-ci.org/roryk/quantum-diceware.svg)](http://travis-ci.org/roryk/quantum-diceware)
quantum-diceware uses the
[quantumrandom](https://github.com/lmacken/quantumrandom) package to grab random
numbers from the ANU Quantum Random Numbers Server while generating the words
from the [diceware](http://world.std.com/~reinhold/diceware.html) wordlist.

If you want a really good password, use quantum-diceware to generate a word list, write
it down and keep it in your wallet and make up a story with the words in it. When
you are entering your password try to remember the words just using the story.
If you forget, look at the
word list. After a while you won't need to refer to the word list and you can stick it
someplace safe. A little bit after that you won't need to refer to the story anymore either.

This is useful for making a very long password for Dropbox or 1Password, something that
has the keys to the castle and needs a super good password that is also something you can
type easily.

Usage
=====
    quantum-diceware.py [-h] [-s SEPARATOR] [-f WORDFILE] numwords

Example
=======
    quantum-diceware.py 6
    clomped rash toxic twirling 6th sung

Silly sample story
============
Silly Suzy the Singer clomped over to the bathroom in her Doc Martens to get some cream for her rash.
Unfortunately, the cream was toxic and at her concert that night while she was twirling the
mic during her 6th song, she collapsed. And that was the last time that song was ever sung.

History
=======
This was originally written as a joke, but now I actually use it. Joke is on me.

Rationale
=========
![rationale](http://imgs.xkcd.com/comics/password_strength.png)

Authors
=======
@roryk, @grahams
