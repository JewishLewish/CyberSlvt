<p align="center">
  <img src="https://user-images.githubusercontent.com/65754609/204068035-cdd50b9c-c611-48c5-9bff-35499bd7e6aa.png" width="200">
</p>

# CyberSlvt
Cyberslvt was created as a 'joke' coding language for me to work on while I was bored. It does function perfectly and I will work on minor updates time to time. If you are interested in adding more or forking onto the code then feel free to do so. 


## Statements
```She Said: [STRING]``` -> Outputs [STRING]

```She Remembered: [VARIABLE NAME] = [VARIABLE's NAME VALUE]``` -> No Output. Saves variable.

```She Left``` -> Ends File. 

```She Checked If: [CONDITION]``` -> Will Run Anything Inside, If it's true

```She Checked While: [CONDITION]``` -> Will Run Anything Inside, While it's true

```She Left``` -> Ends the file entirely.


## Callings
```var.[VARIABLE NAME]``` -> Replaces the variable with the value of the variable.

```math{[INSERT MATH EQUATION]}``` -> Does the math inside the math{} calling. Outputs int.

```floatmath{[INSERT MATH EQUATION]}``` -> Does the math inside the math{} calling. Outputs float.

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
