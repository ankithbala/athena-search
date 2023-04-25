from haystack.document_stores.elasticsearch import ElasticsearchDocumentStore
from haystack.nodes import ElasticsearchRetriever
from haystack.nodes import FARMReader
from haystack.pipelines import ExtractiveQAPipeline


# Initialize the document store
document_store = ElasticsearchDocumentStore(host="elasticsearch", username="", password="", index="document")


# Initialize the retriever
retriever = ElasticsearchRetriever(document_store=document_store)

# Initialize the reader
reader = FARMReader(model_name_or_path="deepset/bert-base-cased-squad2", use_gpu=False)

# Initialize the QA pipeline
pipeline = ExtractiveQAPipeline(reader=reader, retriever=retriever)

# Ask a question and get an answer
question = "What is Haystack?"
prediction = pipeline.run(query=question)

# Print the answer(s)
print(prediction["answers"])

'''
query = {
  "query": {
    "match_all": {}
  }
}

from elasticsearch import Elasticsearch
es = Elasticsearch(["elasticsearch"],  http_auth=("",""))
indices = es.cat.indices()

# Print the names of all indices
print(indices)
es.delete_by_query(index='document', body=query)
'''