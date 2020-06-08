- Generally, you need quotes around phrases and field values that include white spaces, commas, pipes, quotes, brackets or keywords.
    - `... | search "error | stats count"`
    - `error "AND" | dedup`
    - `error "startswith=foo" | dedup`

- The backslash character (\) is used to escape quotes, pipes, and itself.
    - `... | eval myfield="6"`  ->  6
    - `... | eval myfield="\""` ->  "
    - `... | eval myfield="\\"` ->  \
    - `... | eval myfield="\"`  ->  error


- field
    - null field
    - empty field
    - empty value
    - multivalue field
