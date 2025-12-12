
`````{prf:example} A block diagram for Go Fish
:label: se-ex-block
````{figure}
```{mermaid}

flowchart LR
    subgraph User Interface
        ui-hd["Hand Display"]
        ui-dd["Deck Display"]
        ui-ps["Player Score"]
    end

    subgraph Game Objects
        go-h["Hand"]
        go-d["Deck"]
    end

    gs["Game State"]

     go-h --->|*..1| gs
     go-d --->|1| gs
     gs --->|1| ui-hd
     gs --->|1| ui-dd
     gs --->|1..*| ui-ps

```
````
`````
