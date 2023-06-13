from setuptools import setup, Extension, find_packages

setup(
    name="pasteboard",
    version="0.3.3",
    packages=find_packages("src"),
    package_dir={"": "src"},
    ext_modules=[
        Extension(
            "pasteboard._native",
            sources=["src/pasteboard/pasteboard.m"],
            extra_compile_args=["-Wall", "-Wextra", "-Wpedantic", "-Werror"],
            extra_link_args=["-framework", "AppKit"],
            language="objc",
        )
    ],
    zip_safe=False,
)
