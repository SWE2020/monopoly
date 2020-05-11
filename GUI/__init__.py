if __name__ == '__main__':
    import game_intro
    import Name_Selection
else:
    from GUI.game_intro import game_intro
    from GUI.Name_Selection import select
    from GUI.mode_selection import mode_select
    from GUI.utils import rescale, Button, InputBox, GameText, grayscale
