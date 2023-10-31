#!/usr/bin/python3
for c in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
	if (c == 'e') or (c == 'q'):
		continue
	print("{}".format(c),  end='')
