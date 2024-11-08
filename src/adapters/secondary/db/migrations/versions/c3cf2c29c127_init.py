"""init

Revision ID: c3cf2c29c127
Revises: 
Create Date: 2024-11-03 19:02:13.719066

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'c3cf2c29c127'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False, comment='Идентификатор'),
    sa.Column('username', sa.String(length=50), nullable=False, comment='Имя пользователя'),
    sa.Column('password', sa.String(), nullable=False, comment='Захешированный пароль пользователя'),
    sa.Column('created_at', sa.DateTime(), nullable=False, comment='Дата и время создания записи'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('favorite_movies',
    sa.Column('id', sa.Integer(), nullable=False, comment='Идентификатор'),
    sa.Column('user_id', sa.Integer(), nullable=False, comment='Идентификатор пользователя'),
    sa.Column('kinopoisk_id', sa.Integer(), nullable=False, comment='Идентификатор фильма на кинопоиске'),
    sa.Column('added_at', sa.DateTime(), nullable=False, comment='Дата и время добавления фильма в избранное'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='user_id_fkey', onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id', 'kinopoisk_id', name='uq_user_favorite_movie')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favorite_movies')
    op.drop_table('users')
    # ### end Alembic commands ###
