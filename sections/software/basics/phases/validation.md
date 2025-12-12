### Unit Testing

With implementation complete, we move to the right side of the V, which consists
of the verification activities. The first verification phase is the isolated
verification of each unit, called **unit testing**. In this phase, we design and
carry out tests of the units we have implemented. When designing tests, it is
important to draw from the unit design directly, instead of designing tests
against the actual implemented code. Testing the code against the design ensures
that we are not drawing the target around the arrow. Tests, particularly unit
tests, can and should, be separated into two classes of tests. The first class
is those on the "happy path", validating that "good" well-formed input generates
expected output, see @se-ex-happyut. The second class are those on the "unhappy
path", validating that "bad" or malformed input is handled as expected, see
@se-ex-unhappyut. Each public, accessible to external units, interface of a unit
should have at least one unit test. If validation in this, or the following
phases, finds deficiencies in the design, the V model allows for that feedback
to be pushed to earlier phases and addressed by flowing back through the V
model.

#### Test Cards

As we walk up the right side of the V, instead of diagrams we utilize test
cards. A test card is used to define a set of requirements that a test will be
implemented against. Each test card has four fields with content as follows:

-   **Test Name**: The unique name for the test. This name is used in test
    reports to identify what has failed.

-   **Description**: The description of what the test is validating and how that
    validation works. This section may include text and diagrams.

-   **Inputs**: A set of inputs to feed the unit.

-   **Outputs**: The outputs that are expected when the inputs are fed to the
    unit.

The following are two examples of unit test cards for the Go Fish product. One
test card is on the happy path, and one is on the unhappy path.

````{prf:example} A happy path test card for a player turn in Go Fish
:label: se-ex-happyut

```{test-card} Request a card, reponse is positive

**Description**: Active player requests a card from a target player. The target
player has the requested card and produces it.

**Inputs**:

-   A valid requested card
-   A valid target player with requested card in hand

**Outputs**:

-   Active player puts the received card in hand
```
````

````{prf:example} A unhappy path test card for a player turn in Go Fish
:label: se-ex-unhappyut

```{test-card} Illegally request a card

**Description**: Active player requests a card that is not in their hand.

**Inputs**:

-   An invalid requested card

**Outputs**:

-   Active player is notified the request failed

```
````

### Integration Testing

While working in software, it is rare for a system to have a single unit or a
collection of units that are completely uncoupled (@se-def-coup). When we do
have units that depend on each other, we call the process of sticking those units
together, **integration**. We verified during the unit tests that implemented
units work individually as expected. In the integration testing phase, we verify
that implemented units work together as expected. Tests in this phase should be
designed against the artifacts from the software design phase
(@subsec-softearedesign) as well as the use cases defined in the requirements
phase (@subsec-requirements).

### Acceptance Testing

When we have completed unit and integration testing, we have verified that the
software, based on the design, doesn't unexpectedly break and satisfies written
requirements (use cases). However, we have not yet verified that the system
satisfies what all stakeholders wanted. In our Go Fish example, this phase may
include a presentation to a customer. This is the point where a customer may
find that our interpretations of @se-fig-bad_req disagree, and we update to
@se-fig-bad_req_fixed.
