import torch
import raytracing
import numpy as np

N = 16

if False:
    rays_o = torch.randn(N, 3).cuda()
    a = raytracing._raytracing.clamp(rays_o, 0.0, 0.0)
else:

    vertices = np.ones((N, 3), dtype=np.float32)
    faces = np.ones((N, 3), dtype=np.uint32)

    ray_tracer = raytracing.RayTracer(vertices, faces)

    rays_o = torch.randn(N, 3).cpu()
    rays_d = torch.randn(N, 3).cpu()
    positions = torch.randn(N).cpu()
    face_normals = torch.randn(N, 3).cpu()
    depth = torch.randn(N).cpu()
    ray_tracer.impl.trace(rays_o, rays_d, positions, face_normals, depth)