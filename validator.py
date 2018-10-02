import re

num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),(50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]


def num2roman(num):
    roman = ''
    while num > 0:
        for i, r in num_map:
            while num >= i:
                roman += r
                num -= i
    return roman


##   Generate roman numerals    ##
roman_numerals = []
for i in range(1,5000):
  roman_numerals.append(num2roman(i))

false_positives = ['IIV', 'CCM', 'IL', 'IC']
print len(roman_numerals), "Roman Numerals generated"
##################################

##   Get User Entry Input      ##
print "Enter A Regex String"
re_string = raw_input()
print "read \""+ re_string + "\""
#################################

##   Check that entry matches all true positives    ##
true_pos_matches = 0
for numeral in roman_numerals:
  if re.findall(re_string, numeral):
    true_pos_matches += 1
######################################################

##   Check that entry matches no false positives    ##
false_pos_matches = 0
for numeral in false_positives:
  if re.findall(re_string, numeral):
    false_pos_matches += 1
######################################################

print "Found", true_pos_matches, "true positive and", false_pos_matches, "false positive matches."

if (true_pos_matches == 4999) & (false_pos_matches == 0):
  print "Congratualtions! That is a correct answer!"
else:
  print "Sorry! Please try again!"

raw_input()

