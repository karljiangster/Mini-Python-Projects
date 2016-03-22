from trie_dict import create_trie_node, add_word, \
is_word, num_completions, get_completions, Trie


def test_add_words(words): 
    t = create_trie_node()
    for word in words: 
        add_word(word, t)
    return t

def test_is_word(): 
    print("Testing is_word")
    words = ["are", "and", "a", "an", "be", "bee", "Be"]
    t = test_add_words(words)
    for word in ["hippie", "are", "a", "bee", "Be", "an", "b", "ar"]: 
        if ( is_word(word, t) != (word in words) ): 
            print("\tfailed on: ", word)

    print("Finished testing is_word")

def test_completions(): 
    t = create_trie_node()

test1()


'''
print(is_word("Be", t, True))
print(is_word("arerferf", t))
print(is_word("and", t))
print(is_word("a", t))
print(is_word("an", t))
print(is_word("bee", t))
print(get_next_letters(t['a']))


print("and", num_completions("and", t))#1
print("b", num_completions("b", t)) #1
print("be", num_completions("be", t))#1
print("a", num_completions("a", t)) #4

print(trie_prefix("an", t))
''' 


'''
t2 = create_trie_node() 
add_word("a", t2)

add_word("are", t2)
'''


'''t3 = create_trie_node()
add_word("a", t3) 
add_word("and", t3)
add_word("are", t3)
add_word("art", t3)
add_word("ate", t3)
print(get_completions("a", t3))'''





#t1 test 
#print(get_completions("a", t))

# Example of an assertion. If "bee" was not inserted
# correctly in the trie, the following statement will
# cause the program to exit with an error message.

#assert is_word("are", t)
'''
def permutations(p):
    if len(p) == 1:
        # Base case
        return [ p ]
    else:
        # Recursive case
        rv = []
        for x in p:
            # List without 'x'
            p_prime = [v for v in p if v!=x]
            print(p_prime)
            perms = permutations(p_prime)
            for perm in perms:
                pl = [x] + perm
                rv.append(pl)
        return rv
permutations([1,2,3])
'''