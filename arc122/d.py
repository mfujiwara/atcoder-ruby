class TrieNode:
    def __init__(self):
        self.children = [None,None]
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, s):
        cur = self.root
        for ch in s:
            i=int(ch)
            if cur.children[i]==None:
                cur.children[i]=TrieNode()
            cur = cur.children[i]
    def mini(self, s):
        cur=self.root
        ret=""
        for ch in s:
            i=int(ch)
            if cur.children[i]:
                cur=cur.children[i]
                ret+="0"
            else:
                cur=cur.children[1-i]
                ret+="1"
        return ret
N=int(input())
array=list(map(int, input().split()))
array.sort()
def calc(array):
    #print(array)
    if len(array)==0 or array[-1]==0:
        return 0
    max_bit=array[-1].bit_length()    
    array1=[]
    max_bit=pow(2,max_bit-1)
    while array and array[-1]>=max_bit:
        array1.append(array.pop()-max_bit)
    array1=array1[::-1]
    if len(array)%2==0:
        # 最大bitは考慮しなくていいように分割して再起
        return max(calc(array),calc(array1))
    else:
        tree=Trie()
        for a in array:
            tree.insert(bin(a+max_bit)[2:])
        ret=bin(2*max_bit-1)[2:]
        for a in array1:
            v=tree.mini(bin(a+max_bit)[2:])
            ret=min(ret,v)
        return int(ret,2)+max_bit
ret=calc(array)
print(ret)
