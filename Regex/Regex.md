Regex - it gonna look for a specified pattern in a given text
pattern is a sequence of characters, which represents multiple strings
EX:  'i[st]'(the whole stuff is a string, because it's between '')-->  is, it
'python[23]'--> python2, python3

syntax
re.search(pattern, text)
re.match(pattern, text)
re.finditer(pattern, text)
re.findall(pattern, text)

the characters inside a list - "[sid]"(it specifically searches for s, i, d) and characters in string "sid"(it specifically searches for sid) aren't same pattern searching in a given text

\w  - matches any single letter, digit and underscore with zero spaces in the ouput
\W - the stuff that can't find by \w, \W gonna find it

\d - searches the numbers

. - Matches any single character except newline character, dot means anything
\. - especially searches for dot

^ - start of string and start of the line in case of multiline string

\b - empty string at the beginning or end of a word

\B - empty string not at the beginning or end of a word

\t, \n, \r - Matches tab, newline, return respectively

{2}  exactly two times(it's applicable for a single character)
{2, 4}  2,3 or 4 times(it's applicable for a single character)
{2,} two or more times(it's applicable for a single character)
{1,} or +  - one or more times(it's applicable for a single character)

* - 0 or more times(it's applicable for a single character)

? - once or none(lazy)(it's applicable for a single character)

search

match

findall

finditer

split

sub

subn