from langchain import PromptTemplate, LLMChain


def generate_title(llm, filename):

    # Map
    map_template = """[INST] <<SYS>>
        You are a helpful assistant. Complete the task below. Output the answer only. Do not include any greetings or instructions.
        <</SYS>>
        Generate a title for a podcast episode from the filename below:
        {filename}[/INST]
        """
    map_prompt = PromptTemplate.from_template(map_template)
    map_chain = LLMChain(llm=llm, prompt=map_prompt)

    # Process each chunk through the map_chain
    title = map_chain.run(filename)
    title = title.replace(
        "Sure! Here's a possible title for your podcast episode based on the given filename:", "")

    return title
