# pykit: 
Helper classes and functions that allow users to import and perform some basic cleaning on files whilst converting them to dataframes.  These are especially helpful when loading dataframes into databases (e.g. using Snowflake's python connector).

### Pykit Example:
The following demonstrates how to call the LocalFiles() class which contains a function called list_files that returns an array of the file names in that location. The second function create_df_dict, creates a dictionary containing file names as the keys and the corresponding dataframes as the values.
```python
## PyKit Example:
my_drive = '[your_drive_location]' # use to point your script to pykit on your local
import sys
sys.path.append(my_drive)

input_dir = '[where you are storing a bunch of files]'

def main():
   	#Import LocalFiles module from ascap_py pykit
   	lf = pykit.LocalFiles()

   	#creates an array of all of the files in the input location
	input_dir = ascap_py_drive + 'files/quick_load/inputs/'
   	files = lf.list_files(directory=input_dir)
   	print(files) #array

   	#outputs a dictionary with file name as key and df of file as value for all files in a given location
   	dfs = lf.create_df_dict(directory=input_dir
   						   ,list_files=files #array
   						   ,delimiter=',' #default val
   						   ,header='infer') #default val

if __name__ == '__main__':
    main()
```

## Contributing
Pull requests are welcome, but this code is primarily meant to demonstrate basic Python chops.  It's generally quick helper code.  Please contact me if you'd like to make a pull request.

## License
Copyright (c) 2022 C. Poulos

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.