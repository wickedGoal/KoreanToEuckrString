Some programs with Oracle SQL DB store Korean text in euc-kr byte sequence.

e.g) "가나다" -> \'b0\'a1\'b3\'aa\'b4\'d9

This is to convert Korean string to euc-kr byte sequence string
so that Korean text search query can be made.
