### Arborescent Tangle Generator

#### Class Diagram

```mermaid
classDiagram
    generator_rlitt --|> generator
    generator_rlitt_config_t --|> generator_config_t
    generator_rlitt_config_t *-- note_awptt
    generator_rlitt_config_t *-- gen_rlitt_positivity_e
    generator_rlitt *-- generator_rlitt_config_t

    class generator {
        <<interface>>
    }

    class generator_rlitt {
<<>>
}

class gen_rlitt_positivity_e {
    <<enum>>
    uninit,
    positive,
    negative,
    neutral
}

class generator_rlitt_config_t {
<<struct>>
+ note_awptt rootstock[]
+ gen_rlitt_positivity_e rootstock_positivity[]
+ note_awptt scion[]
+ string buffer
}

class generator_config_t {
<<interface>>

}

class note_awptt {
<<>>
}

```

#### Language

C

#### Implements

-   Generator Interface (@sec-interfaces-generator)

#### Uses

-   Notation arborescent weighted planar tangle tree notation
    (@sec-library-awptt-note)

#### Libraries

N/A

#### Functionality

##### Public Structures

###### Arborescent Generator Config Structure

The config structure contains the data needed for generating a set of algebraic
tangle trees from a collection of lists of twist vectors.

This includes:

-   An integer representation of the target crossing number.
-   A notation structure for an algebraic tangle tree.
-   A pointer to a multidimensional array of twist vectors.
-   A string buffer for holding the stringified algebraic tangle tree.

##### Public Functions

###### Config Function

The config function configures the local instance variable of the generator.

This process is described in the following state machines:

```mermaid
stateDiagram-v2
  state "Init local config" as Sc

    [*] --> Sc
    Sc --> [*]

```

###### Generate Function

The generation function carries out the Arborescent tangle generation until the
inputs are exhausted. The function may contain sub machines that can be broken
out into functions in the implementation.

This process is described in the following state machines:

```mermaid
stateDiagram-v2
	state "Init" as init1
```

##### Private Functions


#### Validation

##### Config interface

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

##### Generate interface

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

```{note}
A block diagram for the component under development
```
