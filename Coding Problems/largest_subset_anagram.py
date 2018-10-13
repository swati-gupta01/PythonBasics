from collections import Counter
def find_ana_pair(str):
    str=str.lower().split(' ')
    print(str)
    for i in range(0,len(str)):
        str[i]=''.join(sorted(str[i]))
    print(str)
    freq_d=Counter(str)
    return (max(freq_d.values()))


str='Ant Magenta magnate tan gnamate'
print(find_ana_pair(str))