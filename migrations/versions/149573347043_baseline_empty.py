"""baseline (empty)

Revision ID: 149573347043
Revises:
Create Date: 2025-09-09 12:41:05.489448

"""

from collections.abc import Sequence

# revision identifiers, used by Alembic.
revision: str = "149573347043"
down_revision: str | Sequence[str] | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
