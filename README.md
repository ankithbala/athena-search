# Athena Search

**Basic Installation**

Use [pip](https://github.com/pypa/pip) to install a basic version of Haystack's latest release:

```
    pip install farm-haystack
```

This command installs everything needed for basic Pipelines that use an Elasticsearch DocumentStore.

**Full Installation**

To use more advanced features, like certain DocumentStores, FileConverters, OCR, or Ray, install further dependencies. The following command installs the latest version of Haystack and all its dependencies from the main branch:

```
git clone https://github.com/deepset-ai/haystack.git
cd haystack
pip install --upgrade pip
pip install -e '.[all]' ## or 'all-gpu' for the GPU-enabled dependencies
```

**Custom Installation**
You can choose the dependencies you want to install. To do so, specify them in the `pip install` command:

```
pip install 'farm-haystack[DEPENDENCY_OPTION]'
```
You can find a full list of dependency options at [haystack/pyproject.toml](https://github.com/deepset-ai/haystack/blob/main/pyproject.toml#L96).

If you're running pip version earlier than 21.3, you can't install dependency groups that reference other groups. Instead, you can only specify groups that contain direct package references:

```
# instead of '[all]'
pip install 'farm-haystack[sql,only-faiss,only-milvus1,weaviate,pinecone,opensearch,graphdb,inmemorygraph,crawler,preprocessing,ocr,onnx,ray,dev]'

# instead of '[all-gpu]'
pip install 'farm-haystack[sql,only-faiss-gpu,only-milvus1,weaviatepinecone,opensearch,graphdb,inmemorygraph,crawler,preprocessing,ocr,onnx-gpu,ray,dev]'
```

**Installing the REST API**
Haystack comes packaged with a REST API so that you can deploy it as a service. Run the following command from the root directory of the Haystack repo to install REST_API:

```
pip install rest_api/
```

**Other Operating Systems**

**Windows**
We recommend installing [WSL](https://learn.microsoft.com/en-us/windows/wsl/install) to use Haystack on Windows:

```
pip install farm-haystack -f https://download.pytorch.org/whl/torch_stable.html
```

**Apple Silicon (M1)**

Macs with an M1 processor require some extra dependencies to install Haystack:

```
# some additional dependencies needed on m1 mac
brew install postgresql
brew install cmake
brew install rust

# haystack installation
GRPC_PYTHON_BUILD_SYSTEM_ZLIB=true pip install git+https://github.com/deepset-ai/haystack.git
```



![image](https://raw.githubusercontent.com/deepset-ai/haystack/main/docs/img/concepts_haystack_handdrawn.png)





