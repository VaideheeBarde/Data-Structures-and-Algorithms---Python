class BstNode:
    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right

def pair_includes_ansector_and_descendant_of_m(possible_anc_or_desc_0, possible_anc_or_desc_1, middle):
    search_0, search_1 = possible_anc_or_desc_0, possible_anc_or_desc_1

    #Perform interleaved searching from possible anc_or_desc_0 and
    #possible_anc_or_desc_1 for middle

    while (search_0 is not possible_anc_or_desc_1 and search_0 is not middle and search_1 is not possible_anc_or_desc_0 and search_1 is not middle and (search_0 or search_1)):
        if search_0:
            search_0 = (search_0.left if search_0.data > middle.data else search_0.right)
        if search_1:
            search_1 = (search_1.left if search_1.data > middle.data else search_1.right)

    #If both searches were unsuccessful, or we got from 
    #possible_anc_or_desc_0 to possible_anc_or_desc_1 without seeing middle, or from
    #possible_anc_or_desc_1 to possible_anc_or_desc_0 without seeing middle, that means
    #middle cannot lie between possible_anc_or_desc_0 and possible_anc_or_desc_1

    if ((search_0 is not middle and search_1 is not middle) or search_0 is possible_anc_or_desc_1 or search_1 is possible_anc_or_desc_0):
        return False
    
    def search_target(source, target):
        while source and (source is not target):
            source = source.left if source.data > target.data else source.right
        return source is target

    #If we get here, we already know one of the possible_anc_or_desc_0 or possible_anc_or_desc_1 has a path to middle
    #Check if middle has a path to possible_anc_or_desc_1 or to possible_anc_or_desc_0
    return search_target(middle, possible_anc_or_desc_1 if search_0 is middle else possible_anc_or_desc_0)

m = BstNode(31)
l = BstNode(29, None, m)
n = BstNode(41)
k = BstNode(37, l, n)
p = BstNode(53)
j = BstNode(23, None, k)
o = BstNode(47, None, p)
i = BstNode(43, j, o)
h = BstNode(13)
g = BstNode(17, h)
d = BstNode(2)
e = BstNode(5)
c = BstNode(3, d, e)
f = BstNode(11, None, g)
b = BstNode(7, c, f)
a = BstNode(19, b, i)

print(pair_includes_ansector_and_descendant_of_m(a, k, j))
print(pair_includes_ansector_and_descendant_of_m(i, m, j))
print(pair_includes_ansector_and_descendant_of_m(i, p, o))
print(pair_includes_ansector_and_descendant_of_m(b, a, i))
print(pair_includes_ansector_and_descendant_of_m(n, k, j))