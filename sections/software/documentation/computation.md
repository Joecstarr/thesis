<!-- prettier-ignore-start -->
(sec-interfaces-computation)=
### Computation Interface
<!-- prettier-ignore-end -->

The computation interface defines the general form for a component used to perform a knot operation.
When the computation component is invoked, it produces a single output. The computation component
does not allocate memory, it must be configured with sufficient buffer space to successfully
execute.

#### Class Diagram

$\,$

````{figure}
```{mermaid}
classDiagram
    computation *-- comp_config_t
    computation *-- comp_result_t
    class computation {
        <<Interface>>
        - comp_config_t config
        - comp_result_t result
        + int comp_config(comp_config_t config)
        + int comp_compute()
        + comp_result_t comp_result()
    }

    class comp_config_t {

        + int *storage_write(key, index, value)
    }

    class comp_result_t {

    }

```
````

#### Functionality

##### Public Structures

###### Computation Configuration Structure

The computation configuration structure defines the collection of data the component needs for a
single run. Setting a configuration should be considered equivalent to instantiating a class in a
high-level language. However, in this case, there is only ever a single active instance of the
class.

###### Computation Result Structure

The computation result structure defines the collection of data the component will produce in a
single run. This is used as an alternative to the write interface, allowing the component to be used
internally in other computation or generator components.

##### Public Functions

###### Configuration Function

The function will take a configuration as input and set the local configuration instance to that
input. The function returns a flag indicating whether the function was successful. This function can
be considered analogous to the `init` function of a class in a high-level language.

###### Compute Function

When this function is invoked, the computation process begins. The actual internal functionality is
specific to the specific computation. The function returns a flag indicating whether the function
was successful.

The flow for a computation is modeled by the following state machine:

````{figure}
```{mermaid}
stateDiagram-v2
    state "Get data" as gd
    state "Work on data" as wod
    state "Report value or values" as rv
    state check_flag <<choice>>
    state "Set computed flag" as gd
    [*] --> check_flag
    check_flag --> gd : Configuration has not been processed
    check_flag --> [*]  : Configuration has been processed
    gd  -->  wod
    wod --> rv
    rv  -->  [*]
```
````

###### Result Function

When this function is invoked, the result of the computation process is reported. The actual
internal functionality is specific to the specific computation.
