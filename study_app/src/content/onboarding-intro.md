## **What is Gherkin?**

Gherkin uses a set of special keywords to give structure and meaning to executable specifications. Most lines in a Gherkin document start with one of these keywords.

### **Feature**

The `Feature` keyword provides a high-level description of a software feature and groups related scenarios. The first primary keyword in a Gherkin document must always be `Feature`, followed by a `:` and a short text describing the feature. Free-form description text can be added underneath.

### **Scenario / Example**

A `Scenario` (also written as `Example`) is a concrete example that illustrates a business rule. It consists of a list of steps and follows this pattern: describe an initial context (`Given` steps), describe an event (`When` steps), and describe an expected outcome (`Then` steps).

### **Steps: Given, When, Then, And, But**

`Given` steps describe the initial context of the system — the scene of the scenario. Their purpose is to put the system in a known state before the user starts interacting with it.

`When` steps describe an event or action — this can be a person interacting with the system, or an event triggered by another system.

`Then` steps describe an expected outcome or result. The outcome should be an observable output — something that comes out of the system, such as a report or user interface — rather than a behaviour buried inside the system.

When multiple `Given` or `Then` steps follow each other, `And` and `But` can be used to make the scenario read more fluently.

Here is a basic example:

```gherkin
Feature: Guess the word

Scenario: Breaker joins a game
 Given the Maker has started a game with the word "silky"
 When the Breaker joins the Maker's game
 Then the Breaker must guess a word with 5 characters
```

### **Background**

If the same `Given` steps are repeated across all scenarios in a `Feature`, they can be grouped under a `Background` section. A `Background` is placed before the first scenario and its steps are run before each scenario.

### **Scenario Outline**

The `Scenario Outline` keyword runs the same scenario multiple times with different combinations of values. It uses `< >`-delimited parameters as a template, and an `Examples` table provides the concrete values for each run.

```gherkin
Scenario Outline: eating
 Given there are <start> cucumbers
 When I eat <eat> cucumbers
 Then I should have <left> cucumbers

 Examples:
  | start | eat | left |
  | 12 | 5 | 7 |
  | 20 | 5 | 15 |
```

---

Each `.feature` file contains exactly one `Feature`, made up of one or more `Scenario` blocks, each with `Given`/`When`/`Then` steps describing the expected behaviour of the system.

**For full Gherkin reference visit [https://cucumber.io/docs/gherkin/reference](https://cucumber.io/docs/gherkin/reference)**

## **Example 1**

### **Original task description**

You are given a number n. Print n lines, i-th line should consist of i characters "\*". Lines' indices are 1-based.

**Input:** The only line of input contains an integer n (1 ≤ n ≤ 50).

**Output:** Output the described pattern.

**Examples:**

**Input**

3

**Output**

```
*
**
***
```

**Input**

6

**Output**

```
*
**
***
****
*****
******
```

### **Gherkin specification**

```gherkin
Feature: Asterisk triangle pattern
 As a programmer
 I want to print a triangular asterisk pattern
 So that line i contains exactly i asterisks

Rule: Input / Output format
 The program reads a single integer n (1 ≤ n ≤ 50) from stdin.
 The program prints n lines, where line i (1-indexed) contains i asterisk characters.

Scenario: Single row
 Given the input n is 1
 When the pattern is printed
 Then the output is:
 *

Scenario: Three rows
 Given the input n is 3
 When the pattern is printed
 Then the output is:
 *
 **
 ***

Scenario: Six rows
 Given the input n is 6
 When the pattern is printed
 Then the output is:
 *
 **
 ***
 ****
 *****
 ******

Scenario Outline: Various values of n produce the correct number of lines and last-line length
 Given the input n is
 When the pattern is printed
 Then the output has exactly <n> lines
 And the last line contains exactly <n> asterisks

 Examples:
  | n  |
  | 1  |
  | 3  |
  | 6  |
  | 50 |
```

## **Example 2**

### **Original task description**

The INI file format is a de facto standard for configuration files. INI files are simple text files with a basic structure. They are commonly associated with Microsoft Windows, but are also used on other platforms.

Each line in an INI file stands for a key-value mapping or defines a new section. A key-value line has a format "key=value", where key is the name of some property, and value is its value. It is possible that it will be spaces on both sides of the key and/or value; the spaces should be ignored.

A section line has a format "[section]". It means that all key-value lines after it define properties of the specified section. Of cause, the following section line changes the current section. A section line may have spaces around any of the brackets.

Also, you should ignore comment lines — the first non-space character of a comment line is ";".

Your task is to write a program that will format given INI-file in a special way:

- first, print key-value lines which do not belong to any section;
- print all the sections in the lexicographical (alphabetical) order of their names;
- inside each of the two previous items, order key-value lines lexicographically by "key";
- if there is more than one key-value line with the same key inside a single section (or outside any sections), leave only one line (which appears later in the input data);
- remove all redundant spaces and lines.

Input

The first line contains a single integer n (1 ≤ n ≤ 510) — the number of lines in the given INI-file.

The rest of the input contains a valid INI-file in n lines. Values of section, key, and value contain only Latin letters, digits, "." and/or "-".

Each line has a length not exceeding 255 characters and not less than 1 character. The total length of all the lines doesn’t exceed 10000.

Output

Print a formatted INI-file.

Examples

Input

```
11
a= 1
b=a
a = 2
 ; comment
[z]
1=2
[y]
2=3
[z]
2=1
[w]
```

Output

```
a=2
b=a
[w]
[y]
2=3
[z]
1=2
2=1
```

### **Gherkin specification**

```gherkin
Feature: INI file formatter
  As an INI file processor
  I want to reformat a given INI file according to strict ordering and deduplication rules
  So that the output is canonical and clean

  Rule: Input / Output format
    The program reads n from stdin, then n lines of an INI file.
    The program prints the reformatted INI file to stdout.

  Rule: Formatting rules
    Comment lines (first non-space character is ";") are discarded.
    Key-value lines have the form "key=value" (spaces around key and value are stripped).
    Section lines have the form "[section]" (spaces around brackets are stripped).
    Key-value lines before any section header belong to the global (no-section) namespace.
    Sections are printed in lexicographic order of section name.
    Within each section (and globally), key-value pairs are printed in lexicographic order by key.
    If a key appears more than once in the same section, only the last occurrence is kept.
    Empty sections (with no key-value pairs) are still printed with their header.

  Scenario: Global key-value pairs are deduplicated, last value wins
    Given the INI file contains:
      | line   |
      | a= 1   |
      | b=a    |
      | a = 2  |
    When the file is formatted
    Then the output contains "a=2" before "b=a"

  Scenario: Sections are printed in lexicographic order
    Given the INI file contains sections z, y, and w
    When the file is formatted
    Then sections appear in order: w, y, z

  Scenario: Comments are removed from output
    Given the INI file contains a line " ; this is a comment"
    When the file is formatted
    Then no comment lines appear in the output

  Scenario: Empty section is still printed
    Given the INI file contains "[w]" with no key-value pairs under it
    When the file is formatted
    Then "[w]" appears in the output

  Scenario Outline: Full formatting of a sample INI file
    Given the INI file has 11 lines as in the first example
    When the file is formatted
    Then the output matches:
      | line  |
      | a=2   |
      | b=a   |
      | [w]   |
      | [y]   |
      | 2=3   |
      | [z]   |
      | 1=2   |
      | 2=1   |

    Examples:
      | ignored |
      | -       |

```
