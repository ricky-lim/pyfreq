@_:
    just --list


# Recreate project from nothing
[group('setup')]
fresh: clean install


# Remove temporary files
[group('setup')]
clean:
    rm -rf \
        .venv .pytest_cache \
        .mypy_cache .ruff_cache \
        .coverage htmlcov 
    find . \
        -type d \
        -name "__pycache__" \
        -exec rm -rf {} +


# Ensure project virtualenv is up to date
[group('setup')]
install:
    uv sync


# Run our CLI
[group('dev')]
run *args :
    uv run pyfreq {{ args}}


# Run test
[group('dev')]
test *args:
    uv run -m pytest {{ args }}


# Perform all quality check
[group('quality')]
check-all: lint cov typing


# Run linting
[group('quality')]
lint:
    - uv run -m ruff check --fix --unsafe-fixes .
    - uv run -m ruff format .


# Run typing
[group('quality')]
typing:
    uv run -m mypy src


# Run tests coverage
[group('quality')]
@cov:
    just _cov erase
    just _cov run -m pytest
    just _cov report
    just _cov html


_cov *args:
    uv run -m coverage {{ args }}
