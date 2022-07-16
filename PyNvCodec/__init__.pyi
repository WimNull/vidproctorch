#
# Automatically generated file, do not edit!
#

"""Python bindings for Nvidia-accelerated video processing"""
from __future__ import annotations
from .LibPyNvCodec import *
import typing
import numpy
_Shape = typing.Tuple[int, ...]

__all__ = [
    "BGR",
    "BT_601",
    "BT_709",
    "BY_NUMBER",
    "BY_TIMESTAMP",
    "ColorRange",
    "ColorSpace",
    "ColorspaceConversionContext",
    "CudaBuffer",
    "CudaVideoCodec",
    "CuvidParserException",
    "EXACT_FRAME",
    "GetNumGpus",
    "H264",
    "HEVC",
    "HwResetException",
    "JPEG",
    "MPEG",
    "MotionVector",
    "NO_PTS",
    "NV12",
    "PREV_KEY_FRAME",
    "PacketData",
    "PixelFormat",
    "PyBufferUploader",
    "PyCudaBufferDownloader",
    "PyFFmpegDemuxer",
    "PyFfmpegDecoder",
    "PyFrameUploader",
    "PyNvDecoder",
    "PyNvEncoder",
    "PySurfaceConverter",
    "PySurfaceDownloader",
    "PySurfaceRemaper",
    "PySurfaceResizer",
    "RGB",
    "RGB_32F",
    "RGB_32F_PLANAR",
    "RGB_PLANAR",
    "SeekContext",
    "SeekCriteria",
    "SeekMode",
    "Surface",
    "SurfacePlane",
    "UDEF",
    "UNDEFINED",
    "UNSPEC",
    "VP9",
    "Y",
    "YCBCR",
    "YUV420",
    "YUV422",
    "YUV444",
    "cconverter"
]

from . import LibPyNvCodec as nvc

class cconverter:
    """
    Colorspace conversion chain.
    """
    def __init__(self, width: int, height: int, gpu_id: int):...

    def add(self, src_fmt: nvc.PixelFormat, dst_fmt: nvc.PixelFormat) -> None:...

    def run(self, src_surface: nvc.Surface) -> nvc.Surface:...


