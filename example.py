#!/usr/bin/env python
# written for python2.6

'''
Simple string concat example
to help demonstrate statement corruption
(e.g SQLi)

The goal is to generate two quoted sentences 
by abusing the name input field.

The comments within main() are meant to show what a 
developer may think during the process.
by: b1ack0wl
'''

import time, sys

def main():
# Deadline: yesterday lol
# Needed functionality: Ask user for name,
#			Add their name to our sentence, 
#			Print it.
#
# Desired Output: 'Hello NAME! :D'
#
# TODO: Later on we will pass the 
#       generated name into a SQL 
#       statement so it can go into 
#       a SQL database.

	name = raw_input("[+] Please type in your name and press ENTER: ")
	print "[+] Generating string...\n"
	time.sleep(1.5) # for effect.
	# Create String 
	sentence = "'Hello %s! :D'" %(name)
	# Print String
	print sentence
	print "\n[+] Exiting program...\n"
	sys.exit(0)

if __name__ == '__main__':
	main()

