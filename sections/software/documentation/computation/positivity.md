<!-- prettier-ignore-start -->
(sec-computation-neutrality)=
### Arborescent Tangle Positivity Computation
<!-- prettier-ignore-end -->

The arborescent tangle positivity computation implements a portion of the
theoretical use case seen in @sec-rlitt-generation.

#### Class Diagram

$\,$

````{figure}
```{mermaid}
classDiagram
    comp_rlitt_positivity ..|> computation
    comp_rlitt_positivity_config_t ..|> notation_wptt
    comp_rlitt_positivity_config_t ..|> comp_config_t
    comp_rlitt_positivity *-- comp_rlitt_positivity_config_t
    comp_rlitt_positivity_result_t ..|> comp_rlitt_positivity_flvrs_e
    comp_rlitt_positivity_result_t ..|> comp_result_t
    comp_rlitt_positivity *-- comp_rlitt_positivity_result_t
    comp_rlitt_positivity_result_t *-- comp_rlitt_positivity_flvrs_e

    class computation {
        <<External Interface>>
    }

    class comp_rlitt_positivity {
    <<External>>
    }

    class notation_wptt{
    <<External>>
    }

    class comp_rlitt_positivity_config_t {

    + notation_wptt *tree
    }

    class comp_config_t {
    <<External Interface>>
    }

    class comp_rlitt_positivity_result_t {

    + comp_rlitt_positivity_flvrs_e result
    }
    class comp_rlitt_positivity_flvrs_e {
    <<Enumeration>>
     uninit,
     positive,
     negative,
     neutral,
     undefined
    }

    class comp_result_t {
    <<External Interface>>
    }


```
````

#### Language

C

#### Implements

- Computation Interface (@sec-interfaces-computation)

#### Uses

- Notation Weighted Planar Tangle Tree (@sec-library-wptt-note)

#### Libraries

N/A

#### Functionality

##### Public Structures

###### Configuration Structure

The configuration structure contains the data needed for computing the
positivity of an input WPTT.

This includes:

- A pointer to a read-only notation structure for a WPTT.

###### Result Structure

The result structure contains the enumerated value identifying the positivity of
the input tree.

##### Public Functions

###### Configuration Function

The configuration function sets the local configuration variable of the
computation.

This process is described in the following state machines:

````{figure}
```{mermaid}
stateDiagram-v2
  state "Initialize local configuration" as Sc

    [*] --> Sc
    Sc --> [*]

```
````

###### Compute Function

The compute function carries out the arborescent tangle positivity computation.
The function may contain sub-machines that can be broken out into functions in
the implementation. The "walk the tree" function should be implemented with a
stack-based iterative approach.

This process is described in the following state machines:

````{figure}
```{mermaid}
stateDiagram-v2
    state "Initialize<br/>• Set tree as neutral<br/>• Set stick length to 0<br/>• Set stick has -2 to false<br/>• Set stick has 2 to false" as init
    state "Execute the walk the tree sub-machine for each vertex"

    [*] --> init
    init --> walk
    walk --> [*]
```
````

**Walk the tree**

````{figure}
```{mermaid}
stateDiagram-v2
        direction LR
        state nciz <<choice>>
        state mtew <<choice>>
        state nn <<choice>>
        state np <<choice>>
        state "Set positive" as sp
        state "Set negative" as sn
        state "Set undefined and exit the outer routine" as su
        state join_undef <<join>>

        state nr <<choice>>
        state wit <<choice>>
        state "Increment stick length" as isl
        state "Set stick to have 2" as sstht
        state "Set stick to have -2" as ssthmt

        state slo <<choice>>
        state hpm2 <<choice>>

        [*] --> nciz
        nciz --> mtew : Number of children is 0 and stick length is 0
        mtew --> np: Weight is -2
        mtew --> [*]: Else
        mtew --> nn: Weight is 2
        np --> join_undef: Else
        np --> sn: Tree not already marked negative
        nn --> join_undef: Else
        nn --> sp: Tree not already marked positive
        su --> [*]
        sp --> [*]
        sn --> [*]

        nciz --> isl: Number of children is 1
        isl --> nr
        nr --> [*]:Else
        nr --> wit: Vertex is not the root vertex
        wit --> sstht: Weight is 2
        sstht --> [*]
        wit --> ssthmt: Weight is -2
        wit --> [*]: Else
        ssthmt --> [*]

        nciz --> slo: else
        slo --> [*]: else
        slo --> hpm2: Stick has length 1
        hpm2 --> nn: Stick has a weight of 2
        hpm2 --> np: Stick has a weight of -2
        hpm2 --> [*]
        join_undef --> su

```
````

