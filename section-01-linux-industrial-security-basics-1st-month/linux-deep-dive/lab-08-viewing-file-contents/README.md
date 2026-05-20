# Lab 08 - Viewing File Contents

## Objectives
- Learn file viewing commands
- Use head, tail, more, and grep
- Search text efficiently in Linux

---

# Task 1 - head Command

## View First 10 Lines

```bash
head example.txt
```

## View First 5 Lines

```bash
head -n 5 example.txt
```

---

# Task 2 - tail Command

## View Last 10 Lines

```bash
tail example.txt
```

## View Last 15 Lines

```bash
tail -n 15 example.txt
```

---

# Task 3 - more Command

## Open File

```bash
more example.txt
```

## Navigation
- Spacebar → Next page
- Enter → Next line
- q → Quit

---

# Task 4 - grep Command

## Search Text

```bash
grep "Linux" example.txt
```

## Case Insensitive Search

```bash
grep -i "linux" example.txt
```

## Recursive Search

```bash
grep -r "Linux" .
```

---

# Screenshots

## Head Command Output
```text
screenshots/01-head-command.png
```

## Tail Command Output
```text
screenshots/02-tail-command.png
```

## More Command Output
```text
screenshots/03-more-command.png
```

## Grep Command Output
```text
screenshots/04-grep-command.png
```

---

# Outcome
Successfully learned:
- Viewing files using head and tail
- Interactive browsing with more
- Searching text using grep
- Linux text processing basics
