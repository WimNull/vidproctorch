try:
    from .LibPytorchNvCodec import *
except Exception as e:
    print('Exception:', e)

__all__ = [
    "DptrToTensor",
    "TensorToDptr",
    "makefromDevicePtrUint8"
]