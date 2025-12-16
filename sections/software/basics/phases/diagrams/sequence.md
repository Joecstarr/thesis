`````{prf:example} A sequence diagram for Go Fish turn
:label: se-ex-seq
````{figure}
```{mermaid}

sequenceDiagram
    participant o as Player 1
    participant t as Player 2
    participant d as Deck

    o ->> t: Asks for a card
    alt is negative
    t ->> o: Responds in the negative
    o ->> d: Requests a card
    d ->> o: Distributes a card
    else is positive
    t ->> o: Responds in the postive
    t ->> o: Distributes a card
    end

```
````
`````
