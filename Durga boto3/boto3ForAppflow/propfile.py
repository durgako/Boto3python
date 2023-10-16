import configparser
config = configparser.RawConfigParser()
config.read('flowNames.properties')
for each_section in config.sections():
    for (each_key, each_val) in config.items(each_section):
        print(each_key)
        print(each_val)






