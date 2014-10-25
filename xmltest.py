#!/usr/bin/python

from xml.dom import minidom
from xml.dom.minidom import parseString

doc = minidom.parse('example.xml')

elements = doc.getElementsByTagName('file')
for element in elements:
	print '--', element.tagName
	children = element.childNodes
	for child in children:
		if child.nodeType != child.TEXT_NODE:
			print child.childNodes[0].data
		# print textnode.data
	# print element.tagName

#pretty_print = lambda data: '\n'.join([line for line in parseString(data).toprettyxml(indent='\t').split('\n') if line.strip()])
#file = open('example_out.xml', 'w')
#file.write(pretty_print(doc.toprettyxml()))
#file.close()

file = open('example_out.xml', 'w')
file.write(doc.toxml())
file.close()