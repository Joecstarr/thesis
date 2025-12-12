### The Job Server

We will now give a brief overview for the software design of the job server.
Full documentation and implementation information can be found on GitHub
[@joestarrUiowaAppliedTopologyTanglenomicon_web_apiV0012025]. The job server is
designed to be used for the distribution and handling of generation jobs.
Additionally, the job server serves as the backend for the coming presentation
layer for the generated tangle data. The use cases for the job server are
modeled in the following use case diagram (@js-fig-uc).

````{figure}
:label: js-fig-uc
```{mermaid}

flowchart LR
    subgraph Generation
        direction LR
        G1([Get Montesinos job])
        G2([Report Montesinos job])
        G3([Get Arborescent job])
        G4([Report Arborescent job])
    end
    subgraph Presentation
        direction LR
        PL1([Get paged tangles])
        PL2([Get specific tangle])
        PL3([Get tangles with property])
    end

    subgraph Job Handling
        direction LR
        JH1([Build job])
        JH2([Clean up stale jobs])
        JH3([Clean up complete jobs])
        JH4([Mark job as complete])
        JH5([Mark job as new])
        JH6([Mark job as pending])
        JH7([Fill job queue])
    end
    subgraph Database Handling
        direction LR
        DH1([Mark progress])
        DH2([Write record set])
        DH3([Read record set])
    end

    client["Client fa:fa-user"]
    time["Time fa:fa-user"]
    client --> G1
    client --> G2
    client --> G3
    client --> G4
    time --> JH2
    time --> JH3
    time --> JH7
    JH1 -. include .-> JH5
    JH2 -. include .-> JH6
    JH7 -. include .-> JH1
    JH1 -. include .-> DH3
    JH3 -. include .-> DH1
    JH3 -. include .-> DH2
    G1 -. include .-> JH6
    G2 -. include .-> JH4
    G3 -. include .-> JH6
    G4 -. include .-> JH4
    client --> PL1 -. include .-> DH3
    client --> PL2 -. include .-> DH3
    client --> PL3 -. include .-> DH3

```
````

These use cases are realized in the software design block diagram

````{figure}
:label: js-fig-bd
```{mermaid}

flowchart LR
    tanglenomicon_data_api["Tanglenomicon API"]
    subgraph Interfaces
        age["Generation Endpoint\n&lt;&lt;interface&gt;&gt;"]
        ape["Presentation Endpoint\n&lt;&lt;interface&gt;&gt;"]
        aj["Job\n&lt;&lt;interface&gt;&gt;"]
        es["State\n&lt;&lt;enumeration&gt;&gt;"]
        o["ORM\n&lt;&lt;enumeration&gt;&gt;"]
    end

    subgraph Internal
        dc["DB Connector"]
        jq["Job Queue"]
        cs["ConfigurationStore"]
        sm["Security Model"]
    end

    subgraph Arborescent
        arpe["Arborescent Presentation Endpoint"]
        aro["ORM"]
        arj["Arborescent Job"]
        arge["Arborescent Generation Endpoint"]
    end

    subgraph Montesinos
        mpe["Montesinos Presentation Endpoint"]
        mo["ORM"]
        mj["Montesinos Job"]
        mge["Montesinos Generation Endpoint"]
    end

    subgraph Generic
        gpe["Presentation Endpoint"]
        go["ORM"]
    end
    subgraph rational
        rpe["Presentation Endpoint"]
        ro["ORM"]
    end

    rpe --->|1| tanglenomicon_data_api
    mge --->|1| tanglenomicon_data_api
    arge --->|1| tanglenomicon_data_api
    jq --->|1| tanglenomicon_data_api
    sm --->|1| tanglenomicon_data_api
    gpe --->|1| tanglenomicon_data_api
    cs ---> tanglenomicon_data_api
    dc --->|1| jq
    dc --->|1| sm
    mj --->|1 . . *| jq
    arj --->|1 . . *| jq
    mpe -.-> ape
    arpe -.-> ape
    mj -.-> aj
    arj -.-> aj
    mo -.-> o
    aro -.-> o
    mge -.-> age
    arge -.-> age
    aj -.-> es
    gpe -.-> ape
    go -.-> o
    rpe -.-> ape
    ro -.-> o
```
````
