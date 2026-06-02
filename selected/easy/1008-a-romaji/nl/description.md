# Romaji

## Goal

Determine whether a given word is a valid Berlanese word.

## Rules

- Vowels are: `a`, `o`, `u`, `i`, `e`. All other letters are consonants.
- Every consonant **except** `n` must be immediately followed by a vowel.
- The letter `n` may be followed by any letter or may appear at the end of the word.
- If all consonants (other than `n`) satisfy the rule, the word is Berlanese.

## Input / Output

- **Input**: a single string `s` (1 ≤ |s| ≤ 100) of lowercase Latin letters.
- **Output**: `YES` if the word is Berlanese, `NO` otherwise (case-insensitive).
