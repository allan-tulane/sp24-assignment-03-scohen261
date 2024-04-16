import math, queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            return(MED(S[1:], T[1:]))
        else:
            return(1 + min(MED(S, T[1:]), MED(S[1:], T)))


def fast_MED(S, T, MED={}):
  if (S, T) in MED:
      return MED[(S, T)]

  if len(S) == 0:
      MED[(S, T)] = len(T)
      return len(T)

  if len(T) == 0:
      MED[(S, T)] = len(S)
      return len(S)

  if S[0] == T[0]:
      MED[(S, T)] = fast_MED(S[1:], T[1:], MED)
      return MED[(S, T)]

  MED[(S, T)] = 1 + min(
      fast_MED(S, T[1:], MED),   
      fast_MED(S[1:], T, MED),    
      fast_MED(S[1:], T[1:], MED) 
  )
  return MED[(S, T)]

def fast_align_MED(S, T, MED={}):
  if (S, T) in MED:
      return MED[(S, T)]

  if len(S) == 0:
      MED[(S, T)] = (len(T), "-" * len(T), T)
      return (len(T), "-" * len(T), T)

  if len(T) == 0:
      MED[(S, T)] = (len(S), S, "-" * len(S))
      return (len(S), S, "-" * len(S))

  if S[0] == T[0]:
      MED[(S, T)] = fast_align_MED(S[1:], T[1:], MED)
      return (MED[(S, T)][0], S[0] + MED[(S, T)][1], T[0] + MED[(S, T)][2])

  insertion = fast_align_MED(S, T[1:], MED)
  deletion = fast_align_MED(S[1:], T, MED)
  substitution = fast_align_MED(S[1:], T[1:], MED)

  min_distance = min(insertion[0], deletion[0], substitution[0])

  if min_distance == insertion[0]:
      aligned_S = "-" + insertion[1]
      aligned_T = T[0] + insertion[2]
  elif min_distance == deletion[0]:
      aligned_S = S[0] + deletion[1]
      aligned_T = "-" + deletion[2]
  else:
      aligned_S = S[0] + substitution[1]
      aligned_T = T[0] + substitution[2]

  MED[(S, T)] = (min_distance + 1, aligned_S, aligned_T)

  return MED[(S, T)]
