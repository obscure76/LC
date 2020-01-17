class Solution(object):
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        swl = [x.lower() for x in wordlist]
        wll = [len(x) for x in wordlist]
        r = []
        vowels = ['a', 'e', 'i', 'o', 'u']
        for w in queries:
            if len(w) not in wll:
                r.append("")
                continue
            if w in wordlist:
                r.append(w)
                continue
            found = False
            lw = w.lower()
            if lw in swl:
                r.append(wordlist[swl.index(lw)])
                continue
            if found:
                continue
            for sw in swl:
                if len(sw) != len(lw):
                    continue
                for i in range(len(sw)):
                    if (sw[i] in vowels) or sw[i] == lw[i]:
                        continue
                    else:
                        break
                else:
                    r.append(wordlist[swl.index(sw)])
                    found = True
                    break
            if not found:
                r.append("")
        return r

    def spellchecker2(self, wordlist, queries):
        word_set = set(wordlist)
        word_map = {x: True for x in word_set}
        lower_map = {x.lower(): x for x in word_set}
        devowel_map = {self.replace_all(x): x for x in word_set}
        for i in range(len(queries)):
            if queries[i] in word_map:
                continue
            lower_query = queries[i].lower()
            if lower_query in lower_map:
                queries[i] = lower_map[lower_query]
                continue
            devowel_query = self.replace_all(queries[i])
            if devowel_query  in devowel_map:
                queries[i] = devowel_map[devowel_query]
                continue

            queries[i] = ''
        return queries

    def replace_all(self, st):
        for c in 'aeiou':
            st = st.replace(c, '#')
        return st


s = Solution()
wordlist = ["YellOw"]
queries = ["yllw"]
print s.spellchecker(wordlist, queries)
wordlist = ["KiTe","kite","hare","Hare"]
queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
output = ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]

print wordlist
print queries
print s.spellchecker2(wordlist, queries)
print output
print "\n\n\n"


wordlist = ["v","t","k","g","n","k","u","h","m","p"]
queries = ["n","g","k","q","m","h","x","t","p","p"]
output = ["n","g","k","","m","h","","t","p","p"]
print s.spellchecker(wordlist, queries)
print output

print "\n\n\n"
print wordlist
print queries
print s.spellchecker2(wordlist, queries)
print output