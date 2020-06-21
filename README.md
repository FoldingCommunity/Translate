# Translate

Thank you for helping us reach even more people around the world by adapting the
experience to their native language.

**Before you start translating, please read this README to learn how we
collaborate and how to find out what is already done and what is left to do.**

## What do we translate?

We will start translating the [Folding@Home](https://foldingathome.org) website.
We are starting with the following webpages: 

1. https://foldingathome.org
2. https://foldingathome.org/about/
3. https://foldingathome.org/start-folding/
4. https://foldingathome.org/diseases/
5. https://foldingathome.org/statistics/

We will add more pages as we go on. Please look out for the announcements.

## Coordination
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

## How do we translate?
So far we have extracted text blocks and created yaml files in 
[Localization/en-US](Localization/en-US). Please copy the yaml in your 
language's folder, edit the ``language`` code in the yaml file, and
translate the text between the quotation marks 
(e.g. `` " These are the text that need to be translated " ``). 

Please use your favourite text editor to make the edit. On Windows, you could 
use [Notepad++](https://notepad-plus-plus.org/) or 
[Atom](https://atom.io/).

Please stick to the format, this will help with the automated webpage generation
in the later stage. 

Please parsed your yaml files through a yaml verifier, e.g. 
[YAML Lint](http://www.yamllint.com/) or 
[onlineyamltools](https://onlineyamltools.com/validate-yaml) before commiting.

### Why are we using YAML? 
We use YAML because it enables automation. The idea is that one of us will be 
writing a Wordpress blog post generator, which takes in YAML files, and generates 
Wordpress blog posts for Folding@home website. 

We believe that YAML files are quite easy for non-programmers to read and edit,
so even if we don't manage to create a blog post generator, it should not be
too difficult to manually copy and paste the content from YAML files and 
create blog posts manually. The structure of the YAML file serve as a metadata 
to guide the webmasters at editing languages which they might not understand. 

### Translation style guide
Please also check out the [Wiki](https://github.com/FoldingCommunity/Translate/wiki)
for the translation style guide. Please feel free to contribute to the Wiki. 

### Examples:

- [Localization/sv-SE/home.yaml](Localization/sv-SE/home.yaml)
is the Swedish translation for
[Localization/en-US/home.yaml](Localization/en-US/home.yaml)
- [Localization/de-DE/about.yaml](Localization/de-DE/about.yaml)
is the German translation for
[Localization/en-US/about.yaml](Localization/en-US/about.yaml)
- [Localization/fr-FR/about.yaml](Localization/fr-FR/about.yaml)
is the French translation for
[Localization/en-US/about.yaml](Localization/en-US/about.yaml)

We will be adding more examples as translation progress. 

## What if I need help? 
Please feel free to open an Github issue, and tag 
[fangfufu](https://github.com/fangfufu/), 
[ReadyPlayerEmma](https://github.com/ReadyPlayerEmma)
and/or 
[Antonthynell](https://github.com/Antonthynell). Alternatively, you could
post a message in the main transation channel on Folding@home Dev Discord
server and tag one of us. 