class ColorRange():
    """
    Members:

      MPEG

      JPEG

      UDEF
    """
    def __init__(self, arg0: int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    JPEG: LibPyNvCodec.ColorRange # value = ColorRange.JPEG
    MPEG: LibPyNvCodec.ColorRange # value = ColorRange.MPEG
    UDEF: LibPyNvCodec.ColorRange # value = ColorRange.UDEF
    __members__: dict # value = {'MPEG': ColorRange.MPEG, 'JPEG': ColorRange.JPEG, 'UDEF': ColorRange.UDEF}
    pass
class ColorSpace():
    """
    Members:

      BT_601

      BT_709

      UNSPEC
    """
    def __init__(self, arg0: int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    BT_601: LibPyNvCodec.ColorSpace # value = ColorSpace.BT_601
    BT_709: LibPyNvCodec.ColorSpace # value = ColorSpace.BT_709
    UNSPEC: LibPyNvCodec.ColorSpace # value = ColorSpace.UNSPEC
    __members__: dict # value = {'BT_601': ColorSpace.BT_601, 'BT_709': ColorSpace.BT_709, 'UNSPEC': ColorSpace.UNSPEC}
    pass
class ColorspaceConversionContext():
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, color_space: ColorSpace, color_range: ColorRange) -> None: ...
    @property
    def color_range(self) -> ColorRange:
        """
        :type: ColorRange
        """
    @color_range.setter
    def color_range(self, arg0: ColorRange) -> None:
        pass
    @property
    def color_space(self) -> ColorSpace:
        """
        :type: ColorSpace
        """
    @color_space.setter
    def color_space(self, arg0: ColorSpace) -> None:
        pass
    pass
class CudaBuffer():
    def Clone(self) -> CudaBuffer: ...
    @typing.overload
    def CopyFrom(self, arg0: CudaBuffer, arg1: int) -> None: ...
    @typing.overload
    def CopyFrom(self, arg0: CudaBuffer, arg1: int, arg2: int) -> None: ...
    def GetElemSize(self) -> int: ...
    def GetNumElems(self) -> int: ...
    def GetRawMemSize(self) -> int: ...
    def GpuMem(self) -> int: ...
    @staticmethod
    def Make(arg0: int, arg1: int, arg2: int) -> CudaBuffer: ...
    pass
class CudaVideoCodec():
    """
    Members:

      H264

      HEVC

      VP9
    """
    def __init__(self, arg0: int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    H264: LibPyNvCodec.CudaVideoCodec # value = CudaVideoCodec.H264
    HEVC: LibPyNvCodec.CudaVideoCodec # value = CudaVideoCodec.HEVC
    VP9: LibPyNvCodec.CudaVideoCodec # value = CudaVideoCodec.VP9
    __members__: dict # value = {'H264': CudaVideoCodec.H264, 'HEVC': CudaVideoCodec.HEVC, 'VP9': CudaVideoCodec.VP9}
    pass
class CuvidParserException(Exception, BaseException):
    pass
class HwResetException(Exception, BaseException):
    pass
class MotionVector():
    pass
class PacketData():
    def __init__(self) -> None: ...
    @property
    def bsl(self) -> int:
        """
        :type: int
        """
    @bsl.setter
    def bsl(self, arg0: int) -> None:
        pass
    @property
    def dts(self) -> int:
        """
        :type: int
        """
    @dts.setter
    def dts(self, arg0: int) -> None:
        pass
    @property
    def duration(self) -> int:
        """
        :type: int
        """
    @duration.setter
    def duration(self, arg0: int) -> None:
        pass
    @property
    def pos(self) -> int:
        """
        :type: int
        """
    @pos.setter
    def pos(self, arg0: int) -> None:
        pass
    @property
    def pts(self) -> int:
        """
        :type: int
        """
    @pts.setter
    def pts(self, arg0: int) -> None:
        pass
    pass
class PixelFormat():
    """
    Members:

      Y

      RGB

      NV12

      YUV420

      RGB_PLANAR

      BGR

      YCBCR

      YUV444

      UNDEFINED

      RGB_32F

      RGB_32F_PLANAR

      YUV422
    """
    def __init__(self, arg0: int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    BGR: LibPyNvCodec.PixelFormat # value = PixelFormat.BGR
    NV12: LibPyNvCodec.PixelFormat # value = PixelFormat.NV12
    RGB: LibPyNvCodec.PixelFormat # value = PixelFormat.RGB
    RGB_32F: LibPyNvCodec.PixelFormat # value = PixelFormat.RGB_32F
    RGB_32F_PLANAR: LibPyNvCodec.PixelFormat # value = PixelFormat.RGB_32F_PLANAR
    RGB_PLANAR: LibPyNvCodec.PixelFormat # value = PixelFormat.RGB_PLANAR
    UNDEFINED: LibPyNvCodec.PixelFormat # value = PixelFormat.UNDEFINED
    Y: LibPyNvCodec.PixelFormat # value = PixelFormat.Y
    YCBCR: LibPyNvCodec.PixelFormat # value = PixelFormat.YCBCR
    YUV420: LibPyNvCodec.PixelFormat # value = PixelFormat.YUV420
    YUV422: LibPyNvCodec.PixelFormat # value = PixelFormat.YUV422
    YUV444: LibPyNvCodec.PixelFormat # value = PixelFormat.YUV444
    __members__: dict # value = {'Y': PixelFormat.Y, 'RGB': PixelFormat.RGB, 'NV12': PixelFormat.NV12, 'YUV420': PixelFormat.YUV420, 'RGB_PLANAR': PixelFormat.RGB_PLANAR, 'BGR': PixelFormat.BGR, 'YCBCR': PixelFormat.YCBCR, 'YUV444': PixelFormat.YUV444, 'UNDEFINED': PixelFormat.UNDEFINED, 'RGB_32F': PixelFormat.RGB_32F, 'RGB_32F_PLANAR': PixelFormat.RGB_32F_PLANAR, 'YUV422': PixelFormat.YUV422}
    pass
class PyBufferUploader():
    def UploadSingleBuffer(self, arg0: numpy.ndarray[uint8]) -> CudaBuffer: ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int, arg2: int) -> None: ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int) -> None: ...
    pass
class PyCudaBufferDownloader():
    def DownloadSingleCudaBuffer(self, arg0: CudaBuffer, arg1: numpy.ndarray[uint8]) -> bool: ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int, arg2: int) -> None: ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int) -> None: ...
    pass
