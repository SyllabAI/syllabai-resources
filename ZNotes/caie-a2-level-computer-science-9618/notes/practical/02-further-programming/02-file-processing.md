## File Processing

These are the pseudocodes available for files.

```tsx
OPENFILE name FOR WRITE // WRITE/READ/APPEND/RANDOM
WRITEFILE name, value // Writes one line
READFILE name, variable // Reads one line
GETRECORD name, identifier // Write a record to a file
PUTRECORD name, identifier // Reads a record from a file
SEEK name, address // Move to a specific address within a file
CLOSEFILE name
```

**Example**

```tsx
OPENFILE “Text.txt” FOR READ
WHILE NOT EOF(“Text.txt”) DO
 READFILE “Text.txt”, Value
 OUTPUT Value
ENDWHILE
CLOSEFILE “Text.txt”
```

### Sequential/Serial Files

**Reading**

```ts
OPENFILE CarFile FOR WRITE
FOR i ← 1 TO MaxRecords
 GETRECORD CarFile, Car[i]
NEXT i
CLOSEFILE CarFile 
```

**Writing**

```ts
OPENFILE CarFile FOR READ
FOR i ← 1 TO MaxRecords
 PUTRECORD CarFile, Car[i]
NEXT i
CLOSEFILE CarFile 
```

### Random Files

**Reading**

```ts
OPENFILE CarFile FOR RANDOM
Address ← Hash(ThisCar.VehicleID)
SEEK CarFile, Address
GETRECORD CarFile, ThisCar
CLOSEFILE CarFile
```

**Writing**

```ts
OPENFILE CarFile FOR RANDOM
Address ← Hash(ThisCar.VehicleID)
SEEK CarFile, Address
PUTRECORD CarFile, ThisCar
CLOSEFILE CarFile
```