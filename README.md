# Folding@home Translation Text Repository

Thank you for helping us reach even more people around the world by adapting the
experience to their native language.

**IMPORTANT UPDATE: We have switched away from YAML format to PO format. Please
read the updates.**

**Before you start translating, please read this README to learn how we
collaborate and how to find out what is already done and what is left to do.**

**Please check out the "Coordination" section, and the
[coordination threads](https://github.com/FoldingCommunity/Translate/labels/coordination-thread) 
to find out how your language team is coordinating with each other. Please
submit pull requests to your language team's repository first. Your language
team coordinator will collate all the translation changes, and submit a pull 
request to this repository.**

## What has changed?
After the discussion within the translation plugin development team, we have 
decided to move from the custom YAML format to the more standardised 
[gettext](https://en.wikipedia.org/wiki/Gettext) Portable Object (PO) format. 
We have decided to embed formatting (*not layout*) within the PO files. This
allows each PO file to follow the paragraph structure of the original webpage, 
while enabling more flexibility the translated text within each paragraph. 

We believe that the format change is necessary for the long term maintainability
of the project. We apologise for the extra work that you have to do. It is
important to note that in software development, sometimes there are occasional 
requirements changes that require code refactoring and rewrite. This happens 
more often at the beginning of the project. We believe that there will not be
major format changes down the line.

However we believe that the extra works we have to do is minimal - you should be
able to copy and paste your translated works

The old YAML-based files are archived in the 
[old-yaml branch](https://github.com/FoldingCommunity/Translate/tree/old-yaml).

## How do we translate? 
Please copy the files from [Localization/en-US](Localization/en-US) to your
local language folder, e.g. [Localization/zh-CN](Localization/zh-CN) and update
the metadata fields. Then, for each file, translate each ``msgid`` to ``msgstr``. 

We are using Markdown for formatting the strings to be translated and the 
translated string. We have made the decision to support the following Markdown
syntaxes: 

 - Links: e.g. ``[Example](http://example.net/)``
 - Bold text: e.g. ``**Example**``
 - Italic: e.g. ``*example*``

For more information on Markdown, feel free to have a look at 
[Github's official guide](https://guides.github.com/features/mastering-markdown/),
 however, we are only supporting the formatting syntaxes statated above.

**We would recommend to use one of the specialized free editors that are available
for work with PO files:**
* [Poedit](https://poedit.net/)
* [Lokalize](https://kde.org/applications/en/office/org.kde.lokalize)

They simplify the process a lot, because they take care of the correct formatting
so that you can focus completely on the translation. You will have to add/edit the
header data manually, however, as they are not supported by those tools. They also
usually add more fields to the header automatically, which is perfectly okay.

Alternatively, you can use a text editor, such as
[Notepad++](https://notepad-plus-plus.org/) or [Atom](https://atom.io/) if you
prefer. Please remember to *set your encoding to UTF-8!*.

### PO file mandatory metadata
At the top of each PO file, it is mandatory to have the following metadata
fields:

 1. ``Schema-Version`` - The schema version of this PO file, e.g. ``1.2``.
 In future, we may have minor update to the format of the PO files.
 2. ``URL`` - The URL of the webpage that generated the PO file.
 3. ``Source-Language`` - The original language of the webpage, it should be
 ``en-US`. However, as FAH project grows, we may start seeing webpages that were
 written in language that was not English.
 4. ``Source-Version`` - The version code for the source PO file,
  e.g. ``1.2``.
 5. ``Source-Last-Modified`` - The last modification date for the source PO
 file, this must be  in the format of **YYYYMMDD**, e.g. ``20200704``.
 6. ``Target-Language`` - The target language for this PO file, e.g. ``zh-CN``.
 7. ``Target-Version`` - The version code for the target PO file,
 e.g. ``1.2.1``. (Note that it should be a subversion of ``Source-Version``,
  please refer to the note below.)
 8. ``Target-Last-Modified`` - The last modification date for this PO file, this
 must be in the format of **YYYYMMDD**, ``20200704``.
 9. ``"Content-Type: text/plain; charset=UTF-8\n"`` is needed to remove warnings
 during PO file validation. Your contribution should be in UTF-8 anyways. 
 

Please note that: 

 - For dates, ``YYYY`` is the 4-digit year, ``MM`` is the 2-digit month,
 and ``DD`` is the 2-digit day.
 - The ``Source-Version`` should follow the format of ``x.y``, where ``x`` and
 ``y`` are both integers. Increase in ``x`` indicates a major structure
 change, e.g. adding or removing a paragraph. Increase in ``y`` indicates a
  minor change, e.g. a spelling mistake. Note that ``x`` and ``y`` can have
  multiple digits, e.g. ``1.12``. ``y`` should start at 0.
 - The ``Target-Version`` should also follow the format of ``x.y.z``. ``x`` and
 ``y`` should follow the ``x`` and ``y`` in ``Original-Version``. ``z`` should
 start at 0. It should be incremented before pushing the updated PO file to the
 main repository. ``z`` should be reset to 0, if a new ``Source-Version`` is
 released.

The metadata should be stored as ``msgstr`` for an empty ``msgid``. It
should look like this:

    msgid ""
    msgstr ""
    "FAH-Translate-Schema-Version: 1.0\n"
    "URL: https://foldingathome.org/diseases/\n"
    "Source-Language: en-US\n"
    "Source-Version: 1.0\n"
    "Source-Last-Modified: 20200705\n"
    "Target-Language: zh-CN\n"
    "Target-Version: 1.0.0\n"
    "Target-Last-Modified: 20200706\n"
    "Content-Type: text/plain; charset=UTF-8\n"

Please note that PO file editors may add their own fields. This is totally okay.

### How do I add a PO file?
It's awesome that you're eager to do more translations. For now, however, we don't have an established process yet to add new pages to the translation effort. We have to be careful with how we define the message IDs to ensure that they will later work correctly with our translation system. The translation coordination team will add more files as our processes mature and become more stable.

### Translation style guide
Please also check out the [Wiki](https://github.com/FoldingCommunity/Translate/wiki)
for the translation style guide. Please feel free to contribute to the Wiki. 

We will be adding more examples as translation progress. 

### Coordination
There are languages with multiple translators, please organise a team amongst
yourself. Please feel free to use the Folding@home Dev Discord server, or other
communication methods your translation team is comfortable with.

We recommend one member of your language team to fork this repository, and give
write access to all translators within your team, so every member of your team
can commit directly to the forked repository. We would like members within a
language team to discuss and review the translation. Once your team has agreed
upon a final version of the translation, please create a pull request for
this repository.

**Every language team will come up with their own ways of working and also might
be defining guidelines to follow. Check with them to find out what they already
did and where help is needed.**

You can check out the [Wiki](https://github.com/FoldingCommunity/Translate) for
some general guidelines and we would highly recommend joining the development
Discord server to easily coordinate with the other translators (and to avoid
working on the same things).

## Todo for developers
For this respository, we urgently need followings:

- [ ] PO file verification as a Github action

Other development tasks include: 
- [ ] A proper PO file generator
- [ ] PO file to HTML converter. 

## What if I need help? 
Please feel free to open an Github issue, and tag 
[Fufu (fangfufu)](https://github.com/fangfufu/), 
[Till Helge (Tar-Minyatur)](https://github.com/Tar-Minyatur),
[ReadyPlayerEmma](https://github.com/ReadyPlayerEmma)
and/or 
[Antonthynell](https://github.com/Antonthynell). Alternatively, you could
post a message in the main transation channel on Folding@home Dev Discord
server and tag one of us. 
