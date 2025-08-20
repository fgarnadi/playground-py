.PHONY: sync check fmt

sync:
	@uv sync --all-packages --no-install-workspace

check:
	@ruff check || true
	@ruff format --check || true

fmt:
	@ruff check --fix
	@ruff format