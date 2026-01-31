#include <torch/extension.h>
#include <pybind11/eigen.h>
#include <raytracing/raytracer.h>

void clamp_op(
    torch::Tensor& result,
    const torch::Tensor& image,
    float low, float high
);

torch::Tensor clamp(const torch::Tensor& image, float low, float high) {
    torch::Tensor result = image.clone();
    clamp_op(result, image, low, high);

    return result;
}


using namespace raytracing;

PYBIND11_MODULE(TORCH_EXTENSION_NAME, m) {

pybind11::class_<RayTracer>(m, "RayTracer").def("trace", &RayTracer::trace);

m.def("create_raytracer", &create_raytracer);
m.def("clamp", &clamp, "Clamp Images within Range");
}