class PyFFmpegDemuxer():
    def AvgFramerate(self) -> float: ...
    def Codec(self) -> CudaVideoCodec: ...
    def ColorRange(self) -> ColorRange: ...
    def ColorSpace(self) -> ColorSpace: ...
    @typing.overload
    def DemuxSinglePacket(self, packet: numpy.ndarray[uint8]) -> bool: ...
    @typing.overload
    def DemuxSinglePacket(self, packet: numpy.ndarray[uint8], sei: numpy.ndarray[uint8]) -> bool: ...
    def Format(self) -> PixelFormat: ...
    def Framerate(self) -> float: ...
    def Height(self) -> int: ...
    def IsVFR(self) -> bool: ...
    def LastPacketData(self, arg0: PacketData) -> None: ...
    def Numframes(self) -> int: ...
    def Seek(self, arg0: SeekContext, arg1: numpy.ndarray[uint8]) -> bool: ...
    def Timebase(self) -> float: ...
    def Width(self) -> int: ...
    @typing.overload
    def __init__(self, arg0: str) -> None: ...
    @typing.overload
    def __init__(self, arg0: str, arg1: typing.Dict[str, str]) -> None: ...
    pass
class PyFfmpegDecoder():
    def DecodeSingleFrame(self, arg0: numpy.ndarray[uint8]) -> bool: ...
    def GetMotionVectors(self) -> numpy.ndarray[MotionVector]: ...
    def __init__(self, arg0: str, arg1: typing.Dict[str, str]) -> None: ...
    pass
class PyFrameUploader():
    def Format(self) -> PixelFormat: ...
    @typing.overload
    def UploadSingleFrame(self, frame: numpy.ndarray[numpy.float32]) -> Surface: ...
    @typing.overload
    def UploadSingleFrame(self, frame: numpy.ndarray[uint8]) -> Surface: ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int, arg2: PixelFormat, arg3: int) -> None: ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int, arg2: PixelFormat, arg3: int, arg4: int) -> None: ...
    pass
