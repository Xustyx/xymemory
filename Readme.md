# XyMemory
[XyMemory][git-repo-url] is a simple project based on [memorpy][git-memorpy-url] that allows read and write process memory.

# Example of use
To start we only need to download this repository, open python command line, import this module and start fun.

```sh
$> git clone https://github.com/Xustyx/xymemory.git xymemory
$> python
```
```python
#Import module
>>> from xymemory import *
#Creates a DataManager that handles a process.
>>> dm = DataManager("StarCraft.exe")
#Read unsigned int
>>> dm.read(0x0057F0F0, "uint")
50
#Read string
>>> dm.read(0x0059B420, "string")
'Computer'
>>>
```

# Actually supported types and methods
### Types
- BYTE: 'byte'
- STRING: 'string'
- INT: 'int'
- UINT: 'uint'

### Methods (DataManager)
* DataManager(process_name)
  * process_name: The process name to handle.
* read(address, type)
  * address: Memory address in hexadecimal format.
  * type: The string value of desired Type.


[git-repo-url]: <https://github.com/Xustyx/xymemory.git>
[git-memorpy-url]: <https://github.com/n1nj4sec/memorpy>