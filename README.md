Jit VCS

A minimal content-addressed version control system built from scratch in Python.

This project implements the core storage and commit mechanics behind systems like Git, focusing on immutability, hashing, and DAG-based history tracking.

Project Status

Core object storage and commit pipeline are implemented.

The system currently supports:

Commit object creation

Deterministic serialization

Content-addressed storage

OID verification

Sharded persistent storage

HEAD tracking

Commit loading by OID

History traversal and tree/state objects are planned next.

Design Philosophy

Jit is built around three core principles:

Content Addressing
Every object is identified by the hash of its serialized bytes.

Immutability
Once written, an object can never be modified.

Deterministic Serialization
The same commit data always produces the same byte representation and hash.

Architecture Overview
1. Commit Object

A commit contains:

parents (list of OIDs)

state_hash (represents repository state)

timestamp

message (optional)

authorship metadata (optional)

Commits are serialized into a deterministic, line-based format.

2. Serialization Layer

Responsible for:

Converting commit objects into byte sequences

Reconstructing commit objects from raw bytes

Ensuring stable hashing input

Serialization output is encoded as UTF-8 bytes.

3. Hashing Layer

Hash is computed over serialized bytes.

The resulting OID uniquely identifies the object.

OID is used as filename in storage.

Invariant:

hash(serialized_bytes) == OID
Stored bytes must match hash.

4. Persistent Storage

Objects are stored in a sharded directory structure:

DAG_FOLDER_PATH/
ab/
cdef1234...

Where:

First 2 hex characters → shard folder

Remaining characters → filename

Properties:

Immutable storage (raises error if object exists)

Binary write mode

No mutation allowed

5. Verification

When loading an object:

Locate file by OID

Read raw bytes

Recompute hash

Verify it matches requested OID

Deserialize into Commit object

If verification fails → error is raised.

6. HEAD

Tracks the current commit OID.

Used as parent reference for new commits.

Current Capabilities

✔ Create commit
✔ Serialize commit deterministically
✔ Hash commit
✔ Store commit in sharded structure
✔ Enforce immutability
✔ Load commit by OID
✔ Verify commit integrity

Planned Features

Commit history traversal (log)

Tree objects (directory state)

Blob objects (file contents)

Checkout functionality

Branch support

Object headers (Git-style object format)

Garbage collection

Refactoring OID type consistency

Core Invariants

Objects are immutable.

OID = hash(serialized_bytes).

Stored bytes are never altered.

Serialization must be deterministic.

Breaking any of these invalidates the system.

Why This Project Exists

This project exists to deeply understand:

Content-addressed storage

DAG-based version control

Object hashing and integrity

Immutability in distributed systems

Internal mechanics of Git

The goal is not to replicate Git fully, but to understand and implement its foundational concepts from first principles.

Skills Demonstrated

Systems design

File system persistence

Cryptographic hashing

Data serialization

DAG modeling

Integrity verification

Immutable storage architecture

Author

Built as a systems learning project.
