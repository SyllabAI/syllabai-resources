## Recursion

- A function/procedure that calls itself is known as a recursive function/procedure.
- Must have a base case and a general case. The general case calls the recursive function.
- Some compilers may also convert recursive functions into iterative ones.
- **Advantage:** Cleaner code
- **Disadvantage:** Large amounts of memory needed

When a recursive function is called, the address of the line as well as any additional arguments are saved to the stack. This continues until the base call is reached. Then from there it works backwards carrying out any operations until the first line is reached.