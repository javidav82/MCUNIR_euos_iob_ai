# utils/loader.py
import joblib
import onnxruntime

def load_model(path):
    if path.endswith(".pkl"):
        return joblib.load(path)
    elif path.endswith(".onnx"):
        return onnxruntime.InferenceSession(path)
    else:
        raise ValueError("Formato de modelo no soportado")
