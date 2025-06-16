<!-- prettier-ignore-start -->
(sec-computation-neutrality)=
### Arborescent Tangle Neutrality Computation
<!-- prettier-ignore-end -->

The arborescent tangle neutrality computation implements a portion of the
theoretical use case seen in @sec-RLITT-generation. Particularly, the neutrality
operation defined in @rli-gen-sec-pm-con.

#### Class Diagram

```mermaid
classDiagram
    comp_neutrality ..|> computation
    comp_neutrality_config_t ..|> notation_wptt
    comp_neutrality_config_t ..|> comp_config_t
    comp_neutrality *-- comp_neutrality_config_t
    comp_neutrality_result_t ..|> notation_wptt
    comp_neutrality_result_t ..|> comp_result_t
    comp_neutrality *-- comp_neutrality_result_t
    comp_neutrality_result_t *-- comp_neutrality_neutralities_e

    class computation {
        <<External Interface>>
    }

    class comp_neutrality {
    <<External>>
    }

    class notation_wptt{
    <<External>>
    }

    class comp_neutrality_config_t {

    + notation_wptt *tree
    }

    class comp_config_t {
    <<External Interface>>
    }

    class comp_neutrality_result_t {

    + comp_neutrality_neutralities_e result
    }
    class comp_neutrality_neutralities_e {
    <<Enumeration>>
     uninit,
     neutral,
     not-neutral
    }

    class comp_result_t {
    <<External Interface>>
    }


```

#### Language

C

#### Implements

-   Computation Interface (@sec-interfaces-computation)

#### Uses

-   Notation Weighted Planar Tangle Tree (@sec-library-wptt-note)

#### Libraries

N/A

#### Functionality

##### Public Structures

###### Config Structure

The config structure contains the data needed for computing the neutrality of an
input arborescent tangle.

This includes:

-   A pointer to a read-only notation structure for a WPTT.

###### Result Structure

The config structure contains the enumerated value of the neutrality of the
input tree.

##### Public Functions

###### Config Function

The config function configures the local instance variable of the computation.

This process is described in the following state machines:

```mermaid
stateDiagram-v2
  state "Initialize local config" as Sc

    [*] --> Sc
    Sc --> [*]

```

###### Compute Function

The compute function carries out the arborescent tangle neutrality computation.
The function may contain sub machines that can be broken out into functions in
the implementation. The walk the tree function should be implmented with a
stack-based iteration.

This process is described in the following state machines:

```mermaid
stateDiagram-v2
    state "Initialize" as init
    state "• Set tree as neutral" as init
    state "• Set stick length to 0" as init
    state "• Set stick has $$\ \pm2\ $$ to false" as init

    walk: Walk the tree

    state walk {
        state is_stick_end <<choice>>
        state is_weight_leaf_pm2 <<choice>>
        state is_weight_pm2 <<choice>>
        state has_pm2 <<choice>>
        state is_len_1 <<choice>>

        snnv: Set tree as Non-neutral
        isl: Increment sick length
        csl: Set stick length to 0
        ssf: Set stick has $$\ \pm2\ $$ to false
        sst: Set stick has $$\ \pm2\ $$ to true
        [*]--> is_stick_end
        is_stick_end --> isl: else
        is_stick_end --> is_weight_leaf_pm2: Number of children is 0
        is_weight_leaf_pm2 --> snnv: Weight of leaf is $$\ \pm2$$
        is_weight_leaf_pm2 --> [*]: else
        snnv --> [*]
        is_stick_end --> is_len_1: Number of children is $$\ 2\leq$$
        is_len_1 --> has_pm2: Sick has lenght 1
        has_pm2 --> csl :else
        is_len_1 --> csl: else
        has_pm2 --> snnv :Sick has a $$\ \pm 2$$
        csl -->ssf
        ssf --> [*]
        isl --> is_weight_pm2
        is_weight_pm2 --> sst : Weight of node is $$\ \pm2$$
        is_weight_pm2 --> [*] : else
        sst --> [*]

    }

    [*] --> init
    init --> walk
    walk --> [*]
```

###### Result Function

When this function is invoked, the result of the neutrality computation process
is reported.

#### Validation

##### Config Function

###### Positive Tests

```{test-card} Valid Config

A valid config for the computation is passed to the function.

**Inputs:**

- A valid config.

**Expected Output:**

A positive response.

```

###### Negative Tests

```{test-card} Null Config

A null config for the computation is passed to the function.

**Inputs:**

- A null config.

**Expected Output:**

A negative response.

```

```{test-card} Null Config Parameters

A config with various null parameters is passed to the function.

**Inputs:**

- A config with null tree.

**Expected Output:**

A negative response.

```

##### Compute Function

###### Positive Tests

```{test-card} A valid config

A valid config is set for the component. The computation is executed and
returns successfully. The result written to the write interface is correct.

**Inputs:**

- A valid config is set.

**Expected Output:**

- A positive response.
- A correct output on the write interface.

```

```{test-card} A valid config with null write interface

A valid config is set for the component with null write. The computation is
executed and returns successfully.

**Inputs:**

- A valid config is set.

**Expected Output:**

- A positive response.

```

###### Negative Tests

```{test-card} Not Configured

The compute interface is called before configuration.

**Inputs:**

- None.

**Expected Output:**

A negative response.

```

##### Result Function

###### Positive Tests

```{test-card} A valid config and computation

A valid config is set for the component. The computation is executed and
returns successfully. The resulting value is correct when read from the result
interface.

**Inputs:**

- A valid config is set.

**Expected Output:**

- A positve response.
- The result is correct.
```

###### Negative Tests

```{test-card} Computation not executed

The result interface is called before compute has been run.

**Inputs:**

- None.

**Expected Output:**

A negative response.

```
