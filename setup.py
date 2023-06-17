from setuptools import setup, Extension, find_packages

setup(
    name="pasteboard",
    version="0.3.4",
    packages=find_packages("src"),
    package_dir={"": "src"},
    ext_modules=[
        Extension(
            "pasteboard._native",
            sources=["src/pasteboard/pasteboard.m"],
            extra_compile_args=[
                "-Wall",
                "-Wextra",
                "-Wpedantic",
                "-Werror",
                "-mmacosx-version-min=13.0",
            ],
            extra_link_args=["-framework", "AppKit", "-mmacosx-version-min=13.0"],
            language="objc",
        )
    ],
    zip_safe=False,
)
