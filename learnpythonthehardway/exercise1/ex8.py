# -*- coding: UTF-8 -*-
formatter = "%r %r %r %r"
formatter1 = "%s %s %s %s"
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, False)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)
print formatter % ("找", "找", "zhao", "zhao")  # '\xe6\x89\xbe' '\xe6\x89\xbe' 'zhao' 'zhao'
print formatter1 % ("找", "找", "zhao", "zhao") # 找 找 zhao zhao