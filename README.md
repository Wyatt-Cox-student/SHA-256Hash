Cryptography Assignment

This project demonstrates SHA-256 hashing, a Caesar cipher, and digital signatures using Python and OpenSSL.

The main Python file is crypto_app.py. It allows the user to create a SHA-256 hash from either text or a file. It also allows the user to encrypt and decrypt text using a Caesar cipher.

To run the program, open a terminal in the project folder and use:

python crypto_app.py

The program will display a menu where you can choose between hashing text, hashing a file, using the Caesar cipher, or exiting the program.

The message.txt file is included as a simple test file. It can be used when testing the file hashing option and is also used for the digital signature portion of the assignment.

For the digital signature, OpenSSL is used to create a private key, public key, and signature.

Generate the private key:

openssl genrsa -out signature_files/private_key.pem 2048

Generate the public key:

openssl rsa -in signature_files/private_key.pem -pubout -out signature_files/public_key.pem

Sign message.txt:

openssl dgst -sha256 -sign signature_files/private_key.pem -out signature_files/signature.bin message.txt

Verify the signature:

openssl dgst -sha256 -verify signature_files/public_key.pem -signature signature_files/signature.bin message.txt

If the signature is valid, OpenSSL should display:

Verified OK

Overall, this project shows how hashing can be used to check data integrity, how a basic substitution cipher can encrypt and decrypt text, and how digital signatures can be used to verify a file.