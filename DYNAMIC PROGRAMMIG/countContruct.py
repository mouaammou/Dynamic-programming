def count_construct(target, wordbank):
   if target == "":
      return 1
   
   count = 0
   for str in wordbank:
      if target.startswith(str):
         rest = target[len(str):]
         result = count_construct(rest, wordbank)
         count += result

   return count

# print(count_construct('aaaab', ['a', 'aa', 'b']))
# # ...existing code...

# print(count_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))  # Output: 1
# print(count_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))  # Output: 0
# print(count_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))  # Output: 4

# # Famous "purple" example
# print(count_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))  # Output: 2

# # where recursion need memoization:
# print(count_construct("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",["a", "aa", "aaaa", "aaaaa"]))

"""
   memoization approach
"""

def countcontruct_memo(target, wordbank, memo=None):
   if memo is None:
      memo = {}
   if target in memo:
      return memo[target]
   if target == "":
      return 1

   count = 0
   for word in wordbank:
      if target.startswith(word):
         rest = target[len(word):]
         result = countcontruct_memo(rest, wordbank, memo)
         count +=result

   memo[target] = count
   return count

# print("&&&&&&&&&&&&&&&&&&&& memoization approach: *****************************")
# print(countcontruct_memo('aaaab', ['a', 'aa', 'b']))
# # ...existing code...

# print(countcontruct_memo('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))  # Output: 1
# print(countcontruct_memo('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))  # Output: 0
# print(countcontruct_memo('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))  # Output: 4

# # Famous "purple" example
# print(countcontruct_memo('purple', ['purp', 'p', 'ur', 'le', 'purpl']))  # Output: 2

# # where recursion need memoization:
# print(countcontruct_memo("a" * 998 + "b",["a", "aa", "aaaa", "aaaaa"]))


"""
   bottom - up approach
"""

def countconstruct_tab(target, wordbank):
   target_len = len(target)
   array = [0 for _ in range(target_len + 1)]
   array[0] = 1

   for i in range(target_len + 1):
      # if array[i] != 0:
         for word in wordbank:
            if target[i: i + len(word)] == word:
               array[i + len(word)] += array[i]
   return array[target_len]
print("&&&&&&&&&&&&&&&&&&&& bottom up approach: *****************************")
print(countconstruct_tab('aab', ['a', 'aa', 'b']))
# # ...existing code...

print(countconstruct_tab('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))  # Output: 1
print(countconstruct_tab('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))  # Output: 0
print(countconstruct_tab('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))  # Output: 4

# Famous "purple" example
print(countconstruct_tab('purple', ['purp', 'p', 'ur', 'le', 'purpl']))  # Output: 2

# where recursion need memoization:
print(countconstruct_tab("a" * 100000 + "b",["a", "aa", "aaaa", "aaaaa"]))