s = "Strings are awesome!"

print("Length of s = %d" % len(s))

print("The first occurrence of the letter a = %d" % s.index("a"))

print("The first five characters are '%s'" % s[:5])

print("The thirteenth character is '%s'" % s[12])

print("The characters wit odd index are '%s'" %s [1::2])

print("The last five charactes are '%s'" % s[-5])

print("String in uppercase: %s" % s.upper())

print("String in lowercase: %s" % s.lower())

if s.startswith("Str"):
    print("String starts with 'Str!'. Good!")

if s.endswith ("ome!"):
    print("Strings ends with 'ome!'. Good!")

print("Split the words of the string: %s" % s.split(" "))
