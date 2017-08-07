
# HashTable方法1
def isAnagram1(self, s, t):
  hash1 = {}
  hash2 = {}

  for char in s:
      if char in hash1:
          hash1[char] += 1
      else:
          hash1[char] = 1

  for char in t:
      if char in hash2:
          hash2[char] += 1
      else:
          hash2[char] = 1

  return hash1 == hash2

# HashTable方法2
def isAnagram2(self, s, t):
  hash1 = {}
  hash2 = {}

  for char in s:
      hash1[char] = hash1.get(char, 0 ) + 1
  for char in t:
      hash2[char] = hash2.get(char, 0) + 1

  return hash1 == hash2

# HashTable方法3  利用Unicode，创建2个 Fixed Size Array
def isAnagram3(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    hash1 = [0]*26
    hash2 = [0]*26

    for char in s:
        hash1[ord(char) - ord('a')] += 1
    for char in t:
        hash2[ord(char) - ord('a')] += 1

    return hash1 == hash2


# HashTable方法4  利用Unicode，创建1个 Fixed Size Array
def isAnagram4(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    arr = [0]*26

    for char in s:
        arr[ord(char) - ord('a')] += 1
    for char in t:
        arr[ord(char) - ord('a')] -= 1

    for num in arr:
        if num is not 0:
            return False
    return True
