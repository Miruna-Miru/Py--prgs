'''This module provides functions for wrapping, filling, and formatting plain text.
For example, we can adjust the line breaks in an input paragraph using the textwrap module.'''


'''textwrap.indent(text, prefix, predicate=None)
Parameters
text: This is the text that is to be indented.
prefix: This is the prefix to be added to the beginning of the text lines.
predicate: This can be used to control which lines in the text are indented.'''



import textwrap as tw 
def wrap(string, max_width):
    result=[]
    for i in range(0, len(string), max_width) : # st,diff,end
      paragraphs = string[i:i+max_width]
      result.append(paragraphs)

    # Join the paragraphs with newline characters to format the output
    result = '\n'.join(result)
    return result

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
