# Spack-build-scripts
A repo where I store a variety of scripts that I wrote to help automate the process of building new spack packages
## Manifest
* parse_requirements_txt.py - parses a requirements.txt file in the format of [name]==[version], extracts the names, and prints them to the terminal in the form of the standard spack package syntax. 
- [ ] Make an option for working with version numbers
- [ ] Make an option for pasting directly into the script
- [ ] Do something so that it can interact with spack to check if deps exist in one of our repos
