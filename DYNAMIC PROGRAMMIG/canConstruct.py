def canconstruct(target, wordbank):
   if target == "":
      return True

   for str in wordbank:
      if target.startswith(str):
         rest = target[len(str):]
         result = canconstruct(rest, wordbank)
         if result == True:
            return True
   return False

# print(canconstruct("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaak", ['a', 'abc', 'cd', 'def', 'abcd', 'f']))

# print(canconstruct("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaz", ["a", "a", "a", "a", "a"]))

"""
   memoization approach
"""

def canconstruct_memo(target, wordbank, memo=None):
   if memo is None:
      memo = {}
   if target in memo:
      return memo[target]
   if target == "":
      return True
   
   for str in wordbank:
      if target.startswith(str):
         rest = target[len(str):]
         result = canconstruct_memo(rest, wordbank, memo)
         if result is True:
            memo[target] = True
            return True

   memo[target] = False
   return False

# print(canconstruct_memo("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaak", ['a', 'abc', 'cd', 'def', 'abcd', 'f']))

# print(canconstruct_memo("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaz", ["a", "a", "a", "a", "a"]))

# This will likely cause a RecursionError on most systems
# print(canconstruct_memo("a" * 999 + "b", ["a", "aa", "aaa", "aaaa", "aaaaa"]))


"""
   bottom up approach
"""

def canconstruct_tab(target, wordbank):
   len_str = len(target)
   array = [False for _ in range(len_str + 1)]
   array[0] = True

   for i in range(len_str):    
      if array[i] is True:
         for str in wordbank:
            if target[i:i+len(str)] == str and i + len(str) <= len_str:
               array[i + len(str)] = True

   return array[len_str]

# Example 1: Should return True
print(canconstruct_tab("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))

# Example 2: Should return false
print(canconstruct_tab("skateboards", ["sk", "ate", "board", "bo", "ard", "ska", "te"]))

# Example 3: Should return False
print(canconstruct_tab("hellos", ["he", "llo", "hel", "lo", "world"]))

# Example 4: Should return true
print(canconstruct_tab("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
# print(canconstruct_tab("abc", ['ab', 'a', 'bc', 'c']))


# print(canconstruct_tab("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaz", ["a", "a", "a", "a", "a"]))

# This will likely cause a RecursionError on most systems
print(canconstruct_tab("a" * 10000 + "b", ["a", "aa", "aaa", "aaaa", "aaaaa"]))