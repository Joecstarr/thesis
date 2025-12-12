<!-- prettier-ignore-start -->
(sec-library-wptt-note)=
### Weighted Planar Tangle Tree Notation
<!-- prettier-ignore-end -->

This component implements an extended version of the linearization strategy
outlined in @sec-arborescent-linear. The extensions are to add support for the
abriviated trees detailed by Bonahon and Seibenmann
[@bonahonNewGeometricSplittings2016].

#### Class Diagram
$\,$

````{figure}
```{mermaid}
classDiagram
    note_wptt ..|> notation
    note_wptt *-- note_wptt_t
    note_wptt_t *-- note_wptt_node_t
    note_wptt_node_t *-- note_wptt_order_e
    note_wptt_t *-- note_wptt_V4_label_e

    note_wptt_t ..|> note_t
    class note_t {
        <<External Interface>>
    }
    class note_wptt_t {

       + note_wptt_node_t* root
       + note_wptt_node_t* node_buffer
       + note_wptt_V4_label_e label
       + size_t node_buffer_len
    }

    class note_wptt_order_e {
        <<Enumeration>>
        uninit,
        forward,
        reverse
    }

    class note_wptt_V4_label_e {
        <<Enumeration>>
        uninit,
        none,
        i,
        x,
        y,
        z
    }

    class note_wptt_node_t {

       + note_wptt_node_t* children[MAX_CN]
       + uint8_t weights[MAX_CN]
       + size_t number_of_children
       + uint8_t number_of_rings
       + note_wptt_order_t order
    }

    class notation {
        <<External Interface>>
    }


```
````

#### Language

C

#### Implements

-   Notations Interface (@sec-interfaces-notation)

#### Uses

The WPTT notation component does not use any other components.

#### External Libraries

The WPTT notation component does not use any external libraries.

#### Functionality

##### Public Structures

###### Notation structure

The interface structure for the component is designed to match the non memory
allocating design goals of non-runner components. That means this notation
structure contains:

-   A pointer to the root of the WPTT
-   A buffer of/for nodes in the WPTT
-   A length for the buffer supplied to the component instance
-   A $V_4$ label for the WPTT

###### Node structure

We saw in the use case description an outline for the important data that needs
to be encoded in a WPTT data structure. This data is summarized as:

-   Children and their cyclic order
-   Weights and their location in the cyclic order
-   Number of rings

Each of these items are easy to encode in a C structure. The children (except
parent linkage) are encoded as an array of pointers to the children.
Additionally, this array implicitly encodes a cyclic order of the children by
the order in the array. Weights are encoded likewise in an array. Weight index
is interpreted as "after" the same child weight in order as seen below.

```{prf:example} Interleaved index

For child array $[c_0,c_1,\cdots,c_{n-1}]$ and weight array
$[w_0,w_1,\cdots,w_{n-1}]$. The order as described in the
@sec-arborescent-linear is given as:

-   Forward $$w_0c_0w_1c_1\cdots w_{n-1}c_{n-1}w_{n}$$ Forward it the assumed
    default.
-   Reverse $$w_{n}c_{n-1}w_{n-1}\cdots,w_1c_1w_0, $$

```

Finally, read order is encoded as a simple enum consisting of:

-   uninit
-   forward
-   reverse

This allows components to invert read order, read from $(n-1)\to 0$, at runtime.

##### Public Functions

###### Decode Function

The decode function takes in the linearized string form of the WPTT and encodes
it as a `note_WPTT_node_t`.

This process is described in the following state machines:

````{figure}
```{mermaid}
stateDiagram-v2
    state "Init<br>• stack array<br>• stack index<br>• char pointer" as vj
    state "read label from $$\,V_4$$" as rl
    state "Handle Root Init" as ri
    state if_end_of_string <<choice>>
    state "Execute char checker" as rn
    state "Move char pointer to</br> next char in string" as nc
    [*] --> vj
    vj --> rl
    rl --> ri
    ri --> if_end_of_string
    if_end_of_string --> nc: is not end of string
    nc --> rn
    rn --> if_end_of_string
    if_end_of_string --> [*]: is end of sting

```
````

