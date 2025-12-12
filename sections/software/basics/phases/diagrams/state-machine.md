
`````{prf:example} A state machine diagram for Go Fish turn
:label: se-ex-sm
````{figure}

```{mermaid}

stateDiagram-v2
    select: Select player to ask for a card
    fish: Ask player for a card
    match: Group hand into books
    rc: Receive a card
    dac: Draw card from deck
    state has_card <<choice>>

    [*] --> select
    select --> fish
    fish --> has_card
    has_card --> dac: Target player does not have card
    has_card --> rc: Target player has card
    dac --> match
    rc --> match
    match --> [*]
```
````
`````
