"""Stream type classes for google-forms."""

from __future__ import annotations

import sys
import typing as t

from singer_sdk import typing as th  # JSON Schema typing helpers

from google_forms.client import GoogleFormsStream

if sys.version_info >= (3, 9):
    import importlib.resources as importlib_resources
else:
    import importlib_resources


class DynamicStream(GoogleFormsStream):
    """Define custom stream."""

    name = "google-forms-stream"
    replication_key = "lastSubmittedTime"
    schema = th.PropertiesList(
        th.Property("responseId", th.StringType),
        th.Property("createTime", th.DateTimeType),
        th.Property("lastSubmittedTime", th.DateTimeType),
        th.Property("answers", th.StringType),
    ).to_dict()
