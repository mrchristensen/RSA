# RSA Implementation

This is a fully functional implementation of [RSA](https://en.wikipedia.org/wiki/RSA_(cryptosystem)), which involves finding multiplicative inverses and modular exponentiation.

## How to Run the Code
The values are hard coded in, so simply run [```python main.py```](/main.py) to find the values needed for RSA

## Values
* The values *p* adn *q* are found using openssl to find a safe prime of 512 bites (```openssl prime -safe -generate -bits 512```) (the values are also checked such that the high order bit is set as well as *e* and *phi* being relatively prime)
* *e* is set to 65537 by convention (as defined in the spec)
* *phi* is defined as:  *(p - 1) * (q - 1)*
* *n* is defined as:  *p * q*
* *d* (*ed = 1 % ϕ(n)*), and the plain/cipher text (*m^d % n* and *m^e % n*), are generated on the fly (with the values given by the auto grader (https://grader.cs465.byu.edu/rsa)

The modular exponentiation, gdc, and gdc extended are done using handmade algorithms (divide and conquer, euclid, and euclid extended respectively).

## Version
Use Python 3.7.2
