'''
Created on Feb 15, 2015

@author: Vinodh Periyasasmy

Module that contains implementation for apriori algorithm - which is used for frequent 
item set mining and associate rule mining.

Apriori is based on the premise that any subset of a frequent item set should be frequent as well. Alternatively,
if any subset of a given set S is infrequent, then the set S will also be infrequent.

Credits: Jiawei Han: Pattern Discovery in Data Mining. Coursera Course.

Runs O (n * n)

'''

from sets import Set
from __builtin__ import int
import logging


#Input Transaction Database

tran1 = Set(['I1', 'I2', 'I5'])
tran2 = Set(['I2', 'I4'])
tran3 = Set(['I2', 'I3'])
tran4 = Set(['I1', 'I2', 'I4'])
tran5 = Set(['I1', 'I3'])
tran6 = Set(['I2', 'I3'])
tran7 = Set(['I1', 'I3'])
tran8 = Set(['I1', 'I2','I3','I5'])
tran9 = Set(['I1', 'I2', 'I3'])

alltransactions = [tran1, tran2, tran3, tran4, tran5, tran6, tran7, tran8, tran9]

'''

Mines the frequent item sets given the minimum support value & prints them

'''

def apriori(min_support):
    if(not isinstance(min_support, int)):
        raise ValueError('Minimum Support Should be an Integer!')
        
    logging.info('Minimum Support specified is {}'.format(min_support))
    
    freq_set = generateOneItemSets(min_support);
    logging.debug('One Item Candidates Sets are {}'.format(freq_set));
    candidates = frozenset(freq_set.keys());
    
    logging.debug('One Item Candidates {}'.format(candidates));
    
    # Initialize Item Set Size to start from 2
    item_set_size = 2;
    while len(candidates) > 0:
        candidates = pruneNonFrequent(generateCandidates(candidates, item_set_size), min_support)
        logging.info('Frequent Item Sets of size {} are {} '.format(item_set_size, candidates))
        item_set_size = item_set_size + 1;
        
    
    

def generateOneItemSets(min_support):
    logging.debug('All transactions from db are {}'.format(alltransactions))
    oneItemSet = {};
    for tran in alltransactions:
        for item in tran:
            logging.debug('item is {}'.format(item))
            itemset = frozenset([item]);
            oneItemSet[itemset] = oneItemSet.get(itemset,0) + 1;
            logging.debug('the key and value are {} & {} respectively'.format(itemset, oneItemSet[itemset]))
    
    # Remove Items that don't have a minimum support 
    oneItemSet = {key: value for key, value in oneItemSet.items() if value >= min_support}                
    return oneItemSet;

'''
Function to generate all possible candidates
'''
def generateCandidates(candidates, itemset_size):
    ret = set(i.union(j) for i in candidates for j in candidates if len(i.union(j)) == itemset_size)
    return ret    
        

'''
Function to remove candidates that don't meet the minimum support threshold 
'''    
def pruneNonFrequent(candidates, min_support):
    ret = set();
    for candidate in candidates:
        count = 0;
        for tran in alltransactions:
            if(candidate.issubset(tran)):
                count = count + 1
        if(count >= min_support):       
            ret.add(candidate);
    
    logging.debug('the return values are {}'.format(ret))        
    return ret;