class PyNvDecoder():
    def AvgFramerate(self) -> float: ...
    def ColorRange(self) -> ColorRange: ...
    def ColorSpace(self) -> ColorSpace: ...
    @typing.overload
    def DecodeFrameFromPacket(self, frame: numpy.ndarray[uint8], enc_packet_data: PacketData, packet: numpy.ndarray[uint8]) -> bool: ...
    @typing.overload
    def DecodeFrameFromPacket(self, frame: numpy.ndarray[uint8], enc_packet_data: PacketData, packet: numpy.ndarray[uint8], packet_data: PacketData) -> bool: ...
    @typing.overload
    def DecodeFrameFromPacket(self, frame: numpy.ndarray[uint8], packet: numpy.ndarray[uint8]) -> bool: ...
    @typing.overload
    def DecodeFrameFromPacket(self, frame: numpy.ndarray[uint8], packet: numpy.ndarray[uint8], packet_data: PacketData) -> bool: ...
    @typing.overload
    def DecodeSingleFrame(self, frame: numpy.ndarray[uint8]) -> bool: ...
    @typing.overload
    def DecodeSingleFrame(self, frame: numpy.ndarray[uint8], packet_data: PacketData) -> bool: ...
    @typing.overload
    def DecodeSingleFrame(self, frame: numpy.ndarray[uint8], seek_context: SeekContext) -> bool: ...
    @typing.overload
    def DecodeSingleFrame(self, frame: numpy.ndarray[uint8], seek_context: SeekContext, packet_data: PacketData) -> bool: ...
    @typing.overload
    def DecodeSingleFrame(self, frame: numpy.ndarray[uint8], sei: numpy.ndarray[uint8]) -> bool: ...
    @typing.overload
    def DecodeSingleFrame(self, frame: numpy.ndarray[uint8], sei: numpy.ndarray[uint8], packet_data: PacketData) -> bool: ...
    @typing.overload
    def DecodeSingleFrame(self, frame: numpy.ndarray[uint8], sei: numpy.ndarray[uint8], seek_context: SeekContext) -> bool: ...
    @typing.overload
    def DecodeSingleFrame(self, frame: numpy.ndarray[uint8], sei: numpy.ndarray[uint8], seek_context: SeekContext, packet_data: PacketData) -> bool: ...
    @typing.overload
    def DecodeSingleSurface(self) -> Surface: ...
    @typing.overload
    def DecodeSingleSurface(self, packet_data: PacketData) -> Surface: ...
    @typing.overload
    def DecodeSingleSurface(self, seek_context: SeekContext) -> Surface: ...
    @typing.overload
    def DecodeSingleSurface(self, seek_context: SeekContext, packet_data: PacketData) -> Surface: ...
    @typing.overload
    def DecodeSingleSurface(self, sei: numpy.ndarray[uint8]) -> Surface: ...
    @typing.overload
    def DecodeSingleSurface(self, sei: numpy.ndarray[uint8], packet_data: PacketData) -> Surface: ...
    @typing.overload
    def DecodeSingleSurface(self, sei: numpy.ndarray[uint8], seek_context: SeekContext) -> Surface: ...
    @typing.overload
    def DecodeSingleSurface(self, sei: numpy.ndarray[uint8], seek_context: SeekContext, packet_data: PacketData) -> Surface: ...
    @typing.overload
    def DecodeSurfaceFromPacket(self, enc_packet_data: PacketData, packet: numpy.ndarray[uint8]) -> Surface: ...
    @typing.overload
    def DecodeSurfaceFromPacket(self, enc_packet_data: PacketData, packet: numpy.ndarray[uint8], packet_data: PacketData) -> Surface: ...
    @typing.overload
    def DecodeSurfaceFromPacket(self, packet: numpy.ndarray[uint8]) -> Surface: ...
    @typing.overload
    def DecodeSurfaceFromPacket(self, packet: numpy.ndarray[uint8], packet_data: PacketData) -> Surface: ...
    @typing.overload
    def FlushSingleFrame(self, frame: numpy.ndarray[uint8]) -> bool: ...
    @typing.overload
    def FlushSingleFrame(self, frame: numpy.ndarray[uint8], packet_data: PacketData) -> bool: ...
    @typing.overload
    def FlushSingleSurface(self) -> Surface: ...
    @typing.overload
    def FlushSingleSurface(self, packet_data: PacketData) -> Surface: ...
    def Format(self) -> PixelFormat: ...
    def Framerate(self) -> float: ...
    def Framesize(self) -> int: ...
    def Height(self) -> int: ...
    def IsVFR(self) -> bool: ...
    def LastPacketData(self, arg0: PacketData) -> None: ...
    def Numframes(self) -> int: ...
    def Timebase(self) -> float: ...
    def Width(self) -> int: ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int, arg2: PixelFormat, arg3: CudaVideoCodec, arg4: int) -> None: ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int, arg2: PixelFormat, arg3: CudaVideoCodec, arg4: int, arg5: int) -> None: ...
    @typing.overload
    def __init__(self, arg0: str, arg1: int) -> None: ...
    @typing.overload
    def __init__(self, arg0: str, arg1: int, arg2: int) -> None: ...
    @typing.overload
    def __init__(self, arg0: str, arg1: int, arg2: int, arg3: typing.Dict[str, str]) -> None: ...
    @typing.overload
    def __init__(self, arg0: str, arg1: int, arg2: typing.Dict[str, str]) -> None: ...
    pass
