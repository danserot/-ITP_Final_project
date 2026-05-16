from datetime import datetime

class BaseEntity:
    def __init__(self, name: str):
        self._name = name      
        self._created_at = datetime.now()
    @property
    def name(self) -> str:
        return self._name
    @name.setter
    def name(self, value: str):
        if not value or not isinstance(value, str):
            raise ValueError("Name must be a non-empty string")
        self._name = value.strip()
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name!r})"

class Player(BaseEntity):
    def __init__(self, name: str):
        super().__init__(name)                  
        self._scores: list[tuple[int, str]] = []
        self._dates_played: set[str] = set()

    def add_score(self, score: int, date: str) -> None:
        self._validate_score(score)
        self._validate_date(date)
        self._scores.append((score, date))
        self._dates_played.add(date)

    @property
    def scores(self) -> list[tuple[int, str]]:
        return list(self._scores)          
    @property
    def total_games(self) -> int:
        return len(self._scores)
    @property
    def average_score(self) -> float:
        if not self._scores:
            return 0.0
        return sum(s for s, _ in self._scores) / len(self._scores)

    @property
    def best_score(self) -> int:
        if not self._scores:
            return 0
        return max(s for s, _ in self._scores)

    @property
    def dates_played(self) -> set[str]:
        return set(self._dates_played)

    def best_score_on_date(self, date: str) -> int:
        daily = [s for s, d in self._scores if d == date]
        return max(daily) if daily else 0

    def to_dict(self) -> dict:
        return {
            "player": self._name,
            "total_games": self.total_games,
            "average_score": round(self.average_score, 2),
            "best_score": self.best_score,
            "scores": [{"score": s, "date": d} for s, d in self._scores],
        }
    @staticmethod
    def _validate_score(score: int) -> None:
        if not isinstance(score, int) or score < 0:
            raise ValueError(f"Score must be a non-negative integer, got: {score!r}")

    @staticmethod
    def _validate_date(date: str) -> None:
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            raise ValueError(f"Date must be in YYYY-MM-DD format, got: {date!r}")
    def __str__(self) -> str:
        return (
            f"Player: {self._name} | "
            f"Games: {self.total_games} | "
            f"Avg: {self.average_score:.1f} | "
            f"Best: {self.best_score}"
        )