from langchain.document_loaders import TextLoader, DirectoryLoader

def load_docs(pickle = False):
    if pickle:
        loader = DirectoryLoader(
        "./docs",
        glob="**/*.pkl",
        recursive=True,
        loader_cls=TextLoader
    )
    else:
        # Load docs
        loader = DirectoryLoader(
            "./docs",
            glob="**/*.txt",
            recursive=True,

            loader_cls=TextLoader
        )

    docs = loader.load()

    # loaders = [
    #     TextLoader("./docs/ALittleHackToMakeAmazingAdsThatConvert_no_timestamps.txt"),
    #     TextLoader("./docs/99YardsDothNotATouchdownMake_no_timestamps.txt"),
    # ]
    # docs = []
    # for loader in loaders:
    #    docs.extend(loader.load())

    return docs
