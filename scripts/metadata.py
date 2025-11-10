import os
import sys
import base64
import json
from datetime import datetime


def get_encoded_metadata(additional_data: dict = {}) -> str:
  username = os.environ.get('STUDENT_USERNAME', 'unknown_user')
  kernel_name = os.environ.get('CONDA_DEFAULT_ENV', 'unknown_kernel')

  data = {
      'username': username,
      'kernel_name': kernel_name, **additional_data
  }
  return encode_metadata(data)


def encode_metadata(data: dict) -> str:
  """
  Encode metadata (username, filename, timestamp) into a base64 string.

  Args:
      data: Dictionary containing metadata
  Returns:
      str: Base64 encoded metadata string
  """
  data['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  return base64.b64encode(json.dumps(data).encode()).decode()


def decode_metadata(encoded_metadata):
  # Add missing padding if needed
  missing_padding = len(encoded_metadata) % 4
  if missing_padding:
    encoded_metadata += '=' * (4 - missing_padding)

  decoded_bytes = base64.b64decode(encoded_metadata)
  return json.loads(decoded_bytes.decode())
