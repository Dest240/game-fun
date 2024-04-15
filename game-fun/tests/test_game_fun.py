from game_fun import main

#def test_main():
#    results = main("rock","paper")
#    assert results =='You LOSE. Paper beats Rock.'

def test_main(capsys):
    main("rock","paper")
    captured = capsys.readouterr()
    assert captured.out == "You LOSE. Paper beats Rock.\n"

