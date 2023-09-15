# WikiLinker

![Alt text](avatars/linker.png?raw=true "Wikilinker")

Wikilinker is a chainlit based app to perform arbitrary named entity recognition on a given text using UniversalNER (a task-specific LLM). Identified entities are exactly matched with wikipedia page titles and a summary of the wikipedia page is linked to those entities should the wikipedia pages exist.

Check out the [demo video](https://www.linkedin.com/posts/activity-7107430138702610437-rMkc/) of the app on my linkedin.

## Installation

You can install the wikilinker package via pip by executing the following command:

```bash
pip install git+https://github.com/sebastianschramm/wikilinker.git
```

or by first cloning the repository and then installing by executing the following command in the root of the cloned repository:

```bash
pip install .
```

## Start the app

You have 2 ways to start the wikilinker.
The recommende way is to use the provided script command "neo" (make sure you have the wikilinker package installed prior to that):

```bash
neo
```

Alternatively, if you have cloned the respository, you can use the chainlit cli in the root of the repository:

```bash
chainlit run wikilinker/server.py
```

## Usage of the app

First, provide an entity type in plain English, e.g., "city" or "medical condition."
Then, enter the text in which you want to find the selected entities.

If entities are identified, the words will be highlighted, and you will be able to click on them to see the summary of their Wikipedia page if a Wikipedia entry exists.
