import os, sys, time
import torch
from tqdm import tqdm

import PyNvCodec as nvc
import PytorchNvCodec as pnvc

def test1():
    print(dir(nvc))
    print(dir(pnvc))


class cconverter:
    """
    Colorspace conversion chain.
    """
    def __init__(self, width: int, height: int, gpu_id: int):
        self.gpu_id = gpu_id
        self.w = width
        self.h = height
        self.chain = []

    def add(self, src_fmt: nvc.PixelFormat, dst_fmt: nvc.PixelFormat) -> None:
        self.chain.append(nvc.PySurfaceConverter(
            self.w, self.h, src_fmt, dst_fmt, self.gpu_id))

    def run(self, src_surface: nvc.Surface) -> nvc.Surface:
        surf = src_surface
        cc = nvc.ColorspaceConversionContext(nvc.ColorSpace.BT_601,
                                             nvc.ColorRange.MPEG)

        for cvt in self.chain:
            surf = cvt.Execute(surf, cc)
            if surf.Empty():
                raise RuntimeError('Failed to perform color conversion')

        return surf.Clone(self.gpu_id)


def surface_to_tensor(surface: nvc.Surface) -> torch.Tensor:
    """
    Converts planar rgb surface to cuda float tensor.
    """
    if surface.Format() != nvc.PixelFormat.RGB_PLANAR:
        raise RuntimeError('Surface shall be of RGB_PLANAR pixel format')

    surf_plane = surface.PlanePtr()
    img_tensor = pnvc.DptrToTensor(surf_plane.GpuMem(),
                                   surf_plane.Width(), surf_plane.Height(),
                                   surf_plane.Pitch(), surf_plane.ElemSize())
    if img_tensor is None:
        raise RuntimeError('Can not export to tensor.')

    img_tensor.resize_(3, int(surf_plane.Height()/3), surf_plane.Width())
    return img_tensor


def test2():
    vidp = 'test.mp4'
    gpu_id = 0
    nvDec = nvc.PyNvDecoder(vidp, gpu_id)
    w,h = nvDec.Width(),nvDec.Height()
    to_rgb = cconverter(w, h, gpu_id)
    to_rgb.add(nvc.PixelFormat.NV12, nvc.PixelFormat.YUV420)
    to_rgb.add(nvc.PixelFormat.YUV420, nvc.PixelFormat.RGB)
    to_rgb.add(nvc.PixelFormat.RGB, nvc.PixelFormat.RGB_PLANAR)
    imgs = []
    while True:
        # Decode NV12 surface
        src_surface = nvDec.DecodeSingleSurface()
        if src_surface.Empty():
            break
        # Convert to planar RGB
        rgb_pln = to_rgb.run(src_surface)
        if rgb_pln.Empty():
            break
        frame = surface_to_tensor(rgb_pln)
        imgs.append(frame)
    imgs = torch.stack(imgs, dim=1)
    print(imgs.shape)


if __name__=='__main__':
    funname = 'test1'
    if len(sys.argv)>=2:
        funname = sys.argv[1]
        sys.argv.remove(funname)
    globals()[funname]()