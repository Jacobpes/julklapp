# Christmas Gift Assignment Script

## Overview
This script is used to assign who will buy Christmas gifts for whom in a group, ensuring that:

1. No one is assigned to buy a gift for their partner.
2. No one is assigned to buy a gift for someone who is already buying a gift for them.
3. Each person gets exactly one person to buy a gift for, and everyone is assigned uniquely.

The script takes into consideration partner restrictions and performs random assignments while adhering to all rules defined.

## How It Works

1. **Input List**: The script takes a list of pairs representing partners. Each pair contains two individuals who should not be assigned to buy gifts for each other.

    ```python
    people = [["Dani", "Emmi"], ["Evert", "Maria"], ["Jacob", "Amanda"], ["Albert", "Jemina"], ["Juulia", "Junna"]]
    ```

2. **Assignment Process**: The script performs the following steps:
   - Flattens the list of pairs into a single list of individuals.
   - Randomly assigns gift-givers to receivers.
   - Ensures that the receiver is not the giver's partner, that they haven't already been assigned, and that there are no reciprocal assignments.

3. **Validation and Recursion**: If a valid assignment cannot be found for a particular giver (i.e., no eligible receivers remain), the script restarts the entire assignment process to ensure all rules are followed.

## Usage

To run the script, simply execute it in a Python environment. The assignments will be printed to the console.

```sh
python assign_gifts.py
```

The output will display who is buying a gift for whom, for example:

```
Dani buys a gift for Jemina
Emmi buys a gift for Jacob
Evert buys a gift for Junna
...
```

## Requirements
- Python 3.x

No additional libraries are required for running the script.

## Notes
- The assignment process may restart multiple times if a valid set of assignments cannot be generated. This is to ensure that all conditions are met.
- The script uses a recursive approach to handle invalid states, which works well for small groups but may need optimization for larger groups.

## License
This script is open-source and available for anyone to use and modify.

## Author
- Jacob Pesämaa 2024

