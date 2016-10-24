#!/usr/bin/env python

import json
import sys
# import re

class AmazonParser:
    def __init__(self, path=None, outpath=None):
        self.path = path
        self.outpath = outpath
        self.text = ""

    def parse(self):
        with open(self.path, "r") as f:
            self.amz_string = f.read()
            self.amz_string = self.amz_string.replace('}\n', '},\n')
            self.amz_string = "[ {} ]".format(self.amz_string[0:len(self.amz_string)-2])
            # print(len(self.amz_string))
            # print(self.amz_string[len(self.amz_string)-500:len(self.amz_string)])
            amzdict = json.loads(self.amz_string)
            for review in amzdict:
                self.text += "{} ".format(review["reviewText"])

    def saveCorpus(self):
        with open(self.outpath, "w") as f:
            f.write(self.text)

def main():
    home_kitchen10k = AmazonParser(sys.argv[1], sys.argv[2])
    home_kitchen10k.parse()
    home_kitchen10k.saveCorpus()

if __name__ == "__main__":
    main()
