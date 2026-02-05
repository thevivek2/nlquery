# A complete offline AI based program that does natural language to sql conversion. 
## Works under limited cpu i5 and 16GB RAM while other programs are also running
## Uses ollama and its models phi, phi4 

download, install & run ollama, https://ollama.com/download/windows <br/>
get phi, phi4 model, `ollama pull phi`  <br/>
install python modules, `pip install fastapi uvicorn ollama` <br/>
                       `pip install fastapi uvicorn ollama sentence-transformers faiss-cpu` <br/>


`python Main.py` <br/>
`python Main2.py` <br/>

# Purpose that extends As Data Analysis Agent
## Finding AI best and efficient models to use offline that overcomes need of generating sql from natural laguage
## Providing best need context to it from huge schema set/descriptions
## Query can be used via SQL tools, DBeaver, MySQL Workbench to get data/reports etc...

![Example](NL-to-SQL.png)

Custom provided huge schema defination can be indexed doing <br/>
`python .\index\indexer.py` <br/>

Optionals: <br>
To see while you wait for ollama to respond <br/>
`ollama ps`
`taskkill /IM ollama.exe` /F  <br/>
if you want to start ollama from command line  </br>
`ollama serve`
`test.sh` simply run a prompt in ollama


