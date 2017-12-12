import re

''' 
List of Regular Expression

? = zero or one time
* = zero or more times
+ = one or more times
() = group
\ = scape
| = or
. = any char except new line
.* = anything
\d = digit
\D = not digit
\w = letter
\W = not letter
\s = space, tab or new line
\S = not space, tabe or new line
{a number here} = repetition
{number minumum, number maximum} = repetition with range
[characters in here] = multiple or
[char - char] = range of letters
[^char] 
^ = starts
$ = ends
'''

message = 'Call me 123-123-1234 tomorrow, or at 321-321-3214'

phoneNumRegex = re.compile(r'(\d{3}-\d{3}-\d{4})')

print(phoneNumRegex.findall(message))