import json
from functools import wraps
from pathlib import Path


class BankError(Exception):
    pass


class InsufficientFundsError(BankError):
    pass


# --- THE DECORATOR ---
def audit(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        # 1. Execute the business logic (Must pass 'self' into func!)
        new_balance = func(self, *args, **kwargs)

        # 2. Log exactly what the assert test expects: e.g., "deposit:(500,)"
        self.logs.append(f"{func.__name__}:{args}")

        # 3. Return the resulting balance
        return new_balance

    return wrapper


# --- BASE CLASS ---
class Account:
    # 1. Typo fixed: __init__, and balance is int
    def __init__(self, aid: str, owner: str, balance: int = 0):
        self.aid = aid
        self.owner = owner
        self.logs: list[str] = []  # Syntax fixed
        self.balance = balance  # Triggers the setter below

    # 2. Methods moved OUTSIDE __init__ (Indentation fixed)
    @property
    def balance(self) -> int:
        return self._balance

    @balance.setter
    def balance(self, value: int):
        # The parameter is 'value', so check 'value'
        if value < 0:
            raise ValueError("Balance can't be negative")
        self._balance = value  # Store it in the hidden variable

    @audit
    def deposit(self, amt: int) -> int:
        if amt <= 0:
            raise ValueError("Amount can't be negative")
        # 3. MUST use self.balance
        self.balance += amt
        return self.balance

    @audit
    def withdraw(self, amt: int) -> int:
        if amt <= 0:
            raise ValueError("Amount can't be negative")

        # 4. Check if they have enough money
        if self.balance < amt:
            raise InsufficientFundsError("Not enough balance")

        self.balance -= amt
        return self.balance

    def to_dict(self) -> dict:
        return {
            "type": "Account",
            "aid": self.aid,
            "owner": self.owner,
            "balance": self.balance,
            "logs": self.logs,
        }

    @classmethod
    def from_dict(cls, data: dict):
        obj = cls(aid=data["aid"], owner=data["owner"], balance=data["balance"])
        # 2. Inject the logs array directly
        obj.logs = data["logs"]
        # 3. Return the fully restored object
        return obj


# --- CHILD CLASS ---
class CheckingAccount(Account):
    def __init__(self, aid: str, owner: str, balance: int = 0, overdraft: int = 500):
        self.overdraft = overdraft
        # 5. Do not return super(). Just call it.
        super().__init__(aid, owner, balance)

    # 6. OVERRIDING THE SETTER
    # We use @ParentName.propertyName.setter
    @Account.balance.setter
    def balance(self, value: int):
        # New Rule: Can drop to negative overdraft limit
        if value < -self.overdraft:
            raise ValueError("Exceeded overdraft limit")
        self._balance = value

    # 7. OVERRIDING WITHDRAW
    @audit
    def withdraw(self, amt: int) -> int:
        if amt <= 0:
            raise ValueError("Amount can't be negative")

        # Check against the new limit
        if (self.balance - amt) < -self.overdraft:
            raise InsufficientFundsError("Exceeded overdraft limit")

        self.balance -= amt
        return self.balance


def save_ledger(file_path: Path, accounts: list) -> None:
    payload = [acc.to_dict() for acc in accounts]
    tmp_path = file_path.with_suffix(".tmp")
    tmp_path.write_text(json.dumps(payload, indent=2))
    tmp_path.replace(file_path)


def load_ledger(file_path: Path) -> list:
    if not file_path.exists():
        return []
    payload = json.loads(file_path.read_text())
    return [Account.from_dict(item) for item in payload]


if __name__ == "__main__":
    db_path = Path("bank_ledger.json")
    accounts = load_ledger(db_path)
    # Test Base Account
    a1 = Account("A1", "Aditya", 1000)
    if not accounts:
        print("No database found. Creating a new account for Aditya...")
        my_account = Account("A1", "Aditya", 0)
        accounts.append(my_account)
    else:
        my_account = accounts[0]
        print(
            f"Database loaded! Welcome back {my_account.owner}. Balance: ${my_account.balance}"
        )

    while True:
        action = input("\nDo you want to (d)eposit, (w)ithdraw, or (q)uit? ").lower()

        if action == "q":
            print("Shutting down server...")
            break

        elif action == "d":
            amt = int(input("Enter deposit amount: "))
            my_account.deposit(amt)
            print(f"Success! New Balance: ${my_account.balance}")
            save_ledger(db_path, accounts)  # SAVE TO HARD DRIVE

        elif action == "w":
            amt = int(input("Enter withdrawal amount: "))
            try:
                my_account.withdraw(amt)
                print(f"Success! New Balance: ${my_account.balance}")
                save_ledger(db_path, accounts)  # SAVE TO HARD DRIVE
            except InsufficientFundsError as e:
                print(f"ERROR: {e}")
