import pprint

import ipfsapi

c = ipfsapi.connect()
result = c.add("mysite", True)

pp = pprint.PrettyPrinter(indent=2)
pp.pprint(result)
