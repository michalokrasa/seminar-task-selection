# Restore Internet Address

## Goal

Reconstruct a valid Internet address from a string missing punctuation marks.

## Rules

- The address format is `<protocol>://<domain>.ru[/<context>]`.
- `<protocol>` is either "http" or "ftp".
- `<domain>` is a non-empty string of lowercase English letters.
- `<context>` is optional and, if present, is a non-empty string of lowercase English letters.
- The input string is derived from a valid address by removing ":", "/", and ".".

## Input / Output

- **Input**: A single non-empty string of up to 50 lowercase English letters.
- **Output**: A single line containing a valid reconstructed Internet address. Multiple valid outputs are allowed.
