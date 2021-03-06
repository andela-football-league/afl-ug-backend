"""empty message

Revision ID: 5fa860be380f
Revises: a0089a928d64
Create Date: 2019-04-20 06:07:06.835430

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "5fa860be380f"
down_revision = "a0089a928d64"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "person", "email", existing_type=sa.VARCHAR(length=50), nullable=False
    )
    op.alter_column(
        "person", "name", existing_type=sa.VARCHAR(length=50), nullable=False
    )
    op.add_column(
        "person_profile", sa.Column("person_id", sa.Integer(), nullable=False)
    )
    op.drop_constraint(
        "person_profile_person_fkey", "person_profile", type_="foreignkey"
    )
    op.create_foreign_key(
        None, "person_profile", "person", ["person_id"], ["person_id"]
    )
    op.drop_column("person_profile", "person")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "person_profile",
        sa.Column("person", sa.INTEGER(), autoincrement=False, nullable=False),
    )
    op.drop_constraint(None, "person_profile", type_="foreignkey")
    op.create_foreign_key(
        "person_profile_person_fkey",
        "person_profile",
        "person",
        ["person"],
        ["person_id"],
    )
    op.drop_column("person_profile", "person_id")
    op.alter_column(
        "person", "name", existing_type=sa.VARCHAR(length=50), nullable=True
    )
    op.alter_column(
        "person", "email", existing_type=sa.VARCHAR(length=50), nullable=True
    )
    # ### end Alembic commands ###
