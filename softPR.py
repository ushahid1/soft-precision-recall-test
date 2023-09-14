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
            try:
                sim =model.similarity(tk,tk_2)
                print(i,tk,tk_2, sim)
                sc.append(sim)
                i = i + 1
            except KeyError:
                sc.append(0)
                i = i + 1
        sc=np.array(sc)
        sc2.append(np.max(sc,axis=0))
    return sc2

def get_softP(pred_scores):
    sum1=0
    for tk_score in pred_scores:
        sum1= sum1 + tk_score
        
    return sum1/len(pred_scores)
def get_softR(gt_scores):
    sum1=0
    for tk_score in gt_scores:
        sum1= sum1 + tk_score
        
    return sum1/len(gt_scores)
	
pred= sys.argv[1]
gt = sys.argv[2]

pred= pred.split()
gt= gt.split()

print(get_softP(get_score(pred,gt)))
print(get_softP(get_score(gt,pred)))
#token_scores= get_score(ground_truth,pred)
#token_scores