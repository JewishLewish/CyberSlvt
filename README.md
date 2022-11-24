# CyberSlvt
Coding Language for Data Engineering


## Statements
```She Said: [STRING]``` -> Outputs [STRING]

```She Remembered: [VARIABLE NAME] = [VARIABLE's NAME VALUE]``` -> No Output. Saves variable.

```She Left``` -> Ends File. 

```She Checked If: [CONDITION]``` -> Will Run Anything Inside, If it's true

```She Checked While: [CONDITION]``` -> Will Run Anything Inside, While it's true


## Callings
```var.[VARIABLE NAME]``` -> Replaces the variable with the value of the variable.

```math{[INT IN HERE]}``` -> Does the math inside the math{} calling.

## Other
```;``` -> Can be used to make two lines of command run in one sentence.

## Examples
```py
Input -> She Remembered: x = 2; She Said: var.x
Output -> 2
```

```py
Input -> She Remembered: x = 2
She Checked While: var.x != 4
  She Said: var.x
  She Remembered: x = math{var.x + 1}
  
Output -> 2
3
```
