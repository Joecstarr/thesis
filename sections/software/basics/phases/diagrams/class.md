`````{figure}

````{figure}
:label: se-cd-fig-agg

```{mermaid}
classDiagram
    A *--B
```
An aggregation connection. Class A aggregates Class B.
````
````{figure}
:label: se-cd-fig-real

```{mermaid}
classDiagram
    A ..|> B
```
A realization connection. Class A realizes Class B.
````
`````

`````{prf:example} A class diagram for a Go Fish player.
:label: se-ex-class
````{figure}

```{mermaid}
classDiagram
    class Player{
        +Hand hand
        +List[Book] books
        +get_score()
        +go_fishing()
        +check_card_in_hand()
        -count_books()
        -make_books()
    }
    class Hand{
    }
    class Book{
    }
    class Card{
    <<External>>
    }
    class CardSuit{
        <<External Enumeration>>
    }
    class CardCollection{
        <<External Interface>>
    }
    Book *-- Card
    Player *-- Hand
    Player *-- Book
    Hand *-- Card
    Card *-- CardSuit
    Hand ..|> CardCollection
    Book ..|> CardCollection

```
````
`````
