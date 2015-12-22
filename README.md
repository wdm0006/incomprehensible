Incomprehensible: how to write list comprehensions and alienate people
======================================================================

A collection of list comprehensions that solve arbitrary tasks concisely, but not necessarily in a way that any sane 
person would be able to quickly understand when stumbling upon it.

As an example:

    [y for z in [x if isinstance(x, list) else [x] for x in nested] for y in z]
    
Will flatten a list of mixed types one level.  So:

    [1, 2, 3, [4, 'B', 6], {'7': 'A}]
    
Becomes:

    [1, 2, 3, 4, 'B', 6, {'7': 'A}]
    
Who knew?


Contents
========

Each example has the list comprehension itself included as a function, that can be imported if you want.

 * Dedupe Dict-List: deduplicates a list of dictionaries using a subset of keys in the dictionaries.
 * Flatten List: the above example that flattens a list one level
 * Split-Strip-Coerce: parses a delimited string into a list with supported types of int, float and str.
 
Usage
=====

This is really intended as a reference, but you can install it as a package if you want to use parts.

To install it:

    $pip install git+https://github.com/wdm0006/incomprehensible.git
    
Then to use part:

    >>import incomprehensible as inc
    >>inc.dedupe_dictlist(...)
 
License
=======

BSD 3-clause license
