
from models.player import Player
from models.match import Match


class Leaderboard:

    def __init__(self):
        self._players: dict[str, Player] = {}

    def load_matches(self, matches: list[Match]) -> None:
        for match in matches:
            self._add_score(match.player_name, match.score, match.date)

    def load_from_raw(self, data: list[dict]) -> None:
        for entry in data:
            match = Match.from_dict(entry)
            self._add_score(match.player_name, match.score, match.date)

    def get_rankings(self) -> list[tuple[int, str, float, int]]:
        sorted_players = sorted(
            self._players.values(),
            key=lambda p: p.average_score,
            reverse=True,
        )
        return [
            (rank + 1, p.name, round(p.average_score, 2), p.best_score)
            for rank, p in enumerate(sorted_players)
        ]

    def get_best_overall(self) -> tuple[str, int] | None:
        if not self._players:
            return None
        best_player = max(self._players.values(), key=lambda p: p.best_score)
        return (best_player.name, best_player.best_score)

    def get_best_by_date(self, date: str) -> tuple[str, int] | None:
        candidates = [
            (p.name, p.best_score_on_date(date))
            for p in self._players.values()
            if date in p.dates_played
        ]
        if not candidates:
            return None
        return max(candidates, key=lambda x: x[1])

    def get_all_dates(self) -> list[str]:
        all_dates: set[str] = set()
        for player in self._players.values():
            all_dates.update(player.dates_played)
        return sorted(all_dates)

    def get_player(self, name: str) -> Player | None:
        return self._players.get(name)

    @property
    def player_count(self) -> int:
        return len(self._players)

    def print_leaderboard(self) -> None:
        rankings = self.get_rankings()
        print("\n" + "=" * 50)
        print(f"{'LEADERBOARD':^50}")
        print("=" * 50)
        print(f"{'#':<5} {'Player':<15} {'Avg Score':>10} {'Best':>8}")
        print("-" * 50)
        for rank, name, avg, best in rankings:
            print(f"{rank:<5} {name:<15} {avg:>10.2f} {best:>8}")
        print("=" * 50)

        best = self.get_best_overall()
        if best:
            print(f"\n Overall Best: {best[0]} with {best[1]} pts")

        print("\n Best by date:")
        for date in self.get_all_dates():
            result = self.get_best_by_date(date)
            if result:
                print(f"   {date}: {result[0]} — {result[1]} pts")
        print()

    def _add_score(self, player_name: str, score: int, date: str) -> None:
        if player_name not in self._players:
            self._players[player_name] = Player(player_name)
        self._players[player_name].add_score(score, date)
