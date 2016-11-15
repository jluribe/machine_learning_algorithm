#
#   Maximum Likelihood Hypothesis
#
#
#   In this quiz we will find the maximum likelihood word based on the preceding word
#
#   Fill in the NextWordProbability procedure so that it takes in sample text and a word,
#   and returns a dictionary with keys the set of words that come after, whose values are
#   the number of times the key comes after that word.
#   
#   Just use .split() to split the sample_memo text into words separated by spaces.

def NextWordProbability(sampletext,word):
    # wordlist = sampletext.split()
    # wordindex = wordlist.index(word)
    # newwordlist = wordlist[wordindex+1:len(wordlist)]
    # newdict = {}
    # for index, curword in enumerate(newwordlist):
    #     if curword in newdict:
    #       newdict[curword] = newdict[curword] + 1
    #     else:
    #       newdict[curword] = 1

    # return newdict
    # generate a list of words
    wordlist = sampletext.split()
    # check if a particular preceding word is in the word list or not, if so, return the indecies
    if word in wordlist:
        indecies = [i for i,x in enumerate(wordlist) if x == word]
    else:
        pass
    # the indecies of words after the preceding word
    indecies_after = [i+1 for i in indecies]
    # return a list of the words after the preceding word
    newwordlist = [wordlist[i] for i in indecies_after]
    wordcount = {}
    for word in newwordlist:
        if word in wordcount:
            wordcount[word] += 1
        else:
            wordcount[word] = 1
    
    return wordcount

sample_memo = '''
Milt, we're gonna need to go ahead and move you downstairs into storage B. We have some new people coming in, and we need all the space we can get. So if you could just go ahead and pack up your stuff and move it down there, that would be terrific, OK?
Oh, and remember: next Friday... is Hawaiian shirt day. So, you know, if you want to, go ahead and wear a Hawaiian shirt and jeans.
Oh, oh, and I almost forgot. Ahh, I'm also gonna need you to go ahead and come in on Sunday, too...
Hello Peter, whats happening? Ummm, I'm gonna need you to go ahead and come in tomorrow. So if you could be here around 9 that would be great, mmmk... oh oh! and I almost forgot ahh, I'm also gonna need you to go ahead and come in on Sunday too, kay. We ahh lost some people this week and ah, we sorta need to play catch up.
'''

print NextWordProbability(sample_memo, "gonna")
