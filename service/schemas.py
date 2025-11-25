from pydantic import BaseModel
from typing import Optional

class ClientInput(BaseModel):
    фамилия: str
    кредитный_рейтинг: float
    город: str
    пол: str
    возраст: float
    стаж_в_банке: float
    баланс_депозита: Optional[float]
    число_продуктов: float
    есть_кредитка: int
    активный_клиент: int
    оценочная_зарплата: float
    баланс_депозита_missing: int
