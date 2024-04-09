def get_pair_counts(lst):
    pair_dict = {}
    for i in range(len(lst) - 1):
        pair = (lst[i], lst[i+1])
        if pair in pair_dict:
            pair_dict[pair] += 1
        else:
            pair_dict[pair] = 1
    #sorted_pair_counts = sorted(pair_dict.items(), key=lambda x: x[1], reverse=True)
    #return sorted_pair_counts
    return pair_dict




def pair_switch(token,pair,new_pair):
    i=0
    np=[]
    while i < len(token):
        if i<len(token)-1 and token[i] and token[i]==pair[0] and token[i+1]==pair[1]:
            np.append(new_pair)
            i+=2
        else :
            np.append(token[i])
            i+=1
    return np


def bpe(tokens):
    merges = {}
    vocab_size=276
    number_of_merges=vocab_size-256
    bpe_tokens=list(tokens)
    for i in range(number_of_merges):
        pair_dict=get_pair_counts(bpe_tokens)
        pair = max(pair_dict, key=pair_dict.get)
        print(f"Token {pair} is merged as {i+256}")
        bpe_tokens=pair_switch(bpe_tokens,pair,i+256)
        merges[pair] = i+256
    return merges,bpe_tokens