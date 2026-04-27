import ssl
import weakref
from typing import TypeVar, Type, Final, Optional

import certifi
from betterproto import ServiceStub
from grpclib.client import Channel

T: Final[TypeVar] = TypeVar('T', bound=ServiceStub)


class S3MClientFactory:
    def __init__(self,
                 endpoint: str,
                 token: str,
                 additional_metadata: Optional[dict] = None,
                 ssl_context: Optional[ssl.SSLContext] = None,
                 ):

        # Parse endpoint

        if endpoint.startswith("https://"):
            endpoint = endpoint[len("https://"):]
        endpoint = endpoint.rstrip("/")

        if ":" in endpoint:
            host, port_str = endpoint.rsplit(":", 1)
            try:
                port = int(port_str)
            except ValueError:
                raise ValueError(f"Failed to parse port: {port_str}")
        else:
            host = endpoint
            port = 443

        self.service_url = host
        self.port = port

        # Set metadata
        self.metadata = additional_metadata or {}
        if token:
            self.metadata["authorization"] = token

        # Create SSL context
        if ssl_context is None:
            ssl_context = ssl.create_default_context(cafile=certifi.where())

        # Create channel
        self.channel = Channel(host=host, port=port, ssl=ssl_context)

        # Set finalizer
        self._finalizer = weakref.finalize(self, self._cleanup, self.channel)

    def create_client(self, stub_class: Type[T], **kwargs) -> T:
        return stub_class(self.channel, metadata=self.metadata, **kwargs)

    def close(self):
        if hasattr(self, 'channel'):
            self.channel.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._finalizer()

    @staticmethod
    def _cleanup(channel):
        channel.close()
