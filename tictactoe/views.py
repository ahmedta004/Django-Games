# tictactoe/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest

WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # cols
    (0, 4, 8), (2, 4, 6)              # diagonals
]

def index(request):
    """Home page: show 'Start game' button or redirect to current game."""
    if request.session.get('game'):
        return redirect('tictactoe:game')
    return render(request, 'tictactoe/index.html')

def new_game(request):
    """Initialize a new game in the session and redirect to board."""
    request.session['game'] = {
        'board': [''] * 9,     # 9 empty cells
        'player': 'X',         # X always starts
        'winner': None,        # 'X' or 'O' when someone wins
        'draw': False
    }
    # ensure session is saved
    request.session.modified = True
    return redirect('tictactoe:game')

def game(request):
    """Render the board. If no game in session, go to index."""
    game = request.session.get('game')
    if not game:
        return redirect('tictactoe:index')
    return render(request, 'tictactoe/game.html', {'game': game})

def move(request, pos):
    """Handle a move at position pos (0..8). Must be POST."""
    if request.method != 'POST':
        return HttpResponseBadRequest("POST required")

    game = request.session.get('game')
    if not game or pos < 0 or pos > 8:
        return redirect('tictactoe:index')

    # If already finished or cell occupied, ignore
    if game.get('winner') or game.get('draw') or game['board'][pos]:
        return redirect('tictactoe:game')

    # Make the move
    game['board'][pos] = game['player']

    # Check winner
    winner = check_winner(game['board'])
    if winner:
        game['winner'] = winner
    elif '' not in game['board']:
        game['draw'] = True
    else:
        # Switch player
        game['player'] = 'O' if game['player'] == 'X' else 'X'

    request.session['game'] = game
    request.session.modified = True
    return redirect('tictactoe:game')

def reset(request):
    """Remove game from session and return to index."""
    try:
        del request.session['game']
    except KeyError:
        pass
    return redirect('tictactoe:index')

def check_winner(board):
    """Return 'X' or 'O' if there is a winner, else None."""
    for a, b, c in WIN_LINES:
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]
    return None
