def all_construct(target, wordbank):
   if target == "":
      return [[]]
   
   array_2d = []
   for word in wordbank:
      if target.startswith(word):
         rest = target[len(word):]
         result = all_construct(rest, wordbank)
         for i in range(len(result)):
            result[i] = [word] + result[i]
         array_2d += result


   return array_2d

# print(all_construct("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaz", ["a", "aa", 'b']))
   
"""
   memoization approach
"""

def all_construct_memo(target, wordbank, memo=None):
   if memo is None:
      memo = {}
   if target in memo:
      return memo[target]
   if target == "":
      return [[]]
   
   array_2d = []

   for word in wordbank:
      if target.startswith(word):
         rest = target[len(word):]
         result = all_construct_memo(rest, wordbank, memo)
         for i in range(len(result)):
            result[i] = [word] + result[i]
         array_2d += result

   memo[target] = array_2d
   return array_2d

# print(all_construct_memo("aabz", ["a", "aa", 'b']))
# print(all_construct_memo("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", ["a", "aa", 'b']))

"""
   bottom up approach
"""

def all_construct_tab(target, wordbank):
   target_len = len(target)
   array = [[] for _ in range(target_len + 1)]
   array[0] = [[]]

   for i in range(target_len):
      for word in wordbank:
         if target[i: i + len(word)] == word:
            new_combi = [combination + [word] for combination in array[i]]
            array[i + len(word)] += new_combi

   return array[target_len]
print(all_construct_tab("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabz", ["aa", "a", "b"]))