### Arborescent Tangle Generator

The arborescent tangle generator implements a portion of the theoretical use
case seen in @sec-arborescent.

#### Class Diagram

```mermaid
classDiagram
    generator_rlitt ..|> generator
    generator_rlitt_config_t ..|> generator_config_t
    generator_rlitt_config_t *-- note_wptt
    generator_rlitt_config_t *-- gen_rlitt_positivity_e
    generator_rlitt *-- generator_rlitt_config_t

    class generator {
        <<External Interface>>
    }

    class generator_rlitt {
<<External>>
}

class gen_rlitt_positivity_e {
    <<Enumeration>>
    uninit,
    positive,
    negative,
    neutral
}

class generator_rlitt_config_t {

+ note_wptt rootstock[]
+ gen_rlitt_positivity_e rootstock_positivity[]
+ note_wptt scion[]
+ string buffer
}

class generator_config_t {
<<External Interface>>

}

class note_wptt {
<<External>>
}

```

#### Language

C

#### Implements

-   Generator Interface (@sec-interfaces-generator)

#### Uses

-   Notation arborescent weighted planar tangle tree (@sec-library-wptt-note)

#### Libraries

N/A

#### Functionality

##### Public Structures

###### Arborescent Generator Config Structure

The config structure contains the data needed for generating a set of
arborescent tangles from a collection of arborescent rootstock and collection of
arborescent good scions.

This includes:

-   A notation structure for an WPTT.
-   A pointer to a multidimensional array of twist vectors.
-   A string buffer for holding the stringified algebraic tangle tree.

##### Public Functions

###### Config Function

The config function configures the local instance variable of the generator.

This process is described in the following state machines:

```mermaid
stateDiagram-v2
  state "Initialize local config" as Sc

    [*] --> Sc
    Sc --> [*]

```

###### Generate Function

The generation function carries out the Arborescent tangle generation until the
inputs are exhausted. The grafting operation is carried out by a call to the
computation grafting component (@sec-computation-grafting) and the neutrality
determination is carried out by the neutrality computation component
(@sec-computation-neutrality).

This process is described in the following state machines:

```mermaid
stateDiagram-v2
    outer_for: "for each rootstock"
    state outer_for {
        inner_for: "for each scion"
        state inner_for {
            graft: Graft scion to rootstock forming $$\Gamma$$
            pos: Identify the neutrality of $$\Gamma$$
            rep: Report $$\Gamma$$ and its neutrality
            [*] --> graft
            graft --> pos
            pos --> rep
            rep --> [*]
        }
        [*] --> inner_for
        inner_for --> [*]
    }


    [*] --> outer_for
    outer_for-->[*]
```

##### Private Functions

###### Identify the neutrality of $$\Gamma$$

#### Validation

##### Config Function

###### Positive Tests

```{test-card} Valid Config

A valid config for the generator is passed to the function.

**Inputs:**

- A valid config.

**Expected Output:**

A positive response.

```

###### Negative Tests

```{test-card} Null Config

A null config for the generator is passed to the function.

**Inputs:**

- A null config.

**Expected Output:**

A negative response.

```

##### Generate Function

```{test-card} Valid Config and generation

A valid config is set and the generation is called.

**Inputs:**

- The twist vector lists
    1. $\,$
        - [ 0 1 1 ]
        - [ 0 2 2 ]
        - [ 0 3 3 ]
    2. $\,$
        - [ 1 1 1 ]
        - [ 1 2 2 ]
    3. $\,$
        - [ 2 1 1 ]
        - [ 2 2 2 ]
        - [ 2 3 3 ]
        - [ 2 4 4 ]

**Expected Output:**

The algebraic tangle trees:
-  +[1 1 0]+[1 1 1][1 1 2]
-  +[1 1 0]+[1 1 1][2 2 2]
-  +[1 1 0]+[1 1 1][3 3 2]
-  +[1 1 0]+[1 1 1][4 4 2]
-  +[1 1 0]+[2 2 1][1 1 2]
-  +[1 1 0]+[2 2 1][2 2 2]
-  +[1 1 0]+[2 2 1][3 3 2]
-  +[1 1 0]+[2 2 1][4 4 2]
-  +[2 2 0]+[1 1 1][1 1 2]
-  +[2 2 0]+[1 1 1][2 2 2]
-  +[2 2 0]+[1 1 1][3 3 2]
-  +[2 2 0]+[1 1 1][4 4 2]
-  +[2 2 0]+[2 2 1][1 1 2]
-  +[2 2 0]+[2 2 1][2 2 2]
-  +[2 2 0]+[2 2 1][3 3 2]
-  +[2 2 0]+[2 2 1][4 4 2]
-  +[3 3 0]+[1 1 1][1 1 2]
-  +[3 3 0]+[1 1 1][2 2 2]
-  +[3 3 0]+[1 1 1][3 3 2]
-  +[3 3 0]+[1 1 1][4 4 2]
-  +[3 3 0]+[2 2 1][1 1 2]
-  +[3 3 0]+[2 2 1][2 2 2]
-  +[3 3 0]+[2 2 1][3 3 2]
-  +[3 3 0]+[2 2 1][4 4 2]

```
