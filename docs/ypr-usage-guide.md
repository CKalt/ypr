# YPR and YDL - Detailed Usage Guide

## Understanding YPR

YPR stands for three different programming languages: YAML, Python, and Rust. 

- **YAML (Yet Another Markup Language)**: YAML is a data-oriented language widely used for configuration files and data serialization. In the YPR framework, YAML is utilized to describe and monitor the project's high-level architecture. It outlines the entire project, such as directory structures, module names, their respective functions, and interactions.

- **Python**: Python, a high-level interpreted programming language known for its simplicity and readability, is used to implement parts of the system. It serves as one of the main programming languages in the YPR framework.

- **Rust**: Rust is a multi-paradigm language focused on performance and safety, notably safe concurrency. It also plays a vital role in the system's implementation, working side-by-side with Python.

## YDL - Yaml Domain Language

YDL is a domain-specific language (DSL) utilized in the YPR framework. It enables a more expressive and succinct definition of the project's modules and their interactions than YAML alone. YDL significantly improves the readability and maintainability of project descriptions and facilitates the automatic generation of Python and Rust source code.

YDL files define modules and their functions in a structured and clear way. A YDL file includes the name and description of a module, the attributes, functions and any language-specific implementations. It also details any function calls made within the defined functions.

## Usage of YAML in YPR

YAML plays a pivotal role in managing the architecture of the project. It defines the project's stages, features, and enhancements, the organization of the codebase, and the relationships between different components.

A project in YPR typically contains YAML files that represent each stage of the project (Px), and a root YAML file (PRoot) that offers an overview of the entire project. 

Each Px YAML file defines the features, enhancements, and syntax of the corresponding stage. It also describes the structure of the codebase, including the locations of Python, Rust, and YDL files. Importantly, the Px YAML file specifies the various modules, their functions, and their language-specific implementations.

The PRoot YAML file, on the other hand, provides an overall summary of the project. It lists the stages, their descriptions, and the features and enhancements introduced in each stage.

### Example of a YAML file in YPR (P1.ypr):

```yaml
name: P1
description: "BooleanLogic: A language that expresses and evaluates boolean logic"

structure:
  P1:
    - P1.ypr
    ydl:
      - constants.ydl
      - operators.ydl
      - evaluator.ydl
      - parser.ydl
      - shell.ydl
    rust:
      - Cargo.toml
      src:
        - constants.rs
        - operators.rs
        - evaluator.rs
        - parser.rs
        - shell.rs
    python:
      - setup.py
      src:
        - constants.py
        - operators.py
        - evaluator.py
        - parser.py
        - shell.py
