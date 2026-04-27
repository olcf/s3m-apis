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
