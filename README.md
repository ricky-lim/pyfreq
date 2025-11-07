# pyfreq

This is a sample application demonstrating how to build a command-line interface (CLI) using only [UV](https://github.com/astral-sh/uv). 
The project is intentionally minimal to showcase the essentials of CLI development without extra dependencies.

## Blog

Read more about building Python CLIs with UV in this blog post:  

- [build-cli-with-uv](https://ricky-lim.github.io/blog/build-cli-with-uv)  
- [development-workflow-with-just](https://ricky-lim.github.io/blog/development-workflow-with-just)

## How to Run

1. Make sure you have [UV](https://github.com/astral-sh/uv) installed.
2. Make sure you have [just](https://github.com/casey/just) installed.

```bash
# All the development workflow
just

# Get started
just fresh

# Run
just run developer jokes.txt

# Test
just test

# Quality check
just check-all
```

## How to use

```bash
pyfreq developer jokes.txt
```

This will count the occurrences of the word "developer" in the file `jokes.txt`.
