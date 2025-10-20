# re.search(pattern, string)	Finds the first match anywhere in the string
# re.match(pattern, string)	Matches the pattern only at the beginning
# re.findall(pattern, string)	Returns all matches as a list
# re.sub(pattern, repl, string)	Replaces all matches with another string
# re.split(pattern, string)	Splits the string based on the pattern
# re.compile(pattern)	Precompiles a regex for reuse

#common patterns for regular expressions are
# \d - matches any digit
# \D - matches any non-digit
# \w - matches any alphanumeric character
# \W - matches any non-alphanumeric character
# \s - matches any whitespace character
# \S - matches any non-whitespace character
# . - matches any character except a newline
# ^ - matches the start of a string
# $ - matches the end of a string

#Example usage of regular expressions in python
import re
# Example 1: Searching for a pattern
pattern = r'\d+'
text = 'The number is 123'
match = re.search(pattern, text)    
print(match)
# Example 2: Finding all matches
pattern = r'\d+'    
text = 'The number is 123'        
matches = re.findall(pattern, text)    
print(matches)    
# Example 3: Replacing a pattern
pattern = r'\d+'    
text = 'The number is 123'        
new_text = re.sub(pattern, 'X', text)    
print(new_text)    
# Example 4: Splitting a string
pattern = r'\s+'    
text = 'Hello World'        
parts = re.split(pattern, text)    
print(parts)        
# Example 5: Compiling a regex
pattern = r'\d+'    
compiled_pattern = re.compile(pattern)
text = 'The number is 123'        
match = compiled_pattern.search(text)    
print(match)    