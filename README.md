## Structure of project folder
1. Docs folder
    - Contain document files.
2. Data folder
    - Contain data files used in the implementation.
3. Src folder
    - Contain packages, modules used in the implementation.
4. Main folder
    - Named as its purpose.
    - Contain main files to run your app.
5. Test folder
    - Contains files for testing the files in main folder.
6. Requirement text file
    - List of libraries need to be installed for implementation

### * Note for running test file
Run all tests in the directory of project folder with the code in below:  
```
python3 -m unittest discover -v
```
- All test file must have prefix test_ in name 
- All testcases must have prefix test_ in name
- All modules must have a <b>\_\_init\_\_.py</b> file in their folder 