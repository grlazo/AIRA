## AI Research Assistant (AIRA)

Your AI Research Assistant (AIRA) needs a few things to get started.
Basically you need the Ollama AI interface (****ollama.ai****) installed, 
and the Ianaconda (or miniconda3) to set up a python environment.

Ollama can be istalled on Linux, Windows, or Apple (check your requirements).

Once you have Ollama installed, you need an embedding model and a 
large language model (LLM). You can visit the website to discover all 
that is available. It's best to install your ollama instance under the 
conda environment to make sure both are working under the same environment.

For instance on a Windows machine you would start your Anaconda Powershell
and run the following commands:
```
$ ollama pull nomic-embed-text
$ ollama pull llama3.1
```
The above will get you started; you may change these later.

You can check if ollama is running on your local machine by opening a web 
browser to the following address: http://localhost:11434/
It should display: ****ollama is running****
 
Next you will need to set up your conda environment; start by naming your
environment:
```
$ conda create --name AIRA python==3.12
$ conda activate AIRA
$ conda list
```
Create a working directory for the AIRA files somewhere. Eventually you can 
change the name of the AIRA directory to your favorite SUBJECT matter for 
your prompt topics and papers.

You will install needed packages in this environment; updates often occur 
so validated packages and versions will be included in a requirements.txt 
file. I like to install each individually to make sure everything loads 
properly.
```
$ pip install pypdf
$ pip install pytest
$ pip install boto3
$ pip install langchain-community
$ pip install langchain-ollama
$ pip install langchain-chroma
```
original source is from a tutorial at: ****github.com/pixegami/rag-tutorial-v2****
modifications were made to reflect updates in available python packages.

There should be no issues under a Linux environment, but the peculiar steps 
suggested were encountered when walking someone through this process for a 
Windows machine (not sure about Apple).

Now you're ready to create the vector store for your collection of PDF documents.
Place your PDF files in a directory called '***data***'. Start with one, or a few, to 
start until you're comfortable with the limitations on your machine settings. 
There can be a hard-limit overflow which will fail populating the vector store.

Once the PDFs are in place the directory structure should look like:
```
./AIRA/data/file01.pdf
./AIRA/data/file02.pdf
./AIRA/data/file03.pdf
./AIRA/get_embedding_function.py
./AIRA/populate_database.py
./AIRA/query_data.py
./AIRA/requirements.txt
./AIRA/RunningAIRA.txt
```
Enable the embedding function:
```
$ python get_embedding_function.py
```
Load documents into vector store:
```
$ python populate_database.py
```
You are ready to begin Retrieval Augmented Generation (RAG) prompts:
```
$ python query_data.py "Can you summarize the contents of the documents provided?"
```
If it replies you may be on a new road to discovery. Have fun!

As your collection of information grows, try adding new documents into the 
'****./data****' directory and re-issue the embedding and populate python 
commands. If new documents are detected they will be added to your vector 
database (remember not to over-populate the ability of the vector store to 
read your documents (a 41500 chunk limit size was in chromdb version used).

You can unpack multiple subject directories renaming the AIRA directory to
different topics such as biology, chemistry, fruits, vegetables, etc...

Note: If you're in a Linux command shell, do:
```
$ grep '\$' README.md to see commands to issue after installing ollama.
```