class PyNvEncoder():
    @typing.overload
    def EncodeSingleFrame(self, frame: numpy.ndarray[uint8], packet: numpy.ndarray[uint8]) -> bool: ...
    @typing.overload
    def EncodeSingleFrame(self, frame: numpy.ndarray[uint8], packet: numpy.ndarray[uint8], sei: numpy.ndarray[uint8]) -> bool: ...
    @typing.overload
    def EncodeSingleFrame(self, frame: numpy.ndarray[uint8], packet: numpy.ndarray[uint8], sei: numpy.ndarray[uint8], sync: bool) -> bool: ...
    @typing.overload
    def EncodeSingleFrame(self, frame: numpy.ndarray[uint8], packet: numpy.ndarray[uint8], sei: numpy.ndarray[uint8], sync: bool, append: bool) -> bool: ...
    @typing.overload
    def EncodeSingleFrame(self, frame: numpy.ndarray[uint8], packet: numpy.ndarray[uint8], sync: bool) -> bool: ...
    @typing.overload
    def EncodeSingleSurface(self, surface: Surface, packet: numpy.ndarray[uint8]) -> bool: ...
    @typing.overload
    def EncodeSingleSurface(self, surface: Surface, packet: numpy.ndarray[uint8], sei: numpy.ndarray[uint8]) -> bool: ...
    @typing.overload
    def EncodeSingleSurface(self, surface: Surface, packet: numpy.ndarray[uint8], sei: numpy.ndarray[uint8], sync: bool) -> bool: ...
    @typing.overload
    def EncodeSingleSurface(self, surface: Surface, packet: numpy.ndarray[uint8], sei: numpy.ndarray[uint8], sync: bool, append: bool) -> bool: ...
    @typing.overload
    def EncodeSingleSurface(self, surface: Surface, packet: numpy.ndarray[uint8], sync: bool) -> bool: ...
    def Flush(self, packets: numpy.ndarray[uint8]) -> bool: ...
    def FlushSinglePacket(self, packets: numpy.ndarray[uint8]) -> bool: ...
    def Format(self) -> PixelFormat: ...
    def Height(self) -> int: ...
    def Reconfigure(self, settings: typing.Dict[str, str], force_idr: bool = False, reset_encoder: bool = False, verbose: bool = False) -> bool: ...
    def Width(self) -> int: ...
    @typing.overload
    def __init__(self, settings: typing.Dict[str, str], cuda_context: int, cuda_stream: int, format: PixelFormat = PixelFormat.NV12, verbose: bool = False) -> None: ...
    @typing.overload
    def __init__(self, settings: typing.Dict[str, str], gpu_id: int, format: PixelFormat = PixelFormat.NV12, verbose: bool = False) -> None: ...
    pass
class PySurfaceConverter():
    def Execute(self, arg0: Surface, arg1: ColorspaceConversionContext) -> Surface: ...
    def Format(self) -> PixelFormat: ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int, arg2: PixelFormat, arg3: PixelFormat, arg4: int) -> None: ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int, arg2: PixelFormat, arg3: PixelFormat, arg4: int, arg5: int) -> None: ...
    pass