###### Encode Function

The encode function takes in a `note_wptt_node_t` and encodes it into the
linearized string form of the WPTT.

This process is described in the following state machines:

````{figure}
```{mermaid}
stateDiagram-v2
    state "Init<br>• stack parent array<br>• stack child_idx array<br>• stack_idx as 0<br>• active node as root" as vj
    state "Push to stack<br>• root<br>• 0 to child_idk" as prts
    state "Convert the $$\,V_4$$ label to a string" as sl
    state "Execute 'handle stack'" as handle_stack
    state "Execute 'handle string conversion'" as handle_stringify
    state "stack_idx--" as simm2
    state "Add weight at</br>child_idx of active node to string" as sw
    state if_root_labeled_done <<choice>>
    state if_children_exhausted <<choice>>
    state if_stack_idx_exhausted <<choice>>

    [*] --> vj
    if_children_exhausted --> handle_stack: else
    if_stack_idx_exhausted --> [*]: if stack_idx < 0
    vj --> if_root_labeled_done
    handle_stack --> handle_stringify
    if_root_labeled_done --> prts: Tree does not have a label
    if_root_labeled_done --> sl: Tree has a label
    sl --> prts
    prts --> sw
    sw --> if_children_exhausted
    if_children_exhausted --> if_stack_idx_exhausted: if child_idx > active node number_of_children
    if_stack_idx_exhausted --> simm2: else
    simm2 --> sw
    handle_stringify --> sw
```
````

##### Private Functions decode path

Documented here are the functionality required by the notation but not exposed
publicly. The functions may contain sub machines that can be broken out into
functions in the implementation.

###### Char Checker Function

This function checks a character passed to it and updates the current notation
instance with one of seven execution paths. These paths are based on the class
the character falls into:

