# HASH Check App
Project I started to practice the practical application of Python.

App will accept a local file path and an optional HASH string. After selecting a HASH library, the app will compare the provided HASH string with the hashed file and alert the user if it matches or not. If the HASH string is left blank, the app will generate the hash of the file using the selected hash library.

### Prerequisites
Python 3.5.2

## Running the tests

A local File Path is always required. Depending on if a Hash value is entered the program will either produce the hash if non is given or execute validation the hash of the file and the provided hash value.

You will need to update the provided file path examples to wherever you choose to save the test files on your local system.

### Break down into end to end tests

Using the inlcuded GitHub-Logo.png file, you should be able to conduct the tests of each hash library.

1. Locate the included GitHub-Logo.png file that is included in this repository.
2. Input local system path in the File Path field.
3. Choose a Hash library radio button and paste its provided hash value in the Hash field.
4. Click Run.
5. Repeat for remaining libraries.

NOTE: All of these examples should return a successful match.
```
File: C:/Path/To/File/GitHub-Logo.png
MD5 Hash: d8161a975fa3c78baef1d9f59088e8cd
SHA1 Hash: 9d131b3f73b47c51254e44215f067660c94a140d
SHA256 Hash: 3f42cf5a0bfbaee981d22411dd5a5a6dd3568d2272961d7c81ac06f7d821794b
SHA512 Hash: 25b0c0bfb8b88ed15d213f57d9027168d1ce29aca76c47dc105ceec7000367a4ab8b9a85f525b6e19ac4d1625ba659da0ca49c939cf73a76b665da4d556485d3
```


## Built With
* Python 3.5.2

## Authors
* **Gavin Greer** - *Initial work* - [nivagator](https://github.com/nivagator)

## Acknowledgments

* Python Programming Second Edition by John Zelle
* Python in Easy Steps by Mike McGrath
