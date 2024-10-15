import re


# Using re.match() 
print(re.match(r'world', 'hello world'))   # Output: None (because 'world' is not at the beginning) 
# Using re.search() 
print(re.search(r'world', 'hello world'))  # Output: Match object (because 'world' is found) 

# replace a string using regex

print(re.sub("\d+","$","phani chinta 181 number")) # entire number is replaced with #
print(re.sub("\d","$","phani chinta 181 number")) # all three numbers are replaced with ###


name = "phaneendhra chinta"

print(re.match("(\w+) (\w+)",name))

text = "<html><body>Hello</body></html>"

# this matches everythin in b/w <>
print(re.search(r"<.*>",text).group())

# this matches only the first occurences <>
print(re.search(r"<.*?><.*?>",text).group()) # <html><body>

email = "phaneendhra.chinta@thundersoft.com"
#^[\w.-] starts with alpha, numeric, - .
# @[a-zA-Z\d] after the domain, get only alpha value
# +\. -> \. implies search dot (liek \w how we search words)
# [a-zA-Z]{2,4}$ -> ending get alpha values with min len=2, ,max len =4
print(re.match(r"^[\w.-]*@[a-zA-Z\d]+\.[a-zA-Z]{2,4}$",email))

phone= "+91-9191919191"
print(re.match(r"^\+\d{2}-[\d+]{10}$",phone))

# Extracting the hastag words from the tweets 
tweet = "Loving the new #iPhone! It's so much better than #Android. #TechNews"

print(re.findall(r"#(\w+)",tweet))

# Extracting the subdomain from the URL

pattern = r"https?://([a-zA-Z0-9-]+)\.([a-zA-Z0-9-]+)\.[a-zA-Z]{2,4}$"
urls = 'https://blog.example.com'
print(re.search(pattern,urls))