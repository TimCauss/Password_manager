import psutil
from passlib.context import CryptContext


cpu_nbr = psutil.cpu_count(logical=False)
memory_free = psutil.virtual_memory().free / (1024 * 1024)


def password_context() -> object:
    """
    configure the Argon2 context for password hashing
    based on system's free memory and CPU count
    Returns:
        A configured context object for the Argon2 hashing algorithm
    """
    memory_free = psutil.virtual_memory().free / (1024 * 1024)
    time_cost = max(2, cpu_nbr)
    mem_cost = max(1024, int(memory_free/2))
    parallelism = cpu_nbr

    pwd_context = CryptContext(
        schemes=["argon2"],
        default="argon2",
        argon2__time_cost=time_cost,
        argon2__memory_cost=mem_cost,
        argon2__parallelism=parallelism
    )
    return pwd_context


def hash_password(password: str) -> str:
    """Permet de générer le hash d'un password en utilisant le context de
    l'aglo généré par la fonction  `password_context()`"""
    return password_context().hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    """Permet de vérifier le password en utilisant le hash généré par  la
    fonction 'hash_password'"""
    return password_context().verify(password, hashed_password)
