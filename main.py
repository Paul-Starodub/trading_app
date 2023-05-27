from fastapi import FastAPI
from pydantic import BaseModel
from pydantic.fields import Field

app = FastAPI(title="Trading App")


fake_users = [
    {"id": 1, "role": "admin", "name": "Bob"},
    {"id": 2, "role": "investor", "name": "John"},
    {"id": 3, "role": "trader", "name": "Matt"},
]


class User(BaseModel):
    id: int
    role: str
    name: str


@app.get("/users/{user_id}", response_model=list[User])
def get_user(user_id: int):  # str by default
    return [user for user in fake_users if user.get("id") == user_id]


fake_trades = [
    {
        "id": 1,
        "user_id": 1,
        "currency": "BTC",
        "side": "buy",
        "price": 123,
        "amount": 2.12,
    },
    {
        "id": 2,
        "user_id": 1,
        "currency": "BTC",
        "side": "sell",
        "price": 125,
        "amount": 2.12,
    },
]


class Trade(BaseModel):
    id: int
    user_id: int
    currency: str = Field(max_length=5)
    price: float = Field(ge=0)
    amount: float


@app.post("/trades")
def add_trades(trades: list[Trade]):
    fake_trades.extend(trades)
    return {"status": 200, "data": fake_trades}
