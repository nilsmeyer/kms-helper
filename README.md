# kms-helper
Just a small tool library that makes it easier to decrypt / encrypt strings
with KMS, for use in #cloud-config or whatever. This project is not affiliated
Amazon. 

## Requirements
* Python (tested with python 3.7)
* boto3 (for accessing AWS)
* Click (for CLI processing)

## Usage
After installation:
```bash
kms-helper --help
kms-helper encrypt --help
kms-helper decrypt --help
```
