
from datetime import datetime
from models.player import BaseEntity


class Match(BaseEntity):
   

    def __init__(self, player_name: str, score: int, date: str):
        super().__init__(player_name)
        self._score = self._parse_score(score)
        self._date = self._parse_date(date)
    @property
    def player_name(self) -> str:
        return self._name

    @property
    def score(self) -> int:
        return self._score

    @property
    def date(self) -> str:
        return self._date

    @property
    def date_obj(self) -> datetime:
        """Parsed datetime object for comparisons/sorting."""
        return datetime.strptime(self._date, "%Y-%m-%d")
    @classmethod
    def from_dict(cls, data: dict) -> "Match":
        """
        Factory method — creates a Match from a raw JSON dict.
        Usage: match = Match.from_dict({"player": "Alice", "score": 120, "date": "2026-01-01"})
        """
        required_keys = {"player", "score", "date"}
        missing = required_keys - data.keys()
        if missing:
            raise KeyError(f"Missing keys in match data: {missing}")
        return cls(
            player_name=data["player"],
            score=data["score"],
            date=data["date"],
        )

    def to_dict(self) -> dict:
        """Serialize back to dict — for file_services.py to save."""
        return {
            "player": self._name,
            "score": self._score,
            "date": self._date,
        }


    @staticmethod
    def _parse_score(score) -> int:
        if not isinstance(score, int) or score < 0:
            raise ValueError(f"Score must be a non-negative integer, got: {score!r}")
        return score

    @staticmethod
    def _parse_date(date: str) -> str:
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except (ValueError, TypeError):
            raise ValueError(f"Date must be YYYY-MM-DD format, got: {date!r}")
        return date

    def __str__(self) -> str:
        return f"Match({self._name}, score={self._score}, date={self._date})"

    def __lt__(self, other: "Match") -> bool:
        """Allows sorting matches by score: sorted(matches)"""
        return self._score < other._score
