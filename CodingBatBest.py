# 1
# Warmup-1 > sleep_in
# The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a 
# weekday or we're on vacation. Return True if we sleep in.

# sleep_in(False, False) → True
# sleep_in(True, False) → False
# sleep_in(False, True) → True

def sleep_in(weekday, vacation):
	return(not weekday or vacation)


###################################################################################################
# 2
# Warmup-1 > monkey_trouble
# We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if they are both 
# smiling or if neither of them is smiling. Return True if we are in trouble.

# monkey_trouble(True, True) → True
# monkey_trouble(False, False) → True
# monkey_trouble(True, False) → False

def monkey_trouble(a_smile, b_smile):
	return(a_smile == b_smile)


###################################################################################################
# 3
# Warmup-1 > sum_double
# Given two int values, return their sum. Unless the two values are the same, then return double their sum.

# sum_double(1, 2) → 3
# sum_double(3, 2) → 5
# sum_double(2, 2) → 8

def sum_double(a, b):
	return((a + b) + (a == b)*(a + b))


###################################################################################################
# 4
# Warmup-1 > pos_neg
# Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only 
# if both are negative.

# pos_neg(1, -1, False) → True
# pos_neg(-1, 1, False) → True
# pos_neg(-4, -5, True) → True

def pos_neg(a, b, negative):
  return((negative and a+b<0) or (not negative and a*b<0))  



###################################################################################################
# 5
# Warmup-2 > array_count9
# Given an array of ints, return the number of 9's in the array.

# array_count9([1, 2, 9]) → 1
# array_count9([1, 9, 9]) → 2
# array_count9([1, 9, 9, 3, 9]) → 3

def array_count9(nums):
  	count = 0
  	for num in nums:
    	count += num == 9
  	return(count)


###################################################################################################
# 6
# Warmup-2 > array_front9
# Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.

# array_front9([1, 2, 9, 3, 4]) → True
# array_front9([1, 2, 3, 4, 9]) → False
# array_front9([1, 2, 3, 4, 5]) → False
## Bonne Solution:
def array_front9(nums):
	end = len(nums)
  	if end > 4:
    	end = 4
  	for i in range(end):
    	if nums[i] == 9:
     	return(True)
  	return(False)

## Mauvaise solution:
##### Plusieurs pb:
# 1- On réassigne une nouvelle valeur à nums, ce qui n'est pas nécessaire dans la première solution
# 2- On parcourt toute la liste, alors que dans la première solution, la boucle s'arrête dès qu'un élément de la liste vaut 9
 def array_front9(nums):
 	count = 0
  	if len(nums) > 4:
    	nums = nums[:4]
  	for num in nums:
    	count += num == 9
  	return(count>0)

###################################################################################################
# 7
# Warmup-2 > string_match
# Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" 
# yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.

# string_match('xxcaazz', 'xxbaaz') → 3
# string_match('abc', 'abc') → 2
# string_match('abc', 'axc') → 0

def string_match(a, b):
  	count = 0
  	l = min(len(a), len(b))
  	for i in range(l-1):
    	count += a[i:i+2] == b[i:i+2]
  	return(count)

# !!!! Caution: use range(l-1) to avoid index out of bound when comparing letters 2 by 2.


###################################################################################################
# 8
# Logic-2 > make_bricks
# We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) 
# and big bricks (5 inches each). Return True if it is possible to make the goal by choosing from the
# given bricks. This is a little harder than it looks and can be done without any loops.

# make_bricks(3, 1, 8) → True
# make_bricks(3, 1, 9) → False
# make_bricks(3, 2, 10) → True

def make_bricks(small, big, goal):
  	if big == 0:
    	return(goal <= small)
  	else:
    	q = goal//5
    	r = goal%5
    	if (q <= big and r <= small):
     	 	return(True)
    	else:
      		big_all = big*5
      		goal_reste = goal - big_all
      		if(q > big and goal_reste <= small):
        		return(True)
      		else:
        		return(False)


###################################################################################################
# 9
# Logic-2 > lone_sum
# Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, it does not count towards
# the sum.

# lone_sum(1, 2, 3) → 6
# lone_sum(3, 2, 3) → 2
# lone_sum(3, 3, 3) → 0

def lone_sum(a, b, c):
  	return(a*(a!=b)*(a!=c)+b*(b!=a)*(b!=c)+c*(c!=a)*(c!=b))


###################################################################################################
# 10
# Logic-2 > lucky_sum
# Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does not count towards the sum and values to its 
# right do not count. So for example, if b is 13, then both b and c do not count.

