from typing import List

import chainlit as cl

from wikilinker.ner import get_ner
from wikilinker.wiki import get_wiki_summary

AUTHOR_LINKER = "WIKILINKER"
AUTHOR_NER = "NER"
AUTHOR_USER = "User"
NER_MODEL_NAME = "SebastianSchramm/UniNER-7B-type-GPTQ-4bit-128g-actorder_True"


async def create_avatars():
    await cl.Avatar(
        name=AUTHOR_LINKER,
        path="avatars/linker.png",
    ).send()
    await cl.Avatar(
        name=AUTHOR_NER,
        path="avatars/llama.png",
    ).send()
    await cl.Avatar(
        name=AUTHOR_USER,
        path="avatars/user.png",
    ).send()


async def display_summaries(named_entities: List[str]):
    for entity in named_entities:
        await cl.Text(
            name=entity, content=get_wiki_summary(entity), display="side"
        ).send()


async def display_ner(entity_type: str, named_entities: List[str], parent_message_id):
    await cl.Message(
        content=f"Recognized the following entities of type {entity_type['content']}:"
        f"\n\t{named_entities}",
        parent_id=parent_message_id,
        author=AUTHOR_NER,
    ).send()


async def process_message(message: dict, entity_type: str):
    named_entities = get_ner(
        message, entity_type=entity_type, model_name=NER_MODEL_NAME
    )
    await display_ner(
        entity_type=entity_type,
        named_entities=named_entities,
        parent_message_id=message["id"],
    )
    await display_summaries(named_entities=named_entities)


@cl.on_chat_start
async def main():
    await create_avatars()

    entity_type = await cl.AskUserMessage(
        content="Which entity type do you want to link?",
        timeout=30,
        author=AUTHOR_LINKER,
    ).send()
    if entity_type:
        message = await cl.AskUserMessage(
            content="Which text do you want to process?",
            timeout=30,
            author=AUTHOR_LINKER,
        ).send()
        if message:
            await process_message(message=message, entity_type=entity_type["content"])
