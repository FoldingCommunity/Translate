# Translate

Thank you for helping us reach even more people around the world by adapting the
experience to their native language.

## What do we translate?

We will start translating the [Folding@Home](https://foldingathome.org) website.
We are starting with the following webpages: 

1. https://foldingathome.org
2. https://foldingathome.org/about/
3. https://foldingathome.org/start-folding/
4. https://foldingathome.org/diseases/
5. https://foldingathome.org/statistics/

We will add more pages as we go on. Please look out for the announcements.

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

### Examples:

- [Localization/sv-SE/home.yaml](Localization/sv-SE/home.yaml) is a Swedish
translated example for 
[Localization/en-US/home.yaml](Localization/en-US/home.yaml)

We will be adding more examples as translation progress. 

## What if I need help? 
Please feel free to open an Github issue, and tag 
[fangfufu](https://github.com/fangfufu/) and/or 
[Antonthynell](https://github.com/Antonthynell)