class PySurfaceDownloader():
    @typing.overload
    def DownloadSingleSurface(self, surface: Surface, frame: numpy.ndarray[numpy.float32]) -> bool: ...
    @typing.overload
    def DownloadSingleSurface(self, surface: Surface, frame: numpy.ndarray[uint8]) -> bool: ...
    def Format(self) -> PixelFormat: ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int, arg2: PixelFormat, arg3: int) -> None: ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int, arg2: PixelFormat, arg3: int, arg4: int) -> None: ...
    pass
class PySurfaceRemaper():
    def Execute(self, arg0: Surface) -> Surface: ...
    def Format(self) -> PixelFormat: ...
    @typing.overload
    def __init__(self, arg0: numpy.ndarray[numpy.float32], arg1: numpy.ndarray[numpy.float32], arg2: int, arg3: int, arg4: PixelFormat, arg5: int) -> None: ...
    @typing.overload
    def __init__(self, arg0: numpy.ndarray[numpy.float32], arg1: numpy.ndarray[numpy.float32], arg2: int, arg3: int, arg4: PixelFormat, arg5: int, arg6: int) -> None: ...
    pass
class PySurfaceResizer():
    def Execute(self, arg0: Surface) -> Surface: ...
    def Format(self) -> PixelFormat: ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int, arg2: PixelFormat, arg3: int) -> None: ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int, arg2: PixelFormat, arg3: int, arg4: int) -> None: ...
    pass
class SeekContext():
    @typing.overload
    def __init__(self, seek_frame: int) -> None: ...
    @typing.overload
    def __init__(self, seek_frame: int, mode: SeekMode) -> None: ...
    @typing.overload
    def __init__(self, seek_frame: int, mode: SeekMode, seek_criteria: SeekCriteria) -> None: ...
    @typing.overload
    def __init__(self, seek_frame: int, seek_criteria: SeekCriteria) -> None: ...
    @property
    def mode(self) -> SeekMode:
        """
        :type: SeekMode
        """
    @mode.setter
    def mode(self, arg0: SeekMode) -> None:
        pass
    @property
    def num_frames_decoded(self) -> int:
        """
        :type: int
        """
    @property
    def out_frame_pts(self) -> int:
        """
        :type: int
        """
    @out_frame_pts.setter
    def out_frame_pts(self, arg0: int) -> None:
        pass
    @property
    def seek_frame(self) -> int:
        """
        :type: int
        """
    @seek_frame.setter
    def seek_frame(self, arg0: int) -> None:
        pass
    pass
