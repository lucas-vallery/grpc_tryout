# Create python virtual environment
```bash
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```
To export the package list use the following command once the virtual environment is activated :
```bash
pip freeze > requirements.txt
```

# Generate code from .proto
## Python
```bash
python -m grpc_tools.protoc -I interface/ --python_out=interface/ --pyi_out=interface/--grpc_python_out=interface/ interface/camera-inteface.proto
```