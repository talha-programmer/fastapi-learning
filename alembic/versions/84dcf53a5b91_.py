"""empty message

Revision ID: 84dcf53a5b91
Revises: 
Create Date: 2023-10-03 18:06:06.997557

"""
from typing import Sequence, Union
import os
import json

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql
from db.models.user import Role

# revision identifiers, used by Alembic.
revision: str = '84dcf53a5b91'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_profiles_id', table_name='profiles')
    op.drop_table('profiles')
    op.drop_index('ix_users_email', table_name='users')
    op.drop_index('ix_users_id', table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    users = op.create_table('users',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('email', mysql.VARCHAR(length=100), nullable=False),
    # sa.Column('role', mysql.ENUM(Role.student, Role.teacher), nullable=True),
    sa.Column('created_at', mysql.DATETIME(), nullable=False),
    sa.Column('updated_at', mysql.DATETIME(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )

    op.add_column(
        "users",
        sa.Column('role', sa.Enum('student', 'teacher', name="role"), nullable=True),
    )


    op.create_index('ix_users_id', 'users', ['id'], unique=False)
    op.create_index('ix_users_email', 'users', ['email'], unique=False)

    # Seed students data
    with(open(os.path.join(os.path.dirname(__file__), "../data/students.json"))) as f:
        student_data = f.read()
    
    op.bulk_insert(users, json.loads(student_data))

    op.create_table('profiles',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('first_name', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('last_name', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('bio', mysql.TEXT(), nullable=True),
    sa.Column('is_active', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('user_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('created_at', mysql.DATETIME(), nullable=False),
    sa.Column('updated_at', mysql.DATETIME(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='profiles_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('ix_profiles_id', 'profiles', ['id'], unique=False)
    # ### end Alembic commands ###
