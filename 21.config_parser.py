#!C:\Python27\python.exe
def parse_conf_file(file):
  dict_servers = {}
  dict_server_details = {}
  server_exist = False
  fob=open(file,'r')
  if fob!=None:
    lines=fob.readlines()
    for line in lines:
      if line.startswith('#'):
        continue
      if line.startswith('['):
        #print line
        if server_exist==True:
           dict_servers[server_name]=dict_server_details
           dict_server_details={}
           server_exist=False
        if server_exist==False:
          server_name=line[1:-2]
          #print server_name
          server_exist=True
      elif server_exist==True:
        if line!='\n':
            key,value=line.split('=')   
            if '#' in value:
                value=value.split('#')[0]
            dict_server_details[key]=value.strip()
    else:
      dict_servers[server_name]=dict_server_details
    print dict_servers

def main():
   file = 'server_details.conf'
   parse_conf_file(file)
if __name__=='__main__':
   main()
   