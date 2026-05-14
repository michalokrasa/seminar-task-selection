# Chat Server's Outgoing Traffic

## Goal

Calculate the total number of bytes a chat server transmits while processing a sequence of commands.

## Rules

- The chat starts empty.
- A `+<name>` command adds a person to the chat room.
- A `-<name>` command removes a person from the chat room.
- A `<sender>:<message>` command causes the server to send the message to **every** current participant (including the sender). The traffic produced equals `len(message)` × (number of current participants).
- Add and Remove commands produce no traffic.

## Input / Output

- **Input**: up to 100 commands, one per line.
- **Output**: a single integer — the total bytes of outgoing traffic.
