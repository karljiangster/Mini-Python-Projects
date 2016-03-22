# CS121: Auto-completing keyboard using Tries
#
# usage: python trie_dict.py <dictionary filename>
#
# YOUR NAME(s) HERE

import os
import sys
from sys import exit
import tty
import termios
import fcntl
import string

import trie_shell

count = "count"
final = "final"


class Trie: 

    def __init__(self):
        self.children = {}
        self.count = 0 
        self.final = False 

    def insert(self, word): #Inserts a word into the Trie.
        self.count += 1 
        if not word: 
            self.final = True 
            return 
        if not word[0] in self.children: 
            self.children[ word[0] ] = Trie()

        self.children[ word[0] ].insert( word[1:] )


    def get_child(self, word): 
        '''
        Returns the descendant node of the given word. 
        If the given word is not in the Trie, will return an empty Trie 
        (count = 0 & final = False)
        ''' 

        if not word: 
            return self
        if word[0] not in self.children: 
            return Trie() 
        return self.children[ word[0] ].get_child( word[1:] )


    def contains(self, word): #Returns whether the word is in the Trie
        return self.get_child(word).final 


    def get_contents(self): 
        contents = [] 
        if self.final: 
            contents += [""]
        for c in self.children: 
            contents += map( lambda s: c + s, self.children[c].get_contents() )

        return contents 


def create_trie_node():
    return Trie()


def add_word(word, trie):
    if not trie.contains(word): 
        trie.insert(word)


def is_word(word, trie):
    return trie.contains(word)

def num_completions(word, trie):
    return trie.get_child(word).count
    

def get_completions(word, trie, search_prefix = True):
    return trie.get_child(word).get_contents()


if __name__ == "__main__":
    trie_shell.go("trie_dict")

