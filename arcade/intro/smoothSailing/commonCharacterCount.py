def solution(s1, s2):
    freq1 = {c: s1.count(c) for c in set(s1)}
    freq2 = {c: s2.count(c) for c in set(s2)}
    
    return sum(min(freq1.get(x), freq2.get(x)) if freq2.get(x) else 0 for x in freq1)