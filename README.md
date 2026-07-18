# name_generator
Unintelligent generator of random strings of characters. Use it for D&amp;D or something.

## Usage
### On its own
Navigate to the repo directory in a terminal and run `python generate.py --count (count) --save --print`

Args:<br>
`-c/--count`: How many names to generate. Omit if you only want one name.<br>
`-s/--save`: Save output to `output/names.txt`.<br>
`-p/--print`: Print output. Omit if you don't want your terminal spammed.<br>

### In another project
Import the module, then run `name_generator.generate()` to return a string or list of strings.

Args:<br>
`n`: How many names to generate. Defaults to `None` (1 name in a single string). Otherwise, returns a list of strings.<br>
`config`: If you want to customize letter frequencies and word counts. Defaults to the config specified in `config.py`.<br>
`save_output`: Whether to save the output to `output/names.txt`.<br>
`print_output`: Whether to print the output.<br>

<br>
**Disclaimer**: Good results not guaranteed. If you're using this to actually name something, you'll probably want to generate a couple thousand words at a time and cherry-pick the good ones.