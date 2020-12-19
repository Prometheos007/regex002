#Regex Object

import re

#Joins the groups and checks if the found num exists in list. Adds if doesn't
def checkandadd(tup, lis):				

	for i in range(len(tup)):
		l = ''			#temporary var
		for j in tup[i]:	#iterates over groups	
			j = j.lstrip()	#removes unneccessary spaces
			l += j 			#joins the groups
		if l not in lis:	#check if exists and adds
			lis.append(l)
			print('appended', l) #confirmation




matches = []
for r in re_list:
   matches += re.findall( r, string)

print(matches)
#regex obj 1 
phone1 = re.compile(r'''
	(\+?\d{,2})?	#Country Code
	(\s|-)?		
	(\d{3})			
	(\s|-)?	
	(\d{3})			#3-3-4 Phone Number
	(\s|-)?
	(\d{4})
''', re.VERBOSE)


#regex obj 2
phone2 = re.compile(r'''
	(\+?\d{,2})?	#Country Code
	(\s|-)?		
	(\d{5})						#3-3-4 Phone Number
	(\s|-)?
	(\d{5})
''', re.VERBOSE)

st = '+91 9869049069, 8425069329, +91-986-904-9069, 96999-18373'

liss = []

mo = phone1.findall(st)
lo = phone2.findall(st)


checkandadd(mo,liss)
#checkandadd(lo,liss)


for i in liss:
	print(i)