# lucky_sum(1, 2, 3) → 6
# lucky_sum(1, 2, 13) → 3
# lucky_sum(1, 13, 3) → 1

def lucky_sum(a, b, c):
  	return((a!=13)*(a + (b!=13)*(b + (c!=13)*c)))


###################################################################################################
# 11
# Logic-2 > round_sum
# For this problem, we'll round an int value up to the next multiple of 10 if its rightmost digit is 
#  or more, so 15 rounds up to 20. Alternately, round down to the previous multiple of 10 if its 
#  rightmost digit is less than 5, so 12 rounds down to 10. Given 3 ints, a b c, return the sum of
#   their rounded values. To avoid code repetition, write a separate helper "def round10(num):" and 
#   call it 3 times. Write the helper entirely below and at the same indent level as round_sum().

# round_sum(16, 17, 18) → 60
# round_sum(12, 13, 14) → 30
# round_sum(6, 4, 4) → 10

def round_sum(a, b, c):
  	return(round10(a) + round10(b) + round10(c))

def round10(num):
  	r = num%10
  	q = num//10
  	return((r >= 5)*((q+1)*10) + (r < 5)*(q*10))



###################################################################################################
# 12
# String-2 > cat_dog
# Return True if the string "cat" and "dog" appear the same number of times in the given string.

# cat_dog('catdog') → True
# cat_dog('catcat') → False
# cat_dog('1cat1cadodog') → True

def cat_dog(str):
  	if ("cat" in str)*("dog" in str) == 0 and ("cat" in str)+("dog" in str) !=0:
    	return(False)
  	else:
    	count_cat = count_pat(str, "cat")
    	count_dog = count_pat(str, "dog")
    	return(count_cat == count_dog)
  

def count_pat(str, pat):
  	if pat not in str:
    	return(0)
  	else:
    	count = 0
    	l = len(str)
	    l_pat = len(pat)
    	for i in range(l-1):
      		count += str[i:i+l_pat] == pat
    	return(count)


###################################################################################################
# 13
### Bon exemple d'erreur d'approche avec While et les listes indexées:


# List-2 > sum13
# Return the sum of the numbers in the array, returning 0 for an empty array. 
# Except the number 13 is very unlucky, so it does not count and numbers that come immediately 
# after a 13 also do not count.

# sum13([1, 2, 2, 1]) → 6
# sum13([1, 1]) → 2
# sum13([1, 2, 2, 1, 13]) → 6

## ERROR: index out of range
## l'expression avant le "and" est évaluée en premier et si elle vraie la suite est evaluée:
## donc dans le while qui suit il faut évaluer "i < len(nums))" d'abord ou on obtient un "index out of range"
## La 


def sum13(nums):
  	if len(nums) < 1:
    	return(0)
  	else:
    	res = 0
    	i = 0
    	while(nums[i] != 13 and (i < len(nums))):
      		res += nums[i]
      		i += 1
    	return(res)
    

# Bonne Solution:
def sum13(nums):
  	if len(nums) < 1:
    	return(0)
  	else:
    	res = 0
    	i = 0
    	while((i < len(nums)) and nums[i] != 13):
      		res += nums[i]
      		i += 1
    	return(res)


###################################################################################################
# 14

# List-2 > sum13
# Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count 
# and numbers that come immediately after a 13 also do not count.

# sum13([1, 2, 2, 1]) → 6
# sum13([1, 1]) → 2
# sum13([1, 2, 2, 1, 13]) → 6

def sum13(nums):
  	if len(nums) < 1:
    	return(0)
  	else:
    	res = nums[0]*(nums[0] != 13)
    	i = 1
    	while(i < len(nums)):
      		res += nums[i]*(nums[i] != 13)*(nums[i-1] != 13)
      		i += 1
    	return(res)


###################################################################################################
# 15
# List-2 > sum67
# Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 
# (every 6 will be followed by at least one 7). Return 0 for no numbers.

# sum67([1, 2, 2]) → 5
# sum67([1, 2, 2, 6, 99, 99, 7]) → 5
# sum67([1, 1, 6, 7, 2]) → 4

def sum67(nums):
  if len(nums) == 0:
    return(0)
  else:
    i = 0
    res = 0
    while(i<len(nums)):
      if nums[i] != 6:
        res += nums[i]
        i += 1
      else:
        i += 1
        if nums[i] == 7:
          i += 1
        else:
          while(i < len(nums) and nums[i]!=7):
            i += 1
          i += 1
    return(res)
