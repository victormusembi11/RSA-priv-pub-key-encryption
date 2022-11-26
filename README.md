# RSA-priv-pub-key-encryption

## Asymmetric Encryption

Public-key cryptography, or asymmetric cryptography, is the field of cryptographic systems that use pairs of related keys. Each key pair consists of a public key and a corresponding private key. Key pairs are generated with cryptographic algorithms based on mathematical problems termed one-way functions. Security of public-key cryptography depends on keeping the private key secret; the public key can be openly distributed without compromising security.

In a public-key encryption system, anyone with a public key can encrypt a message, yielding a ciphertext, but only those who know the corresponding private key can decrypt the ciphertext to obtain the original message.

The most obvious application of a public key encryption system is for encrypting communication to provide confidentiality – a message that a sender encrypts using the recipient's public key which can be decrypted only by the recipient's paired private key.

**Note:**

I've encrypted the message using public key and then signed it with my own
private key.

Typically when you are having two peers (peer1 & peer2) then if peer1 is sending
a message to peer2 then the message should be encrypted using the public key of peer2
however it's signed using the private key of peer1 which is actually the peer sending
the message and on the other side (the recipient side) which is peer2 they will decrypt
the message using their own private key and then verify the signature of the message
using the public key of peer1 (the sender).

However in this case it's not just. It only a simple show case of how to use rsa lib.

## Use

### Create a virtual envronment

```bash
python3 -m venv venv
```

### Source the enviornment

```bash
source venv/bin/activate
```

### Run the py code

run on the terminal

```bash
python3 rsasrc.py
```

You will be promted to enter a message. Example:

```bash
Enter a message: <enter your message here>
```

**sample output on the terminal:**

```bash
Cipher text: b'-\xf6\x16\xe7\xde\x0b\x82\x07;\xf1\xc5o\xc5\x9a\xd4\x85\x88\xebFZ\xafc\x00\xfe\x0e\x1e\\\xd7\xc0\xacd\xf0\x9b\xd4I\x89C(w\xd2|\x95\x86\xf0$R\xf7\x08\x97\xa4\xffu&H\n\xf2\x93\x9b,\xf6\x88\xe8<\xcb\xad\xa7\xb7Qo\x92\xf7\xf6>\xb3\x7f\x7fm\xfe\x91/\x98\xdd\xf71\xe6\x7f-Z\x147\xc2\xda$n\x11\xe5\xf5\xfan2\xdd\x7f\xb5=\xd9\x99\xb2\x0b\xf3\x1b\xefEs?\xa8\x10)\x9e\xa5]H4\xb0\xf2)M\xec\xa0'

Signature: b"b\x1a\xae1Jw\xe0\xaf\xf0x*p;J\xa2OK\x1cu\xb1\x85\xd0\x95\xbb\x96\x15\x9e\x08 \x1d\x96\xdb\xce\xddA\xce\xf1]\xfak\xb7\xd2C\x06^6\xe7\xa3-/\x98b\xcb\xa2\x1c\x8e8\x82?\xc9\xb3\xc2\xa2K\xa4X\xc2\xfco\xcd\x81P4&\x04-\xcc\rQ\xff\x97\xdb\xbaDxVz\xb4\xc6\xb8b\xfeW\x15\x0c\x07\x17\x180\x89\xba\n\xd6\xc4\x8a\xd1\xe5/XY\x86'\xe6>\xf6j\xc1B\x8f\xf7\xa2v\xba&\x8b\xc2K\x12"


Plain text: hello world
Signature verified!
```
