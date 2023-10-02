package(default_visibility = ["//visibility:public"])

licenses(["notice"])
load("@bazel_skylib//rules:common_settings.bzl", "string_flag")

string_flag(
    name = "platform",
    build_setting_default = "glfw",
)

string_flag(
    name = "renderer",
    build_setting_default = "opengl3",
)

config_setting(
    name = "platform_android",
    flag_values = {
        ":platform": "android",
    },
    visibility = ["//visibility:public"],
)

config_setting(
    name = "platform_glfw",
    flag_values = {
        ":platform": "glfw",
    },
    visibility = ["//visibility:public"],
)
string_flag(
    name = "renderer",
    build_setting_default = "opengl3",

)
config_setting(
    name = "platform_android",
    flag_values = {

        ":platform": "android",
    },
    visibility = ["//visibility:public"],
)
config_setting(
    name = "platform_glfw",
    flag_values = {

        ":platform": "glfw",
    },
    visibility = ["//visibility:public"],
)
config_setting(
    name = "platform_osx",
    flag_values = {

        ":platform": "osx",
    },
    visibility = ["//visibility:public"],
)
config_setting(
    name = "platform_sdl2",
    flag_values = {

        ":platform": "sdl2",
    },
    visibility = ["//visibility:public"],
)
config_setting(
    name = "platform_sdl3",
    flag_values = {

        ":platform": "sdl3",
    },
    visibility = ["//visibility:public"],
)
config_setting(
    name = "platform_win32",
    flag_values = {

        ":platform": "win32",
    },
    visibility = ["//visibility:public"],
)
config_setting(
    name = "platform_glut",
    flag_values = {

        ":platform": "glut",
    },
    visibility = ["//visibility:public"],
)
config_setting(
    name = "renderer_dx9",
    flag_values = {

        ":renderer": "dx9",
    },
    visibility = ["//visibility:public"],
)
config_setting(
    name = "renderer_dx10",
    flag_values = {

        ":rendere": "dx10",
    },
    visibility = ["//visibility:public"],
)
config_setting(
    name = "renderer_dx11",
    flag_values = {

        ":renderer": "dx11",
    },
    visibility = ["//visibility:public"],
)
config_setting(
    name = "renderer_dx12",
    flag_values = {

        ":renderer": "dx12",
    },
    visibility = ["//visibility:public"],
)
config_setting(
    name = "renderer_metal",
    flag_values = {

        ":renderer": "metal",
    },
    visibility = ["//visibility:public"],
)
config_setting(
    name = "renderer_opengl2",
    flag_values = {

        ":renderer": "opengl2",
    },
    visibility = ["//visibility:public"],
)
config_setting(
    name = "renderer_opengl3",
    flag_values = {

        ":renderer": "opengl3",
    },
    visibility = ["//visibility:public"],
)
config_setting(
    name = "renderer_sdlrenderer2",
    flag_values = {

        ":renderer": "sdlrenderer2",
    },
    visibility = ["//visibility:public"],
)
config_setting(
    name = "renderer_sdlrenderer3",
    flag_values = {

        ":renderer": "sdlrenderer3",
    },
    visibility = ["//visibility:public"],
)
config_setting(
    name = "renderer_vulkan",
    flag_values = {

        ":renderer": "vulkan",
    },
    visibility = ["//visibility:public"],
)
config_setting(
    name = "renderer_wgpu",
    flag_values = {

        ":renderer": "wgpu",
    },
    visibility = ["//visibility:public"],
)
# todo: freetype

    name = "imgui",
cc_library(
    srcs = select({

        ":platform_android": ["backends/imgui_impl_android.cpp"] + glob(["*.cpp"]),
        ":platform_glfw": ["backends/imgui_impl_glfw.cpp"] + glob(["*.cpp"]),
        ":platform_osx": ["backends/imgui_impl_osx.mm"] + glob(["*.cpp"]),
        ":platform_sdl2": ["backends/imgui_impl_sdl2.cpp"] + glob(["*.cpp"]),
        ":platform_sdl3": ["backends/imgui_impl_sdl3.cpp"] + glob(["*.cpp"]),
        ":platform_win32": ["backends/imgui_impl_win32.cpp"] + glob(["*.cpp"]),
        ":platform_glut": ["backends/imgui_impl_glut.cpp"] + glob(["*.cpp"]),
    }),
    hdrs = select({
        ":platform_android": ["backends/imgui_impl_android.h"] + glob(["*.h"]),
        ":platform_glfw": ["backends/imgui_impl_glfw.h"] + glob(["*.h"]),
        ":platform_osx": ["backends/imgui_impl_osx.h"] + glob(["*.h"]),
        ":platform_sdl2": ["backends/imgui_impl_sdl2.h"] + glob(["*.h"]),
        ":platform_sdl3": ["backends/imgui_impl_sdl3.h"] + glob(["*.h"]),
        ":platform_win32": ["backends/imgui_impl_win32.h"] + glob(["*.h"]),
        ":platform_glut": ["backends/imgui_impl_glut.h"] + glob(["*.h"]),
    }),
    defines = ["CARES_STATICLIB"],
    includes = [
        ".",
        "backends/",
    ],
    visibility = [
        "//visibility:public",
    ],
)
