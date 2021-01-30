## User Interfaces for Programming Languages: The Compendium

This compendium covers research and practice in the field of 
user interfaces for programming languages. It has not yet been published online.
The  first round of contributions will be made by students in [EECS 598](http://web.eecs.umich.edu/~comar/courses/ui-for-pl/) at Michigan during Fall 2019. After that, the compendium will be published online and contributions from the rest of the community will be welcome.


### Build Instructions

The compendium is built using the [Sphinx](http://www.sphinx-doc.org/) document generation system.

The required libraries are listed in `requirements.txt` and can be installed using `pip` as follows:

```
$ pip install -r requirements.txt
```

Then you can build the HTML output by typing `make` at the shell. 
The result is the `html` directory. The `make clean` command will delete the build artifacts.

### Contributing

Contributions are made through GitHub's pull request mechanism. To quickly propose edits to a single file, you can find it on Github (e.g. by clicking on the Edit on Github link at the top of the corresponding page) and click the pencil icon. For more sophisticated changes, fork the repository and make a pull request.

The compendium is structured as one file per topic area in the `src`
directory, with `index.rst` as the top-level organizational hub.

#### reStructuredText
Compendium content is written in
[reStructuredText](http://docutils.sourceforge.net/docs/ref/rst/directives.html),
with the extensions supported by [Sphinx](http://www.sphinx-doc.org/).
This format is similar to Markdown, but offers some more advanced features.

Please follow these conventions for headings:

```
First Level
===========

Second Level
------------

Third Level
~~~~~~~~~~~

Fourth Level
************

Fifth Level
+++++++++++
```

#### Citations
We use BibTeX for citations, via the [sphinxcontrib-bibtex](https://sphinxcontrib-bibtex.readthedocs.io/en/latest/) extension. See `src/notation.rst` for examples of how to include bibliography entries in your article. 

This extension is somewhat limited, so we need to use the following workarounds:
1. Each .bib file can have no more than 9 entries, so just make new files, e.g. `notation.bib`, `notation2.bib` and so on, as needed.
2. Each .bib file must be added to the `bibtex_bibfiles` list in `conf.py`.
3. Sphinx will generate warnings if you have not explicitly cited a bibliography entry in the text. To get around this, you can include a hidden area at the bottom of each file to cite items that you have not otherwise cited. See the bottom of `notation.rst` for an example.
4. There are certain lexical limitations on the cite keys, e.g. they cannot have capital letters. I recommend using cite keys of the form `lastnameYY` where `YY` is the two digit year, e.g. `hughes95`.

You can find BibTeX entries using [Google Scholar](https://scholar.google.com/) or [DBLP](https://dblp.uni-trier.de/). Please remove extraneous details, e.g. conference locations and dates, and publisher names and locations. For common publication venues, it is okay to use abbreviations, e.g. `OOPSLA`, rather than full conference names.

### Contributors

The compendium is maintained by [Cyrus Omar](https://web.eecs.umich.edu/~comar) (comar@umich.edu).

The Sphinx setup was adapted from [EECS 490 course notes](https://github.com/eecs490/notes) prepared 
by Amir Kamil (akamil@umich.edu). 

### License 

All contributions are governed by the [Creative Commons
Attribution-ShareAlike 4.0 International
license](https://creativecommons.org/licenses/by-sa/4.0/).
