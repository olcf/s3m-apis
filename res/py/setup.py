import re

import setuptools

# Read module version from build.info
version = None
with open("build.info", "r") as f:
    for line in f:
        match = re.search(r"source\.module\.version:\s*(\S+)", line)
        if match:
            version = match.group(1)
            break

if version is None:
    raise RuntimeError("source.module.version not found in build.info")

setuptools.setup(
    name="s3m-apis-grpcio",
    version=version,
    author="Oak Ridge Leadership Computing Facility",
    description="Collection of compiled S3M gRPC+protobuf modules utilizing grpcio.",
    packages=setuptools.find_packages(),
    install_requires=[
        "grpcio-tools==1.70",
        "protobuf",
    ],
    include_package_data=True,
    python_requires=">=3.9",
)
