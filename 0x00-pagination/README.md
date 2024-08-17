# 0x00. Pagination

Pagination is a way of breaking up a large amount of data into smaller, manageable chunks, usually in the form of pages. Instead of showing everything at once, which can be overwhelming and slow, pagination helps to display a small part of the data at a time.

## Resource
[REST API Desing: Pagination] (https://www.moesif.com/blog/technical/api-design/REST-API-Design-Filtering-Sorting-and-Pagination/#pagination)
[HATEOAS] (https://en.wikipedia.org/wiki/HATEOAS)

## Learning Objectives
* How to paginate a dataset with simple page and page size parameters
* How to paginate a dataset with hypermedia metadata
* How to paginate in a deletion-resilient manner

## Requirements
* All your files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/env python3`
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should use the `pycodestyle` style (version 2.5.*)
* The length of your files will be tested using `wc`
* All your modules should have a documentation `(python3 -c 'print(__import__("my_module").__doc__)')`
* All your functions should have a documentation `(python3 -c 'print(__import__("my_module").my_function.__doc__)'`
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
* All your functions and coroutines must be type-annotated.

## Setup: `Popular_Baby_Names.csv`
[use this data file] (https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/misc/2020/5/7d3576d97e7560ae85135cc214ffe2b3412c51d7.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240817%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240817T190705Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=aabf8db4045846126d9fbd292cf59b5c1e1ffcfa52b786d55b40a58fe21759fd) for your project
