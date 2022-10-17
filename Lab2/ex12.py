from typing import List

def ex12(words: List[str]) -> List[List[str]]:
   
    return [t for t in
            [[words[x] for x in range(y, len(words)) 
            if words[x][-2:] == words[y][-2:] and #verfica ca ultimele 2 litere sa fie la fel
            words[x][-2:] not in [words[w][-2:] 
            for w in range(y)]]
            for y in range(len(words))]
            if len(t) > 0]

if __name__ == '__main__':
    print(ex12(['ana', 'banana', 'carte', 'arme', 'parte']))