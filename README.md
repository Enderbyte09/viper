# viper
viper
## DANGER! THIS IS A VIRUS! RUNNING THIS MAY DAMAGE YOUR COMPUTER

### How it works:
When you run the stage zero file (virus.py), this happens
1. All files on the system will be scanned for uninfected Python files
2. These files will have a gzipped copy of virus.py inserted into them.
3. They are now stage 1 files. Stage 1 files work as well as stage zero files.

Stage one files do this:
1. It starts a new thread so that the infected program still works normally.
2. It then runs like stage zero.

### Notes

Viper will NOT infect standard library files, BUT it will infect site-package files.
To defeat a stage one file, comment out but DO NOT DELETE the two lines of malicious code.
