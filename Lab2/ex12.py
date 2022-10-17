from typing import List


def ex12(input_words: List[str]) -> List[List[str]]:
   
    return [t for t in
            [[input_words[x] for x in range(y, len(input_words)) if input_words[x][-2:] == input_words[y][-2:] and
              input_words[x][-2:] not in [input_words[w][-2:] for w in range(y)]] for y in range(len(input_words))]
            if len(t) > 0]

if __name__ == '__main__':
    print(ex12(['ana', 'banana', 'carte', 'arme', 'parte']))