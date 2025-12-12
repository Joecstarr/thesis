<!-- prettier-ignore-start -->
(sec-computation-grafting)=
### Arborescent Tangle Grafting Computation
<!-- prettier-ignore-end -->

The arborescent tangle grafting computation implements a portion of the
theoretical use case seen in @sec-arborescent. Particularly, the grafting
operation defined in @rli-gen-def-grafting_op-wpt.

#### Class Diagram

$\,$

````{figure}
```{mermaid}
classDiagram
    comp_rlitt_grafting --|> computation
    comp_rlitt_grafting_config_t --|> notation_wptt
    comp_rlitt_grafting_config_t --|> comp_config_t
    comp_rlitt_grafting *-- comp_rlitt_grafting_config_t
    comp_rlitt_grafting_result_t --|> notation_wptt
    comp_rlitt_grafting_result_t --|> comp_result_t
    comp_rlitt_grafting *-- comp_rlitt_grafting_result_t

    class computation {
        <<interface>>
    }

    class comp_rlitt_grafting {
<<External>>
}

class notation_wptt{
<<>>
}

class comp_rlitt_grafting_config_t {
<<struct>>
+ notation_wptt *rootstock
+ notation_wptt *scion
+ uint8 grating_idx
+ notation_wptt output_buffer
}

class comp_config_t {
<<interface>>
}

class comp_rlitt_grafting_result_t {
<<struct>>
+ notation_wptt result
}

class comp_result_t {
<<interface>>
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

The configuration structure contains the data needed for computing the grafting
of two input arborescent tangles.

This includes:

- Rootstock pointer to a read-only notation structure for a WPTT.
- Scion pointer to a read-only notation structure for a WPTT.
- An index, in the total order, of the vertex in the rootstock to graft the
  scion onto.
- A buffer to place the resultant tangle into.

###### Result Structure

The results structure contains a weighted planar tangle tree that is the result
of grafting the configured rootstock to the configured scion at the configured
index.

##### Public Functions

###### Configuration Function

The configuration function sets the local configuration variable of the
computation.

This process is described in the following state machines:

````{figure}
```{mermaid}
stateDiagram-v2
  state "Initialize local config" as Sc

    [*] --> Sc
    Sc --> [*]

```
````

###### Compute Function

The compute function carries out the arborescent tangle grafting computation.
The function may contain sub machines that can be broken out into functions in
the implementation.

This process is described in the following state machines:

````{figure}
```{mermaid}
stateDiagram-v2
    copy_normalize_tree: Copy and normalize<br/>rootstock into buffer
    graft: Graft at vertex i

    [*] --> copy_normalize_tree
    copy_normalize_tree --> graft
    graft --> [*]
```
````

###### Result Function

When this function is invoked, the result of the neutrality computation process
is reported.

##### Private Functions

#### Graft Scion to Rootstock

````{figure}
```{mermaid}
stateDiagram-v2
    find_node: Identify the ith node
    set_count: Increment child count
    add_node: Add root of scion<br>to the child list
    move_weight: Move last weight right<br>one and replace with 0

    [*] --> find_node
    find_node --> set_count
    set_count --> add_node
    add_node --> move_weight
    move_weight --> [*]
```
````

#### Validation

##### Configuration Function

###### Positive Tests

```{Test-Card} Valid Configuration

A Valid Configuration for the Computation Is Passed to the Function.

**Inputs:**

- A Valid Configuration.

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

- A configuration with null rootstock.
- A configuration with null scion.

**Expected Output:**

A negative response.

```

##### Compute Function

###### Positive Tests

```{test-card} A valid Configuration

A valid configuration is set for the component. The computation is executed and
returns successfully. The result written to the write interface is correct

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

```{test-card} A Valid Configuration and Computation

A valid configuration is set for the component. The computation is executed and
returns successfully. The resulting value is correct when read from the result
interface.

**Inputs:**

- A valid configuration is set.

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
