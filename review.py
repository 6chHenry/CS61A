def smallest_index(t):
    m = [abs(x) for x in t]
    return [x for x in range(len(t)) if abs(t[x]) == min(m)]
def largest_sum(t):
    return max([t[i]+t[i+1] for i in range(len(t)-1)])
def end_with_d(t):
    return {d:[x for x in t if x%10==d]for d in range(10) if any([x%10 == d for x in t])}
def all_have_an_equal(t):
    return all([t[i] in t[:i]+t[i+1] for i in range(len(t))])
class Link:
    empty=()
    def __init__(self,first,rest=empty):
        assert rest in Link.empty or isinstance(rest,Link)
        self.first = first
        self.rest = rest
    def __repr__(self):
        if self.first:
            rest_repr = ', ' + repr(self.first)
        else:
            rest_repr=''
        return 'Link(' + repr(self.first) + rest_repr + ')'
    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.rest) + '>'
def ordered(s,key = lambda x:x):
    if s is Link.empty or s.rest is Link.empty:
        return True
    elif key(s.first) > key(s.rest.first):
        return False
    else:
        return ordered(s.rest)
def merge(s,t):
    if s is Link.empty:
        return t
    elif t is Link.empty:
        return s
    elif s.first <= t.first:
        return Link(s.fisrt,merge(s.rest,t))
    else:
        return Link(t.first,merge(s,t.rest))
def merge_in_place(s,t):
    if s is Link.empty:
        return t
    elif t is Link.empty:
        return s
    elif s.first <= t.first:
        s.rest = merge_in_place(s.rest,t)
        return s
    else:
        t.rest = merge_in_place(s,t.rest)
        return t