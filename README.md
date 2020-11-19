# CHAT-APPLICATION-WITH-NTRU-DJANGO
This project implements process of a privacy preserving secured chatting web application app using <b>Django Stack and NTRU cryptography.</b>
The web application will be accessible only to the authorized users and not to anyone.
The Secured Chat will provide the user with secured flawless and non-stop communication between peers. 
We have using <b>web sockets in python and Django channels with NTRU cryptosystem.</b>





<b>EXPLANATION OF METHOD USED</b>


EXPLANATION OF METHOD USED
INITIALIZATION

1.	First of all, the general parameters of the system, N, p and q 
2.	We took
a.	N =11
b.	P = 3
c.	Q=32

3.	Two random polynomials f and g, with a degree at most N-1 and integer coefficients between [-1 ; 1] has been chosen. We have chosen

f(x) = [-1, 1, 1, 0, -1, 0, 1, 0, 0, 1, -1]
g(x) = [-1, 0, 1, 1, 0, 1, 0, 0, -1, 0, -1]

4.	Then the project calculates the modular multiplicative inverse fp of f (mod p) and modular multiplicative inverse fq of f (mod q)
                        

5.	Then public key is generated h
                                                 
6.	The polynomials f, fp and g are private key 
polynomial h and the numbers, p, q and N are available to the general public


MEESAGE GENRATION (M) (NOVELITY)

7.	Message from the user is taken in the form of string.
8.	
9.	Each letter of string is converted into ASCII and each ASCII is converted into binary.

10.	And each binary corresponding to each ASCII is passed into encryption process



ENCRYPTION

11.	A random variable r is chosen known as binding value and ciphertext is calculated 
 



DECRYPTION

12.	There are 3 steps of decryption



The first step of the decryption is calculating a polynomial a, such that
                                
 polynomial b is calculated
                                  
secret polynomial fp is used to obtain the message
                 
                                 
Message is converted back into string

