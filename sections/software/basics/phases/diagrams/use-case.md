
````{prf:example} A use case diagram for Go Fish
:label: se-ex-usecase
```{mermaid}

flowchart LR

    player["Player fa:fa-user"]
    dealer["Dealer fa:fa-user"]
    P1([Fishes for a card])
    P2([Matches four cards<br> into a 'book'.])
    P3([Draw a card from the deck])
    D1([Shuffle the deck])
    player --> P1
    player --> P3
    dealer --> D1
    P1 -. include .-> P2
    P3 -. include .-> P2

```
````
