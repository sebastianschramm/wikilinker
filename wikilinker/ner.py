import json

from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline


def prepare_model_pipeline(model_name: str) -> pipeline:
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto")

    ner_gen = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        do_sample=False,
        max_new_tokens=100,
        return_full_text=False,
    )
    return ner_gen


def get_prompt_template():
    pt = """A virtual assistant answers questions from
         a user based on the provided text.
         USER: Text: {input_text}
         ASSISTANT: I’ve read this text.
         USER: What describes {entity_name} in the text?
         ASSISTANT:
         """
    return pt


def get_ner(input_text: str, entity_type: str, gen_ner):
    prompt = get_prompt_template().format_map(
        {"input_text": input_text, "entity_name": entity_type.lower()}
    )
    try:
        ner_list = json.loads(gen_ner(prompt)[0]["generated_text"])
    except Exception:
        ner_list = []
    return ner_list
