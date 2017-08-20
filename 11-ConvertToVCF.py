__author__ = 'Krishna Ajjarapu'
import sys
import csv


#Assume file format as Firsname,Lastname,Contact,Email,Organization
#Convert a "comma separated values" file to vcf contact cards

def convert_to_vcf(filename):

   
   source = open(filename,'r')
   dest = open('Contacts_PythonBatch_9.vcf','w')
   reader = csv.reader( source )
   n=0
   for row in reader:
       dest.write('BEGIN:VCARD' + '\n')
       dest.write( 'N:' + row[0] + ';' + row[1] + "\n")
       dest.write('TEL;CELL: '+ row[2] + '\n')
       dest.write('EMAIL: '+ row[3] + '\n')
       dest.write('ORG: '+ row[4] + '\n')
       dest.write('END:VCARD' + '\n')
       dest.write('\n')
       
       n+=1 # Count for number of contacts
   dest.close()
   print("Total number of contacts coverted to vcf are: {0}".format(n))

def main(args):
    if len(args)!=2:
       print("Usage:\n")
       print("{0} filename".format(args[0]))
       return
    convert_to_vcf(args[1])
    
if __name__=="__main__":
    main(sys.argv)