## Core principle

Your description is the only thing the LLM sees when generating a solution. It must fully replace a task as a spec with nothing implicit and nothing assumed.

## 1. Start from the provided task, not from your own understanding

Re-derive the spec directly from the original statements. Avoid paraphrasing loosely. Every rule, edge case, and I/O constraint in the task should appear somewhere in your description.

## 2. Keep NL and Gherkin versions informationally equivalent

Since the study compares formats, both versions of the same task should encode the same rules and constraints. If one version mentions a constraint (e.g., max 100 commands), the other must too.

## 3. Structure Gherkin consistently

Feature header with role/goal framing → Rule: block for I/O format → One or more rules describing behavior → Scenario/Scenario Outline per distinct behavior.

```
Feature: <task name>
│ As a <role>
│ I want <capability>
│ So that <outcome>
│
├─ Rule: Input / Output format
│ <I/O format sentence(s)>
│
├─ Rule: One or more behavior-specific rules
│ <list of behaviors belonging to this rule>
│
├─ Background:
│ Given <shared setup>
│ And <shared setup>
│
├─ Scenario: <behavior 1>
│ Given <context>
│ When <action>
│ Then <expected result>
│
├─ Scenario: <behavior 2 / edge case>
│ Given <context>
│ When <action>
│ Then <expected result>
│
└─ Scenario Outline: <parameterized case>
 Given <template context>
 When <template action>
 Then <expected <result>>

     Examples:
       | result |
       | ...    |
```

## 4. No algorithm hints

Describe observable behavior (inputs → outputs). Avoid specifying intended algorithm or data structure. E.g. say `the traffic increases by len(message) × participants` (a rule), not `use a hash set to track participants`.

## 5. Cover distinct cases, not just the happy path

Include boundary/edge conditions mentioned in the original statement (empty input, single item, max size, ties, etc.) as separate Scenarios or Rules bullets. Each should be independently checkable.  
Reuse the sample I/O from the task as at least one worked example (Gherkin Scenario Outline Examples: table, or an explicit example in the NL rules).

## 6. Stay self-contained and concise

No references to figures/images, no domain knowledge beyond what's stated.  
Target the same rough length as the examples above (~15–50 lines). It should be long enough to be unambiguous but short enough to stay a single-page prompt.

## 7. Precision over prose

Use exact format strings examples (+\<name\>, \<sender\>:\<message\>) and exact output types ("a single integer") rather than vague language ("some info about the user").

## 8. Language agnostic

Do not assume any programming language-specific syntax or semantics. The prompts will be used to generate code in multiple programming languages.
