"""empty message

Revision ID: 6c1b0006e18f
Revises: 
Create Date: 2019-04-14 19:35:06.175655

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "6c1b0006e18f"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "team",
        sa.Column("team_id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=50), nullable=False),
        sa.PrimaryKeyConstraint("team_id"),
        sa.UniqueConstraint("name"),
    )
    op.create_table(
        "person",
        sa.Column("person_id", sa.Integer(), nullable=False),
        sa.Column("first_name", sa.String(length=50), nullable=False),
        sa.Column("last_name", sa.String(length=50), nullable=False),
        sa.Column("role", sa.String(length=50), nullable=True),
        sa.Column("position", sa.String(length=50), nullable=True),
        sa.Column("team_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["team_id"], ["team.team_id"]),
        sa.PrimaryKeyConstraint("person_id"),
    )
    op.create_table(
        "team_manager",
        sa.Column("manager_id", sa.Integer(), nullable=False),
        sa.Column("manager", sa.Integer(), nullable=False),
        sa.Column("captain", sa.Integer(), nullable=False),
        sa.Column("team", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["captain"], ["person.person_id"]),
        sa.ForeignKeyConstraint(["manager"], ["person.person_id"]),
        sa.ForeignKeyConstraint(["team"], ["team.team_id"]),
        sa.PrimaryKeyConstraint("manager_id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("team_manager")
    op.drop_table("person")
    op.drop_table("team")
    # ### end Alembic commands ###
