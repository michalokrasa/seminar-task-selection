Feature: Sentence language detection by suffix
  As a suffix-based language classifier
  I want to detect the language of a sentence from its ending
  So that I can label it as Filipino, Japanese, or Korean

  Rule: Input / Output format
    The program reads from stdin: first line is an integer t (1 ≤ t ≤ 30), then t lines each containing one sentence string.
    The program prints t lines to stdout, each containing "FILIPINO", "JAPANESE", or "KOREAN".

  Scenario: Sentence ending with "po" is Filipino
    Given the sentence is "kamusta_po"
    When the language is detected
    Then the result is "FILIPINO"

  Scenario: Sentence ending with "desu" is Japanese
    Given the sentence is "genki_desu"
    When the language is detected
    Then the result is "JAPANESE"

  Scenario: Sentence ending with "masu" is Japanese
    Given the sentence is "ohayou_gozaimasu"
    When the language is detected
    Then the result is "JAPANESE"

  Scenario: Sentence ending with "mnida" is Korean
    Given the sentence is "annyeong_hashimnida"
    When the language is detected
    Then the result is "KOREAN"

  Scenario Outline: Language detection for multiple sentences
    Given the sentence is "<sentence>"
    When the language is detected
    Then the result is "<language>"

    Examples:
      | sentence                                    | language  |
      | kamusta_po                                  | FILIPINO  |
      | genki_desu                                  | JAPANESE  |
      | ohayou_gozaimasu                            | JAPANESE  |
      | annyeong_hashimnida                         | KOREAN    |
      | hajime_no_ippo                              | FILIPINO  |
      | bensamu_no_sentou_houhou_ga_okama_kenpo     | FILIPINO  |
      | ang_halaman_doon_ay_sarisari_singkamasu     | JAPANESE  |
      | si_roy_mustang_ay_namamasu                  | JAPANESE  |
