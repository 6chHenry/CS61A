class Link:
    empty = ()
    def __init__(self,first,rest=empty):
        assert rest is Link.empty or isinstance(rest,Link)
        self.first = first
        self.rest = rest
    def __repr__(self):
        if self.rest:
            rest_repr = ',' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr +')'
    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.fisrt) + ' '
            self = self.first
        return string + str(self.first) + '>'
def range_link(start,end):
    """Return a link contaning consecutive integers from start to end"""
    if start >= end:
        return Link.empty
    else:
        return Link(start,range_link(start + 1,end))
def map_link(f,s):
    """Return a Link that contains f(x) for each x in Link s"""
    if s is Link.empty:
        return s
    else:
        return Link(f(s.first)),map_link(f,s.rest)
def filter_link(f,s):
    """Return a Link that contains only the elements x of Links for which f(x) is a true value"""
    if s is Link.empty:
        return s
    filtered_rest = filter_link(f,s.rest)
    if f(s.first):
        return Link(s.first,filtered_rest)
    else:
        return filtered_rest
odd = lambda x : x% 2 == 1
square = lambda x : x* x

r = range_link(1,6)
s = filter_link(odd,r)
t = map_link(square,s)

def add(s,v):
    if s.first > v:
        s.first,s.rest = v,Link(s.first,s.rest)
    elif s.first < v and is_empty(s.rest):
        s.rest = Link(v)
    elif s.first < v:
        add(s.rest,v)
    return s
def is_empty(m):
    if m == ():
        return True
    else:
        return False
class Tree:
    def __init__(self,label,branches=[]):
        self.label = label
        for branch in branches:
            assert isinstance(branch,Tree)
        self.branches = list(branches)
    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(repr(self.label),branch_str)
    def __str__(self):
        return '\n'.join(self.indented())
    def indented(self):
        lines = []
        for b in self.branches:
            for line in b.indented():
                lines.append(' ' + line)
        return [str(self.label)] + lines
    def is_leaf(self):
        return not self.branches

def fib_tree(n):
    if n == 0 or n == 1:
        return Tree(n)
    else:
        left = fib_tree(n-2)
        right = fib_tree(n-1)
        fib_n = left.label + right.label
        return Tree(fib_n,[left,right])
def leaves(t):
    if t.is_leaf():
        return [t.label]
    else:
        all_leaves = []
        for b in t.branches:
            all_leaves.extend(leaves(b))
        return all_leaves
def height(t):
    if t.is_leaf():
        return 0
    else:
        return 1 + max([height(b) for b in t.branches])