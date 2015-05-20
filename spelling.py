#simple program to train with spelling listening
#it requires espeak

import subprocess

def execute_unix(inputcommand):
   p = subprocess.Popen(inputcommand, stdout=subprocess.PIPE, shell=True)
   (output, err) = p.communicate()
   return output

stringa = "AHIEEIEIARIHEYAHIYREAIWRERYHAERIARYHERAIRHAERHYREAI"

for c in stringa:

 # write out to wav file 
 #b = 'espeak -w temp.wav "%s" 2>>/dev/null' % a  

 #print(c)
 #print('\r')
 # speak aloud
 c = 'espeak -k5 -s150 --punct="<characters>" "%s" 2>>/dev/null' % c

 #execute_unix(b) 
 execute_unix(c) 


print("Press any key to see the string...")
input()
print(': ', stringa, ' :' )
print()
