def test_average_score_placeholder():
    scores = [100, 200, 300]
    average = sum(scores) / len(scores)
    assert average == 200


def test_best_score_placeholder():
    scores = [120, 180, 150]
    assert max(scores) == 180