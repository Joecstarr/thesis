# The First Tangle Datasets

This chapter will describe the methodology used to answer two of the essential questions detailed in
@sec-intro-overview.

> "How do I systematically construct rational tangles?", "How do I tell two rational tangles I make
> apart?", and "How do I generate new rational tangles?"

> "How do I systematically construct Montesinos tangles?", "How do I tell two Montesinos tangles I
> make apart?", and "How do I generate new Montesinos tangles?"

The methodologies outlined in this section are for relatively simple classes of tangles, the
rational and Montesinos tangles. As we progress, we will see a common solution pattern that outlines
the general approach to the more difficult algebraic/arborescent case in @sec-arborescent. That
approach takes the form of the cadence:

1. Define the object.
2. Define equivalence for the object.
3. Identify a unique representation.
4. Generate those unique representatives[^rep]

```{include} ./rational.md

```

```{include} ./montesinos.md

```

[^rep]:
    Each tangle can be represented by an infinite number of diagrams. A unique representative in
    this context means a particular "flavor" of diagram that exists for every tangle in the class we
    are concerned about.
