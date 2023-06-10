# ypr
YPR – Yaml, Python, Rust compiler development framework.
The YPR framework is designed to deliver a robust implementation of the Prolog language through a unique approach that combines three programming languages: Python, Rust, and YAML. At the top of the framework sits YAML, which defines and monitors the entire project and its architecture, including directory structures, module names, functions, and their interactions.
The Prolog system is developed in stages, represented as "Prolog Lite" languages (P1, P2, ..., Px, ..., Pn), each progressively increasing in complexity and functionality. Python and Rust independently implement functionally equivalent units for each stage of the Prolog-lite sequence, while YAML serves as the orchestrating language, defining and monitoring the project's architecture and facilitating the coordination between Python and Rust implementations.
The YAML structure within the YPR framework includes Yx instances for each stage (Px), capturing the necessary information for generating language references. Additionally, there is a YRoot document that provides an overview of the P1...Pn series and their relationships, facilitating iterative development and refinement. Each Px represents a distinct set of feature enhancements over the previous stage (P(x-1)), allowing for iterative development and refinement.
A key aspect of the YPR framework is the 100% syntax and semantic compatibility between each stage (Px) and the ultimate version (Pn) of the Prolog system. This property, known as the "Px Compatibility Rule," is crucial. It allows us to assert that a specific stage (Px) is incorrect if it fails to pass the Px Compatibility Rule, indicating that its code does not run in all higher-level stages.
The YPR framework incorporates a JSON schema and a set of semantic rules to establish the validity of YPR YAML documents. These documents define the project structure, architecture, and configurations. While the YPR YAML documents play a critical role in driving the project, they are not standalone languages in their own right. Instead, they leverage the expressive power of YAML to define and manage the evolving Prolog system. The possibility of developing a DSL (Domain-Specific Language) may arise in the future, but for now, the focus remains on leveraging YAML.
In summary, the YPR framework combines YAML, Python, and Rust to develop a Prolog implementation. Python and Rust independently implement functionally equivalent units for each stage of the Prolog-lite sequence, while YAML serves as the orchestrating language, defining and monitoring the project's architecture and facilitating the coordination between Python and Rust implementations. The framework ensures syntax and semantic compatibility, provides language references, and utilizes JSON schema and semantic rules to validate YPR YAML documents. While a DSL may be considered in the future, YAML remains the primary choice for leveraging its capabilities within the YPR framework.

%YPR 1.0
name: PRoot
description: Root document for defining the Prolog Lite stages

stages:
  - name: P1
    description: "BooleanLogic: A language that expresses and evaluates boolean logic"
    features:
      - Constants
      - Operators: [",", ";", "\\+"]
    enhancements:
      - Basic parsing and evaluation
    shell: |
      Prolog Lite - P1 Shell
      Enter your Prolog queries or use built-in commands:
      - Type 'exit.' to quit the shell.
      - Type 'consult("<filename>").' to load a file with P1 facts.

  - name: P2
    description: "PropositionalLogic: An extension of BooleanLogic to include variables"
    features:
      - Variables
    enhancements:
      - Introduction of environment or variable assignment

  - name: P3
    description: "PredicateLogic: Extends PropositionalLogic to include predicates and quantifiers"
    features:
      - Predicates
      - Quantifiers
    enhancements:
      - Variable scoping

  - name: P4
    description: "FirstOrderLogic: Builds upon PredicateLogic to include functions"
    features:
      - Functions
    enhancements:
      - Transition from propositional to first-order logic

  - name: P5
    description: "HornClausalLogic: Extends FirstOrderLogic to restrict it to Horn clauses"
    features:
      - Horn clauses
    enhancements:
      - Crucial for Prolog's computational model

  - name: P6
    description: "SimpleProlog: Extends HornClausalLogic to include the basic features of Prolog"
    features:
      - Facts
      - Rules
      - Queries
    enhancements:
      - Introduction of execution model for query satisfaction

  - name: P7
    description: "PrologWithBacktracking: Enhances SimpleProlog with support for backtracking"
    features:
      - Backtracking
    enhancements:
      - Quintessential feature of Prolog's execution model

  - name: P8
    description: "PrologWithBuiltinPredicates: Builds upon PrologWithBacktracking by adding support for built-in predicates"
    features:
      - Built-in predicates (arithmetic operations, list operations, I/O operations, etc.)
    enhancements:
      - Expanded functionality through built-in predicates

  - name: P9
    description: "PrologWithCut: Extends PrologWithBuiltinPredicates with support for the cut operator"
    features:
      - Cut operator
    enhancements:
      - Influences the backtracking mechanism

  - name: Pn
    description: "FullProlog: The final stage that incorporates all remaining features of the Prolog standard"
    features:
      - Modules
      - Operator definitions
      - Exceptions
      # Add more features as needed
    enhancements:
      - Complete implementation of the Prolog standard


%YPR 1.0
name: P1
description: "BooleanLogic: A language that expresses and evaluates boolean logic"

syntax:
  constants: [true, false]
  operators:
    - name: ','
      arity: 2
    - name: ';'
      arity: 2
    - name: '\\+'
      arity: 1

examples:
  - expression: ',(true, false)'
    result: false
  - expression: ';(true, false)'
    result: true
  - expression: '\\+(true)'
    result: false

tests:
  - query: ',(true, false).'
    expected: false
  - query: ';(true, false).'
    expected: true
  - query: '\\+(true).'
    expected: false

shell: |
  Prolog Lite - P1 Shell
  Enter your Prolog queries or use built-in commands:
  - Type 'exit.' to quit the shell.
  - Type 'consult("<filename>").' to load a file with P1 facts.

  ?- ',(true, false).'
  Result: false

  ?- ';(true, false).'
  Result: true

  ?- '\\+(true).'
  Result: false

  ?- exit.
  Exiting Prolog Lite - P1 Shell

