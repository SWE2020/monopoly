if __name__ == '__main__':
    import game_intro
    import name_selection
else:
    from GUI.game_intro import game_intro
    from GUI.name_selection import select
    from GUI.utils import rescale, Button, InputBox, GameText, grayscale
