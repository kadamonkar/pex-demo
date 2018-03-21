#H1 Quick Demo project-  python executables(pex)


#H2 How to build a pex file 
```shell
pex . -r requirements.txt -c test.py -o test.pex -f dist
```

#H2 How to execute pex file
```shell
./test.pex https://www.google.ca/ 
```
