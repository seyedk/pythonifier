# Installation issues
I could not install `psycopg2` on macos, python 3.9. Thanks to the [stackoverflow](https://stackoverflow.com/a/56110800/2336328) post, I used the following commands to help installing psycopg2:

```
brew install postgresql

export LDFLAGS="-L/usr/local/opt/openssl/lib"

export CPPFLAGS="-I/usr/local/opt/openssl/include"

pip3 install psycopg2

```
