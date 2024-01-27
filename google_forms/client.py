"""Custom client handling, including GoogleFormsStream base class."""

from __future__ import annotations
from os import PathLike
import json
from enum import Enum

from typing import Any, Iterable
from singer_sdk._singerlib.schema import Schema

from singer_sdk.streams import Stream
from singer_sdk.tap_base import Tap

from google.oauth2 import service_account
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build


class GoogleCredentialType(Enum):
    # TODO: incase we want to support additional authentication methods
    """Credential type enum."""

    SERVICE_ACCOUNT_FROM_FILE = "service_account_from_file"


class GoogleFormsStream(Stream):
    # TODO: maybe the scopes should be configurable
    SCOPES = [
        "https://www.googleapis.com/auth/forms.body.readonly",
        "https://www.googleapis.com/auth/forms.responses.readonly",
    ]
    DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"

    """Stream class for GoogleForms streams."""

    def __init__(
        self,
        tap: Tap,
        schema: str | PathLike | dict[str, Any] | Schema | None = None,
        name: str | None = None,
    ) -> None:
        super().__init__(tap, schema, name)

        self.service = build(
            "forms",
            "v1",
            credentials=GoogleFormsStream.google_credential_factory(
                GoogleCredentialType("service_account_from_file"),
            ),
            discoveryServiceUrl=self.DISCOVERY_DOC,
            static_discovery=False,
        )

    @staticmethod
    def google_credential_factory(
        credential_type: GoogleCredentialType = None,
        **kwargs: Any,
    ) -> Credentials:
        """Factory method for creating Google API credentials."""
        if credential_type == GoogleCredentialType.SERVICE_ACCOUNT_FROM_FILE:
            # creates a Google API credential type from a service account file
            credentials = service_account.Credentials.from_service_account_file(
                filename=kwargs.get("client_secrets_path")
            ).with_scopes(GoogleFormsStream.SCOPES)
        else:
            raise Exception("Credential type not supported")

        return credentials

    @staticmethod
    def get_form_responses(
        form_id: str,
        credential: Credentials,
    ) -> dict:
        pass

    def get_records(
        self,
        context: dict | None,  # noqa: ARG002
    ) -> Iterable[dict]:
        """Return a generator of record-type dictionary objects.

        The optional `context` argument is used to identify a specific slice of the
        stream if partitioning is required for the stream. Most implementations do not
        require partitioning and should ignore the `context` argument.

        Args:
            context: Stream partition or context dictionary.

        Raises:
            NotImplementedError: If the implementation is TODO
        """
        # TODO: Write logic to extract data from the upstream source.
        # records = mysource.getall()  # noqa: ERA001
        # for record in records:
        #     yield record.to_dict()  # noqa: ERA001
        errmsg = "The method is not yet implemented (TODO)"
        raise NotImplementedError(errmsg)
