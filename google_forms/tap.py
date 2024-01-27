"""GoogleForms tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

from google_forms import streams
from google_forms.client import GoogleCredentialType


class TapGoogleForms(Tap):
    """GoogleForms tap class."""

    name = "tap-google-forms"
    config_jsonschema = th.PropertiesList(
        th.Property(
            "client_secrets_path",
            th.StringType,
            description="File Path to Google API Client Secrets",
        ),
        th.Property(
            "credential_type",
            th.StringType,
            description="The credential type for authenticating with Google APIs.",
            required=True,
            allowed_values=[c.value for c in GoogleCredentialType],
        ),
        th.Property(
            "form_id",
            th.StringType,
            description="The Google Forms form ID. https://docs.google.com/forms/d/<FORM_ID>/edit",
            required=True,
        ),
    ).to_dict()

    def discover_streams(self) -> list[streams.GoogleFormsStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [
            streams.DynamicStream(self),
        ]


if __name__ == "__main__":
    TapGoogleForms.cli()
