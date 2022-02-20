# Alex Martelli's Borg: A Non-Pattern

This is adapted from [Alex Martelli's Five Easy Pieces](http://www.aleax.it/5ep.html) 
article. See also [Singleton? We don't need no stinkin' singleton!](https://code.activestate.com/recipes/66531/),
especially the comments.  

It's often very useful to avoid passing references to commonly used objects and
to avoid the problems inherent in a singleton's dependence on *object identity*.

`Borg` provides a simple, lightweight
alternative that maintains a shared state across object instantiations. All that's
required is inheritance, and a simple set up. Originally written around 2001, it
has stood the test of time.

As Alex Martelli is careful to point out, Borg is *not* a singleton!

## Example
See `example/borg_example` for a sample implementation easily adaptable to your needs. 
Note that the shared state is preserved although the object references *are* different.

# License
MIT License Copyright &copy; 2022 Chris Skiscim

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.