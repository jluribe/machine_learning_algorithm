from __future__ import division
import operator

sample_memo = '''
Milt, we're gonna need to go ahead and move you downstairs into storage B. We have some new people coming in, and we need all the space we can get. So if you could just go ahead and pack up your stuff and move it down there, that would be terrific, OK?
Oh, and remember: next Friday... is Hawaiian shirt day. So, you know, if you want to, go ahead and wear a Hawaiian shirt and jeans.
Oh, oh, and I almost forgot. Ahh, I'm also gonna need you to go ahead and come in on Sunday, too...
Hello Peter, whats happening? Ummm, I'm gonna need you to go ahead and come in tomorrow. So if you could be here around 9 that would be great, mmmk... oh oh! and I almost forgot ahh, I'm also gonna need you to go ahead and come in on Sunday too, kay. We ahh lost some people this week and ah, we sorta need to play catch up.
'''

corrupted_memo = '''
Yeah, I'm gonna --- you to go ahead --- --- complain about this. Oh, and if you could --- --- and sit at the kids' table, that'd be --- 
'''

data_list = sample_memo.strip().split()

words_to_guess = ["ahead","could"]

### splitString working - used in main
import re

def splitString(sampletext):
    words = re.split('\W+', sampletext)
    words = filter(None, words)
    words = [x.lower() for x in words]
    for i, word in enumerate(words):
        if word == "re":
            word = "are"
        if word == "kay":
            word = "ok"
    return words


############################################################ RECURSIVE IMPLEMENTATION - WORKING        
class Node:
    word = ''
    depth = 0
    found_ixs = []
    count = 0
    p = 0.0
    p_joint = 0.0
    parent = None
    children = []

def findWords(node, words):
    #find the occurences of the_word and populate indices
    if not node:
        return
    
    for i, word in enumerate(words):
        if node.word == word:
            #print 'Found the_word = "{}" at ix {}'.format(word, i)
            node.found_ixs.append(i)            

def findNextWords(node, words):
    dict = {}
    #walk through all indices and find the next word
    for i in node.found_ixs:
        if((i+1)<len(words)):
            next_word = words[i+1]
            #print '**** Next word i={} "{}"'.format(i+1, next_word)
            node = dict.get(next_word) 
            if(not node):
                node = Node()
                node.found_ixs = []
                node.word = next_word
            node.found_ixs.append(i+1)
            dict[next_word] = node
            
    return dict
        
def totalNumWords(d):
    n = 0
    for key in d:
        node = d[key]
        n = n + len(node.found_ixs)
    return n

def constructTree(node, words, max_distance):
    cur_node = node
    if(cur_node.depth >= max_distance):
        return
    d = findNextWords(cur_node, words)
    #return
    #walk through the directory
    if(d):
        nwords = totalNumWords(d)
        #print 'At level {}, total number of words {}'.format(cur_node.depth, nwords)
        for key in d:
            node = d[key]
            node.count = len(node.found_ixs)
            node.p = node.count/nwords
            node.p_joint = node.p * cur_node.p
            node.parent = cur_node
            node.children = []
            node.depth = cur_node.depth + 1
            cur_node.children.append(node)

            #print '* ConstructTree Found="{}" with distance {} and prob {} and joint_p = {}'.\
        #                format(key, node.depth, node.p, node.p_joint)

        constructTree(node, words, max_distance)    
    return

def selectLikelyWord(node, at_distance, best_node, all_candidates):
    if node.depth == at_distance:
        all_candidates[node.word] = node.p_joint
        if best_node and node.p_joint > best_node.p_joint:
            #print 'selectLikelyWord: Found best node {} with p={}'.format(node.word, node.p_joint)
            return node
        
    for child in node.children:
        best_node = selectLikelyWord(child, at_distance, best_node, all_candidates)
                
    return best_node

def LaterWords(sample,word,distance):
    '''@param sample: a sample of text to draw from
    @param word: a word occuring before a corrupted sequence
    @param distance: how many words later to estimate (i.e. 1 for the next word, 2 for the word after that)
    @returns: a single word which is the most likely possibility
    '''
    
    # TODO: Given a word, collect the relative probabilities of possible following words
    # from @sample. You may want to import your code from the maximum likelihood exercise.
    words = splitString(sample)
    print 'The Word is "{}"'.format(word)

    if True:
        #initialize node with first word
        Root = Node()
        Root.word = word
        Root.found_ixs = []
        findWords(Root, words)
        constructTree(Root, words, distance)
        all_candidates = {}
        best_node = selectLikelyWord(Root, distance, Root, all_candidates)
        sort = sorted(all_candidates.items(), key=operator.itemgetter(1))
        return best_node.word
    else:
        info = collectInfo(words, word, distance)
        createTree(info, distance)
        
    return words

print LaterWords(sample_memo,"ahead",2)