###### Result Function

When this function is invoked, the result of the positivity computation process
is reported.

#### Validation

##### Configuration Function

###### Positive Tests

```{test-card} Valid Configuration

A valid configuration for the computation is passed to the function.

**Inputs:**

- A valid configuration.

**Expected Output:**

A positive response.

```

###### Negative Tests

```{test-card} Null Configuration

A null configuration for the computation is passed to the function.

**Inputs:**

- A null configuration.

**Expected Output:**

A negative response.

```

```{test-card} Null Configuration Parameters

A configuration with various null parameters is passed to the function.

**Inputs:**

- A configuration with null tree.

**Expected Output:**

A negative response.

```

##### Compute Function

###### Positive Tests

```{test-card} A Valid Configuration

A valid configuration is set for the component. The computation is executed and
returns successfully. The result written to the write interface is correct.

**Inputs:**

- A valid configuration is set.

**Expected Output:**

- A positive response.
- A correct output on the write interface.

```

```{test-card} A Valid Configuration With Null Write Interface

A valid configuration is set for the component with null write. The computation is
executed and returns successfully.

**Inputs:**

- A valid configuration is set.

**Expected Output:**

- A positive response.

```

```{test-card} Correct Handling of the Root

A valid configuration is set for the component. The computation is executed and
returns successfully. The result written to the write interface is correct.

**Inputs:**

- A valid configuration is set, the configured tree is integral with the following weights:
    - 2
    - -2
    - 3

**Expected Output:**

- A positive response.
- A correct output on the write interface.

```

```{test-card} Correct Handling of a Leaf Vertex

A valid configuration is set for the component. The computation is executed and
returns successfully. The result written to the write interface is correct.

**Inputs:**

- A valid configuration is set, the following trees are configured:
    - `i([2][3])`
    - `i([-2][3])`
    - `i([3][3])`
    - `i([2][-2])`
    - `i([2][-2 -2])`

**Expected Output:**

- A positive response.
- A correct output on the write interface.

```

```{test-card} Correct Handling of an Internal Vertex

A valid configuration is set for the component. The computation is executed and
returns successfully. The result written to the write interface is correct.

**Inputs:**

- A valid configuration is set, the following trees are configured:
    - `i([3](([3][3])2))`
    - `i([3](([3][3])-2))`
    - `i([3](([3][3])3))`
    - `i((([3][3])2)(([3][3])-2))`

**Expected Output:**

- A positive response.
- A correct output on the write interface.
```

#### Negative Tests

```{test-card} Not Configured

The compute interface is called before configuration.

**Inputs:**

- None.

**Expected Output:**

A negative response.

```

##### Result Function

###### Positive Tests

```{test-card} A Valid Configuration and Computation

A valid configuration is set for the component. The computation is executed and
returns successfully. The resulting value is correct when read from the result
interface.

**Inputs:**

- A valid configuration is set with the following trees:
    - `i([2][3])`
    - `i([-2][3])`
    - `i([3][3])`
    - `i([2][-2])`

**Expected Output:**

- A positive response.
- The result is correct.
```

###### Negative Tests

```{test-card} Computation Not Executed

The result interface is called before compute has been run.

**Inputs:**

- None.

**Expected Output:**

A negative response.

```
