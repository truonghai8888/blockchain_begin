from base64 import b64decode

import ipfsapi

c = ipfsapi.connect()
with c.pubsub_sub("bitcoin") as sub:
    for message in sub:
        string = b64decode(message["data"])
        print(string)
        break
