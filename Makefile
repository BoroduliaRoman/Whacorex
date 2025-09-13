# ---------- Make targets for Whacorex ----------
# Запуск: make <target>
# Примеры: make lint | make fix | make types | make run

PORT ?= 8000
HOST ?= 127.0.0.1

.PHONY: lint fix types run clean

# Быстрая проверка стиля и типов (ничего не меняет)
lint:
	ruff check .
	black --check .
	isort --check-only .
	mypy app

# Авто-правки стиля
fix:
	ruff check . --fix
	isort .
	black .

# Только типы
types:
	mypy app

# Локальный запуск API (перезагрузка при изменениях)
run:
	uvicorn app.main:app --host $(HOST) --port $(PORT) --reload

# Уборка кешей Python
clean:
	python -c "import shutil, pathlib; [shutil.rmtree(p, ignore_errors=True) for p in map(pathlib.Path, ['.mypy_cache','__pycache__'])]"

# Test
.PHONY: test

test:
	python -m pytest -q
