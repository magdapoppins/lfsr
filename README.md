# Fibonacci Linear Feedback Shift Register 

### Running Haskell samples
To run these files, run GHC's interactive mode from the command line by the command `ghci`. The GHCI prompt appears as a sign that everything is ok. You can load a file by typing `:l filename` and reload by `:r`.
In non-interactive mode the code files can be compiled by `ghc [filename].hs` and after that run by `./[filename]`.

### Running the Python3 samples
The `.py` files can be run with python3 by the command `python3 [filename].py`. The tests for the files live in the `tests.py` file and can be run simply by running that file.

### Stream ciphers 
- produce a pseudorandom bitstream
- key at least as long as plaintext (random key stream)
- initialization vector (IV), neither random nor secret, should be used only once for init purposes
- secret key (remains the same)
- initial state 
- seed value

### Linear Feedback Shift Registers (LFSR)
- the output of the shift register is manipulated and fed back into it's input letting it cycle endlessly through a sequence of patterns
- the sequence at which it cycles depends on the taps selected and the length of the register
- the new input is generated from taps by the `xor` or `xnor` functions

### Pseudorandom bit generators
- if cryptographically secure new bits cannot be predicted with an accuracy over 50% even when all previous bits are known 
- 

### Tools
- using the [data bits package](http://hackage.haskell.org/package/base-4.12.0.0/docs/Data-Bits.html)