class SeekCriteria():
    """
    Members:

      BY_NUMBER

      BY_TIMESTAMP
    """
    def __init__(self, arg0: int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    BY_NUMBER: LibPyNvCodec.SeekCriteria # value = SeekCriteria.BY_NUMBER
    BY_TIMESTAMP: LibPyNvCodec.SeekCriteria # value = SeekCriteria.BY_TIMESTAMP
    __members__: dict # value = {'BY_NUMBER': SeekCriteria.BY_NUMBER, 'BY_TIMESTAMP': SeekCriteria.BY_TIMESTAMP}
    pass
class SeekMode():
    """
    Members:

      EXACT_FRAME

      PREV_KEY_FRAME
    """
    def __init__(self, arg0: int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    EXACT_FRAME: LibPyNvCodec.SeekMode # value = SeekMode.EXACT_FRAME
    PREV_KEY_FRAME: LibPyNvCodec.SeekMode # value = SeekMode.PREV_KEY_FRAME
    __members__: dict # value = {'EXACT_FRAME': SeekMode.EXACT_FRAME, 'PREV_KEY_FRAME': SeekMode.PREV_KEY_FRAME}
    pass
class Surface():
    @typing.overload
    def Clone(self, arg0: int) -> Surface: ...
    @typing.overload
    def Clone(self, arg0: int, arg1: int) -> Surface: ...
    @typing.overload
    def CopyFrom(self, arg0: Surface, arg1: int) -> None: ...
    @typing.overload
    def CopyFrom(self, arg0: Surface, arg1: int, arg2: int) -> None: ...
    def Empty(self) -> bool: ...
    def Format(self) -> PixelFormat: ...
    def Height(self, planeNumber: int = 0) -> int: ...
    def HostSize(self) -> int: ...
    @staticmethod
    def Make(arg0: PixelFormat, arg1: int, arg2: int, arg3: int) -> Surface: ...
    def NumPlanes(self) -> int: ...
    def Pitch(self, planeNumber: int = 0) -> int: ...
    def PlanePtr(self, planeNumber: int = 0) -> SurfacePlane: ...
    def Width(self, planeNumber: int = 0) -> int: ...
    pass
class SurfacePlane():
    def ElemSize(self) -> int: ...
    @typing.overload
    def Export(self, arg0: int, arg1: int, arg2: int) -> None: ...
    @typing.overload
    def Export(self, arg0: int, arg1: int, arg2: int, arg3: int) -> None: ...
    def GpuMem(self) -> int: ...
    def Height(self) -> int: ...
    def HostFrameSize(self) -> int: ...
    @typing.overload
    def Import(self, arg0: int, arg1: int, arg2: int) -> None: ...
    @typing.overload
    def Import(self, arg0: int, arg1: int, arg2: int, arg3: int) -> None: ...
    def Pitch(self) -> int: ...
    def Width(self) -> int: ...
    pass
def GetNumGpus() -> int:
    pass
BGR: LibPyNvCodec.PixelFormat # value = PixelFormat.BGR
BT_601: LibPyNvCodec.ColorSpace # value = ColorSpace.BT_601
BT_709: LibPyNvCodec.ColorSpace # value = ColorSpace.BT_709
BY_NUMBER: LibPyNvCodec.SeekCriteria # value = SeekCriteria.BY_NUMBER
BY_TIMESTAMP: LibPyNvCodec.SeekCriteria # value = SeekCriteria.BY_TIMESTAMP
EXACT_FRAME: LibPyNvCodec.SeekMode # value = SeekMode.EXACT_FRAME
H264: LibPyNvCodec.CudaVideoCodec # value = CudaVideoCodec.H264
HEVC: LibPyNvCodec.CudaVideoCodec # value = CudaVideoCodec.HEVC
JPEG: LibPyNvCodec.ColorRange # value = ColorRange.JPEG
MPEG: LibPyNvCodec.ColorRange # value = ColorRange.MPEG
NO_PTS = -9223372036854775808
NV12: LibPyNvCodec.PixelFormat # value = PixelFormat.NV12
PREV_KEY_FRAME: LibPyNvCodec.SeekMode # value = SeekMode.PREV_KEY_FRAME
RGB: LibPyNvCodec.PixelFormat # value = PixelFormat.RGB
RGB_32F: LibPyNvCodec.PixelFormat # value = PixelFormat.RGB_32F
RGB_32F_PLANAR: LibPyNvCodec.PixelFormat # value = PixelFormat.RGB_32F_PLANAR
RGB_PLANAR: LibPyNvCodec.PixelFormat # value = PixelFormat.RGB_PLANAR
UDEF: LibPyNvCodec.ColorRange # value = ColorRange.UDEF
UNDEFINED: LibPyNvCodec.PixelFormat # value = PixelFormat.UNDEFINED
UNSPEC: LibPyNvCodec.ColorSpace # value = ColorSpace.UNSPEC
VP9: LibPyNvCodec.CudaVideoCodec # value = CudaVideoCodec.VP9
Y: LibPyNvCodec.PixelFormat # value = PixelFormat.Y
YCBCR: LibPyNvCodec.PixelFormat # value = PixelFormat.YCBCR
YUV420: LibPyNvCodec.PixelFormat # value = PixelFormat.YUV420
YUV422: LibPyNvCodec.PixelFormat # value = PixelFormat.YUV422
YUV444: LibPyNvCodec.PixelFormat # value = PixelFormat.YUV444
