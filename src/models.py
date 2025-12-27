from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, DateTime, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime, timezone
from typing import List

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_name: Mapped[str] = mapped_column(
        String(200), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(200), nullable=False)
    full_name: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(
        String(200), unique=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False)

    favorites: Mapped[List['Favorite']] = relationship(
        back_populates='user', lazy='selectin'
    )


class Planet(db.Model):
    __tablename__ = 'planets'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    diameter: Mapped[str] = mapped_column(String(100), nullable=False)
    rotation_period: Mapped[str] = mapped_column(String(100), nullable=False)
    orbital_period: Mapped[str] = mapped_column(String(100), nullable=False)
    gravity: Mapped[str] = mapped_column(String(100), nullable=False)
    weather: Mapped[str] = mapped_column(String(100), nullable=False)
    population: Mapped[str] = mapped_column(String(100), nullable=False)
    terrain: Mapped[str] = mapped_column(String(100), nullable=False)
    surface_water: Mapped[str] = mapped_column(String(100), nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False)
    edited_at: Mapped[datetime] = mapped_column(DateTime(
        timezone=True), server_default=func.now(), server_onupdate=func.now(), nullable=False)

    favorite: Mapped[List['Favorite']] = relationship(
        back_populates='planet', lazy='selectin')


class Character(db.Model):
    __tablename__ = 'characters'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    birth_year: Mapped[str] = mapped_column(String(100), nullable=False)
    gender: Mapped[str] = mapped_column(String(100), nullable=False)
    eye_color: Mapped[str] = mapped_column(String(100), nullable=False)
    hair_color: Mapped[str] = mapped_column(String(100), nullable=False)
    skin_color: Mapped[str] = mapped_column(String(100), nullable=False)
    height: Mapped[str] = mapped_column(String(100), nullable=False)
    weight: Mapped[str] = mapped_column(String(100), nullable=False)
    image: Mapped[str] = mapped_column(String(200), nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False)
    edited_at: Mapped[datetime] = mapped_column(DateTime(
        timezone=True), server_default=func.now(), server_onupdate=func.now(), nullable=False)

    favorite: Mapped[List['Favorite']] = relationship(
        back_populates='character', lazy='selectin')


class Vehicles(db.Model):
    __tablename__ = 'vehicles'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    vehicle_class: Mapped[str] = mapped_column(String(200), nullable=False)
    model: Mapped[str] = mapped_column(String(200), nullable=False)
    cost_in_credits: Mapped[str] = mapped_column(String(200), nullable=False)
    manufacturer: Mapped[str] = mapped_column(String(200), nullable=False)
    crew: Mapped[str] = mapped_column(String(200), nullable=False)
    max_speed: Mapped[str] = mapped_column(String(200), nullable=False)
    cargo_capacity: Mapped[str] = mapped_column(String(200), nullable=False)
    image: Mapped[str] = mapped_column(String(200), nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False)
    edited_at: Mapped[datetime] = mapped_column(DateTime(
        timezone=True), server_default=func.now(), server_onupdate=func.now(), nullable=False)

    favorite: Mapped[List['Favorite']] = relationship(
        back_populates='vehicle', lazy='selectin')


class Favorite(db.Model):
    __tablename__ = 'favorites'

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    planet_id: Mapped[int] = mapped_column(ForeignKey('planets.id'))
    character_id: Mapped[int] = mapped_column(ForeignKey('characters.id'))
    vehicle_id: Mapped[int] = mapped_column(ForeignKey('vehicles.id'))

    user: Mapped['User'] = relationship(back_populates='user')
    planet: Mapped['Planet'] = relationship(back_populates='planet')
    character: Mapped['Character'] = relationship(
        back_populates='character')
    vehicle: Mapped['Vehicles'] = relationship(back_populates='vehicle')
