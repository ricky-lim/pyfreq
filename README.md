# pyfreq

This is a sample application demonstrating how to build a command-line interface (CLI) using only [UV](https://github.com/astral-sh/uv). 
The project is intentionally minimal to showcase the essentials of CLI development without extra dependencies.

## Blog

Read more about building Python CLIs with UV in this blog post:  
[build-cli-with-uv](https://ricky-lim.github.io/blog/build-cli-with-uv)  

## How to Run

1. Make sure you have [UV](https://github.com/astral-sh/uv) installed.
2. Run the CLI using the following command:

```bash
uv run pyfreq <word> <filename>
```

Example:

```bash
uv run pyfreq developer jokes.txt
```

This will count the occurrences of the word "developer" in the file `jokes.txt`.
