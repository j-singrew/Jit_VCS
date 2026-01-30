
What problem does this system solve?    
This project explores how to represent and verify non-linear history using a DAG with explicit parent references and deterministic validation rules

What is the core abstraction?


What invariants must NEVER be broken?

A node’s hash must match its contents

A node cannot reference a non-existent parent

History must remain acyclic

Verification must precede persistence


Project scope

Single-user

Local only

CLI only

One parent per node

No merges

No networking

No optimisation