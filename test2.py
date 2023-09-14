import gensim.models.keyedvectors as word2vec
model=word2vec.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin',binary=True)
import sys
import numpy as np

def get_score(tokens,ground_truth):
    sc2=[]
    for tk in tokens:
        i =0
        sc=[]
        for tk_2 in ground_truth:
            sim =model.similarity(tk,tk_2)
            print(i,tk,tk_2, sim)
            sc.append(sim)
            i = i + 1
        sc=np.array(sc)
        sc2.append(np.max(sc,axis=0))
    return sc2

#ground_truth=['Finland','University','UEF','Joensuu']
#tokens = ['Finland','Department','School','Computing','University', 'UEF', 'Science', 'Park', 'Joensuu']
#pred=['Finland','School','Park','Joensuu','UEF','Computing']

print(model.similarity(sys.argv[1],sys.argv[2]))

#token_scores= get_score(ground_truth,pred)
#token_scores