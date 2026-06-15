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
    name="s3m-apis-betterproto",
    version=version,
    author="Oak Ridge Leadership Computing Facility",
    description="Collection of compiled S3M gRPC+protobuf modules utilizing betterproto.",
    packages=setuptools.find_packages(),
    install_requires=[
        "betterproto==2.0.0b7",
        "protobuf",
        "certifi==2025.1.31"
    ],
    include_package_data=True,
    python_requires=">=3.9",
)