-   A delimiter
    -   An opening delimiter
        -   $\LA\right.$
        -   $[$
        -   $($
    -   A closing delimiter
        -   $\left.\RA$
        -   $)$
-   An integer beginning with "0-9" or "-"
-   A space character

This process is described in the following state machines:

````{figure}
```{mermaid}
stateDiagram-v2
    state "Get ring number" as rn
    state "Read twist vector and<br>move char ptr to end of tv" as tv
    state "Read integer weight" as ri
    state "Execute move active node up" as mru
    state "Execute move active node down" as mrd
    state if_is_valid <<choice>>

    cdc
    cdc: Close Delimiter Checker
    state cdc{
        state if_next_char_is_Closedelim <<choice>>

    [*]  --> if_next_char_is_Closedelim
    if_next_char_is_Closedelim --> mru: next char is delimiter $$\,\rangle$$
    if_next_char_is_Closedelim  --> mru: next char is delimiter $$\,)$$
    mru --> [*]
    }
    odc
    odc: Open Delimiter Checker
    state odc{
        state if_next_char_is_opendelim <<choice>>
    [*] --> if_next_char_is_opendelim
    if_next_char_is_opendelim --> tv: next char is delimiter $$\,[$$
    if_next_char_is_opendelim --> rn: next char is delimiter $$\,\langle$$
    if_next_char_is_opendelim --> mrd: next char is delimiter $$\,($$
    tv --> [*]
    rn --> [*]
    mrd --> [*]
    }
    [*] --> if_is_valid
    if_is_valid --> odc: Next char is valid
    if_is_valid --> [*]: else
    odc --> cdc
    cdc --> ri: next char is a number 0-9 or -
    ri --> [*]

```
````

###### Move active node down

This function moves the active node to be a child of the current node.
Functionally, this is the same as descending the WPTT.

This process is described in the following state machines:

````{figure}
```{mermaid}
stateDiagram-v2
    state "Initialize new active node as child</br> of current active node" as child
    state "Add active node to stack" as st
    state "Increment stack index" as isi
    [*] --> st
    st --> child
    child --> isi
    isi --> [*]
```
````

###### Move root up

This function moves the active node to be a parent of the current node.
Functionally, this is the same as ascending the WPTT.

This process is described in the following state machines:

````{figure}
```{mermaid}
stateDiagram-v2

    state "Decrement stack index" as dsi
    state "Set current subtree root to </br> stack array at stack index" as scr

    [*] --> dsi
    dsi --> scr
    scr --> [*]
```
````

##### Private functions Encode path

Documented here are the functionality required by the notation but not exposed
publicly. The functions may contain sub machines that can be broken out into
functions in the implementation.

###### Handle stack

The handle stick function takes a stick and

This process is described in the following state machines:

````{figure}
```{mermaid}
stateDiagram-v2

    state "Push to stack<br>• child node at child_idk node<br>• 0 to child_idx" as pants
    state "stack_idx++" as sipp
    state "child_idx[stack_idx]++" as cipp
    [*] --> pants
    pants --> cipp
    cipp --> sipp
    sipp --> [*]
```
````

###### Handle String Conversion

````{figure}
```{mermaid}
stateDiagram-v2
    state "Convert $$\,\langle$$ to string and ring number" as rn
    state "Add $$\,($$ to string" as par
    state "stack_idx--" as simm
    state "Add to string the stick as twist vector" as stv
    state if_has_rings <<choice>>
    state if_stickcheck <<choice>>
    [*] --> if_stickcheck
    if_stickcheck --> stv: Active node is on a stick
    stv --> simm
    simm --> [*]
    if_stickcheck --> if_has_rings: else
    if_has_rings --> par: else
    if_has_rings --> rn: Active node has rings
    par --> [*]
    rn --> [*]
```
````

#### Validation

##### Decode interface

###### Positive Tests

```{test-card} Valid string representing a knot

A valid string representing a knot (no free bond) is fed to the function.

**Inputs:**

- A valid string representing a knot.
- A stick tree.
- A tree with an essential vertex.
- A tree with a vertex that has ring number.
- A tree with a vertex with more than one weight.

**Expected Output:**

A valid decoding of the string

```

```{test-card} Valid string representing a tangle

A valid string representing a tangle (with free bond) is fed to the function.

**Inputs:**

- A valid string representing a tangle with each label:
    - i
    - x
    - y
    - z
- A stick tree.
- A tree with an essential vertex.
- A tree with a vertex that has ring number.
- A tree with a vertex with more than one weight.

**Expected Output:**

A valid decoding of the string


```

###### Negative Tests

```{test-card} A malformed tree is fed to the function

Various malformed trees are fed to the function.

**Inputs:**

Malformed strings with the following characteristics:

- A missing closing delimiter.
- An unexpected character is in the string.
- The string has more weights than possible.
- An empty string.

**Expected Output:**

The function reports an error.


```

##### Encode interface

###### Positive Tests

```{test-card} A valid knot WPTT is fed to the function

A valid knot WPTT (with no label) is fed to the encode function.

**Inputs:**

- A valid WPTT representing a knot.
- A stick WPTT.
- A WPTT with an essential vertex.
- A WPTT with a vertex that has ring number.
- A WPTT with a vertex with more than one weight.

**Expected Output:**

The function produces the corresponding encoded string.

```

```{test-card} A valid tangle WPTT is fed to the function

A valid tangle WPTT (with label) is fed to the encode function.

**Inputs:**

- A valid WPTT representing a tangle with each label:
    - i
    - x
    - y
    - z
- A stick WPTT.
- A WPTT with an essential vertex.
- A WPTT with a vertex that has ring number.
- A WPTT with a vertex with more than one weight.

**Expected Output:**

The function produces the corresponding encoded string.


```

###### Negative Tests

```{test-card} A malformed WPTT is passed to the function

A malformed WPTT is passed to the function.

**Inputs:**

- A NULL child is present
- A NULL root is present
- An UNInitialize label is present

**Expected Output:**

The function will produce an error.

```

```{test-card} A NULL string buffer is passed

The output string buffer is a NULL pointer.

**Inputs:**

- A NULL pointer buffer is passed to the function

**Expected Output:**

The function will produce an error.
```
