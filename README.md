To use the blockchain module to create a new block, you can use the following code:

```
from prevention_of_communications_forgery.blockchain import Block

data = 'my data'
previous_hash = 'previous hash'

block = Block(data, previous_hash)
```