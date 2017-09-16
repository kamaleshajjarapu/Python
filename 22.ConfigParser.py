#!C:\Users\kajjarapu\AppData\Local\Programs\Python\Python36-32\python.exe
import configparser
def config_parser(filename):
    dict_servers={}
    dict_server_details={}
    config = configparser.ConfigParser()
    config.read(filename)
    if config.sections():
        for key in config:
           dict_server_details={}
           for key1 in config[key]:
              value=config.get(key,key1)
              if '#' in value:
                value=value.split('#')[0]
              dict_server_details[key1]=value 
           if key!='DEFAULT':   
            dict_servers[key]=dict_server_details
          
    return(dict_servers)
          
def main():
    filename=eval(input("Enter a config file:"))
    result=config_parser(filename)
    print(result)

if __name__=='__main__':
    main()
    