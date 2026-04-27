import re

import setuptools

# Read commit hash from build.info
version = None
with open("build.info", "r") as f:
    for line in f:
        match = re.search(r"Commit Hash:\s*(\S+)", line)
        if match:
            version = "0.0.0+" + match.group(1)
            break

if version is None:
    raise RuntimeError("Commit Hash not found in build.info")

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
