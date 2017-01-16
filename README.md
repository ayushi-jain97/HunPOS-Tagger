# HunPOS-Tagger

--tested on Ubuntu 16.04

HunPOS is an open-source Part of Speech Tagger available in NLTK (Toolkit for NLP in Python).

# Installation
https://code.google.com/archive/p/hunpos/source
You may need to install additional packages --libn32curses5 and lib32z1 depending on your OS.

# Running the code

Training data
--train.txt
Format: word tab POS tag

Testing data
--test.txt
Divide the testing data into two files: one that contains words(test_set.txt) and other contains the corresponding POS tags(test_label.txt)

To train the tagger - You can either use the pre trained models available or simple train your own tagger
hunpos-train mytagger < train.txt

To test the data against the testing set using trained tagger
hunpos-tag mytagger < test_set.txt

To save the labelled output to a file --output.txt
hunpos-train mytagger < test_set.txt > output.txt

# Additional parameter
In particular, -t is used to set the number of tags that are taken as context in the contextual probabilities. Default value of t is 2 (Trigram model).
hunpos-train mytagger -t 1 < train.txt

