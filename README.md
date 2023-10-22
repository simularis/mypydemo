Template for a python command line script plus user interface wrapper and pyinstaller

## Building distributable executables

1. Create a Python environment with just the packages in requirements.txt.

```conda create --file=requirements.txt```

2. In a command prompt, use the following command to start pyinstaller.

```pyinstaller buildall.spec```

